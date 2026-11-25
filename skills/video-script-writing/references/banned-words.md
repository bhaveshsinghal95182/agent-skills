# The ban list

Two layers, because they catch different things.

**The floor** — patterns that are wrong for everyone, regardless of voice. Models
default to them when nobody is steering.
**The ceiling** — words this specific creator never says. That part lives in the
voice brief (`voice-dna`), not here.

One instance of anything below, used on purpose, is fine. **Clustering is what
kills a piece**: two or three tells in the same paragraph, or one tell repeated
through a script. So the gate is not "did this line pass", it's "how many AI
defaults are stacked up here".

This list covers words and shapes. The sentence-level rule sits beside it and is
non-negotiable: complete, connected sentences, never a fragment stack. See
`../../voice-dna/references/continuous-prose.md`.

Sources: Kompozy, *The complete AI banned-word library* (Moe Ameen, 2026) for the
category lists, merged with the *AI Slop Ban List* from Luke Robins's Claude skill
pack (2026) for the sentence- and structure-level tells. Edited and reorganised
here; both lists were built for written content, and everything below has been
adapted for narration that has to be said out loud.

---

## 1. Banned openers

Any script, section, paragraph or hook that opens with one of these shapes gets
rewritten. They are all throat-clearing dressed as context.

```
In a world where…        In today's fast-paced world…     In an age where…
In the ever-evolving landscape of…                          More than ever before…
As [industry] continues to evolve…                           In recent years…
At its core…             Welcome to…                      Enter [the solution]…
Hey guys, what's up…     Welcome back to another…         In this video I'm going to…
```

**Replace with:** the claim, the number, the failure, or the result. Start at the
thing itself.

## 2. Banned closers

Do not announce that you are finishing. The ending should land, not be flagged.

```
Ultimately…   In conclusion…   To sum up…   In summary…   All in all…
At the end of the day…   So what does this all mean?   Final thoughts…
Overall…   Taking everything into account…
```

**Replace with:** one concrete line — a callback to the opening, the next action,
or a provocation. Then stop.

## 3. Word-level tells

Catch the **type**, not just the example. These are the words a model reaches for
when it is not thinking.

**Pompous verbs** — replace with the literal verb.
```
delve · unpack · navigate · harness · leverage · utilize · optimize · facilitate ·
foster · cultivate · embark · revolutionize · elevate · empower · unlock ·
streamline · spearhead · grapple · showcase · underscore · illuminate · amplify ·
galvanize · catalyze · transcend · embody · epitomize · curate · alleviate
```

**Metaphorical verbs where the literal one is clearer.** Three recurring shapes:
dramatic metaphors for ordinary failure ("every system *dies* around day 11" →
fails), soft metaphors for ordinary actions ("*leaking into* inbox triage" →
being wasted on), and the delivery-verb tic — *lands, settles, resonates, hits
home, registers*. All of those are AI-coded; use a normal verb. "The point
works."

**The puffed-up "is" family** — when the sentence wants *is* or *are*:
```
serves as · stands as · represents · marks · embodies · constitutes ·
functions as · operates as · emerges as
```

**Inflated adjectives**
```
robust · pivotal · crucial · vital · essential · significant · comprehensive ·
meticulous · innovative · transformative · groundbreaking · seamless ·
multifaceted · intricate · vibrant · ever-evolving · cutting-edge · paramount ·
unparalleled · profound · staggering · breathtaking · game-changing ·
best-in-class · world-class · industry-leading · next-level · frictionless
```

**Magic adverbs**
```
quietly · deeply · fundamentally · remarkably · arguably · notably · significantly ·
profoundly · inherently · undoubtedly · ultimately · invariably · seamlessly ·
effortlessly
```

**Showy nouns**
```
tapestry · landscape · realm · ecosystem · paradigm · framework · journey ·
odyssey · testament · cornerstone · hallmark · pillar · beacon · frontier ·
fabric · mosaic · treasure trove · flywheel · north star · moat
```

**Marketing verbs and nouns**
```
supercharge · turbocharge · maximize · transform · empower · enable (as a benefit
verb) · value-add · synergy · low-hanging fruit · circle back · mission-critical ·
thought leader · subject matter expert · data-driven (when repeated)
```

