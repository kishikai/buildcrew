# build-crew

A Claude Code plugin that turns your main session into a lead dev and hands the routine work to two cheaper helpers. It also gives you a live page where you can watch the work happen.

I built it because staring at a terminal with no idea what's going on gets old fast. Now I keep the tracker open and see which helper is running, which model it's on, and what it's doing.

## What you get

| Part | Job | Model |
|---|---|---|
| Your main session | Plans, makes the hard calls, reviews every helper's work, commits | Whatever you picked for the session |
| `build-crew:searcher` | Reads the code and answers "where is X" questions. It can't edit anything. | Haiku |
| `build-crew:implementer` | Builds what it's told to build, writes tests and runs them. It never commits. | Sonnet |
| `build-crew:progress-tracker` | A skill that creates a live dashboard on claude.ai and keeps it up to date | Your main session |

A start-of-session hook adds the working rules to every session, so there's nothing to paste into `CLAUDE.md`.

## Install

In Claude Code, add this repo as a plugin source:

```
/plugin marketplace add kishikai/buildcrew
```

Then install the plugin from it:

```
/plugin install build-crew@build-crew
```

To install from a local copy, such as an unzipped download, point at the folder instead:

```
/plugin marketplace add ./buildcrew
```

For cloud sessions on claude.ai/code, put this in the environment's setup script:

```bash
claude plugin marketplace add kishikai/buildcrew
claude plugin install build-crew@build-crew --scope user
```

## Using it

The helpers get used once a plan is settled. You can also ask for one by name, for example: "have the searcher find every caller of save_message".

For the tracker, say "set up a progress tracker for this project". Claude then:

1. asks what to call a step (sprint, milestone, phase);
2. creates the page and fills in your plan;
3. updates it whenever a step or a helper starts or finishes.

The page redraws by itself, so you can leave it open in another tab.

The tracker's link is saved in your project as `.claude/build-tracker.json`. Commit that file if you want sessions elsewhere to keep using the same page.

Two things to know about the tracker:

- It's a claude.ai artifact, so it needs Claude Code signed in with a claude.ai account. Without that the helpers still work; Claude just won't offer the tracker.
- The page is private until you share it from its Share menu.

## Changing things

- **Models:** edit `model:` in `agents/searcher.md` and `agents/implementer.md`. The aliases `haiku` and `sonnet` follow the newest version. A full ID such as `claude-sonnet-5-5` pins one.
- **Rules:** edit `context/working-model.md`. It's plain text and goes into every session as it is.
- **Tracker page:** edit `skills/progress-tracker/template/index.html`. `render.py` fills in the project name and your word for a step.

## What's in the repo

```
.claude-plugin/plugin.json        plugin manifest
.claude-plugin/marketplace.json   lets /plugin install from this repo
agents/                           searcher (Haiku) and implementer (Sonnet)
context/working-model.md          the rules added to every session
hooks/hooks.json                  the start-of-session hook that adds them
skills/progress-tracker/          tracker skill, page template, render script
```

## Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md).

## Credits

This README was edited with [humanizer](https://github.com/blader/humanizer) by Siqi Chen ([@blader](https://github.com/blader)), MIT licensed. Its licence notice is in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

MIT. See [LICENSE](LICENSE).
