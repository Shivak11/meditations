# Bundled study designs

These five original CSS systems work offline with fonts already available on the reader's device. They do not need a design service, an account or a package installation. Each supplies typography, responsive layout primitives, focus treatment, print rules and reduced-motion rules. The diagram itself should explain the subject under study.

## Select a system for a new study

Run the selector from the skill directory:

```sh
python3 scripts/select_design.py
```

Read the returned JSON. Its `css` path is relative to the skill directory. Open that CSS file and copy its complete contents into the HTML's `<style>` element so the study remains a single offline file. Follow the returned `brief` when composing the page. Keep selection details in a private source record outside the HTML; the reader does not need a design-system label on the page.

If up to three recent selections are available in the current conversation or an already authorised record, pass their IDs:

```sh
python3 scripts/select_design.py --exclude paper-notes --exclude dark-study
```

The selector chooses uniformly among eligible systems with Python's `SystemRandom`. It does not use the date, inspect transcripts or save history. An unknown historical ID is ignored and listed in `ignored_exclusions`. If exclusions remove every eligible system, it retains the requested study kind and resets exclusions for that selection; `exclusions_reset` reports this. With no history, simply run it without exclusions.

Use `--kind comparison`, `--kind process`, `--kind concept` or `--kind decision` only when restricting the composition helps the subject. Omit it for the full catalogue. `--seed 42` is available for repeatable tests; seeded selection is reported as `seeded`. Do not use a fixed seed for normal new studies.

When code execution is unavailable but the bundled files are readable, choose a suitable system from the catalogue manually. Record `selection_method: manual` in private metadata. Do not claim that a manual choice was random. If the files are also unavailable, follow the text fallback in the main skill; do not claim to have used bundled CSS that you could not read.

Preserve the selected ID and CSS during revisions to the same study. A correction to the wording or diagram does not require another random choice. Change systems when the user requests a redesign or a new study begins.

## The five systems

| System | Typography and layout | Diagram treatment |
|---|---|---|
| Paper notes (`paper-notes`) | Georgia body text, sans-serif headings, warm white ground and occasional margin notes beside a continuous reading column. | Fine rules with open nodes and written annotations; use paired evidence where a distinction matters. |
| Colour blocks (`colour-blocks`) | System sans-serif throughout, large bold headings and broad blue or pale teal section bands. | Use aligned regions for comparison and numbered steps with an explicit order; colour always accompanies labels. |
| Technical diagrams (`technical-diagrams`) | System sans-serif body text, monospace headings and labels, square corners and compact ruled figure frames. | Show input, operation and result in aligned nodes; label each edge with the condition or relationship it represents. |
| Editorial study (`editorial-study`) | System sans-serif body text, large Georgia headings, a narrower reading column and occasional full-width figures. | Give one figure room to explain the main relationship; use prose and captions around it rather than boxing every paragraph. |
| Dark study (`dark-study`) | System sans-serif body text, sans-serif headings, light text on charcoal and a muted mint accent. | Use outlined groups and clear boundaries, with stronger emphasis for the selected or changed state. |

The catalogue is in [registry.json](../assets/design-systems/registry.json). Adapt these systems to the study. Choose a topic-specific comparison, process trace, concept map or decision explanation that matches the actual evidence. A system does not prescribe a canvas, a card grid, icons or a diagram count. Use semantic HTML for text and native controls; add inline SVG only when spatial relationships help. Do not add decorative icons or invented measurements.

## HTML primitives

Include `<meta name="viewport" content="width=device-width, initial-scale=1">`. Use one `<main class="study">`, with a plain `<h1>`, a sentence explaining the study, and the actual content. `.reading` limits long prose to a readable line length; `.lead` marks the opening explanation. `.wide` gives a figure more room where the system supports it. `.with-note` can wrap a reading section and an occasional `<aside class="note">`.

`.comparison` places two related sections beside one another on wider screens and stacks them on small screens. `.sequence` is intended for an ordered list whose list items represent actual steps. `.diagram` frames a figure; `.node` and `.connector` style elements in an inline SVG. `.node` sets SVG fill and stroke, so use `.diagram-node` for a node made from HTML. Set an SVG's `viewBox` to fit the content and provide a title and description with `aria-labelledby`. Keep SVG text large enough at the rendered width; recompose dense diagrams for mobile instead of shrinking the labels.

Use native `<details><summary>…</summary>…</details>` for a reveal when it helps the reader think before comparing. Buttons and summary controls receive at least 44 pixels of height; standalone links and labels use the `.control` class when they are controls rather than prose. Keep ordinary prose links underlined. Group native checkbox and radio inputs inside their `<label>` so the complete 44-pixel label is clickable. The CSS does not supply interaction logic. Any added script must keep controls usable with a keyboard and preserve a readable page if the script fails.

The defaults use 20-pixel body text and 18-pixel captions. Avoid reducing these to fit more content. Keep text and controls within the supplied palette; the test suite checks normal-text contrast of at least 4.5:1 and meaningful non-text boundaries of at least 3:1. Pair colour with a written label, shape or other visible distinction. All systems remove decorative motion under `prefers-reduced-motion` and print with dark text on white.

Before delivery, inspect the study at desktop and phone widths, zoom in, use every reveal with the keyboard, and check print preview. For a printable answer that starts inside a closed disclosure, open it during printing and restore its previous state afterwards; browser handling of closed `<details>` varies. Check that diagram labels remain readable and connected to the right objects. These CSS defaults cannot verify the content or a later override.