**Hedges** — a hedged claim cannot be checked. A person who was there does not
hedge about their own experience.
```
arguably · it is worth noting that · one could argue · broadly speaking ·
generally speaking · in many cases · tends to · can sometimes · may often ·
often considered · is typically · is usually · is generally · is largely ·
might be · could potentially · is essentially
```

**Vague authority** — sounds like evidence, cites nothing.
```
studies show · research suggests · experts agree · data confirms ·
it is well known that · it is widely accepted that · it is no secret that ·
many believe · most agree · industry consensus is · common wisdom says ·
conventional thinking suggests
```

**AI bridge phrases** — transitions used when there is no real connection. A cut
does the same job in zero seconds.
```
furthermore · moreover · in addition · on top of that · beyond that · in essence ·
when it comes to · as we explore · as we examine · as we consider ·
this is more than just · what makes this special
```

---

## 4. Sentence-level tells

The recognisable ones first.

**The "actually, it's Y" reframe.** The all-time tell: set up a claim, then flip
it. `It isn't a tool. It's a movement.` Variants: *not because A but because B*,
*the question isn't X, the real question is Y*, *X was never A, it was B*.

> **The test:** delete the negated half. Does the sentence still make the point?
> If yes, the negation was scaffolding — cut it. If no, the positive claim was too
> weak — sharpen it instead of propping it up.

Carve-out: a real state change is allowed ("After the diagnosis you stopped asking
if it was serious. You started asking what to do now" — that is a genuine shift,
not emphasis).

**"Not just X but Y"** — the same family, and the single most over-used structure
in model output. Assert the second clause directly: "It's a workflow."

**Throat-clearers** — *it's worth noting / importantly / notably / interestingly /
it bears mentioning*. Whatever follows stands on its own.

**Promised payoffs that don't pay** — *here's the thing / here's the kicker /
here's where it gets interesting / what nobody tells you*. A drumroll before an
ordinary line makes the let-down worse. If the next line is good, the drumroll is
unnecessary.

**Teacher-mode announcements** — *let's break this down / let's unpack that / let
me explain / let's dive in*. That is performing the role of a teacher instead of
teaching.

**Reflex analogies** — *think of it as / imagine it like a highway for data*.
Most ideas need a clearer first sentence, not a metaphor.

**Stakes inflation** — every topic dialled to civilisational consequence. Match
the register to the size of the thing. A media server is not a defining moment for
the industry.

**Self-asked questions** — *the result? brutal. / what does that mean? everything.*
If the point is worth making, make it.

**Stacked negation buildups** — *not a feature. not a flaw. a choice.* Cut to the
claim.

**-ing tail flourishes** — sentences ending in pseudo-analysis: "*…signalling a
deeper shift*", "*…underscoring the importance*". Either write the analysis as its
own sentence or cut it.

**The fake counter** — *despite its challenges, it continues to grow.* A
counterpoint raised only to be dismissed. Engage it properly or drop it.

**Manufactured concept labels** — inventing "the supervision paradox" and then
referencing it as if it were known. Naming a thing you genuinely teach is fine;
decoration is not.

**"Imagine a world where…"** and **phantom-future projection** — *a year from
today you'll wish…*. If the stakes are real they exist today; replace with a
present observation the viewer can check against their own memory.

**Fabricated specificity** — invented numbers and day-counts ("around day 11",
"improved by 47%", "on the seventh attempt"). The hedge is the tell: *around*,
*about*, *roughly* wrap a number the model isn't sure of. If the source doesn't
supply it, drop it. "A couple of weeks" beats invented precision.

**Present-tense overuse** — a narration-specific tic. Default to past tense for
what the speaker or viewer has been through ("I had this running on Windows"), and
future for what the viewer will get ("by the end you'll have X"). Present tense is
right for a genuine current fact or a general truth. Diagnostic: would you say it
this way out loud?

**Fake spectrums** — *from X to Y* only when both ends are real and the middle is
meaningful. Otherwise "across", or a list.

**"Real story" claims** — *the truth is simpler / what's actually happening is*.
Asserting clarity instead of showing it.

