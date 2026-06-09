# Dogpile Cache Workbench Notes

This checkout has been converted into a standalone repository named
`dogpile-cache-workbench`.

## What Changed

- Added `dogpile/workbench_branding.py` for workbench name, source URL, and
  display version.
- Exposed the workbench branding constants from `dogpile`.
- Updated README, package URLs, and documentation links to this standalone
  repository.
- Added a focused branding test in `tests/test_workbench_branding.py`.

## Repository Isolation

The git history is rebuilt from this source snapshot. Only the new `origin`
remote should be configured after the private GitHub repository is created, so
branches from `sqlalchemy/dogpile.cache` will not be fetched automatically.
