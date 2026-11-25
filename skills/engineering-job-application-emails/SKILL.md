---
description: "Write personal, technically credible engineering
  internship and job-application emails in Bhavesh's preferred style:
  continuous natural prose, project-led evidence, strong engineering
  explanations, and a thoughtful connection to the company."
name: engineering-job-application-emails
---

# Engineering Job Application Email Skill

## Purpose

Use this skill whenever Bhavesh asks to write, complete, revise,
critique, or tailor an email applying for an engineering internship,
software role, backend role, or adjacent technical position.

The goal is not to produce a conventional cover letter. The goal is to
write an email that sounds like a real builder reaching out to another
person: curious, capable, candid, technically grounded, and genuinely
interested in the work.

The email should make the recipient want to look at the projects and
start a technical conversation.

## Core voice

Write in a voice that is:

-   **Personal and direct:** Address the recipient like a person, not a
    hiring committee.
-   **Enthusiastic without being theatrical:** Genuine excitement is
    welcome; exaggerated flattery is not.
-   **Technically confident but humble:** Explain what was built and
    why, without pretending to know everything.
-   **Candid and slightly informal:** A little personality is good.
    Avoid slang that makes the application feel careless.
-   **Specific:** Use concrete engineering decisions, trade-offs, bugs,
    constraints, and outcomes.
-   **Unforced:** Do not make every sentence sound like a polished
    corporate slogan.

The writing should sound like an engineer explaining work they care
about, not a marketer selling a product.

## The most important style rule: continuous sentences

Bhavesh strongly dislikes broken, choppy sentence composition. Prefer
continuous, natural sentences that carry a complete thought and connect
ideas logically. The shared rule and more before-and-after examples live in
`~/.agents/skills/voice-dna/references/continuous-prose.md`; this skill applies
it to application emails.

Do not write like this:

> I built a service. It has four runtimes. It handles 50+ concurrent
> runs. Each run gets a Linux user. There are CPU limits. I fixed a race
> condition.

Prefer this:

> I built a sandboxed code-execution service that supports four runtimes
> behind a single API and handles more than 50 concurrent runs, with
> each execution isolated under its own Linux user and constrained
> through CPU and process limits. One particularly difficult bug
> involved simultaneous requests attempting to provision the same user,
> which eventually led me to identify and fix a race condition using a
> semaphore.

The second version connects the facts into a coherent explanation. It is
not necessary to make every sentence long; the goal is natural flow, not
run-on sentences.

### Sentence and paragraph rules

1.  Combine closely related facts into complete sentences rather than
    placing each fact on its own line.
2.  Use transitions such as "The interesting part was...", "What made
    this difficult...", "I eventually realised...", "That led me to...",
    and "The part I'm particularly proud of..." when they genuinely
    clarify the relationship between ideas.
3.  Vary sentence length. Use a shorter sentence occasionally for
    emphasis, but do not make the whole email a sequence of fragments.
4.  Keep each paragraph focused on one connected idea, usually two to
    five sentences.
5.  Avoid excessive line breaks. Use paragraph breaks when the thought
    changes, not after every sentence.
6.  Avoid sentence fragments masquerading as headings or explanations.
7.  Do not overuse colons, semicolons, em dashes, or parenthetical
    asides to force a rhythm.
8.  Do not turn every project into a stack of "Problem:", "Solution:",
    "Tech:", and "Impact:" labels. Those labels can be useful in a
    compact portfolio, but the email should read as prose.
9.  Avoid run-on sentences. Continuous prose still needs clear
    punctuation and a logical structure.
10. Do not repeat the same sentence opening across consecutive
    paragraphs.

## Preferred email structure

Adapt this structure to the role and the amount of material available.
It is a guide, not a rigid form.

### 1. Subject

Keep it simple and searchable. Examples:

-   Engineering Intern Application \| Bhavesh Singhal
-   Application for Backend Engineering Intern
-   Engineering Internship --- Bhavesh Singhal

Avoid gimmicky subject lines.

### 2. TL;DR opening

A short, distinctive summary can work well for Bhavesh. It should say
what kind of engineering he enjoys and why he is reaching out.

Example:

> **tl;dr**
>
> I like backend engineering, system design and building things a lot,
> and I'd love to learn from your team because the problem you're
> solving is one of the more interesting engineering challenges I've
> come across.

Keep this to one or two sentences. It should sound natural, not like a
slogan.