**Algorithmic empathy** — *feeling stuck is completely normal / you're not alone*.
Generic reassurance reads as a script.

**Performed self-awareness** — *look, I'll admit I'm biased* / *since we're being
real*. A costume, not honesty.

**Universal truths that teach nothing** — *consistency matters / hard work pays
off*. True, useless, cut.

---

## 5. Structure-level tells

Only visible when you zoom out.

**Repeated paragraphs** — the same point reappearing in two sections. Models loop.
Catch it on a read-through, not a line edit.

**One point, eight phrasings** — restating an idea with new metaphors until a word
count is hit. If you can't find new things to say, end the section.

**One metaphor run the whole way** — the model picks "the engine" or "the ladder"
early and rides it to the end. Use it where it earns its place, then move on.

**Recursive summaries** — preview, say it, summarise it, then summarise the
summary. One layer is fine in a long piece; stacked layers are AI.

**Hidden lists pretending to be prose** — *the first reason is X. the second is Y.*
It's a list; write it as one or make the points flow.

**One-word dramatic paragraphs** — *Wrong.* / *Brutal.* / *And it didn't work. At
all. Ever.*

**Borrowed-authority comparisons** — *Apple didn't build Uber. Facebook didn't
build Spotify.* Sounds smart, says nothing.

**Sentence-length monotony** — three sentences in a row at the same length. In
narration this is the difference between a person and a text-to-speech engine.

**Paragraph-length monotony** — every block three or four sentences.

**Breezed-past curiosity beats** — raising "and here's where it got weird" and
then gliding past it. If you raise it, commit to it. If you can't commit, remove
the tease.

---

## 6. Formatting tells

- **Em-dash addiction.** Cap: 1 per 300 words. Convert most to periods or commas.
- **Tricolon reflex.** Cap: 1 per 500 words. Three-item lists are a base-model
  tic; two items or one claim usually land harder.
- **Bold-first bullets** — every bullet a bolded mini-headline plus colon.
- **Markdown leaking into prose** — headers inside paragraphs.
- **Trailing emojis and decorative Unicode** — arrows, smart quotes, fancy bullets.

---

## 7. Industry add-ons

Take a block if it matches; ignore the rest.

**SaaS / tech** — synergize · synergistic · circle back · low-hanging fruit ·
value-add · cross-functional · agile-first
**Real estate** — motivated seller · investment opportunity · wealth-building ·
passive income · cash-flowing asset
**Coaching / consulting** — mindset shift · limiting beliefs · next-level mindset ·
breakthrough · transformative journey · unlock your potential · 10x your
**Health / wellness** (regulated claims — extra caution) — wellness journey ·
holistic approach · natural solution · gentle yet effective

---

## 8. Slop in the *delivery*, not the words

Specific to narration read by a low-affect or monotone speaker. These lines are
fine on a page and dead in the mouth:

- **Anything that needs vocal emphasis to parse.** Contrastive stress ("it's not a
  *tool*, it's a *workflow*") dies in a flat read. That's also ban #4, which is why
  the two rules reinforce each other.
- **Rhetorical questions** — they want a rising intonation. Without it they sound
  like an accusation or a stall.
- **Exclamation marks and hype words** — "exciting", "amazing", "insane", "crazy".
  Delivered flat they read as sarcasm or disappointment. Cut the word, not the
  tone.
- **Long sentences** — a monotone voice has no intonation contour to carry the
  listener across 30 words. Short sentences reset the pitch, which is the only
  energy a flat voice gets for free.
- **Stacked adjectives** — three descriptors in a row need three stresses.

**What replaces them:** specifics, understatement, and punctuation. A dry fact
delivered evenly is funnier and more credible than an enthusiastic adjective.

---

## Running the gate

```bash
python scripts/check_script.py script.md            # report
python scripts/check_script.py --strict script.md   # exit 1 on any hit
```

The checker covers words and shapes, plus em-dash and tricolon density. It cannot
tell you whether a paragraph is *about* the same thing twice — that's the
read-through. Fix the flags, then read it aloud.

**Replace, do not just delete.** Every category above points at a plainer
alternative. A banned word removed with nothing in its place leaves a hole the
next draft fills with a different banned word.
