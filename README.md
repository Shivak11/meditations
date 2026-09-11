# Meditations

Learn from work you have just finished with AI. Meditations reviews the decisions, corrections and assumptions in that work, explains the relevant concepts and gives you a visual HTML study to revisit.

## Install in Claude

**[Download meditations.zip](https://github.com/Shivak11/meditations/raw/refs/heads/main/meditations.zip)**

This is the ready-to-upload skill package in the repository root. Keep it zipped; you do not need GitHub's whole-repository download.

1. Open [Claude](https://claude.ai/) on your computer. In **Settings → Capabilities**, turn on **Code execution and file creation**.
2. Open **Customize → Skills** from Claude's sidebar.
3. Choose **+ → Create skill → Upload a skill** and select `meditations.zip`.
4. Check that **Meditations** is switched on.

After a working session, paste:

```text
Use Meditations to review the work we just did and create a visual HTML study.
Group the actual topics. For each, state the principle, briefly recall how it arose,
and show one concrete application. Keep each concept within one readable printed page.
Use only the conversation and files available here. Ask before saving lasting notes.
```

On later runs, say **“meditate on this”**. If the work happened elsewhere, attach the relevant file or paste the relevant conversation. Open or download the resulting HTML to study it. Ask for **“text only”** when you prefer a written reflection.

If Claude cannot find the skill, check that it is switched on. Your organisation may need to allow user-created skills. See [Claude's installation instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude) if the menu labels differ.

## Install in Claude Code, Codex or another coding agent

Run this in your terminal and choose your agent when prompted:

```bash
npx skills add Shivak11/meditations
```

Then ask it to **“meditate on this”** and identify the work to review. The terminal installer is separate from the Claude upload method above.

## What you receive

The study opens with a direct session summary. Each topic states its principle immediately, briefly recalls the question or correction that produced it, and shows one concrete application. Distinct topics stay together in their own sections. Each concept fits within one readable A4 page, with the opening included on the first page. Counterexamples and next experiments appear when they add something useful.

For example, suppose you asked AI to organise files named `note-2.txt` and `note-10.txt`. A text-based sort can place `note-10.txt` first because it compares the first differing character. The principle would be to compare the number when it represents the intended order. A short comparison of the two resulting lists makes the difference visible. This is an illustrative use case; it is not a claim about a session the skill observed.

The default output is one self-contained HTML file with readable text and topic-related visuals. Interactions are included when they help explain the concept. The essential explanation remains readable without JavaScript, and the file supports printing. Generating the study needs an agent that can create files. If that is unavailable, Meditations gives a text reflection and says that it could not create HTML.

## Five designs included

StyleRef and Impeccable are optional. The package includes these designs:

| Design | Visual treatment |
|---|---|
| Paper notes | A light reading layout with clearly annotated examples |
| Colour blocks | Strong flat colours and prominent comparisons |
| Technical diagrams | Precise linework and directly labelled relationships |
| Editorial study | A reading-focused hierarchy with integrated evidence |
| Dark study | A dark background with high-contrast explanations |

Without StyleRef, a local selector randomly chooses a design for each new study. It can exclude up to three recent choices when that history is available. Revisions retain their selected design. The agent adapts the layout and diagrams to the subject; these are starting systems, not a promise that every study will be unique.

The designs use local font fallbacks and do not require accounts, remote fonts or extra packages. The finished HTML works offline. If the host cannot execute a random selection, the agent chooses a design and records that limitation in its private source notes.

## What the skill can access

Claude Chat uses the conversation, attachments and preferences you make available there. Installing a skill does not grant access to other apps or files on your computer.

An authorised coding agent can also use relevant project instructions and approved Meditations notes. Preferences extracted from instructions stay within the current run. Credentials, endpoints, client details and private instruction text must not be copied into the study or sent to a design service.

## Lasting notes are optional

The HTML study is the requested output. A separate `meditations.md` record receives an entry only after you approve its exact content and destination. Reflection alone does not authorise a wiki update, memory change, hook installation or publication. The agent keeps its recording state privately and tells you plainly when something has been saved.

The record can preserve a confirmed lesson, a rejection or a narrower replacement for an earlier conclusion. Each entry includes its evidence, uncertainty and what would change it. In Claude Chat, save the approved record as a download and attach it when you want to use it in a later conversation. The skill does not synchronise notes across chats.

## Three reflection modes

| Mode | What it reviews |
|---|---|
| `artifact` | Choices visible in a draft, interface, lesson or other concrete output |
| `session` | Decisions and corrections across a period of work |
| `taste` | Preferences across different kinds of work, with their limits kept clear |

The skill selects one mode from your request. It uses the available evidence and should identify any material gaps. Neither a reflection nor an interactive study establishes that learning or judgement has improved; that requires observation beyond producing the file.

## Update or check the package

Maintainers can rebuild the root download using Python's standard library:

```bash
python3 scripts/package_skill.py
python3 scripts/package_skill.py --check
python3 -m unittest discover -s tests -v
```

The ZIP uses an explicit source allowlist and includes the skill, its references, the design selector, design assets and licence. It excludes repository maintenance files and private study outputs. The package follows [Claude's skill ZIP structure](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Licence

MIT. The bundled fallback designs and selector are included under the repository licence. Any separately retrieved design reference retains its own terms.
