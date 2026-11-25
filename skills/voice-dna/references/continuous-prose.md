# Continuous prose

**The non-negotiable: continuous sentences.** This is the one rule that does
not bend: every sentence carries a complete thought, and the ideas inside a
paragraph connect to each other instead of sitting in a pile of fragments.

A fragment is not a shortcut. "Four runtimes. Fifty concurrent runs. One bug."
reads like a slide deck because it is one. The same facts in a sentence show that
the writer understands how they relate, and that understanding is what the reader
came for.

## The rule

- **Write sentences, not labels.** Every sentence has a subject and a verb and
  finishes its thought. A heading, a bold label and a colon do not make a
  sentence.
- **Join facts that belong together.** If two facts describe the same system, the
  same decision or the same consequence, they usually belong in one sentence with
  a comma, a conjunction or a relative clause.
- **Keep one connected idea per paragraph.** Two to five sentences is the usual
  size. Start a new paragraph when the thought changes, not after every sentence.
- **Let the length follow the thought.** A sentence ends when its thought is
  complete, not when it hits a word count. A long sentence is fine when it stays
  grammatical and the reader can follow it, and a short one is fine when the
  thought really is short. What fails is a chopped thought or a page of
  fragments.
- **Do not stack labels.** "Problem: … Solution: … Tech: … Impact: …" is a
  portfolio card, not prose. Labels are fine in a genuinely parallel list of links
  or options.
- **Use transitions only when they explain something.** "The interesting part
  was", "What made this difficult" and "That led me to" are useful when the
  relationship is real, and noise when it is not.
- **Do not open consecutive paragraphs the same way.** Repeated "I built… I
  used… I added…" is a list wearing paragraph clothes.
- **Continuous does not mean careless.** Split a run-on when it loses its
  subject, repeats itself or makes the reader re-read. Do not split a sentence
  just because it is long; length is not the defect.

## What this is not

This is not a rule for short sentences, not one idea per sentence, and not an
idea per breath. A sentence may carry a claim, its cause, its consequence and a
qualification when they belong together. The only limits are grammar, clarity and
the reader's ability to follow the thread.

The reference implementation is the project prose in
`../../engineering-job-application-emails/SKILL.md`: context, architecture, the
difficult part and the outcome joined into whole sentences.

## Where the rule does not apply

Titles, headings, table cells, code, file paths, on-screen labels and genuinely
parallel list items are not sentences and do not need to be. The rule governs the
prose around them. A list is fine when its items really are parallel; the failure
is using list shape to avoid writing the explanation.

## The test

Read the paragraph aloud. If every full stop lands in the middle of a thought, or
if the paragraph sounds like a series of bullet points read aloud, it is not
finished. Join what belongs together, then read it again.

## Examples

**Choppy:**
> I built a service. It has four runtimes. It handles 50+ concurrent runs. Each
> run gets a Linux user. There are CPU limits. I fixed a race condition.

**Continuous:**
> I built a sandboxed execution service that supports four runtimes behind one
> API and handles more than 50 concurrent runs, with each execution isolated
> under its own Linux user and constrained by CPU and process limits. One
> difficult bug involved simultaneous requests trying to provision the same
> user, which I traced to a race condition and fixed with a semaphore.

The second version is longer because it carries more meaning per sentence, not
because it adds words.

**Choppy:**
> Used Electron and React. Native Rust media engine. Platform capture pipelines.
> Hardware export. Lots of tests.

**Continuous:**
> I used Electron and React for the desktop interface and kept the
> performance-sensitive media work in a native Rust engine. That split let me
> build the editing experience with web technologies without making capture and
> rendering depend on the UI layer.

## Projects and technical explanations

Lead with the strongest, most relevant thing you built. For each project, give the
context, what the system does, the difficult part, the decision and its
trade-off, and the result. Explain why a choice was made, not just which tool was
used. A stack list proves familiarity; a sentence about why the queue is
persistent proves judgement.

A reliable shape:

> I built [project] because [problem]. I wanted [goal], so I built [system and
> architecture]. The interesting part was [challenge or decision]. Rather than
> [weaker approach], I [choice], which meant [trade-off]. The project now
> [verified outcome], and the part I am proud of is [specific detail].

Vary the shape. Do not run the same template five times.

Never invent a metric, a user count, a test count or a deployment. If a number is
not in the source, leave it out or mark it `[need: …]`.

Close the loop with the reader. Name the problem they actually have and show how
the thing you built or the idea you are explaining touches it. Generic enthusiasm
("this is exciting work") is not a connection; a sentence about their real
workflow is.

## Video scripts and spoken prose

The continuous rule survives the change of medium. A script is still made of
sentences, and the sentences still have to connect. The extra constraint is the
mouth: a sentence has to survive being read aloud, which is a test for stumbles
and lost threads, not a licence to chop a long sentence into short ones. A
sentence can run for several clauses when it stays grammatical and the narrator
can carry it.

A flat delivery does not need short sentences; it needs sentences that are
complete and clearly built. "The port was wrong." is a sentence, and so is a
longer sentence that carries the cause and the consequence. "Wrong port." is a
fragment, and it reads as a slide.

**Choppy:**
> Forty minutes. Broken stack to working stack. Same laptop.

**Continuous:**
> It went from a broken stack to a working one in forty minutes, on the same
> laptop.

**Choppy:**
> Settings. Three fields matter here.

**Continuous:**
> Open the settings page, where three fields matter.

Hooks, roadmaps and section payoffs are sentences. A roadmap written as "- the
fix" is a table of contents; written as "First the part that broke, then the
setting that fixed it" it sounds like a person.

## Docs and explanations

Explain in prose, and use a list only when the items are genuinely parallel and
the reader will scan them. Introduce the list with a complete sentence, and keep
every item a complete thought where it can stand alone.

A definition, a caveat and a decision each get a sentence that says what they
mean. A bold label followed by a clipped phrase is not an explanation.

## Editing checklist

- [ ] Every sentence has a subject, a verb and a finished thought.
- [ ] Related facts sit together instead of one per line.
- [ ] Paragraphs hold one connected idea and break when the thought changes.
- [ ] No "Problem: / Solution:" stacks outside a real list.
- [ ] Consecutive paragraphs do not open the same way.
- [ ] Length follows the thought; no sentence is shortened to hit a word count.
- [ ] No run-ons; a long sentence stays grammatical and keeps its thread.
- [ ] Read aloud, it sounds like one person explaining something.
