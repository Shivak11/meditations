# Install Meditations in Claude without a terminal

## Outcome

A first-time visitor can download `meditations.zip` from the repository root, upload it through Claude's Skills interface, and copy a prompt into the conversation they want to review. Command-line installation follows this primary route.

## Locked decisions

- The ready-to-upload ZIP lives at the repository root, with a direct README download link. It is not the GitHub repository source archive.
- The ZIP contains one `meditations/` folder with `SKILL.md`, all three reference documents and the MIT licence. It contains no development records or personal material.
- The main README route uses Claude on a computer: enable code execution, upload under Customize > Skills and turn the skill on, then use a copyable prompt in the work conversation.
- Instructions distinguish an enabled skill from a one-chat attachment and do not claim that pasting a prompt installs a skill.
- Keep the existing name and reflection procedure. Shorten the description to meet the Claude Help Center's documented 200-character limit. Explain how conversation evidence and approved record downloads work in Claude Chat without assuming access to the user's computer.
- Keep `npx skills add Shivak11/meditations` as the secondary route for coding-agent users.

## Ownership

- Orchestrator: README.md, this plan, skills/meditations/SKILL.md, skills/meditations/references/declared-preferences.md, integration, commits, validation and GitHub readback.
- Package worker: scripts/package_skill.py and meditations.zip only. Do not change skill content or documentation. The orchestrator regenerates the archive after content changes settle.
- Independent review: read the finished documentation and archive without editing. Check the beginner journey, package layout, content parity and claims about installation and persistence.

## Validation

1. Inspect the archive: one matching top-level folder, required files, no repository wrapper, no metadata or unrelated files.
2. Compare every archived source with the final files on disk and check reproducible packaging.
3. Check YAML name and description, relative resource links, direct download URL, placement of ZIP instructions before npx and the copyable prompt.
4. Read the diff and audit the complete git status before each commit.
5. Push only this requested public update. Fetch main immediately before integration to preserve concurrent work. Verify the published README and download bytes from GitHub.
6. Report whether native Claude upload was exercised separately from static package and documentation checks. Do not change a signed-in Claude account merely to test the documentation.

## Sources checked

- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

Checked on 11 September 2026.
