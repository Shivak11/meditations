<div align="center">

<img src="assets/meditations-banner.svg" alt="Meditations. A reflection ritual for your own work. It keeps what you rejected." width="820">

</div>

# Meditations

Learn from the work you have just done with AI. Meditations helps you examine your decisions, understand the ideas behind them and choose what to try next.

## Install in Claude

**[Download meditations.zip](https://github.com/Shivak11/meditations/raw/refs/heads/main/meditations.zip)**

This file is ready to upload to Claude. Keep it zipped.

1. Open [Claude](https://claude.ai/) on your computer. In **Settings → Capabilities**, turn on **Code execution and file creation**.
2. Open **Customize → Skills** from Claude's sidebar.
3. Click **+ → Create skill → Upload a skill**, then choose the `meditations.zip` file you downloaded.
4. Find **Meditations** in the skills list and make sure it is switched on.

Once you have finished a piece of work with Claude, return to that conversation and paste this message:

```text
Use the Meditations skill to review the work we just did.

Explain the important concepts in plain language and connect them to the decisions we made. Pay particular attention to my corrections and assumptions. Show where one takeaway might not apply, then suggest a small experiment for next time.

Use only the conversation and files available here. Ask before saving any notes.
```

On later runs, you can simply say **“meditate on this”**. If the work happened elsewhere, attach the relevant file or paste the part of the conversation you want to review.

You should get a review grounded in that work, a question about a conclusion you reached and a small experiment to try. If Claude cannot find the skill, check that it is switched on under **Customize → Skills**.

If the upload option is missing on a work account, your organisation may need to enable user-created skills. See [Claude's instructions for adding skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Install in Claude Code, Codex or another coding agent

If you already use a coding agent, run this in your terminal and choose your agent when prompted:

```bash
npx skills add Shivak11/meditations
```

Then say **“meditate on this”** in the agent and point it at the work you want to review. This terminal installer is separate from the upload method for Claude above.

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

## What it can use on the first run

In Claude Chat, Meditations uses the conversation and files you make available. Installing it does not give Claude access to files on your computer or to conversations in other apps. You can add a few sentences about how you like to work; this is optional.

With a coding agent that has access to your project, it can also read the standing instructions described below.

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

Preferences saved in another app are not local files that this skill can read. If you want them included, you can paste the relevant preferences into the conversation.

## What it never does with those files

Your global instruction file probably contains an API key, a worker URL, a database name, or a rule that belongs to a client.

The skill extracts preference and discards everything else. Nothing read from those files is ever written to `meditations.md`, quoted into an output, or repeated back when you ask what it found. It describes the preference, never the file.

## The file it keeps

With a coding agent, the record is `meditations.md` in your working directory. It gains an entry only when you approve one.

In Claude Chat, you can ask Claude to make a downloadable `meditations.md` after you approve an entry. Save that file and attach it when you want to use those notes in another conversation. Installing the skill does not automatically carry this file between chats.

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
- **It works with the evidence available to the current agent.** Installing it does not grant access to another app's memory, unrelated conversations or your computer's files.
- **The name is deliberate and slightly misleading.** Marcus Aurelius wrote his to himself and never for publication, which is exactly the register. It has nothing to do with mindfulness.

## Updating the download

The ready-to-upload archive is [`meditations.zip`](meditations.zip) at the repository root. Maintainers can rebuild it after changing the skill:

```bash
python3 scripts/package_skill.py
python3 scripts/package_skill.py --check
```

The package follows [Claude's skill ZIP structure](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Licence

MIT. Take it, fork it, keep your own.
