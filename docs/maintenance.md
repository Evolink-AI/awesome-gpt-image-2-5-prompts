# Maintenance

The initial collection contains 250 complete prompts across seven categories. `data/prompts.json` stores the English metadata and original prompt texts. `data/content-layout.json` defines category routing. The category Markdown files are the readable case collection, and each README links to every case in its language.

Review additions when a contributor supplies a complete public prompt and attributable media. Verify model claims against the source, keep them attributed to the creator, and record external input requirements. Do not infer a prompt from an image or silently repair original syntax. Exclude incomplete or promptless submissions.

For updates, preserve existing case identifiers and attribution. Update English first, then have each language’s visible text reviewed. Run `python3 scripts/verify_content.py`, check source and media links, and inspect desktop and narrow renderings before publishing. No scheduled update service is configured by this repository.

Use issues for source corrections and removal requests. Record published content changes in `docs/update-log.md`.
