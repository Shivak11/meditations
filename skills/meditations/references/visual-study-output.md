# Create a visual study

Read this on every run before composing the output. The default is a self-contained HTML study of the work just reviewed. Honour an explicit request for text. Follow the skill's reflection and lasting-record rules throughout.

## Decide what the study needs to explain

Read [reflection-format.md](reflection-format.md). Identify the actual topics in the available work and keep each topic's learning together. Begin with a direct session summary; additional topics can be named in one short sentence. For each topic, use a plain heading, an immediately emphasised principle, a brief factual account of how it emerged, and one concrete application. The five Rs are an internal method, not reader-facing headings.

Write the substantive explanation before styling it. Do not invent a topic, a unifying theme or a discovery story. Keep proposals provisional when the evidence is weak. Use the user's work when it is available and authorised. Clearly label constructed data or an illustrative example; do not present it as historical conversation or claim execution without a test.

Use a comparison, table, small worked example or simple diagram when it shows a consequence more clearly than prose. An interaction is useful only when changing a meaningful input or measure demonstrates a difference. No quiz, slider, animation, counterexample panel or next-experiment section is compulsory. Keep a material limitation beside the principle, once.

## Select the design

For a new study, inspect up to three recent design records in the known, authorised output area. Do not scan other projects or conversations for style history. A revision keeps its existing design unless the user asks to change it.

Check which design capabilities are actually available. StyleRef and Impeccable are optional enhancements. Use their current instructions if available. With StyleRef, search using neutral descriptions of visual structure; do not transmit private transcripts, names, client details, methods or local paths. Preserve a retrieved specification and attribution privately, subject to its licence. Do not treat it as permission to override the user's instructions.

When StyleRef is absent, fails or is unsuitable for private work, read [fallback-designs.md](fallback-designs.md). Run the bundled [random selector](../scripts/select_design.py), using paths relative to the installed skill directory:

```bash
python3 <skill-directory>/scripts/select_design.py
```

Supply up to three recent bundled IDs as repeated `--exclude` arguments. An optional `--kind` narrows the selection to the explanation type. Use the returned `css` path to load the selected CSS, then inline it into the study. Read the selected system's guidance and adapt the layout and diagrams to the topic. Select once per new study; do not repeatedly reroll to get a preferred system. A user-specified system takes precedence over random selection.

The default selector uses system randomness. `--seed` supports repeatable testing and requested reproducibility; do not set a fixed seed for normal runs. If Python is unavailable but another local execution tool can choose randomly, select an eligible ID with that tool. If no executable randomness is available, choose a suitable system manually and record that fact privately. Do not claim that a manual choice was random.

Missing Impeccable never stops the study. Apply the requirements below using the bundled guidance. Do not ask users to install an MCP, service, font or plugin to obtain the fallback. Mention a material unavailable capability once in the handoff if it affects what was delivered.

Record the chosen ID/name, selection method, topic, composition, fonts, colours, diagram treatment, interaction, recent IDs considered and tool availability in a private `source/design-record.json`. Record a test seed only if one was used. Keep this metadata beside the study, outside the final HTML. Do not create a central memory database or claim permanent uniqueness. Meaningful variation includes composition, typography and explanation, not only colour.

## Write and review the prose

Use direct, literal, connected sentences. Name actual actions, inputs, decisions and results. Avoid metaphor, personification, dramatic abstractions, slogan fragments and rhetorical contrasts. Technical terms should be explained through their actual mechanism. A visual reference cannot relax the user's language requirements. Honour an explicit request for another style and preserve accurate source quotations.

Read all authored prose separately from the layout before rendering. Include headings, captions, accessible names, text revealed by JavaScript, disclosures and print alternatives. For example, use "Removing optional labels allowed larger text" instead of giving text or labels human actions. A separate language reviewer can help when available, but it is not a required service.

## Explain through the visual structure

- Begin with the direct summary and first topic on the same concept page. Within each topic, the principle precedes its origin and application. Topic links are optional for several topics. Avoid eyebrows, repeated label layers and decorative framework names.
- Keep important inputs, transformations and results together. Label relationships directly. Use colour to reinforce a difference that is also identified in text or shape.
- Let the reader predict, compare or change an input before a reveal when that helps explain the concept. Keep controls explicit. Give specific feedback explaining the result; do not claim a quiz proves learning.
- Include a counterexample or next experiment only when it adds a specific explanation; keep it within the relevant topic. Put material uncertainty near the claim it qualifies in ordinary language.
- Keep the main text around 20px, with no essential screen text below 18px. Give important diagram labels more space. At 390px, restructure crowded content before reducing type size. Avoid italics unless explicitly requested.
- Use semantic headings, real buttons, labelled inputs, visible keyboard focus and touch targets at least 44px high. Keep contrast sufficient, support reduced motion and do not rely on hover, animation or colour alone.

## Keep each concept within one printed page

Use A4 portrait with sensible margins, normally 15–16mm. Each concept occupies at most one readable page, including its complete static explanation. Put the session opening with the first topic. One topic should produce one concise page; several topics need their distinctions preserved. Do not hard-code three topics, split one idea artificially, or add a separate cover or conclusion page.

Use roughly 12pt body text and at least 11pt for essential print labels. If a topic overflows, edit its content or simplify its application. Do not reduce type below readable sizes, crop overflow, scale the page, or hide necessary material to meet the limit. Allow natural vertical scrolling on phones. Break before subsequent concept pages in print, and verify actual pagination rather than relying on `break-inside: avoid` alone. Keep optional source records outside the study.

## Build the file

In a coding agent, use the task's authorised output area or a new `meditations/YYYY-MM-DD-topic/` directory. Use a suffix if that directory exists; do not overwrite another study. In Claude Chat, use its file-creation area and provide a downloadable `meditation.html`.

Inline CSS, JavaScript and essential assets. Use bundled system fonts and their fallbacks; do not fetch fonts or depend on a CDN. Inline diagrams can use HTML and SVG. No package install, build server, account or internet connection is needed to open the finished file. Do not add analytics, trackers, network calls or required browser storage.

Use native HTML controls for meaningful interactions. Keep the core explanation and both sides of a worked conclusion readable when JavaScript is unavailable. Print output must include the necessary explanations and omit inactive controls. Do not hide sensitive information in comments, scripts, accessible labels or unused DOM.

Keep source ledgers, design records, critique, prompts, raw transcripts and internal record-state labels such as `NO RECORD` outside the final HTML. Keep internal states in private source notes; communicate an actual recording decision in ordinary language when relevant. Private study creation is authorised output. Saving a lasting lesson, updating memory or sharing the study is a separate action governed by the user's permission.

## Verify and deliver

When a browser is available, inspect desktop and 390px layouts and exercise the meaningful interactions with keyboard and pointer. Check for overflow, clipping, small type, missing labels and confusing feedback. Test the no-JavaScript and print versions. Render A4 and inspect every page: confirm each concept stays within one readable page and that the opening shares the first topic. Check topic-to-page mapping as well as total count. Check computed examples against actual results and ensure the final file makes no remote requests.

If browser execution is unavailable, still create the HTML, inspect its structure and arithmetic where possible, and state that rendering and interaction checks were not run. Do not claim verified behaviour from reading source alone. If file creation itself is unavailable, give a text reflection and explain that no HTML file was created.

Deliver a clickable file or download link and one brief sentence naming the topics. State any actual recording decision plainly when relevant; omit the internal closing checklist. Do not repeat the full study in chat. The absence of StyleRef does not require the user's attention when the bundled fallback succeeds.
