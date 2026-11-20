# Working model (build-crew plugin)

The main session is the lead. It plans, makes architecture, security and ambiguous decisions, reviews helpers' work, and makes git commits and pushes.

Routine work goes to two helpers from this plugin:
- `build-crew:searcher` (Haiku, read-only) explores the codebase, finds callers, files and conventions, and answers lookups.
- `build-crew:implementer` (Sonnet) builds well-specified changes with tests once the plan is decided. It never commits.

Every helper result is reviewed before it is acted on or committed. Hard, security-sensitive or ambiguous work stays in the main session.

Progress tracking: when the project has `.claude/build-tracker.json`, that file holds the URL of a live tracker page, and the `build-crew:progress-tracker` skill describes how to keep it current as milestones and helpers start and finish. When a multi-step plan starts and the project has no tracker, offering one fits.
