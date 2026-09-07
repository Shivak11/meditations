# The meditations file

`meditations.md` lives in the working directory. It is written for the user to
reread, not for an audience and not for a machine. Keep it readable top to
bottom as a document, and let the structure serve that rather than the reverse.

It starts empty. It grows only by approval.

## The entry

```markdown
## 2026-09-07 · The chart that argued

**Claim.** Charts earn their place by settling a question, not by covering a
variable. Where a chart shows a variable nobody is deciding about, cut it.

- **Status:** confirmed
- **From:** the awards dashboard, three visual variants of one decision
- **Evidence:** observed. Three builds of the same data recommended three
  different actions, and the difference tracked what each layout put first.
- **Confidence:** medium. One artifact, one domain.
- **What would change it:** a case where an apparently decorative chart turned
  out to carry the decision.
```

Five fields, and every one of them is doing work.

- **Status** is `confirmed`, `rejected`, `narrowed`, or `retired`.
- **From** names the artifact or session, so the claim can be re-examined.
- **Evidence** is labelled `observed`, `stated`, or `inferred`. Never blur them.
- **Confidence** is `high`, `medium` or `low`, and says what it rests on.
- **What would change it** is required. A claim with no falsifier is a slogan.

## Record the rejections

A `rejected` entry is worth more than a confirmed one, because nothing else the
user keeps holds what they turned down. Write the reason in their words.

```markdown
## 2026-09-12 · Restraint is not the through-line

**Claim.** Restraint explains the preference across writing and interface work.

- **Status:** rejected
- **From:** proposed after the dashboard run, tested against three teaching decks
- **Evidence:** stated. "The teaching stuff is loud on purpose and I like it
  loud. Restraint is a writing rule, not a me rule."
- **Confidence:** n/a
- **What this narrows:** the earlier claim now applies to written work only.
```

## Rules for maintaining it

- Never write an entry the user has not approved in this run.
- Never copy a line out of a global instruction file into this file. Only what
  the user confirmed in their own words belongs here.
- Never silently stack a contradiction. When a new finding disagrees with an
  existing entry, propose narrowing or retiring the old one and let the user
  decide. Two confident opposites in one file destroy its value.
- Keep entries in date order, newest last, so it reads as a developing account
  rather than a ranked list.
- Do not summarise the file into a profile. The point is the reasoning, and a
  profile is what remains after the reasoning is thrown away.

## What it is for

On the next run, read it first. It is the accumulated context that makes run
forty sharper than run one.

It is also the artifact. Someone who has run this twenty times has a readable
document of how their own judgment moved, with the evidence attached and the
rejections intact. Very few people have that about themselves.
