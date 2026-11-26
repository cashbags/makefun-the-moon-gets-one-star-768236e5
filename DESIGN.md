# Design — The Moon Gets One Star

## The entry

> One star. We planted a flag there in 1969 and it hasn't done a single thing since.

82 characters, ASCII, one line. `main.py` writes exactly this line to
`/output/entry.txt`, with no trailing newline, on every run.

## Why this line

The judge weighs five things in order, and the line is built to answer them
in that order.

**1. A review of the Moon itself.** The grievance only works for the Moon.
No other product has a flag planted on it in 1969. Swap in any other product
and the sentence stops making sense, which is exactly what the brief asks
for: a line that could only be about the Moon.

**2. Lands on first read.** The joke is a single familiar shape: the
one-star review of a product that does nothing. "Hasn't done a single thing
since" is the punchline, and it arrives in the last clause with nothing after
it to dilute it. There is no wordplay to decode and no second meaning to
catch on a re-read.

**3. Reads like a real review.** The voice is a genuine reviewer complaining
about a neglected purchase: we did our part (planted the flag), it did
nothing back. "We planted a flag there" is a concrete customer action, and
"hasn't done a single thing since" is the exact cadence of a reviewer who
paid for something and got no service. It is not a slogan and not a poem.

**4. A specific, surprising grievance.** The field is flooded with the
obvious Moon jokes: showing up late, ghosting, tides, phases, rent, the same
face, "would not orbit again" — and the brief itself bans craters, cheese,
and brightness. The 1969 flag is none of those. It is a dated, checkable
fact about this one object, used as a customer-service complaint: one job in
1969, nothing since.

**5. Tight.** 82 of 120 characters. Every word earns its place: the rating,
the customer's action, the date, the complaint. The punchline lands before
the limit with room to spare.

## What was rejected

A twelve-candidate tournament (see `CANDIDATES.md`) covered four empty lanes:
borrowed sunlight, the far side never shown, the 1969 flag, and eclipse
photobombing. The borrowed-sunlight lines were the sharpest jokes in the
field ("acts like it invented it"), but their "glow"/"light" wording brushes
the brief's banned brightness lane, so they lost on criterion 4. The far-side
lines were solid but their punchlines were softer ("keeps turning away").
The eclipse lines were funny but a photobomb is a joke about an event, not
a complaint about the product. The 1969 flag lane won because it is the only
one with zero banned-lane exposure and the strongest real-review voice.

## Determinism

`main.py` holds the line as a single string constant and writes it
unchanged. Two runs produce byte-identical output; the sha256 is recorded
in `BUILD-REPORT.md`.
