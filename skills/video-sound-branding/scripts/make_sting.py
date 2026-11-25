#!/usr/bin/env python3
"""Generate a late-90s style rock sting, no samples needed.

    python make_sting.py out.wav
    python make_sting.py out.wav --tempo 140 --seconds 7 --key E

The recipe is the one in SKILL.md: palm-muted power-chord riff, gated snare,
hard-clipped distortion, crash on the last downbeat, then a tape stop into
silence. Mono output, 48 kHz, 16-bit, so it survives a phone speaker.

Needs numpy. No scipy, no sample packs.
"""

from __future__ import annotations

import argparse
import wave
from pathlib import Path

import numpy as np

SR = 48_000


def saw(freq: np.ndarray, n: int, detune: float = 1.0) -> np.ndarray:
    t = np.arange(n) / SR
    phase = np.cumsum(2 * np.pi * freq * detune / SR)
    return 2 * ((phase / (2 * np.pi)) % 1.0) - 1.0


def onepole_lp(x: np.ndarray, cutoff: float) -> np.ndarray:
    alpha = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, sample in enumerate(x):
        acc = (1 - alpha) * sample + alpha * acc
        y[i] = acc
    return y


def guitar_note(freq: float, seconds: float, muted: bool, amp: float = 1.0) -> np.ndarray:
    n = int(SR * seconds)
    # root, fifth, octave — power chord, slightly detuned for width
    voices = []
    for ratio, gain in ((1.0, 1.0), (1.4983, 0.8), (2.0, 0.45)):
        voices.append(saw(np.full(n, freq * ratio), n, 1.0) * gain)
        voices.append(saw(np.full(n, freq * ratio), n, 1.0031) * gain * 0.6)
    body = np.sum(voices, axis=0) / len(voices)
    body = np.tanh(body * 4.5)                 # hard-clip = amp distortion
    body = onepole_lp(body, 3800)              # speaker roll-off

    attack = int(0.004 * SR)
    env = np.ones(n)
    env[:attack] = np.linspace(0, 1, attack)
    if muted:
        decay = np.exp(-np.linspace(0, 7, n))  # palm mute: short and thumpy
        env *= decay
    else:
        env *= np.linspace(1.0, 0.72, n)
        release = int(0.03 * SR)
        env[-release:] *= np.linspace(1, 0, release)
    return body * env * amp


def kick(seconds: float = 0.22) -> np.ndarray:
    n = int(SR * seconds)
    t = np.arange(n) / SR
    freq = 120 * np.exp(-t * 22) + 48
    phase = np.cumsum(2 * np.pi * freq / SR)
    return np.sin(phase) * np.exp(-t * 16)


def snare(seconds: float = 0.14) -> np.ndarray:
    n = int(SR * seconds)
    t = np.arange(n) / SR
    noise = np.random.default_rng(7).normal(0, 1, n)
    tone = np.sin(2 * np.pi * 185 * t)
    body = 0.75 * noise + 0.45 * tone
    # the gate: hard exponential, no tail — the era's fingerprint
    return body * np.exp(-t * 38)


def crash(seconds: float = 1.1) -> np.ndarray:
    n = int(SR * seconds)
    t = np.arange(n) / SR
    noise = np.random.default_rng(11).normal(0, 1, n)
    bright = np.diff(noise, prepend=0.0)       # cheap high-pass
    return bright * np.exp(-t * 3.2) * 0.5


def tape_stop(x: np.ndarray, seconds: float = 0.45) -> np.ndarray:
    n = int(SR * seconds)
    if n >= len(x):
        n = len(x)
    head = x[:-n]
    tail = x[-n:]
    rate = np.linspace(1.0, 0.05, n)           # playback speed falls to a stop
    idx = np.cumsum(rate)
    idx = idx[idx < len(tail) - 1]
    warped = np.interp(idx, np.arange(len(tail)), tail)
    warped *= np.linspace(1, 0, len(warped))
    return np.concatenate([head, warped])


def build(tempo: float, key: str, bars: int) -> np.ndarray:
    roots = {"E": 82.41, "F": 87.31, "G": 98.00, "A": 110.00, "D": 73.42}
    root = roots.get(key.upper(), 82.41)
    beat = 60.0 / tempo
    bar = 4 * beat
    total = int(SR * (bar * bars))
    mix = np.zeros(total)

    def add(sig: np.ndarray, at: float, gain: float = 1.0) -> None:
        start = int(at * SR)
        end = min(total, start + len(sig))
        if end > start:
            mix[start:end] += sig[: end - start] * gain

    # pickup: two muted chugs
    for i in range(2):
        add(guitar_note(root, beat * 0.5, muted=True, amp=0.8), i * beat * 0.5, 0.9)
    offset = beat

    # bar 1: straight palm-muted eighths
    for i in range(8):
        add(guitar_note(root, beat * 0.5, muted=(i % 4 != 3), amp=0.95), offset + i * beat * 0.5)
    offset += bar

    # bar 2: muted eighths with a raised figure on the last two
    for i in range(8):
        note = root if i < 5 else root * 1.1892 if i == 5 else root * 1.3348
        add(guitar_note(note, beat * 0.5, muted=(i < 6), amp=0.95), offset + i * beat * 0.5)
    offset += bar

    # final bar: one held chord, let it ring, then tape stop
    add(guitar_note(root, bar * 0.92, muted=False, amp=1.0), offset)
    add(guitar_note(root * 0.5, bar * 0.92, muted=False, amp=0.5), offset)  # low octave

    for i in range(bars * 2):
        add(kick(), i * beat * 2 * 0.5, 1.0)
    for i in range(bars):
        add(snare(), beat + i * beat * 2, 0.55)
        add(snare(), beat * 3 + i * beat * 2, 0.6)
    add(crash(), offset, 0.9)                  # crash on the final downbeat
    add(kick(), offset, 1.2)

    mix = tape_stop(mix, 0.45)
    mix = np.tanh(mix * 1.1)
    mix = np.concatenate([mix, np.zeros(int(SR * 1.0))])   # silence earns the VO its entry
    mix /= max(1e-9, np.max(np.abs(mix)))
    return mix * 0.89                          # ≈ −1 dBFS peak


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("out", type=Path)
    parser.add_argument("--tempo", type=float, default=132.0)
    parser.add_argument("--key", default="E")
    parser.add_argument("--bars", type=int, default=3)
    args = parser.parse_args()

    audio = build(args.tempo, args.key, args.bars)
    pcm = np.clip(audio * 32767, -32768, 32767).astype("<i2")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(args.out), "wb") as handle:
        handle.setnchannels(1)
        handle.setsampwidth(2)
        handle.setframerate(SR)
        handle.writeframes(pcm.tobytes())
    print(f"wrote {args.out} ({len(audio) / SR:.2f}s, {args.tempo:.0f} bpm, key {args.key})")


if __name__ == "__main__":
    main()
