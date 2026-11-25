# Situation to search term

myinstants search works on names, not descriptions. This table maps what a
video moment *is* to the query that finds it. Terms are ordered by how well
they score on the site; try the first, fall back to the rest.

## Reactions to failure or embarrassment

| Situation | Try in order |
|---|---|
| Something embarrassing happens | `bruh`, `boi what the hell` |
| A fail, crash, or facepalm moment | `fail`, `oof`, `maury lie detector` |
| Something cringe | `cringe`, `bruh` |
| Bad news lands | `sad violin`, `womp womp`, `mission failed` |
| Loss, defeat screen | `mission failed`, `sad violin`, `lost` |
| Slow realization something is wrong | `oh no`, `dun dun dun` |
| Disaster unfolds | `dun dun dun`, `horror music` |

## Reactions to success or surprise

| Situation | Try in order |
|---|---|
| Big reveal, dramatic surprise | `vine boom`, `dramatic surprise`, `what da dog doin` |
| Something impressive | `damn boy he thick`, `giga chad theme` |
| Finally works after many attempts | `hell yeah`, `yeet`, `fanfare` |
| Suspiciously good luck | `sus`, `among us` |
| Money or winning | `money`, `cha ching`, `coins` |
| Plot twist | `plot twist`, `record scratch` |

## Punctuation and transitions

| Situation | Try in order |
|---|---|
| Awkward silence after a bad joke | `crickets`, `silence` |
| Record-scratch freeze frame ("yep, that's me") | `record scratch` |
| Dramatic sting on a wrong statement | `vine boom`, `bruh` |
| Something appearing on screen | `pop`, `ding`, `notification` |
| Error, mistake on screen | `windows xp error`, `error`, `wrong answer buzzer` |
| Time running out | `countdown`, `time bomb` |
| Walking away cool | `cool walk music`, `saxophone` |

## Internet-culture staples

| Situation | Try in order |
|---|---|
| Horny jail / stop that | `bonk`, `horny jail` |
| Ratio / owned | `mobizen got ratioed`, `you got ratioed` |
| Rizz moment | `rizz`, `gyat` |
| Vibe farming | `aura`, `aura farm` |
| Emotional damage | `emotional damage` |
| Michael Rosen / food review | `noice`, `nice` |
| It's at this moment he knew | `he knew`, `at this moment` |
| Bruh moment | `bruh`, `bruh sound effect` |

## Music-ish memes

| Situation | Try in order |
|---|---|
| Something sad but funny | `sad violin`, `womp womp`, `china number one` |
| Impending doom | `dun dun dun`, `horror music`, `attack on titan` |
| Sudden chill / sigma moment | `giga chad theme`, `phonk` |
| Old-school comedy bit | `tom and jerry`, `looney tunes` |

## Reading a candidate list

The `search` command prints numbered results. When helping a user choose,
show title plus what site it came from, and note:

- The plain meme name in the title (`BRUH`, `Vine Boom`) is the canonical
  sound most of the time. Titles with edits ("but bass boosted", "10 hours",
  "edited by DJ ...") are fan versions.
- Score is the script's confidence the result matches the query, not quality.
- A 2-second sting is more usable under narration than a 30-second song; the
  `download` record includes `duration_s` — check it before placing.

## When the table fails

Search myinstants for the *meme's name* (what a commenter would type), not
the emotion. If the meme has a catchphrase, search the catchphrase. If you
only know the emotion, one or two words maximum, then judge the candidates
yourself.
