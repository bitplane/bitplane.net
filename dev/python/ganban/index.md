# ganban

git-based Kanban TUI

## What is this?

Note: this is the plan. half of this isn't working yet. half of it is, and I'm
not saying which half.

`ganban` is a Kanban board that lives in git. It sits in an orphan branch so web
UIs don't offer to merge it. In `ganban`, our tasks stay with the code and we
don't need to rely on external services and API keys. It's just files in a dir.

The board's columns are directories named `id.slug` like `1.backlog`. They
don't need a numeric id, they're ordered alphanumerically so the TUI has the
same order as `ls -l`. The TUI will renumber them for you if you move columns
around.

Cards on a board are symlinks to Markdown docs in the `./.all` dir, which holds
the actual data. The links are ordered in the same way as cards. Keeping them in
`.all` gives them stable IDs, so you can link to them. `ganban` will round up
stray files and replace them with a link, so you don't need to remember `ln`'s
weird syntax.

The first `# heading`, if it's present, will override the title of a card. Any
`## subheading` becomes a section, and the TUI can choose a custom editor for
sections with special names. This is how comments and todo lists work.

You can also add metadata like labels, a due date, assignee, story points - or
anything else you like - using front-matter. Metadata works on columns too, by
editing the `index.md` file in their dir. And the board of course, which can
have a title and settings in its metadata.

When running as a service, `ganban` will sync from remotes that the repo has,
periodically pushing to upstream and resolving conflicts the best it can. This
creates a kind of mesh network for your board.

If you don't like the terminal, you can use the web UI (which looks just like
the TUI.) If you're a robot that isn't good at UIs, `ganban -d` will sync in the
background as you work. If the daemons haunt you, `ganban --sync` for manual
syncing. If you're a bot, there's context-friendly instructions for use in the
board's default `index.md`.

## Overview

Open a repo with ganban and it reads from a `ganban` orphan branch. The board
is just directories (columns) containing symlinks (cards) pointing to
canonical card files. Everything is plain markdown, works with any text
editor, and syncs via git.

## Data Model

### Cards

Canonical card files live in `.all/` with 3-digit numeric IDs:

```
.all/
  001.md
  002.md
  003.md
```

Card format:

```markdown
# Title of the card

Main description goes here, displayed in the body.

## Notes

Subsequent sections become sidebar panels in the TUI.

## Comments

**@user 2024-01-15**: Append-only, TUI adds name + date automatically.

## Links

- blocks [#42](../.all/042.md)
- see also [#7](../.all/007.md)
```

- Title from first `# heading`, not front-matter
- Content before first `##` = main body
- Each `##` = collapsible sidebar section
- `## Comments` = special append-only widget
- `## Links` = relationships, rendered specially
- Cross-references: type `#42`, stored as `[#42](../.all/042.md)` so links work everywhere
- Front-matter only for optional extras (tags, color, custom fields)

Tags on separate lines for clean merges:

```yaml
tags:
 - first
 - second
```

### Columns

Directories with 1-digit numeric prefix for ordering:

```
1.backlog/
2.in-progress/
3.done/
```

- Title from `index.md` first `# heading`, or normalized from dirname
- `in-progress` → `In progress`
- Hidden columns start with `.` (e.g., `.all`)
- Optional `index.md` for description and metadata

### Board Layout

Cards appear in columns as symlinks with 2-digit position prefix:

```
1.backlog/
  01.fix-login-bug.md -> ../.all/001.md
  02.add-feature.md -> ../.all/003.md
2.in-progress/
  01.refactor-api.md -> ../.all/002.md
```

- Symlink name = position + slug (derived from card title)
- Moving card between columns = delete + create symlink
- Reordering within column = rename symlinks
- Archiving = just delete the symlink, card stays in `.all/`
- Orphaned cards (in `.all/` but not linked) accessible via TUI

### Numbering

Default digits: 3 for `.all/`, 1 for columns, 2 for symlinks. Can extend with
hex or base64 if needed, but integers are the default.

## Git Integration

### Reading/Writing Without Checkout

Operates on the `ganban` branch without checking it out, using git plumbing:
- `git show ganban:path` to read
- `git hash-object`, `git mktree`, `git commit-tree` to write
- Or GitPython equivalents

### Sync Workflow

1. Commit before pull (TUI enforces this)
2. `git pull --rebase` on tasks branch
3. Reload board
4. If conflicts, show conflict UI

### Conflict Handling

- **Content conflicts**: git markers show in markdown, user edits them out
- **Broken symlinks**: highlight red, user picks destination or deletes
- **Column renames**: broken links surface as red cards, same fix

### Multi-Remote Sync

- One upstream (push target)
- Optional peer remotes (extra fetch sources)
- Fetch all remotes periodically
- On detecting changes: commit local, rebase, push upstream
- Changes propagate opportunistically through whoever can reach upstream

## Philosophy

- **Permissive**: don't be prescriptive, let users mess with files
- **Resilient**: handle broken states gracefully, offer to fix
- **Minimal**: derive what you can (titles, order), front-matter is opt-in
- **Portable**: works with any markdown renderer, any git host, any editor