### 3. Personalized opening

Refer to the actual post, product, technical idea, or company problem
that prompted the application. Explain what caught his attention and why
it matters to him.

Good approach:

> I came across your post about the engineering internship and was
> genuinely intrigued by what the team is building. I hadn't realised
> anyone was tackling this particular problem in this way, and the
> combination of applied AI and the engineering challenges around it
> made me want to reach out.

Do not invent familiarity, admiration, or a personal relationship. If
the recipient is someone Bhavesh follows or whose work he has genuinely
discussed, that context can be mentioned accurately.

### 4. Brief context before the projects

Move naturally from the opening into evidence:

> Rather than give you another generic introduction about how interested
> I am in engineering, I'd rather show you some things I've actually
> built. These are the projects I'm most proud of, and each taught me
> something different about designing and debugging real systems.

Avoid defensive disclaimers about being a student, being broke, using
AI, or having limited infrastructure unless a constraint is genuinely
relevant to understanding the project. If a project was built on free
tiers, frame this as a practical constraint and explain the engineering
choices it encouraged.

### 5. Project case studies

Choose the strongest and most relevant projects, not necessarily every
project. Each project should normally have:

-   **Context:** What prompted the project or what problem existed?
-   **What was built:** Explain the system in plain but technically
    precise language.
-   **Engineering substance:** Describe the architecture, important
    decisions, constraints, and trade-offs.
-   **A meaningful challenge:** Include a bug, failure mode, bottleneck,
    or design problem when there is a real one.
-   **Outcome or evidence:** Include verified metrics, tests, deployment
    details, or a working link where useful.
-   **Reflection:** Explain what the project taught him, but do not
    force a generic lesson onto every project.

A project section should read as a compact engineering story, not a
README pasted into an email.

#### Recommended project narrative

A reliable pattern is:

> I started building \[project\] because \[specific problem or
> motivation\]. I wanted to \[goal\], so I built \[system and high-level
> architecture\]. The interesting part was \[non-obvious engineering
> challenge or design decision\]. Rather than \[less effective
> approach\], I \[decision and reason\], which meant
> \[result/trade-off\]. The project now \[verified outcome\], and the
> part I'm particularly proud of is \[specific detail\].

Do not mechanically repeat this exact pattern for every project. Vary
the structure so the email feels written, not generated.

#### How much technical detail?

Include enough detail to demonstrate real ownership, but explain why the
details matter.

Weak:

> Built with FastAPI, SQLite, Docker, Redis, and Celery.

Stronger:

> I used FastAPI for the service and a persistent job queue for
> background work because individual processing steps could fail or
> restart independently. Retries and deduplication made jobs safe to
> resume, while verification-before-deletion prevented the pipeline from
> removing source files before every output variant had been checked.

The stronger version communicates engineering judgment, not just tool
familiarity.

### 6. Connect the projects to the company's problem

This is one of the most important sections. Do not simply say the
company is exciting or that the role would be a great learning
opportunity. Identify the actual problem the team is solving and connect
it to relevant experience.

For example, when applying to an applied-AI product that evaluates
student work:

> What interests me about this problem is that evaluating a student's
> work requires more than generating a plausible answer. The system has
> to interpret context, handle ambiguity, remain consistent and know
> when a human should make the final call. That also makes it an
> engineering problem involving submission processing, queues,
> evaluation workflows, failure handling and a usable teacher
> experience. I've explored several pieces of that puzzle independently,
> and I'd love to understand how they come together in a product used by
> real teachers.

This section should demonstrate that Bhavesh has thought about the
product, not merely read the job description.

### 7. Close

Keep the close direct and low-pressure. Include only relevant links and
practical details.

Example:

> I've attached my resume, and you can explore \[project\] here and find
> the rest of my work on \[GitHub\]. If anything catches your attention,
> I'd be happy to walk you through the architecture, implementation
> decisions or the parts that didn't work as expected.
>
> Thank you for taking the time to read this.
>
> Best,\
> Bhavesh

Do not include a phone number, location, portfolio, GitHub, resume
statement, and multiple calls to action unless they are useful. Never
invent contact details or links.

## Case studies

These examples are based on the two application-email approaches Bhavesh
shared. Use them to understand the writing principles; do not copy their
wording blindly.

### Case study A: A technical application to a backend-focused engineer

**Context:** An application inspired by a reference email to an engineer
whose work Bhavesh admired, particularly around backend engineering,
system design, and DRM.

