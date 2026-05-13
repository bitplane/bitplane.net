# 🦀 rars in Rust, bro

I've done a few different reverse engineering projects with LLMs now, and
figured it was time to push the clankers to their limits.

A RAR compressor for every version of RAR ought to have taken me 5 years, which
is why nobody ever bothered. It took 5 weeks of evenings and weekends of
clanking, and cost roughly £40 in subsidised tokens.

Yes it's 55k lines of slop, no it's not that fast, and it almost earned me an
OpenAI ban. But it works.

---

## SPECIF~1.RAR

RAR was originally an LZSS compressor for DOS, which peaked in popularity
as the warez scene's format of choice. Fighting with WinZip for feature
parity and supremacy, WinRAR boasted multi-volume support, recovery records and
even an internal VM, but its USP was always superior compression. It's a
middle-aged format that never stopped growing up, it's as big as a house.

`unrar` comes with source code but that code is not actually free, and
somewhat ironically RAR's author isn't a big fan of piracy. So ideally I'd need
to implement my version from spec, which doesn't really exist.

The monstrous task of creating one involved pulling code from free
decompressor sources in the wild - unar, libarchive, UNRARLIB, plus
random web pages and folk lore.

I then set Claude to work documenting as much as it could. After each pass, I
quizzed it on missing features and maintained an ongoing gaps doc containing the
hard-to-know stuff. This persisted between context resets, which were needed to
flow the tokens into the gaps. It took 2 weeks of cooking, going back and forth
until we had most of the reader side documented. The writer side, however,
remained a mix of confabulation and conjecture.

So next I grabbed the RAR binaries for DOS and Windows, and set to work making
test fixtures, hex-dumping and doing passes in Ghidra and DOSBox-x to get some
idea of how they were packed. Another week or two of work and the gaps started
to close up.

Now I had something that might be useful; spec docs for every version of the
RAR file format:

