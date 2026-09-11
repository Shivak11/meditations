# Read available preferences

Use preferences that the user has supplied or that the current coding agent is authorised to read. Treat them as evidence about a stated preference, not as proof of a stable trait or universal rule. Continue when no preferences are available.

## Available sources

In Claude Chat, use the conversation, supplied preferences and attachments. Its code-execution environment is not the user's computer. Installing the skill does not grant access to other apps or conversations.

In a coding agent, read relevant existing sources within the host's permissions:

| Source | Location |
|---|---|
| Approved Meditations notes | An attached or local `meditations.md` |
| Current project instructions | `AGENTS.md`, `CLAUDE.md` and relevant existing agent rules |
| Global Claude instructions | `~/.claude/CLAUDE.md` |
| Global Codex instructions | `~/.codex/AGENTS.md` |
| Other available agent instructions | Authorised Cursor, Gemini or OpenCode instructions when relevant |

Prefer instruction content already loaded by the host. Do not scan unrelated directories, request new access simply to fill a preference history, or interpret a missing file as a problem. Ask once for missing context only when it materially affects the reflection.

## Separate preferences from configuration

Keep preferences about language, evidence, completion standards, delegated decisions and the work itself. Exclude credentials, endpoints, tool configuration, private paths, client names and operational rules. A technical example inside a language preference does not establish a fact about the user's systems.

Apply extracted preferences within the current run. Do not copy lines from standing instructions into the HTML, reply, source metadata or `meditations.md`. Describe a relevant preference in general terms only when it helps the reflection. Lasting notes should use the wording and scope the user explicitly approves.

## Handle apparent contradictions

Current explicit instructions and an approved example are sufficient direction; do not ask for routine reconfirmation. Different older instructions may apply to different tasks. Describe the apparent difference without exposing private text or file paths, then check whether context explains it. Ask which preference applies when the answer affects this work. Do not assume that a difference between files reveals an unsettled personality trait.

## State the evidence scope

Keep the source inventory in private source notes. In the study, briefly recall the actual question, correction or observation behind each principle. Mention a missing source only when its absence limits a conclusion. Never imply access the host did not provide.