**What worked:**

-   The TL;DR immediately established genuine interest in backend
    engineering and system design.
-   The opening referenced a specific post rather than using a generic
    "I am applying for..." introduction.
-   The projects demonstrated initiative and practical engineering under
    constrained resources.
-   The video-sharing SaaS connected the recipient's technical work to
    Bhavesh's own learning.
-   The close acknowledged that the work was imperfect while showing
    willingness to explain and revise it.

**What to preserve:**

-   Specific enthusiasm for the recipient's work.
-   A clear reason for reaching out to that person in particular.
-   Project links and tangible evidence.
-   A candid statement that Bhavesh is still learning, paired with
    evidence that he builds independently.

**What to improve:**

-   Avoid making the email sound apologetic about limited money or
    free-tier constraints.
-   Do not over-explain that a project is early-stage; state its current
    status and what already works.
-   Make the connection between the recipient's technical interests and
    the project explicit, but do not imply that one tweet taught him an
    entire technology unless that is accurate.
-   Use complete paragraphs instead of abrupt one-line statements.

### Case study B: An engineering internship application to Saraswati AI

**Context:** An application to a remote engineering internship at
Saraswati AI, a team building AI tools to reduce the time teachers spend
checking papers.

**Project evidence available in the draft:**

-   **Recso:** An Electron/React application with a native Rust media
    engine, platform-specific capture pipelines, a shared preview/export
    composition model, hardware-accelerated export, and substantial test
    coverage.
-   **AniGoblin:** A Dockerized FastAPI media-processing pipeline
    integrating with other self-hosted services, with persistent job
    management, retries, deduplication, disk guards, and careful
    cleanup.
-   **Code execution service:** A sandboxed service supporting four
    runtimes and more than 50 concurrent runs, with per-run Linux users,
    resource limits, teardown, and a race-condition fix.
-   **Postgres data layer:** A 33-table Drizzle/Postgres layer with
    migrations and tests, including a change to separate read and
    transactional database access after connection exhaustion.
-   **LLM tooling:** A retrieval application that maps natural-language
    queries to structured filters over a 10,000-plus-entry catalogue,
    plus an MCP server with typed tools.

**What worked:**

-   The strongest projects were selected to show range: media systems,
    background pipelines, concurrency, database architecture, and LLM
    tooling.
-   The email explained concrete failure modes rather than only naming
    technologies.
-   The final connection to Saraswati was thoughtful: evaluating student
    work is not only a model problem, but also a workflow, reliability,
    and human-in-the-loop engineering problem.
-   The application showed how independently explored engineering
    concepts could transfer to a real product.

**What to preserve:**

-   Lead with the most impressive and relevant project.
-   Explain the difficult part of each system, not just its feature
    list.
-   Connect the candidate's experience to the company's actual product
    and users.
-   Use measurable outcomes only when they are real and explainable.

**What to improve:**

-   Do not make every project a sequence of short, isolated sentences.
-   Avoid README-like labels and overly compressed fragments.
-   Keep the project descriptions varied so the email does not feel
    repetitive.
-   Avoid volunteering legally questionable or potentially alarming
    framing. Describe the legitimate engineering problem and
    architecture accurately; never conceal material facts if directly
    asked.
-   Keep the overall email focused. If five projects make it too long
    for the recipient, select the three or four strongest and link to
    the rest.

## Before-and-after examples

### Example 1: Choppy project description

**Avoid:**

> The service supports four runtimes. It handles 50+ concurrent runs.
> Each run gets a Linux user. There are resource limits. I fixed a race
> condition.

**Prefer:**

> The service supports four runtimes behind a single API and handles
> more than 50 concurrent runs, with each execution isolated under its
> own Linux user and constrained by resource limits. One difficult bug
> involved simultaneous requests attempting to provision the same user,
> which I eventually traced to a race condition and fixed using a
> semaphore.

### Example 2: Technology list without reasoning

**Avoid:**

> Built with Electron, React, Rust, wgpu, Media Foundation and PipeWire.

**Prefer:**

> I used Electron and React for the desktop interface, while keeping the
> performance-sensitive media work in a native Rust engine. That
> separation let me build the editing experience with web technologies
> without making the capture and rendering pipeline depend on the UI
> layer.

Only use this wording if it accurately reflects the actual architecture.

### Example 3: Generic company enthusiasm

