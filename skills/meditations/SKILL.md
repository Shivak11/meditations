---
name: meditations
description: >-
  Reflect on work, decisions and taste. Use for "meditate on this", "/meditations",
  "reflect on this", "consolidate this session", or "Aliveness Review".
  Propose lessons and a next experiment.
---

# Meditations

Turn lived work into a sharper judgment without turning every preference into doctrine.

In a coding agent, the skill keeps one file, `meditations.md`, in the user's working directory. It starts empty. It gains an entry only when the user approves one. Over runs it becomes a readable record of how their judgment actually moves, written for them and not for an audience.

In Claude Chat, use the current conversation, attached files and preferences actually available in that context. The chat's code-execution environment is not the user's computer: do not search its home directory for the user's local agent instructions. If the user approves a record, offer `meditations.md` as a downloadable file. Explain that they can attach it in another conversation; do not claim that installing the skill synchronises records between chats.

## Phase 0: Read what the user has already declared

Run this once per session, before the first reflection. It solves the cold start: a first run should have something to say.

Read `references/declared-preferences.md` and follow it. In short:

1. Read `meditations.md` if the user attached it or, in a coding agent, it exists in the working directory. This is the strongest source, because every line in it was confirmed by the user.
2. In a coding agent with authorised file access, read whichever global agent instruction files exist. In Claude Chat, use only preferences available in the conversation. These are declared preferences rather than inferred patterns.
3. Extract only preference. Discard configuration, credentials, paths, endpoints, and client-specific rules.
4. State plainly which sources were found and which were absent. Never imply knowledge the sources did not supply.
5. Hold everything extracted in this run only. Never copy a line from a global instruction file into `meditations.md` or into any output the user might share.

If two instruction files disagree, that disagreement is a finding. Report it. People write these files months apart and almost never compare them, so a contradiction between what they told one tool and what they told another is real evidence about an unsettled preference.

If no source exists, say so in one line and continue. The ritual works with nothing.

Treat a declared preference as a hypothesis, not a fact. The user wrote it at a moment, for a purpose, possibly years ago. Ask them to confirm, narrow, or retire the ones that matter to this run. A confirmed declaration is the cheapest strong evidence available.

## Establish the run

1. Identify the object of reflection and the evidence available in the current context.
2. Select exactly one primary mode. Infer it when clear; otherwise ask one concise question.
3. Distinguish observed evidence, the user's stated interpretation, and your inference.
4. Set the recording state to `NO RECORD` at the start of every run.

| Mode | Select it for | Primary emphasis |
|---|---|---|
| `artifact` | A draft, interface, lesson, decision, or concrete piece of work | Inspect the choices visible in the artifact and run the Aliveness Review. |
| `session` | A completed or interrupted period of work | Consolidate what happened through Review, Relate, Reinforce, Record, Resolve. |
| `taste` | Preferences across books, interfaces, design, writing, teaching, or media | Compare structural rhymes while preserving each surface's own adapter and limits. |

Do not force a mode switch merely because another mode becomes relevant. Note the connection and keep one primary mode.

## Gather evidence before interpretation

- Inspect the artifact or session traces directly when available.
- Name missing evidence instead of filling gaps with biography or personality claims.
- Label important claims as `observed`, `stated`, or `inferred`.
- Express confidence as `high`, `medium`, or `low`; explain what supports it and what could change it.
- Prefer a small number of consequential patterns over exhaustive description.

For `taste` mode, identify the surfaces being compared and keep their adapters separate. Load an available surface adapter before making a taste-bearing judgment. Treat a structural rhyme across surfaces as a comparison, not proof of one hidden cause.

## Run the five Rs

### 1. Review

Reconstruct what actually happened or what the artifact actually does. Identify the consequential choices, surprises, friction, omissions, and moments of energy. Reject a review made only of completed actions.

For `artifact` and `taste` modes, read [references/aliveness-review.md](references/aliveness-review.md) and run the full review. For `session` mode, run it when the session produced or revised a concrete artifact.

### 2. Relate

Connect the evidence to prior patterns, adjacent projects, or another surface only when the connection changes the interpretation. Preserve tensions rather than smoothing them into a single identity story.

Compare against `meditations.md` when it exists. A finding that contradicts an earlier confirmed entry is more valuable than one that agrees with it. Say so when it happens, and propose narrowing or retiring the older entry rather than quietly stacking a second claim beside it.

In `taste` mode:

- Compare form, evidence, restraint, charge, and recognizability across surfaces.
- Preserve medium-specific differences. A book, an interface, and a lesson do not perform the same job.
- Treat a private preference only as a possible contrast instrument, never as an automatic explanation of professional taste.
- Never make a claim about a class of people from an individual preference.

### 3. Reinforce

Choose what may be worth carrying forward. Keep a candidate only when it is specific enough to guide a future choice and supported by more than eloquent phrasing.

Treat `charged specificity` as a working hypothesis, never a foregone conclusion. Search for at least one counterexample, falsifier, or surface where the hypothesis does not explain the preference. Downgrade or narrow the claim when the counterexample holds.

Separate three classes:

- `durable candidate`: likely to guide future judgment across more than one case;
- `local lesson`: useful for this artifact, medium, or moment;
- `interesting residue`: alive but not sufficiently evidenced yet.

### 4. Record

Decide what, if anything, deserves persistence. Do not write automatically to a wiki, memory, doctrine, skill, project page, or public surface.

`meditations.md` is the default destination and the only one this skill writes to without being asked for another. Read [references/meditations-format.md](references/meditations-format.md) before writing to it.

When a record may be useful:

1. Propose the exact insight, destination, visibility, and scope.
2. Explain whether it is evidence, a working hypothesis, or a proposed rule.
3. Ask the user for explicit authorization to write that proposal to that destination.
4. Stop at `PROPOSED RECORD` until authorization arrives.
5. After authorization, write only the approved content and report the exact paths as `RECORDED`.

Record a rejection with the same care as an approval. When the user says a candidate is wrong, that correction is the highest-value evidence the ritual produces, because nothing else the user keeps captures what they turned down. Ask whether to record it, and write it as a `rejected` entry with the reason in their words.

Do not treat a request to meditate as authorization to record. Do not promote private material into public or core doctrine without the user's explicit approval for that transfer. Never write a line lifted from a global instruction file.

### 5. Resolve

Close the run once the reflection reaches diminishing returns. Do not continue probing after the closing packet unless the user asks.

Return every field:

```text
Sources read:
Mode:
Named insight:
Evidence and provenance:
Confidence:
Counterexample or unresolved tension:
Next experiment:
Record verdict: NO RECORD | PROPOSED RECORD | RECORDED
```

Make the next experiment small enough to test the insight in real work. Prefer changing or comparing one artifact over making a broad identity claim.

## Maintain hard boundaries

- Keep private observations sanitized, non-diagnostic, and non-interfering.
- Never infer intimate facts that are not present in evidence the user supplied or explicitly approved.
- Never let private material challenge, rank, veto, or explain professional choices.
- Never make a claim about a class of people from an individual preference.
- Never turn confidence language into fake measurement.
- Never copy credentials, endpoints, file paths, or client-specific rules out of a global instruction file into any persisted or shareable output.
- Do not split the Aliveness Review into a standalone skill until it has been tested across writing, product or interface work, and teaching.