* [📚 spec](https://github.com/bitplane/rar-research)

---

## Building something

Being confidently wrong enough to start, Codex, Claude and I set off building a
(precariously) compatible Rust CLI. The workflow was shaped something like
this:

### Working from spec

Opus is great, but it tends to enthusiastically generate code while missing the
bigger picture. Claude requires remedial passes, refactoring and a short leash,
but is great for a chat about strategy or architecture. Gippity 5.5 stays on
target when left alone, but will rabbit hole you hard if you chat with it too
much. I could give Codex the spec docs and basically tell it to just get on with
it. Very refreshing.

While working from spec, Codex would randomly stop due to cyber violations, and
I'd need to manually compact to continue. Eventually I had to get verified by
OpenAI to stop it from happening. Well, it turned out that at some time during
spec investigation, Claude needed to understand authenticity verification which
is a paid feature. With a context full of reverse engineering tools it cracked
WinRAR and bypassed product registration, then dutifully documented its crimes
in the spec. The docs, when viewed, triggered OpenAI's alarms and stopped it
dead in its tracks. I squashed this out of the git history, and decided *not*
to implement the feature at all.

### One foot on the brake

You've gotta keep an eye on the bots and interrupt when things start to smell
bad. If you don't then they'll special-case their way out of every problem and
around every test, ugly patterns will propagate through your code, and you'll
need an expensive refactor later. I should have done more, but I didn't, and for
that I paid the price later on. The tokens were subsidised, but it was a waste
of my time.

For the last 15 months or so my hobby has been shouting at Claude, so I'm
getting good at interventions. I enjoy it, even if it has damaged my
personality. I tend to swear at Codex far less, maybe because it's faster or
less of a grinning idiot, but probably because it's bland and professional. This
may be a good thing, but I'm not sure yet.

### Tests, for science

Way too many tests. Fragile tests, coverage that doesn't matter,
`excessively_long_test_names_that_fill_your_screen`, these are vital when
working on something this size. They provide a statistical mass that warps text
generation, pulling the bots back on track when they go off-piste or try to cut
corners. So, reams of unit tests and as much coverage as is possible please. We
can always remove them later, right? Right?...

So the tests keep it in shape, but actually running the code is what aligns it
with reality. So the real work is about fixtures, oracles, and updating the spec
where wrong. In doing this, Codex cleared up autofill bullshit
("hallucinations") that had previously passed at least ten rounds of review.

So it turns out that empirically grinding against reality is the best source of
signal, and with enough time the spec was honed into something close to Truth.
Science.

### Cross cutting context

Periodically, I had Claude generate a full review of the code. This helps nudge
the codebase away from an intolerable slop and more towards a tolerable one,
which is the best we can hope for in May 2026.

The problem with review agents though, is enthusiasm. They generate laser
focused nitpickings that quibble over things that don't matter, so you need a
filter.

My filter is, I .gitignore a `review.md` and instruct codex to group reviews
into batches. I then add them to a `plan.md` by functional area, and the plan
drives development tasks. Claude being aware of previous reviews invites
compounding blind spots, telling Codex which things I don't care about pollutes
the context - as all text does. Selective context management, switching between
sessions, rm'ing the review doc, and running on different machines provides
variety that helps the work flow into all the gaps.

After a while I had Claude act as a UAT tester, orchestrate compatibility test
suites and test against archives in the wild too, producing fresh review.md's
that fed into the plan by the usual route. It was a serial process, but not too
much of a bottleneck.

## A first release

By the time I reached RAR 2.9 I was getting a bit bored of reading
machine-generated spew. So I switched to some other projects for a bit. Having a
working CLI for version 1.3 and 1.4 of RAR, which very few tools can even open,
I regenerated this into a new dir and pushed it up to crates.io.

I figured it'd be useful for archivists, even if I gave up. So here it is:

* [🦀 oldrar](https://crates.io/crates/oldrar)
* [🐱 source](https://github.com/bitplane/oldrar)
* [🏠 home](https://bitplane.net/dev/rust/oldrar)

---

## Scoring a `/goal`

I picked it back up late last week when OpenAI released the `/goal` feature.
This is essentially a Ralph loop that allows the bot to grind on at a task
indefinitely, compacting and picking up after filling its meagre context limit.
Running only one session means it doesn't even hit the 5 hour usage limits, so
it ran multiple times for 6+ hours while transcribing the rest of the spec into
code, and once for a solid 16 hours before I interrupted it and demanded a
refactor. It smashed through the bulk of the work this way, flood-filling around
40,000 lines, doing recovery records, encryption, multi-volume support and tons
of spec work that I'm still barely aware of.

While Codex worked, Claude and I found more RAR files and set up a compression
benchmarking and a compatibility regression test suite. Giving Codex the task
of optimizing compression worked surprisingly well, it was able to apply
well-known techniques from other compressors to optimize LZSS to around 5-10%
worse than WinRAR, and beat RAR on some of our test data. WinRAR was optimized
for decades by a skilled and obsessive Russian hacker, I used the median of the
distribution with brute force and ignorance. Coming so close feels like a huge
win given the effort involved. And since I don't want to read the code too much,
it'll have to do.

Performance was a different story. Codex is happy using `valgrind` and
`hyperfine` to find hot spots, and it gobbled up the low hanging fruit without
problems. It fell short on finding the sort of novel performance hacks that a
seasoned C dev would use to squeeze the hot loops, and ended up multiple times
slower. Or it could just be that idiomatic, safe Rust code is slow. I suspect
it's both.

The latest codex model generates code with barely any comments, which I'm a fan
of because comments aren't executed and quickly rot. But comment-aversion plus
compaction equalled a stream of functional regressions in RAR 1.4 compatibility,
mostly with the DOS version of RAR, ones that tripped it up on at least 3
occasions. Putting a comment in the source would have prevented this.

Another thing, Claude's reviews, specially the UAT reviews, got deep into the
details but missed the most obvious thing - that the UX was terrible. It caught
inconsistencies and errors, but until I specifically said "tell me why this is
shit UX", it didn't recommend anything to do with that despite it being the main
goal. This applies to other areas too, they have blind spots by default that
can probably be solved with agent skills or a bit of "uwotm8" in the prompts.

---

## What did we learn?

So the TL;DR is:

0. Working from spec actually works.
1. Modern models are very good at Rust.
2. Autonomous research is extremely powerful.
3. Tests, docs and comments shape the context through mass and steering.
4. Bring your own architecture, or pay a refactoring fee.
5. Don't expect decent performance or novel insights just yet.
6. Bots can overlook the obvious.

---

## 🦀 rars

So here it is, a Rust implementation of RAR. It's sloppy, it's slow, it's almost
two megabytes in size and somewhat worse than WinRAR on compression.

But, it works, and the world now has a free software RAR implementation. So that
was worth the effort.

You can install `rars` like so:

```bash
cargo install rars-cli
```

And the links are here:

* [🏠 home](https://bitplane.net/rust/rars)
* [🦀 crate](https://crates.io/crates/rars)
* [🐱 source](https://github.com/bitplane/rars)

