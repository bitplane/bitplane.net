# ganban

git-based Kanban TUI

![screen](https://bitplane.net/dev/python/ganban/ganban.png)

## What is this?

`ganban` is a Kanban board that lives in git. The data sits in an orphan branch,
so web UIs shouldn't offer to merge it (but they do). In `ganban`, we don't need
to rely on external services and API keys because our tasks stay with the code.
It's all just text files in dirs.

The board's columns are in directories named `id.slug` like `1.backlog`. They're
ordered alphanumerically so the TUI has the same order as `ls -l`. The app
renumbers them for you if you move columns around, or if you used letters or
something other than numbers as an id.

Cards in a column are symlinks to Markdown docs in the `./.all` dir, which holds
the actual data. These links are ordered in the same way as cards. Keeping them
in `.all` gives them stable IDs so you can link to them like you would in a
commit message. You don't need to remember `ln`'s weird syntax because `ganban`
rounds up stray files and replaces them with a link.

The first `# heading` in a document overrides the title of a card. Other
`# headings` or `## subheadings` become sections, and the TUI can choose a
custom editor for sections with special names. This is how comments and task
lists work, they're just markdown with a custom renderer.

You can add metadata like `labels`, a `due` date, `assigned` - or anything else
you like - using front-matter. A full YAML editor is provided for any custom
stuff, and some sensible editors are provided for the defaults.

Metadata works on columns too, you just edit the `index.md` file in their dir,
which you can use to override the column's style. The board itself has a title
and settings in its front-matter, which is how we link committers with multiple
emails to one identity, or give yourself an avatar like 🧔 or 🐴.

When running as a service, `ganban` syncs from remotes that the repo has,
periodically pushing to upstream and resolving any conflicts the best it can.
This creates a kind of mesh network for your board, syncing in the background
without the need for 3rd party services.

Ganban doesn't force you to use its TUI, there's a web UI if you prefer that
sort of thing. If you're a bot or a script, or UIs just aren't for you, then you
can use the CLI instead; see `ganban --help`. If you don't want any kind of
interface then bring your own text editor and commit directly to git.

It can sync in the background with `ganban sync -d`, or, if the daemons haunt
you, just omit the `-d` for a one-time sync.

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
---
whatever: put your metadata here
---
# Title

Main description goes here, displayed in the body. You can link to other cards
by ID like #1

## Notes

Subsequent sections become sidebar panels in the TUI.

## Comments

- [name](mailto:user@email): comments go here like this
```

### Columns

Directories with 1-digit numeric prefix for ordering:

```
1.backlog/
2.in-progress/
3.done/
```

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

Default digits: 3 for `.all/`, 1 for columns, 2 for symlinks.

## Git Integration

### Reading/Writing Without Checkout

Operates on the `ganban` branch without checking it out, using git plumbing:
- `git show ganban:path` to read
- `git hash-object`, `git mktree`, `git commit-tree` to write
- Or GitPython equivalents

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
