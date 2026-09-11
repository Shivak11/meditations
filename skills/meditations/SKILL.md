---
name: meditations
description: Learn from completed work through a visual HTML study. Use for meditate on this, /meditations, reflect on this, consolidate this session, or Aliveness Review. Includes offline design fallbacks.
---

# Meditations

Review completed work to understand its decisions and identify a useful next experiment. Produce a visual HTML study by default, following [references/visual-study-output.md](references/visual-study-output.md). StyleRef and Impeccable are optional; five bundled design systems support users who have neither.

The study is the requested output. A separate, lasting record called `meditations.md` gains an entry only when the user approves one. Creating a study does not authorise saving a preference, changing standing instructions or publishing anything.

In Claude Chat, use the current conversation, attachments and preferences available there. Its code-execution environment is not the user's computer. Do not search its home directory for personal agent instructions. Offer the HTML as a download. If the user approves a lasting record, offer `meditations.md` separately; they can attach it to a later conversation. Do not imply that installation synchronises records between chats.

## Read the available preferences

Once per session, read [references/declared-preferences.md](references/declared-preferences.md). Use an attached or authorised local `meditations.md` when available. In a coding agent, use relevant standing instructions the host permits you to read. Keep extracted preferences within this run; do not copy configuration or private instruction text into the study.

A stated preference can be old or specific to another situation. Distinguish it from an observed pattern. If two preferences appear inconsistent, describe the difference and consider whether different contexts explain it. Ask for clarification only when it affects this reflection. Continue usefully when there is no preference history.

## Establish the run

1. Identify the work and the evidence available in the current context. Do not infer access to another session or app.
2. Select one primary mode from the table. Infer it when clear; otherwise ask one concise question.
3. Distinguish observed evidence, the user's interpretation and your inference.
4. Set the lasting-record state to `NO RECORD`.
5. Read the visual-output reference. For each new study, select a subject-related design; when design tools are absent, randomly choose a bundled system. Preserve the selected design when revising the same study.

| Mode | Use it for | Main task |
|---|---|---|
| `artifact` | A draft, interface, lesson, decision or other concrete output | Examine the choices visible in that work. |
| `session` | A completed or interrupted period of work | Reconstruct decisions, corrections and what remains uncertain. |
| `taste` | Preferences across writing, design, teaching or other work | Compare preferences while keeping each context's purpose and limits clear. |

A connection to another mode can inform the review without changing its main task.

## Gather evidence before interpretation

Inspect the available work directly. Pay particular attention to the user's corrections, changes of direction and assumptions accepted without examination. Separate what the agent did from what the user decided. Explain the underlying concepts when they help the user understand those choices; a technical term needs a concrete example of its actual inputs and results.

Name material gaps in the evidence. Do not invent historical examples, personality explanations or measured improvements. A clearly labelled illustration can explain a concept but cannot prove what happened in the user's session. Prefer a few consequential findings over a list of every completed action.

## Run the five Rs

### 1. Review

Reconstruct what happened and identify the choices that changed the result. Explain why a correction mattered and what assumption it replaced. For concrete artifacts and comparisons of taste, use [references/aliveness-review.md](references/aliveness-review.md). Do not turn the review into praise or a score.

### 2. Relate

Compare the findings with relevant prior work or approved notes when they are available. A connection is useful when it changes the explanation or the next decision. Keep differences between contexts explicit: a preference in a personal reading exercise does not automatically explain a professional design choice.

When a finding conflicts with an approved note, propose narrowing or retiring the earlier conclusion. Do not silently add a contradictory rule or claim a single cause for several unrelated preferences.

### 3. Reinforce

Choose a lesson specific enough to guide a future decision. Search for at least one counterexample or changed condition where it would fail. Explain the limit beside the lesson so the user can judge where to apply it.

Distinguish a candidate for repeated use, a lesson limited to this task, and an unresolved observation. Test the proposed explanation against the evidence; persuasive wording is not evidence. If an older record uses `charged specificity` or `interesting residue`, interpret those terms plainly as, respectively, a proposed preference for specific consequential choices or an unresolved observation. Do not presume either pattern applies.

### 4. Record

Keep lasting notes optional. `meditations.md` is the default record destination, governed by [references/meditations-format.md](references/meditations-format.md).

When a record may help, propose the exact content, destination, visibility and scope. Explain whether it is evidence, a hypothesis or a proposed rule. Obtain explicit authorisation before writing it and remain at `PROPOSED RECORD` until approval arrives. Then write only the approved content and report `RECORDED` with its path.

A rejection can also be useful evidence. Ask whether to record it and preserve the user's reason accurately if they approve. A request to meditate authorises the private study output; it does not authorise lasting notes, memory updates, wiki edits, changes to another skill or publication.

### 5. Resolve

Finish when further reflection would add little. Deliver the HTML study and a short reply with the main lesson, next experiment and `NO RECORD`, `PROPOSED RECORD` or `RECORDED` verdict. If text was requested or file creation is unavailable, deliver the substantive reflection in chat and explain that no HTML file was created.

Across the study and reply, make clear what work was reviewed, what supports the lesson, what remains uncertain and where the lesson might fail. Use ordinary connected prose. Keep internal phase names, source ledgers and design rationale outside the study. Do not repeat the full study in chat or keep questioning the user after delivery.

## Maintain the boundaries

- Use direct, literal language in headings, explanations, captions and interaction feedback. Review all prose independently of the visual design before delivery. Preserve accurate quotations and necessary technical terms. Respect an explicit request for another writing style.
- Keep private observations non-diagnostic and limited to evidence the user supplied or authorised. Never infer intimate facts or generalise about a class of people from an individual preference.
- Do not use private preferences to rank, veto or explain professional choices. Do not introduce intimate material yourself.
- Never copy credentials, endpoints, private paths or client rules from standing instructions into output. Do not send private work to a style search or other external service.
- Do not install hooks, global rules, MCPs, plugins or other services as a side effect of this skill. Bundled design selection works locally.
- Do not claim that reflection, interactive questions or an attractive study have improved judgement or learning without evidence.
