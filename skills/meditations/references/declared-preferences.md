# Reading what the user has already declared

People who work with coding agents keep a file telling those agents how they
like things done. That file is a declaration of preference rather than a record
of activity, which makes it the best cold-start evidence available.

Read it. Do not persist it.

## Where to look, in priority order

| Source | Path | Note |
|---|---|---|
| This skill's own record | `./meditations.md` | Strongest. Every line was confirmed by the user |
| Claude Code, global | `~/.claude/CLAUDE.md` | Usually the longest and most developed |
| Claude Code, project | `./CLAUDE.md` | Scoped to the current work |
| Codex, global | `~/.codex/AGENTS.md` | |
| Cross-tool convention | `./AGENTS.md`, `~/.agents/AGENTS.md` | Increasingly the shared standard |
| Cursor | `~/.cursor/AGENTS.md`, `~/.cursor/rules/*.mdc`, `./.cursor/rules/*.mdc` | |
| Gemini CLI | `~/.gemini/GEMINI.md` | Often present but empty |
| OpenCode | `~/.config/opencode/AGENTS.md` | |

Read every one that exists. Skip the rest silently in the file system and name
them plainly in the report.

**ChatGPT custom instructions and claude.ai personal preferences are stored on
those services and never written to disk.** There is no path to read. If the
user mentions either, offer once: "paste your custom instructions and I will
include them in this run". Never ask twice, and never treat their absence as a
gap in the reflection.

## Separating preference from plumbing

Most of a global instruction file is configuration. Perhaps a quarter is taste.
Extract only the second kind.

**Preference, keep:**

- How they want things said. Register, tone, banned constructions, sentence rules.
- What they consider finished. Proof standards, what counts as evidence.
- What they refuse. Named anti-patterns, words they will not read, shapes they reject.
- Where their judgment sits. Which decisions they insist on making, which they delegate.
- Stated values about the work itself.

**Plumbing, discard:**

- Tool paths, CLI names, install commands, environment variables.
- API endpoints, worker URLs, database references, credentials, rotation notes.
- MCP server names and configuration.
- Repository layouts and directory conventions.
- Client-specific or product-specific business rules.

A line can be both. "Say the same tap could charge twice, not the endpoint is
not idempotent" is a register rule that happens to contain a technical term.
Keep the rule, drop nothing, and do not treat the example as a fact about their
systems.

## What must never leave the run

- Never write a line copied from a global instruction file into `meditations.md`.
- Never quote one into an artifact, a summary, or anything the user might share.
- Never surface a credential, endpoint, path, or client name that came from one,
  even when the user asks what you found. Describe the preference, not the file.

The extracted preferences live in this run and end with it. Only what the user
confirms in their own words reaches `meditations.md`.

## Contradictions are the finding

When two files disagree, report it. Someone who told one tool to stay terse and
another to show its reasoning has an unsettled preference and does not know it,
because nobody diffs these files.

State both instructions, name which file each came from, and ask which one
still holds. A resolved contradiction is a strong first entry, and it gives the
first run something real to say before any history exists.

## Reporting what you read

Open the run with one line naming the sources found and the sources absent. Be
exact. A reflection that implies more knowledge than its sources supplied is
the failure this whole ritual exists to prevent.
