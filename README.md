<div align="center">

<img src="assets/meditations-banner.svg" alt="Meditations. A reflection ritual for your own work. It keeps what you rejected." width="820">

</div>

# Meditations

**A critique ritual for the things you make. Not a mindfulness app.**

```bash
npx skills add Shivak11/meditations
```

Then say "meditate on this" to Claude Code, Codex, Cursor, or any agent that reads skills, and point it at something you made.

---

## What it does

You finish a piece of work. A draft, a screen, a lesson, a deck. It looks fine. You have nobody to argue with about it, and asking an AI usually gets you a compliment sandwich.

This runs a structured review instead. Five questions, and it will not average them into a score:

1. **What is the particular bet here?** Name the choice this commits to that a competent alternative would reject. If no bet is visible, find where category convention replaced judgement.
2. **Where is the charge, and what contains it?** Find the tension or friction giving the work its energy, then find the structure that keeps that energy legible.
3. **What proves this is real?** Point at residue of contact with reality: a concrete detail, a tested interaction, a quoted voice, an imperfection. Distinguish proof from polish.
4. **What have I over-explained?** Find where explanation removed discovery, ambiguity or trust, and say what can be cut or turned into an experience.
5. **Would I recognise this with the logo removed?** If recognition depends on colours and reputation alone, say so.

Then it forms a hypothesis about your taste, and it is required to go looking for a counterexample before it keeps one.

## It knows something about you on the first run

Most reflection tools start empty and stay shallow until you have fed them for weeks.

This one reads what you have already written down. Not your notes, not your history: your **standing instructions to your own coding agents**.

| It reads | Because |
|---|---|
| `~/.claude/CLAUDE.md` | This is you telling an agent how you like things done |
| `~/.codex/AGENTS.md` | Same, for a different tool |
| `./AGENTS.md`, `./CLAUDE.md` | Project-scoped preferences |
| Cursor rules, `GEMINI.md`, OpenCode | Whatever exists |
| `./meditations.md` | Its own record, strongest of all |

Those files are a declaration of preference rather than a record of activity, which makes them unusually good evidence. Everyone who works with agents has one. Almost nobody has read theirs back.

**And it compares them.** People write these files months apart, for different tools, and never diff them. So the first thing the ritual can tell you is where you contradicted yourself.

A real first run, on the machine this was built on, found this:

> Your Claude file has twelve sections. Your Codex file has three. Nine things you have told Claude you have never told Codex, including a rule you marked NON-NEGOTIABLE in capitals.

That is a true and useful thing to learn about yourself in under a minute, with no history at all.

**ChatGPT and claude.ai preferences live on those services and are never written to disk.** There is no way to read them. If you use either, the skill offers once to take a paste, and never asks again.

## What it never does with those files

Your global instruction file probably contains an API key, a worker URL, a database name, or a rule that belongs to a client.

The skill extracts preference and discards everything else. Nothing read from those files is ever written to `meditations.md`, quoted into an output, or repeated back when you ask what it found. It describes the preference, never the file.

## The file it keeps

`meditations.md`, in your working directory. It starts empty and gains an entry only when you approve one.

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

That last field is required. A claim with no falsifier is a slogan.

### It keeps the rejections

This is the part that makes the file worth having.

When you say a finding is wrong, that gets recorded too, with your reason in your own words. Nothing else you keep does this. Your notes hold what you found interesting; nothing holds what you turned down, and the rejections are where taste actually lives.

```markdown
## 2026-09-12 · Restraint is not the through-line

- **Status:** rejected
- **Evidence:** stated. "The teaching stuff is loud on purpose and I like it
  loud. Restraint is a writing rule, not a me rule."
- **What this narrows:** the earlier claim now applies to written work only.
```

It also refuses to stack contradictions. A new finding that disagrees with an older confirmed entry has to propose narrowing or retiring the old one. Two confident opposites in one file would make the whole thing worthless.

## Three modes

| Mode | For |
|---|---|
| `artifact` | A draft, an interface, a lesson, a decision, a concrete thing you made |
| `session` | A stretch of work that finished or got interrupted |
| `taste` | Preferences across books, design, writing, teaching, media |

It picks one and stays in it. Noticing that another mode is relevant is a note, not a reason to switch.

## Nothing is written without you saying so

Every run starts at `NO RECORD`. It proposes what it thinks deserves keeping, explains whether that is evidence, a hypothesis or a rule, and stops until you authorise the exact content and destination. Asking it to reflect is not authorisation to write.

## Honest limits

- **It is a thinking tool, not a capability.** It does not build anything. If you want output, this is the wrong skill.
- **It gets better with use, which means run one is the weakest one.** The bootstrap exists to make run one useful anyway, but a file with twenty entries is a different tool from an empty one.
- **It will disagree with you and it does not soften it.** That is the point, and some days it is unwelcome.
- **It cannot read ChatGPT or claude.ai memory.** Nobody can. Those live on the server.
- **The name is deliberate and slightly misleading.** Marcus Aurelius wrote his to himself and never for publication, which is exactly the register. It has nothing to do with mindfulness.

## Licence

MIT. Take it, fork it, keep your own.