**Avoid:**

> I am very passionate about AI and would love to work at your company
> because it is doing innovative work.

**Prefer:**

> What interests me about your product is that the difficult part isn't
> simply getting a model to produce an answer; it's making the entire
> evaluation workflow reliable enough that teachers can trust and use
> it. That combination of model behaviour, data processing, human review
> and product engineering is exactly the kind of problem I'd like to
> work on.

### Example 4: Defensive disclaimer

**Avoid:**

> I'm just a broke college student, so I used free tools and AI wherever
> possible. Please don't judge the projects too harshly.

**Prefer:**

> I've built most of these projects independently under free-tier
> infrastructure constraints, which meant being deliberate about
> resource usage and making a number of architectural decisions myself.
> I'm happy to explain the trade-offs and the parts I'd approach
> differently today.

Use the second version only when the constraints are relevant. Often, no
disclaimer is needed at all.

### Example 5: Abrupt close

**Avoid:**

> Resume attached. GitHub below. Let me know.

**Prefer:**

> I've attached my resume, and you can find the projects and their
> implementation details on GitHub. If any of them interest you, I'd be
> happy to walk you through the architecture and the decisions behind
> it.

## Editing rules

When revising an existing draft:

1.  Preserve the user's actual experience, technical details, metrics,
    project names, and links.
2.  Improve sentence flow and paragraph transitions without changing the
    underlying claims.
3.  Remove repetition, filler, unnecessary disclaimers, and generic
    claims.
4.  Keep distinctive phrases and personality when they work; do not
    sterilize the writing.
5.  Do not make the email sound excessively formal or like a corporate
    cover letter.
6.  Do not turn the whole email into bullets. Bullets are acceptable for
    a short list of links or genuinely parallel details, but project
    narratives should usually be prose.
7.  Do not invent technical architecture, performance numbers, test
    counts, users, deployments, or business impact.
8.  If an important technical claim is unclear or contradictory, ask one
    focused question or flag it for confirmation rather than silently
    rewriting it as fact.
9.  Keep the recipient's perspective in mind: explain unfamiliar project
    context, prioritize relevance, and avoid making them work to
    understand why a detail matters.
10. When the user asks for a complete email, provide a ready-to-send
    draft with a subject line and appropriate greeting/sign-off.

## Tailoring workflow

Before drafting, identify:

1.  **Recipient:** Who is receiving the email, and what is known about
    their work?
2.  **Opportunity:** What role is being applied for, and what does the
    post or description emphasize?
3.  **Motivation:** What specifically caught Bhavesh's attention?
4.  **Relevant evidence:** Which projects best demonstrate the required
    skills?
5.  **Technical proof:** Which architecture decisions, challenges, and
    outcomes can be stated accurately?
6.  **Connection:** How does the candidate's experience relate to the
    company's product or problem?
7.  **Practical details:** Which resume, portfolio, GitHub, demo,
    location, availability, or contact links should be included?

Use available context first. Do not ask Bhavesh to repeat details
already supplied. If one essential fact is missing, ask one concise
question. If enough information exists, draft the email rather than
delaying with a questionnaire.

## Final quality checklist

Before returning the email, verify:

-   [ ] The opening is specific to the recipient or company.
-   [ ] The TL;DR, if used, sounds like Bhavesh rather than a slogan.
-   [ ] The email gets to concrete work quickly.
-   [ ] Project sections explain why and how, not just what technologies
    were used.
-   [ ] Sentences flow naturally and express complete thoughts.
-   [ ] There are no unnecessary one-sentence fragments or excessive
    line breaks.
-   [ ] Paragraphs transition logically and do not read like
    disconnected README entries.
-   [ ] Technical claims and metrics are grounded in information Bhavesh
    provided.
-   [ ] The connection to the company's problem is thoughtful and
    specific.
-   [ ] The tone is confident, candid, enthusiastic, and human.
-   [ ] There are no unnecessary apologies, exaggerated flattery, or
    generic claims.
-   [ ] The close is simple and includes only relevant links and
    details.
-   [ ] The email is concise enough that a busy engineer can scan it
    without losing the story.

## Default instruction

When in doubt, choose natural continuous prose over fragmented
sentences, concrete engineering evidence over generic enthusiasm, and a
specific human voice over conventional cover-letter language. The email
should feel like Bhavesh wrote it after thinking carefully about the
recipient's work and the engineering problems he wants to solve.
