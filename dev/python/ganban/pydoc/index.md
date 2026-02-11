<a id="ganban"></a>

# ganban

<a id="ganban.model"></a>

# ganban.model

Reactive model tree.

<a id="ganban.model.node"></a>

# ganban.model.node

Reactive tree nodes with change notification and bubbling.

<a id="ganban.model.node.Node"></a>

## Node Objects

```python
class Node()
```

Reactive dict-like tree node.

Stores data in an internal dict, accessed via attribute syntax.
Setting a value to None deletes the key. Dict values are
auto-wrapped as child Nodes. Changes fire watchers and bubble
up through the parent chain.

<a id="ganban.model.node.Node.watch"></a>

#### watch

```python
def watch(key: str, callback: Callback) -> Callable[[], None]
```

Watch a key for changes. Returns an unwatch callable.

<a id="ganban.model.node.Node.keys"></a>

#### keys

```python
def keys()
```

Return children keys.

<a id="ganban.model.node.Node.items"></a>

#### items

```python
def items()
```

Return children items.

<a id="ganban.model.node.Node.values"></a>

#### values

```python
def values()
```

Return children values.

<a id="ganban.model.node.Node.path"></a>

#### path

```python
@property
def path() -> str
```

Dotted path from root to this node.

<a id="ganban.model.node.Node.update"></a>

#### update

```python
def update(other: Node) -> None
```

Update this node in-place to match other, preserving watchers.

<a id="ganban.model.node.Node.rename_key"></a>

#### rename\_key

```python
def rename_key(old_key: str, new_key: str) -> None
```

Rename a key in _children, preserving insertion order.

<a id="ganban.model.node.ListNode"></a>

## ListNode Objects

```python
class ListNode()
```

Ordered, id-keyed collection with change notification.

Items are accessed by string id. Setting to None deletes.
Dicts are auto-wrapped as Nodes. Changes fire watchers and
bubble up through the parent chain.

<a id="ganban.model.node.ListNode.watch"></a>

#### watch

```python
def watch(key: str, callback: Callback) -> Callable[[], None]
```

Watch an item id for changes. Returns an unwatch callable.

<a id="ganban.model.node.ListNode.path"></a>

#### path

```python
@property
def path() -> str
```

Dotted path from root to this node.

<a id="ganban.model.node.ListNode.keys"></a>

#### keys

```python
def keys()
```

Return ordered keys.

<a id="ganban.model.node.ListNode.items"></a>

#### items

```python
def items()
```

Return ordered (key, value) pairs.

<a id="ganban.model.node.ListNode.update"></a>

#### update

```python
def update(other: ListNode) -> None
```

Update this list in-place to match other, preserving watchers.

<a id="ganban.model.node.ListNode.rename_first_key"></a>

#### rename\_first\_key

```python
def rename_first_key(new_title: str) -> None
```

Rename the first key by rebuilding the list.

<a id="ganban.model.loader"></a>

# ganban.model.loader

Load a ganban board from git into a Node tree.

<a id="ganban.model.loader.file_creation_date"></a>

#### file\_creation\_date

```python
def file_creation_date(repo_path: str,
                       file_path: str,
                       branch: str = BRANCH_NAME) -> datetime | None
```

Get the author date of the commit that first added a file on a branch.

Returns None if the file has no history on the branch.

<a id="ganban.model.loader.load_board"></a>

#### load\_board

```python
def load_board(repo_path: str, branch: str = BRANCH_NAME) -> Node
```

Load a complete board from a git branch as a Node tree.

<a id="ganban.model.card"></a>

# ganban.model.card

Card mutation operations for ganban boards.

<a id="ganban.model.card.create_card"></a>

#### create\_card

```python
def create_card(board: Node,
                title: str,
                body: str = "",
                column: Node | None = None,
                position: int | None = None) -> tuple[str, Node]
```

Create a new card and add it to the board.

Returns (card_id, card_node).

<a id="ganban.model.card.find_card_column"></a>

#### find\_card\_column

```python
def find_card_column(board: Node, card_id: str) -> Node | None
```

Find the column containing a card.

<a id="ganban.model.card.move_card"></a>

#### move\_card

```python
def move_card(board: Node,
              card_id: str,
              target_column: Node,
              position: int | None = None) -> None
```

Move a card to target_column at position.

Handles same-column reorder atomically (single list assignment)
to avoid watchers removing the card widget between operations.

<a id="ganban.model.card.archive_card"></a>

#### archive\_card

```python
def archive_card(board: Node, card_id: str) -> None
```

Archive a card by removing it from its column's links.

<a id="ganban.model.writer"></a>

# ganban.model.writer

Save a ganban board (Node tree) to git without touching the working tree.

<a id="ganban.model.writer.MergeRequired"></a>

## MergeRequired Objects

```python
@dataclass
class MergeRequired()
```

Returned by check_for_merge when the branch has diverged.

<a id="ganban.model.writer.save_board"></a>

#### save\_board

```python
def save_board(board: Node,
               message: str = "Update board",
               branch: str = BRANCH_NAME,
               parents: list[str] | None = None) -> str
```

Save a board to git and return the new commit hash.

<a id="ganban.model.writer.check_for_merge"></a>

#### check\_for\_merge

```python
def check_for_merge(board: Node,
                    branch: str = BRANCH_NAME) -> MergeRequired | None
```

Check if saving would require a merge.

<a id="ganban.model.writer.check_remote_for_merge"></a>

#### check\_remote\_for\_merge

```python
def check_remote_for_merge(board: Node,
                           remote: str = "origin",
                           branch: str = BRANCH_NAME) -> MergeRequired | None
```

Check if a remote has changes that need merging.

<a id="ganban.model.writer.try_auto_merge"></a>

#### try\_auto\_merge

```python
def try_auto_merge(board: Node,
                   merge_info: MergeRequired,
                   message: str = "Merge changes",
                   branch: str = BRANCH_NAME) -> str | None
```

Attempt an automatic merge if there are no conflicts.

Returns the new merge commit hash if successful, None if there are conflicts.

<a id="ganban.model.column"></a>

# ganban.model.column

Column mutation operations for ganban boards.

<a id="ganban.model.column.slugify"></a>

#### slugify

```python
def slugify(text: str) -> str
```

Convert text to a URL-friendly slug.

<a id="ganban.model.column.build_column_path"></a>

#### build\_column\_path

```python
def build_column_path(order: str, name: str, hidden: bool = False) -> str
```

Build column directory path from components.

<a id="ganban.model.column.create_column"></a>

#### create\_column

```python
def create_column(board: Node,
                  name: str,
                  order: str | None = None,
                  hidden: bool = False) -> Node
```

Create a new column and add it to the board.

Returns the created column Node.

<a id="ganban.model.column.move_column"></a>

#### move\_column

```python
def move_column(board: Node, column: Node, new_index: int) -> None
```

Move column to new_index in the board's columns ListNode.

Rebuilds the columns ListNode with updated order values and dir_paths.

<a id="ganban.model.column.archive_column"></a>

#### archive\_column

```python
def archive_column(board: Node, column_order: str) -> None
```

Archive a column by removing it from the board.

<a id="ganban.model.column.rename_column"></a>

#### rename\_column

```python
def rename_column(board: Node, column: Node, new_name: str) -> None
```

Rename a column: update its sections title and dir_path.

<a id="ganban.ids"></a>

# ganban.ids

Card ID comparison and generation.

<a id="ganban.ids.compare_ids"></a>

#### compare\_ids

```python
def compare_ids(left: str, right: str) -> int
```

Compare two IDs, padding with leading zeros.

Returns -1 if left < right, 0 if equal, 1 if left > right.

<a id="ganban.ids.max_id"></a>

#### max\_id

```python
def max_id(ids: list[str]) -> str | None
```

Find the highest ID from a list, or None if empty.

<a id="ganban.ids.next_id"></a>

#### next\_id

```python
def next_id(current_max: str | None) -> str
```

Generate the next ID after current_max.

- If None, returns "001"
- If numeric (e.g., "99"), returns str(int + 1) (e.g., "100")
- If non-numeric (e.g., "fish"), returns "1" + "0" * len (e.g., "10000")

<a id="ganban.git"></a>

# ganban.git

Git operations for ganban, with sync and async variants.

<a id="ganban.git.read_ganban_config"></a>

#### read\_ganban\_config

```python
def read_ganban_config(repo_path: str | Path) -> dict
```

Read ganban.* keys from local git config, returned as python-keyed dict.

<a id="ganban.git.write_ganban_config_key"></a>

#### write\_ganban\_config\_key

```python
def write_ganban_config_key(repo_path: str | Path, key: str, value) -> None
```

Write one ganban.* key to local git config.

key is the python name (e.g. sync_interval), converted to git name (sync-interval).

<a id="ganban.git.is_git_repo"></a>

#### is\_git\_repo

```python
def is_git_repo(path: str | Path) -> bool
```

Check if path is inside a git repository.

<a id="ganban.git.init_repo"></a>

#### init\_repo

```python
def init_repo(path: str | Path) -> Repo
```

Initialize a new git repository at path.

<a id="ganban.git.get_remotes_sync"></a>

#### get\_remotes\_sync

```python
def get_remotes_sync(repo_path: str | Path) -> list[str]
```

Get list of remote names for a repository.

<a id="ganban.git.fetch_sync"></a>

#### fetch\_sync

```python
def fetch_sync(repo_path: str | Path, remote_name: str) -> None
```

Fetch from a specific remote.

<a id="ganban.git.push_sync"></a>

#### push\_sync

```python
def push_sync(repo_path: str | Path,
              remote_name: str,
              branch: str = "ganban") -> None
```

Push a branch to a remote.

<a id="ganban.git.get_upstream"></a>

#### get\_upstream

```python
def get_upstream(repo_path: str | Path,
                 branch: str = "ganban") -> tuple[str, str] | None
```

Get the upstream remote and branch for a local branch.

Returns (remote_name, remote_branch) or None if no tracking branch is set.

<a id="ganban.git.remote_has_branch"></a>

#### remote\_has\_branch

```python
def remote_has_branch(repo_path: str | Path,
                      remote_name: str,
                      branch: str = "ganban") -> bool
```

Check if refs/remotes/{remote}/{branch} exists.

<a id="ganban.git.has_branch"></a>

#### has\_branch

```python
async def has_branch(repo_path: str | Path, branch: str = "ganban") -> bool
```

Check if a branch exists in the repository.

<a id="ganban.git.get_remotes"></a>

#### get\_remotes

```python
async def get_remotes(repo_path: str | Path) -> list[str]
```

Get list of remote names for a repository.

<a id="ganban.git.fetch"></a>

#### fetch

```python
async def fetch(repo_path: str | Path, remote_name: str) -> None
```

Fetch from a specific remote.

<a id="ganban.git.push"></a>

#### push

```python
async def push(repo_path: str | Path,
               remote_name: str,
               branch: str = "ganban") -> None
```

Push a branch to a remote.

<a id="ganban.git.create_orphan_branch"></a>

#### create\_orphan\_branch

```python
async def create_orphan_branch(repo_path: str | Path,
                               branch: str = "ganban") -> str
```

Create an orphan branch with an empty commit.

Does not touch the working tree. Returns the commit hash.

<a id="ganban.cli.init"></a>

# ganban.cli.init

Handler for 'ganban init'.

<a id="ganban.cli.init.init_board"></a>

#### init\_board

```python
def init_board(args) -> int
```

Initialize a ganban board in the repository.

<a id="ganban.cli"></a>

# ganban.cli

CLI argument parser and dispatch for ganban.

<a id="ganban.cli.build_parser"></a>

#### build\_parser

```python
def build_parser() -> argparse.ArgumentParser
```

Build the full CLI argument parser.

<a id="ganban.cli._common"></a>

# ganban.cli.\_common

Shared helpers for CLI command handlers.

<a id="ganban.cli._common.load_board_or_die"></a>

#### load\_board\_or\_die

```python
def load_board_or_die(repo: str, json_mode: bool) -> Node
```

Load board from repo path. Exit 1 with message if not found.

<a id="ganban.cli._common.find_column"></a>

#### find\_column

```python
def find_column(board: Node, col_id: str, json_mode: bool) -> Node
```

Lookup column by order ID. Exit 1 listing available columns if not found.

<a id="ganban.cli._common.find_card"></a>

#### find\_card

```python
def find_card(board: Node, card_id: str, json_mode: bool) -> Node
```

Lookup card by ID. Exit 1 if not found.

<a id="ganban.cli._common.save"></a>

#### save

```python
def save(board: Node, message: str) -> str
```

Save board and return commit hash.

<a id="ganban.cli._common.output_json"></a>

#### output\_json

```python
def output_json(data: dict | list) -> None
```

Write JSON to stdout.

<a id="ganban.cli._common.error"></a>

#### error

```python
def error(message: str, json_mode: bool) -> None
```

Print error to stderr and exit 1.

<a id="ganban.cli._common.sections_to_markdown"></a>

#### sections\_to\_markdown

```python
def sections_to_markdown(sections: ListNode, meta) -> str
```

Convert sections ListNode + meta to markdown string.

<a id="ganban.cli._common.meta_to_dict"></a>

#### meta\_to\_dict

```python
def meta_to_dict(meta) -> dict
```

Convert meta Node to plain dict.

<a id="ganban.cli._common.markdown_to_sections"></a>

#### markdown\_to\_sections

```python
def markdown_to_sections(text: str) -> tuple[ListNode, dict]
```

Parse markdown text into (ListNode, meta_dict).

<a id="ganban.cli.board"></a>

# ganban.cli.board

Handlers for 'ganban board' commands.

<a id="ganban.cli.board.board_summary"></a>

#### board\_summary

```python
def board_summary(args) -> int
```

Show board summary: title, columns, card counts.

<a id="ganban.cli.board.board_get"></a>

#### board\_get

```python
def board_get(args) -> int
```

Dump board index.md content.

<a id="ganban.cli.board.board_set"></a>

#### board\_set

```python
def board_set(args) -> int
```

Write board index.md from stdin.

<a id="ganban.cli.card"></a>

# ganban.cli.card

Handlers for 'ganban card' commands.

<a id="ganban.cli.card.card_list"></a>

#### card\_list

```python
def card_list(args) -> int
```

List cards grouped by column.

<a id="ganban.cli.card.card_get"></a>

#### card\_get

```python
def card_get(args) -> int
```

Dump card markdown content.

<a id="ganban.cli.card.card_set"></a>

#### card\_set

```python
def card_set(args) -> int
```

Write card markdown from stdin.

<a id="ganban.cli.card.card_add"></a>

#### card\_add

```python
def card_add(args) -> int
```

Create a new card.

<a id="ganban.cli.card.card_move"></a>

#### card\_move

```python
def card_move(args) -> int
```

Move a card to a column.

<a id="ganban.cli.card.card_archive"></a>

#### card\_archive

```python
def card_archive(args) -> int
```

Archive a card.

<a id="ganban.cli.sync"></a>

# ganban.cli.sync

Handlers for 'ganban sync' command.

<a id="ganban.cli.sync.sync"></a>

#### sync

```python
def sync(args) -> int
```

One-shot sync handler. Dispatches to daemon if -d.

<a id="ganban.cli.sync.sync_daemon"></a>

#### sync\_daemon

```python
def sync_daemon(args, repo_path: str) -> int
```

Loop _do_sync on interval. SIGINT/SIGTERM stops cleanly.

<a id="ganban.cli.column"></a>

# ganban.cli.column

Handlers for 'ganban column' commands.

<a id="ganban.cli.column.column_list"></a>

#### column\_list

```python
def column_list(args) -> int
```

List all columns.

<a id="ganban.cli.column.column_get"></a>

#### column\_get

```python
def column_get(args) -> int
```

Dump column index.md content.

<a id="ganban.cli.column.column_set"></a>

#### column\_set

```python
def column_set(args) -> int
```

Write column index.md from stdin.

<a id="ganban.cli.column.column_add"></a>

#### column\_add

```python
def column_add(args) -> int
```

Create a new column.

<a id="ganban.cli.column.column_move"></a>

#### column\_move

```python
def column_move(args) -> int
```

Move a column to a new position.

<a id="ganban.cli.column.column_rename"></a>

#### column\_rename

```python
def column_rename(args) -> int
```

Rename a column.

<a id="ganban.cli.column.column_archive"></a>

#### column\_archive

```python
def column_archive(args) -> int
```

Archive a column.

<a id="ganban.__main__"></a>

# ganban.\_\_main\_\_

Entry point for ganban CLI.

<a id="ganban.ui.markdown"></a>

# ganban.ui.markdown

Markdown-it plugins for ganban.

<a id="ganban.ui.markdown.mailto_display_plugin"></a>

#### mailto\_display\_plugin

```python
def mailto_display_plugin(md: MarkdownIt, meta: Node,
                          committers: list[str] | None) -> None
```

Core rule replacing mailto link text with emoji + name.

<a id="ganban.ui.markdown.card_ref_plugin"></a>

#### card\_ref\_plugin

```python
def card_ref_plugin(md: MarkdownIt, board: Node) -> None
```

Core rule replacing `NNN` card references with links.

<a id="ganban.ui.markdown.ganban_parser_factory"></a>

#### ganban\_parser\_factory

```python
def ganban_parser_factory(board: Node | None)
```

Return a parser_factory closure for Textual's Markdown widget.

<a id="ganban.ui.blocked"></a>

# ganban.ui.blocked

Blocked toggle widget for card detail screen.

<a id="ganban.ui.blocked.BlockedWidget"></a>

## BlockedWidget Objects

```python
class BlockedWidget(NodeWatcherMixin, Container)
```

Inline blocked toggle that reads and writes ``meta.blocked``.

Shows 🚧 when blocked, 🏭 when not. Click to toggle.

<a id="ganban.ui.search"></a>

# ganban.ui.search

Autocomplete search input with dropdown suggestions.

<a id="ganban.ui.search.SearchInput"></a>

## SearchInput Objects

```python
class SearchInput(Container)
```

Text input with a filterable dropdown of suggestions.

Options are (label, value) tuples. The label is shown in the dropdown,
the value is returned on selection. Free-text is always allowed.

<a id="ganban.ui.search.SearchInput.Submitted"></a>

## Submitted Objects

```python
class Submitted(Message)
```

Posted when the user submits a selection or free text.

<a id="ganban.ui.search.SearchInput.Cancelled"></a>

## Cancelled Objects

```python
class Cancelled(Message)
```

Posted when the user cancels (double-escape).

<a id="ganban.ui.search.SearchInput.set_options"></a>

#### set\_options

```python
def set_options(options: list[tuple[str, str]]) -> None
```

Replace the option list.

<a id="ganban.ui.search.SearchInput.on_input_changed"></a>

#### on\_input\_changed

```python
def on_input_changed(event: Input.Changed) -> None
```

Filter dropdown on every keystroke.

<a id="ganban.ui.search.SearchInput.on_option_list_option_selected"></a>

#### on\_option\_list\_option\_selected

```python
def on_option_list_option_selected(event: OptionList.OptionSelected) -> None
```

Handle mouse click on a dropdown item.

<a id="ganban.ui.search.SearchInput.on_descendant_blur"></a>

#### on\_descendant\_blur

```python
def on_descendant_blur(event: DescendantBlur) -> None
```

Close dropdown when focus leaves a child widget.

<a id="ganban.ui.confirm"></a>

# ganban.ui.confirm

Compact inline confirmation widget.

<a id="ganban.ui.confirm.ConfirmButton"></a>

## ConfirmButton Objects

```python
class ConfirmButton(Static)
```

A button that shows a confirm/cancel menu on click.

Shows a single icon (default: ❌). When clicked, opens a context menu
with ❌ (cancel) and ✅ (confirm). Emits Confirmed message on confirm.

<a id="ganban.ui.confirm.ConfirmButton.Confirmed"></a>

## Confirmed Objects

```python
class Confirmed(Message)
```

Emitted when the action is confirmed.

<a id="ganban.ui.assignee"></a>

# ganban.ui.assignee

Assignee widget with user picker.

<a id="ganban.ui.assignee.resolve_assignee"></a>

#### resolve\_assignee

```python
def resolve_assignee(assigned: str, board: Node) -> tuple[str, str, str]
```

Parse an assigned string and resolve against board users.

Returns (emoji, display_name, email). Board users override the
name and emoji from the parsed committer string.

<a id="ganban.ui.assignee.build_assignee_options"></a>

#### build\_assignee\_options

```python
def build_assignee_options(board: Node) -> list[tuple[str, str]]
```

Build options for the assignee SearchInput from board users and git committers.

Returns (label, value) tuples where label includes emoji and value is the
committer string.

<a id="ganban.ui.assignee.AssigneeWidget"></a>

## AssigneeWidget Objects

```python
class AssigneeWidget(NodeWatcherMixin, Container)
```

Inline assignee display with user picker.

Reads and writes ``meta.assigned`` on the given card meta Node,
and watches the node so external changes are reflected immediately.

<a id="ganban.ui.due"></a>

# ganban.ui.due

Due date widget with inline editing.

<a id="ganban.ui.due.DueDateWidget"></a>

## DueDateWidget Objects

```python
class DueDateWidget(NodeWatcherMixin, Container)
```

Inline due date display with calendar picker.

Reads and writes ``meta.due`` on the given Node directly,
and watches the node so external changes (e.g. the meta editor)
are reflected immediately.

<a id="ganban.ui.menu"></a>

# ganban.ui.menu

Context menu system for ganban UI.

<a id="ganban.ui.menu.MenuItem"></a>

## MenuItem Objects

```python
class MenuItem(Static)
```

A focusable menu item.

<a id="ganban.ui.menu.MenuItem.Clicked"></a>

## Clicked Objects

```python
class Clicked(Message)
```

Posted when this item is clicked.

<a id="ganban.ui.menu.MenuSeparator"></a>

## MenuSeparator Objects

```python
class MenuSeparator(Static)
```

A horizontal separator line.

<a id="ganban.ui.menu.MenuRow"></a>

## MenuRow Objects

```python
class MenuRow(Horizontal)
```

A horizontal row of menu items within a vertical menu.

<a id="ganban.ui.menu.MenuRow.get_focusable_items"></a>

#### get\_focusable\_items

```python
def get_focusable_items() -> list[MenuItem]
```

Return enabled items in this row.

<a id="ganban.ui.menu.MenuRow.navigate"></a>

#### navigate

```python
def navigate(direction: int) -> MenuItem | None
```

Move focus by direction (+1/-1). Return new item, or None at edge.

<a id="ganban.ui.menu.MenuList"></a>

## MenuList Objects

```python
class MenuList(VerticalScroll)
```

Container for menu items.

<a id="ganban.ui.menu.MenuList.Ready"></a>

## Ready Objects

```python
class Ready(Message)
```

Posted when menu has been laid out and has a size.

<a id="ganban.ui.menu.MenuList.on_resize"></a>

#### on\_resize

```python
def on_resize(event) -> None
```

Notify when we have actual dimensions.

<a id="ganban.ui.menu.MenuList.get_navigable_items"></a>

#### get\_navigable\_items

```python
def get_navigable_items() -> list[tuple[Static, list[MenuItem]]]
```

Return (top_level_child, focusable_descendants) for vertical nav.

A plain MenuItem has [itself]. A container has its focusable MenuItems.
Non-focusable items (separators) are skipped.

<a id="ganban.ui.menu.ContextMenu"></a>

## ContextMenu Objects

```python
class ContextMenu(ModalScreen[MenuItem | None])
```

Context menu with keyboard navigation.

<a id="ganban.ui.menu.ContextMenu.ItemSelected"></a>

## ItemSelected Objects

```python
class ItemSelected(Message)
```

Posted when an item is selected.

<a id="ganban.ui.menu.ContextMenu.on_menu_list_ready"></a>

#### on\_menu\_list\_ready

```python
def on_menu_list_ready(event: MenuList.Ready) -> None
```

Adjust menu position when we know actual dimensions.

<a id="ganban.ui.menu.ContextMenu.on_descendant_focus"></a>

#### on\_descendant\_focus

```python
def on_descendant_focus(event) -> None
```

React to any focus change within the menu.

<a id="ganban.ui.menu.ContextMenu.action_focus_prev"></a>

#### action\_focus\_prev

```python
def action_focus_prev() -> None
```

Focus the previous enabled item in current menu (wraps around).

<a id="ganban.ui.menu.ContextMenu.action_focus_next"></a>

#### action\_focus\_next

```python
def action_focus_next() -> None
```

Focus the next enabled item in current menu (wraps around).

<a id="ganban.ui.menu.ContextMenu.action_select_item"></a>

#### action\_select\_item

```python
def action_select_item() -> None
```

Select leaf item or enter submenu.

<a id="ganban.ui.menu.ContextMenu.action_navigate_right"></a>

#### action\_navigate\_right

```python
def action_navigate_right() -> None
```

Move right in row, or enter submenu / select.

<a id="ganban.ui.menu.ContextMenu.action_navigate_left"></a>

#### action\_navigate\_left

```python
def action_navigate_left() -> None
```

Move left in row, or close submenu.

<a id="ganban.ui.menu.ContextMenu.action_close"></a>

#### action\_close

```python
def action_close() -> None
```

Close the entire menu.

<a id="ganban.ui.menu.ContextMenu.on_menu_item_clicked"></a>

#### on\_menu\_item\_clicked

```python
def on_menu_item_clicked(event: MenuItem.Clicked) -> None
```

Handle item click.

<a id="ganban.ui.menu.ContextMenu.on_click"></a>

#### on\_click

```python
def on_click(event: Click) -> None
```

Dismiss menu when clicking outside.

<a id="ganban.ui.menu.ContextMenu.on_calendar_menu_item_selected"></a>

#### on\_calendar\_menu\_item\_selected

```python
def on_calendar_menu_item_selected(event) -> None
```

Handle calendar menu item selection.

<a id="ganban.ui.watcher"></a>

# ganban.ui.watcher

Mixin that manages Node watches with suppression and auto-cleanup.

<a id="ganban.ui.watcher.NodeWatcherMixin"></a>

## NodeWatcherMixin Objects

```python
class NodeWatcherMixin()
```

Mixin for widgets that watch Node keys.

Subclasses should:
- Call ``_init_watcher()`` in ``__init__``
- Use ``self.node_watch(node, key, callback)`` instead of ``node.watch(...)``
- Use ``with self.suppressing():`` around model writes
- Skip writing ``on_unmount`` -- the mixin handles cleanup

<a id="ganban.ui.watcher.NodeWatcherMixin.node_watch"></a>

#### node\_watch

```python
def node_watch(node: Node | ListNode, key: str, callback: Callback) -> None
```

Register a watch that is auto-guarded by suppression and auto-cleaned on unmount.

<a id="ganban.ui.watcher.NodeWatcherMixin.suppressing"></a>

#### suppressing

```python
@contextmanager
def suppressing()
```

Context manager that suppresses watch callbacks for model writes.

<a id="ganban.ui.color"></a>

# ganban.ui.color

Color picker for columns.

<a id="ganban.ui.color.ColorSwatch"></a>

## ColorSwatch Objects

```python
class ColorSwatch(MenuItem)
```

A colored menu item that uses outline for focus instead of background.

<a id="ganban.ui.color.build_color_menu"></a>

#### build\_color\_menu

```python
def build_color_menu() -> list[MenuRow]
```

Build a 4x4 color picker grid with clear in place of black.

<a id="ganban.ui.color.ColorButton"></a>

## ColorButton Objects

```python
class ColorButton(Static)
```

A button that opens a color picker menu.

<a id="ganban.ui.color.ColorButton.ColorSelected"></a>

## ColorSelected Objects

```python
class ColorSelected(Message)
```

Posted when a color is selected.

<a id="ganban.ui"></a>

# ganban.ui

Textual UI for ganban.

<a id="ganban.ui.users"></a>

# ganban.ui.users

Users editor for board meta.

<a id="ganban.ui.users.EmailTag"></a>

## EmailTag Objects

```python
class EmailTag(Container)
```

A single email address tag — click to edit with committer search.

<a id="ganban.ui.users.AddEmailButton"></a>

## AddEmailButton Objects

```python
class AddEmailButton(Container)
```

Searchable input to add a new email address from git committers.

<a id="ganban.ui.users.UserRow"></a>

## UserRow Objects

```python
class UserRow(Vertical)
```

A single user card with title bar and email list.

<a id="ganban.ui.users.AddUserRow"></a>

## AddUserRow Objects

```python
class AddUserRow(Static)
```

EditableText with '+' to add a new user.

<a id="ganban.ui.users.UsersEditor"></a>

## UsersEditor Objects

```python
class UsersEditor(NodeWatcherMixin, Container)
```

Editor for board.meta.users -- a dict of display name -> user info.

<a id="ganban.ui.detail"></a>

# ganban.ui.detail

Detail modals for viewing and editing markdown content.

<a id="ganban.ui.detail.TabButton"></a>

## TabButton Objects

```python
class TabButton(Static)
```

A clickable tab icon button.

<a id="ganban.ui.detail.DetailModal"></a>

## DetailModal Objects

```python
class DetailModal(ModalScreen[None])
```

Base modal screen for detail editing.

<a id="ganban.ui.detail.DetailModal.on_click"></a>

#### on\_click

```python
def on_click(event: Click) -> None
```

Dismiss modal when clicking outside the detail container.

<a id="ganban.ui.detail.DetailModal.action_close"></a>

#### action\_close

```python
def action_close() -> None
```

Close the modal.

<a id="ganban.ui.detail.DetailModal.action_quit"></a>

#### action\_quit

```python
async def action_quit() -> None
```

Quit the app via the main save-and-exit path.

<a id="ganban.ui.detail.CardDetailModal"></a>

## CardDetailModal Objects

```python
class CardDetailModal(DetailModal)
```

Modal screen showing full card details.

<a id="ganban.ui.detail.CompactButton"></a>

## CompactButton Objects

```python
class CompactButton(Static)
```

Toggle button for compact/card view mode.

<a id="ganban.ui.detail.ColumnDetailModal"></a>

## ColumnDetailModal Objects

```python
class ColumnDetailModal(DetailModal)
```

Modal screen showing full column details.

<a id="ganban.ui.detail.BoardDetailModal"></a>

## BoardDetailModal Objects

```python
class BoardDetailModal(DetailModal)
```

Modal screen showing full board details.

<a id="ganban.ui.edit.messages"></a>

# ganban.ui.edit.messages

Messages for editable widgets.

<a id="ganban.ui.edit.messages.Save"></a>

## Save Objects

```python
class Save(Message)
```

Editor finished - save this value.

<a id="ganban.ui.edit.messages.Cancel"></a>

## Cancel Objects

```python
class Cancel(Message)
```

Editor finished - discard changes.

<a id="ganban.ui.edit.document"></a>

# ganban.ui.edit.document

Markdown document editor widget.

<a id="ganban.ui.edit.document.DocHeader"></a>

## DocHeader Objects

```python
class DocHeader(NodeWatcherMixin, Container)
```

Editable document title with rule underneath.

<a id="ganban.ui.edit.document.DocHeader.TitleChanged"></a>

## TitleChanged Objects

```python
class TitleChanged(Message)
```

Emitted when the title changes.

<a id="ganban.ui.edit.document.AddSection"></a>

## AddSection Objects

```python
class AddSection(Static)
```

Widget to add a new subsection.

<a id="ganban.ui.edit.document.AddSection.SectionCreated"></a>

## SectionCreated Objects

```python
class SectionCreated(Message)
```

Posted when a new section is created.

<a id="ganban.ui.edit.document.MarkdownDocEditor"></a>

## MarkdownDocEditor Objects

```python
class MarkdownDocEditor(NodeWatcherMixin, Container)
```

Two-panel editor for markdown sections content.

<a id="ganban.ui.edit.document.MarkdownDocEditor.Changed"></a>

## Changed Objects

```python
class Changed(Message)
```

Emitted when the document content changes.

<a id="ganban.ui.edit.document.MarkdownDocEditor.on_section_editor_heading_changed"></a>

#### on\_section\_editor\_heading\_changed

```python
def on_section_editor_heading_changed(
        event: SectionEditor.HeadingChanged) -> None
```

Update sections when a section heading changes.

<a id="ganban.ui.edit.document.MarkdownDocEditor.on_section_editor_body_changed"></a>

#### on\_section\_editor\_body\_changed

```python
def on_section_editor_body_changed(event: SectionEditor.BodyChanged) -> None
```

Update sections when a body changes.

<a id="ganban.ui.edit.document.MarkdownDocEditor.on_section_editor_delete_requested"></a>

#### on\_section\_editor\_delete\_requested

```python
def on_section_editor_delete_requested(
        event: SectionEditor.DeleteRequested) -> None
```

Remove a subsection.

<a id="ganban.ui.edit.document.MarkdownDocEditor.on_add_section_section_created"></a>

#### on\_add\_section\_section\_created

```python
def on_add_section_section_created(event: AddSection.SectionCreated) -> None
```

Add a new subsection.

<a id="ganban.ui.edit"></a>

# ganban.ui.edit

Editable widget components.

<a id="ganban.ui.edit.viewers"></a>

# ganban.ui.edit.viewers

Viewer widgets that display content and support update(value).

<a id="ganban.ui.edit.viewers.TextViewer"></a>

## TextViewer Objects

```python
class TextViewer(Static)
```

Simple text viewer.

<a id="ganban.ui.edit.viewers.TextViewer.update"></a>

#### update

```python
def update(value: str) -> None
```

Update the displayed text.

<a id="ganban.ui.edit.viewers.MarkdownViewer"></a>

## MarkdownViewer Objects

```python
class MarkdownViewer(VerticalScroll)
```

Markdown viewer container.

<a id="ganban.ui.edit.viewers.MarkdownViewer.update"></a>

#### update

```python
def update(value: str) -> None
```

Update the displayed markdown.

<a id="ganban.ui.edit.viewers.MarkdownViewer.refresh_content"></a>

#### refresh\_content

```python
def refresh_content() -> None
```

Re-render current value (e.g. after external data changes).

<a id="ganban.ui.edit.section"></a>

# ganban.ui.edit.section

Section editor widget.

<a id="ganban.ui.edit.section.SectionEditor"></a>

## SectionEditor Objects

```python
class SectionEditor(Container)
```

Editor for a section with heading and markdown body.

<a id="ganban.ui.edit.section.SectionEditor.HeadingChanged"></a>

## HeadingChanged Objects

```python
class HeadingChanged(Message)
```

Emitted when the section heading changes.

<a id="ganban.ui.edit.section.SectionEditor.BodyChanged"></a>

## BodyChanged Objects

```python
class BodyChanged(Message)
```

Emitted when the section body changes.

<a id="ganban.ui.edit.section.SectionEditor.DeleteRequested"></a>

## DeleteRequested Objects

```python
class DeleteRequested(Message)
```

Emitted when the section delete is confirmed.

<a id="ganban.ui.edit.meta"></a>

# ganban.ui.edit.meta

Tree-shaped metadata editor for Node objects.

<a id="ganban.ui.edit.meta.BoolToggle"></a>

## BoolToggle Objects

```python
class BoolToggle(Static)
```

A simple true/false toggle that cycles on click.

<a id="ganban.ui.edit.meta.ListItemRow"></a>

## ListItemRow Objects

```python
class ListItemRow(Vertical)
```

A single item row in a list editor.

Scalar values render inline. Compound values (dict, list)
render with a header row and the nested editor below.

<a id="ganban.ui.edit.meta.ListItemRow.on_key_value_row_value_changed"></a>

#### on\_key\_value\_row\_value\_changed

```python
def on_key_value_row_value_changed(event) -> None
```

Propagate changes from nested DictEditor.

<a id="ganban.ui.edit.meta.AddListItemRow"></a>

## AddListItemRow Objects

```python
class AddListItemRow(Static)
```

Clickable '+' that opens a type picker to add a new list item.

<a id="ganban.ui.edit.meta.ListEditor"></a>

## ListEditor Objects

```python
class ListEditor(Vertical)
```

Renders a list's items as editable rows.

<a id="ganban.ui.edit.meta.ListEditor.Changed"></a>

## Changed Objects

```python
class Changed(Message)
```

Emitted when the list contents change.

<a id="ganban.ui.edit.meta.KeyValueRow"></a>

## KeyValueRow Objects

```python
class KeyValueRow(Vertical)
```

A single key:value row in the metadata editor.

Scalar values render inline as key : value.
Compound values (dict, list) render with a header row and
the nested editor indented below.

<a id="ganban.ui.edit.meta.AddKeyRow"></a>

## AddKeyRow Objects

```python
class AddKeyRow(Container)
```

Row to add a new key to the metadata.

<a id="ganban.ui.edit.meta.DictEditor"></a>

## DictEditor Objects

```python
class DictEditor(NodeWatcherMixin, Vertical)
```

Renders a Node's children as KeyValueRows + AddKeyRow.

<a id="ganban.ui.edit.meta.MetaEditor"></a>

## MetaEditor Objects

```python
class MetaEditor(Container)
```

Thin wrapper for the tree metadata editor with scroll support.

<a id="ganban.ui.edit.editors"></a>

# ganban.ui.edit.editors

Editor widgets that emit Save/Cancel messages.

<a id="ganban.ui.edit.editors.BaseEditor"></a>

## BaseEditor Objects

```python
class BaseEditor(TextArea)
```

Base editor that emits Save/Cancel.

<a id="ganban.ui.edit.editors.BaseEditor.start_editing"></a>

#### start\_editing

```python
def start_editing(value: str) -> None
```

Start editing. Called by EditableText.

<a id="ganban.ui.edit.editors.TextEditor"></a>

## TextEditor Objects

```python
class TextEditor(BaseEditor)
```

Single-line editor. Enter saves.

<a id="ganban.ui.edit.editors.NumberEditor"></a>

## NumberEditor Objects

```python
class NumberEditor(TextEditor)
```

Single-line numeric editor. Validates input is a number on save.

<a id="ganban.ui.edit.editors.MarkdownEditor"></a>

## MarkdownEditor Objects

```python
class MarkdownEditor(BaseEditor)
```

Multi-line editor. Enter inserts newline.

<a id="ganban.ui.edit.editable"></a>

# ganban.ui.edit.editable

Editable text container widget.

<a id="ganban.ui.edit.editable.EditableText"></a>

## EditableText Objects

```python
class EditableText(Container)
```

Orchestrates view/edit switching for any viewer + editor pair.

<a id="ganban.ui.edit.editable.EditableText.Changed"></a>

## Changed Objects

```python
class Changed(Message)
```

Emitted when the value changes.

<a id="ganban.ui.edit.editable.EditableText.Changed.control"></a>

#### control

```python
@property
def control() -> EditableText
```

The EditableText that changed.

<a id="ganban.ui.edit.editable.EditableText.focus"></a>

#### focus

```python
def focus(scroll_visible: bool = True) -> None
```

Focus the widget - enters edit mode if not already editing.

<a id="ganban.ui.constants"></a>

# ganban.ui.constants

Shared UI icon constants.

<a id="ganban.ui.cal"></a>

# ganban.ui.cal

Calendar widget for date selection.

<a id="ganban.ui.cal.date_diff"></a>

#### date\_diff

```python
def date_diff(target: date, reference: date) -> str
```

Return compact string showing difference between dates.

Examples: "1d", "-3d", "2m", "-1m", "5y", "-2y"
Uses days for <60 days, months for <24 months, years otherwise.

<a id="ganban.ui.cal.NavButton"></a>

## NavButton Objects

```python
class NavButton(Static)
```

Navigation button for calendar.

<a id="ganban.ui.cal.CalendarDay"></a>

## CalendarDay Objects

```python
class CalendarDay(Static)
```

A single day cell.

<a id="ganban.ui.cal.CalendarDay.Clicked"></a>

## Clicked Objects

```python
class Clicked(Message)
```

Posted when this day is clicked.

<a id="ganban.ui.cal.Calendar"></a>

## Calendar Objects

```python
class Calendar(Container)
```

Date picker widget.

<a id="ganban.ui.cal.Calendar.DateSelected"></a>

## DateSelected Objects

```python
class DateSelected(Message)
```

Emitted when a date is selected (None to clear).

<a id="ganban.ui.cal.CalendarMenuItem"></a>

## CalendarMenuItem Objects

```python
class CalendarMenuItem(Container)
```

Menu item containing a calendar picker.

<a id="ganban.ui.cal.CalendarMenuItem.Selected"></a>

## Selected Objects

```python
class Selected(Message)
```

Posted when a date is selected, signals menu to close.

<a id="ganban.ui.cal.DateButton"></a>

## DateButton Objects

```python
class DateButton(Static)
```

A button that opens a calendar menu for date selection.

<a id="ganban.ui.cal.DateButton.DateSelected"></a>

## DateSelected Objects

```python
class DateSelected(Message)
```

Emitted when a date is selected (None to clear).

<a id="ganban.ui.sync_widget"></a>

# ganban.ui.sync\_widget

Sync status indicator widget for the board header.

<a id="ganban.ui.sync_widget.SyncWidget"></a>

## SyncWidget Objects

```python
class SyncWidget(NodeWatcherMixin, Container)
```

Sync status indicator. Shows current sync state as an emoji.

Click to open a context menu with local/remote toggles and interval presets.

<a id="ganban.ui.board"></a>

# ganban.ui.board

Board screen showing kanban columns and cards.

<a id="ganban.ui.board.BoardScreen"></a>

## BoardScreen Objects

```python
class BoardScreen(NodeWatcherMixin, DropTarget, Screen)
```

Main board screen showing all columns.

<a id="ganban.ui.board.BoardScreen.on_editable_text_changed"></a>

#### on\_editable\_text\_changed

```python
def on_editable_text_changed(event: EditableText.Changed) -> None
```

Update board title when header is edited.

<a id="ganban.ui.board.BoardScreen.on_click"></a>

#### on\_click

```python
def on_click(event) -> None
```

Handle clicks on board header area.

<a id="ganban.ui.board.BoardScreen.action_context_menu"></a>

#### action\_context\_menu

```python
def action_context_menu() -> None
```

Show context menu for the focused widget.

<a id="ganban.ui.board.BoardScreen.action_save"></a>

#### action\_save

```python
def action_save() -> None
```

Save the board to git.

<a id="ganban.ui.board.BoardScreen.on_card_widget_move_requested"></a>

#### on\_card\_widget\_move\_requested

```python
def on_card_widget_move_requested(event: CardWidget.MoveRequested) -> None
```

Handle card move request.

<a id="ganban.ui.board.BoardScreen.on_card_widget_archive_requested"></a>

#### on\_card\_widget\_archive\_requested

```python
def on_card_widget_archive_requested(
        event: CardWidget.ArchiveRequested) -> None
```

Handle card archive request.

<a id="ganban.ui.board.BoardScreen.on_add_card_card_created"></a>

#### on\_add\_card\_card\_created

```python
def on_add_card_card_created(event: AddCard.CardCreated) -> None
```

Handle new card creation — commit immediately for timestamp.

<a id="ganban.ui.board.BoardScreen.on_add_column_column_created"></a>

#### on\_add\_column\_column\_created

```python
def on_add_column_column_created(event: AddColumn.ColumnCreated) -> None
```

Handle new column creation.

<a id="ganban.ui.board.BoardScreen.on_column_widget_move_requested"></a>

#### on\_column\_widget\_move\_requested

```python
def on_column_widget_move_requested(event: ColumnWidget.MoveRequested) -> None
```

Handle column move request.

<a id="ganban.ui.board.BoardScreen.on_column_widget_archive_requested"></a>

#### on\_column\_widget\_archive\_requested

```python
def on_column_widget_archive_requested(
        event: ColumnWidget.ArchiveRequested) -> None
```

Handle column archive request.

<a id="ganban.ui.done"></a>

# ganban.ui.done

Done toggle widget for card detail screen.

<a id="ganban.ui.done.DoneWidget"></a>

## DoneWidget Objects

```python
class DoneWidget(NodeWatcherMixin, Container)
```

Inline done toggle that reads and writes ``meta.done``.

Shows ✅ when done, ⬜ when not. Click to toggle.
Watches the node so external changes (e.g. the meta editor or context
menu) are reflected immediately.

<a id="ganban.ui.card"></a>

# ganban.ui.card

Card widgets for ganban UI.

<a id="ganban.ui.card.CardWidget"></a>

## CardWidget Objects

```python
class CardWidget(NodeWatcherMixin, DraggableMixin, Static)
```

A single card in a column.

<a id="ganban.ui.card.CardWidget.MoveRequested"></a>

## MoveRequested Objects

```python
class MoveRequested(Message)
```

Posted when card should be moved to another column.

<a id="ganban.ui.card.CardWidget.ArchiveRequested"></a>

## ArchiveRequested Objects

```python
class ArchiveRequested(Message)
```

Posted when card should be archived.

<a id="ganban.ui.card.AddCard"></a>

## AddCard Objects

```python
class AddCard(Static)
```

Widget to add a new card to a column.

<a id="ganban.ui.card.AddCard.CardCreated"></a>

## CardCreated Objects

```python
class CardCreated(Message)
```

Posted when a new card is created.

<a id="ganban.ui.static"></a>

# ganban.ui.static

Static widget variants.

<a id="ganban.ui.static.PlainStatic"></a>

## PlainStatic Objects

```python
class PlainStatic(Static)
```

Static that doesn't allow text selection.

<a id="ganban.ui.drag"></a>

# ganban.ui.drag

Drag-and-drop infrastructure for ganban UI.

Two mixins:
- DraggableMixin: on dragged widgets, owns the "flying" phase
- DropTarget: on containers, owns the "landing" phase

<a id="ganban.ui.drag.DropTarget"></a>

## DropTarget Objects

```python
class DropTarget()
```

Mixin for widgets that can accept drops.

Returns False to ignore (bubbles to parent), True to consume.

<a id="ganban.ui.drag.DropTarget.drag_over"></a>

#### drag\_over

```python
def drag_over(draggable: DraggableMixin, x: int, y: int) -> bool
```

Called while a draggable hovers over this target. Return True to accept.

<a id="ganban.ui.drag.DropTarget.drag_away"></a>

#### drag\_away

```python
def drag_away(draggable: DraggableMixin) -> None
```

Called when a draggable leaves this target.

<a id="ganban.ui.drag.DropTarget.try_drop"></a>

#### try\_drop

```python
def try_drop(draggable: DraggableMixin, x: int, y: int) -> bool
```

Called on mouse-up to attempt the drop. Return True if accepted.

<a id="ganban.ui.drag.DraggableMixin"></a>

## DraggableMixin Objects

```python
class DraggableMixin()
```

Mixin for widgets that can be dragged.

Subclasses should:
- Call _init_draggable() in __init__
- Implement draggable_make_ghost() to return the ghost widget
- Implement draggable_clicked() for click-without-drag behavior
- Optionally override DRAG_THRESHOLD and HORIZONTAL_ONLY

<a id="ganban.ui.drag.DraggableMixin.draggable_make_ghost"></a>

#### draggable\_make\_ghost

```python
def draggable_make_ghost() -> Widget
```

Create and return the ghost widget for dragging. Override in subclass.

<a id="ganban.ui.drag.DraggableMixin.draggable_clicked"></a>

#### draggable\_clicked

```python
def draggable_clicked() -> None
```

Called when mouse released without dragging. Override for click behavior.

<a id="ganban.ui.drag.DragGhost"></a>

## DragGhost Objects

```python
class DragGhost(Static)
```

Floating overlay showing the card being dragged.

<a id="ganban.ui.drag.CardPlaceholder"></a>

## CardPlaceholder Objects

```python
class CardPlaceholder(Static)
```

Placeholder showing where a dragged card will drop.

<a id="ganban.ui.drag.ColumnPlaceholder"></a>

## ColumnPlaceholder Objects

```python
class ColumnPlaceholder(Static)
```

Placeholder showing where a dragged column will drop.

<a id="ganban.ui.app"></a>

# ganban.ui.app

Main Textual application for ganban.

<a id="ganban.ui.app.ConfirmInitScreen"></a>

## ConfirmInitScreen Objects

```python
class ConfirmInitScreen(ModalScreen[bool])
```

Modal screen asking to initialize a git repo.

<a id="ganban.ui.app.GanbanApp"></a>

## GanbanApp Objects

```python
class GanbanApp(App)
```

Git-based kanban board TUI.

<a id="ganban.ui.app.GanbanApp.action_quit"></a>

#### action\_quit

```python
def action_quit() -> None
```

Cancel sync, save and quit.

<a id="ganban.ui.emoji"></a>

# ganban.ui.emoji

Emoji picker widget.

<a id="ganban.ui.emoji.emoji_for_email"></a>

#### emoji\_for\_email

```python
def emoji_for_email(email: str) -> str
```

Pick a deterministic default emoji for an email address.

Uses the last nibble of the md5 digest, modulo 13.

<a id="ganban.ui.emoji.parse_committer"></a>

#### parse\_committer

```python
def parse_committer(committer: str) -> tuple[str, str, str]
```

Parse a committer string into (emoji, name, email).

Accepts "Name <email>" format. If parsing fails, the full
string is used as both name and email.

<a id="ganban.ui.emoji.build_emoji_menu"></a>

#### build\_emoji\_menu

```python
def build_emoji_menu(email: str | None = None) -> list[MenuRow]
```

Build a 6x5 emoji picker grid with default/clear as first cell.

<a id="ganban.ui.emoji.EmojiButton"></a>

## EmojiButton Objects

```python
class EmojiButton(Static)
```

A button that opens an emoji picker menu.

<a id="ganban.ui.emoji.EmojiButton.EmojiSelected"></a>

## EmojiSelected Objects

```python
class EmojiSelected(Message)
```

Posted when an emoji is selected.

<a id="ganban.ui.emoji.find_user_by_email"></a>

#### find\_user\_by\_email

```python
def find_user_by_email(email: str,
                       meta: Node | None) -> tuple[str, Node] | None
```

Find the (user_name, user_node) for an email in meta.users.

<a id="ganban.ui.emoji.resolve_email_display"></a>

#### resolve\_email\_display

```python
def resolve_email_display(
        email: str,
        meta: Node | None = None,
        committers: list[str] | None = None) -> tuple[str, str] | None
```

Resolve an email to (emoji, display_name).

Checks meta.users first (custom emoji + user name), then
git committers (hash emoji + committer name). Returns None
if the email isn't found in either source.

<a id="ganban.ui.emoji.resolve_email_emoji"></a>

#### resolve\_email\_emoji

```python
def resolve_email_emoji(email: str, meta: Node) -> str
```

Look up the emoji for an email from meta.users, falling back to hash.

<a id="ganban.ui.emoji.EmailEmoji"></a>

## EmailEmoji Objects

```python
class EmailEmoji(NodeWatcherMixin, Static)
```

Display-only emoji resolved from an email address.

Watches meta.users so it updates when custom emojis change.

<a id="ganban.ui.column"></a>

# ganban.ui.column

Column widgets for ganban UI.

<a id="ganban.ui.column.ColumnWidget"></a>

## ColumnWidget Objects

```python
class ColumnWidget(NodeWatcherMixin, DraggableMixin, DropTarget, Vertical)
```

A single column on the board.

<a id="ganban.ui.column.ColumnWidget.MoveRequested"></a>

## MoveRequested Objects

```python
class MoveRequested(Message)
```

Posted when column should be moved.

<a id="ganban.ui.column.ColumnWidget.ArchiveRequested"></a>

## ArchiveRequested Objects

```python
class ArchiveRequested(Message)
```

Posted when column should be archived.

<a id="ganban.ui.column.ColumnWidget.draggable_make_ghost"></a>

#### draggable\_make\_ghost

```python
def draggable_make_ghost()
```

Column IS the ghost — use self with CSS overlay positioning.

<a id="ganban.ui.column.ColumnWidget.on_editable_text_changed"></a>

#### on\_editable\_text\_changed

```python
def on_editable_text_changed(event: EditableText.Changed) -> None
```

Update column name when header is edited.

<a id="ganban.ui.column.ColumnWidget.on_click"></a>

#### on\_click

```python
def on_click(event) -> None
```

Show context menu on right-click.

<a id="ganban.ui.column.ColumnWidget.on_key"></a>

#### on\_key

```python
def on_key(event) -> None
```

Arrow key navigation and shift+arrow card movement.

<a id="ganban.ui.column.ColumnWidget.on_mouse_move"></a>

#### on\_mouse\_move

```python
def on_mouse_move(event) -> None
```

Handle DraggableMixin threshold first, then hover-focus tracking.

<a id="ganban.ui.column.AddColumn"></a>

## AddColumn Objects

```python
class AddColumn(Vertical)
```

Widget to add a new column.

<a id="ganban.ui.column.AddColumn.ColumnCreated"></a>

## ColumnCreated Objects

```python
class ColumnCreated(Message)
```

Posted when a new column is created.

<a id="ganban.ui.card_indicators"></a>

# ganban.ui.card\_indicators

Pure functions for building card indicator text.

<a id="ganban.ui.card_indicators.build_footer_text"></a>

#### build\_footer\_text

```python
def build_footer_text(sections: ListNode,
                      meta: Node,
                      board_meta: Node | None = None) -> Text
```

Build footer indicators from card sections and meta.

Shows assignee emoji if meta.assigned is set.
Shows body icon (dim) if first section has body content.
Shows calendar icon + Xd if meta.due is set, red if overdue.

<a id="ganban.sync"></a>

# ganban.sync

Background sync engine for the TUI.

Runs: pull → load+merge → save → push, gated by board.git.sync toggles.

<a id="ganban.sync.run_sync_cycle"></a>

#### run\_sync\_cycle

```python
async def run_sync_cycle(board)
```

Run one sync cycle: pull → save → merge → load → push.

Reads board.git.sync.{local, remote} to decide which steps to run.
Sets sync.status at each step (fires watchers → UI updates).
All git I/O runs via asyncio.to_thread to stay non-blocking.

<a id="ganban.parser"></a>

# ganban.parser

Parse markdown documents with front-matter.

<a id="ganban.parser.parse_sections"></a>

#### parse\_sections

```python
def parse_sections(text: str) -> tuple[list[tuple[str, str]], dict]
```

Parse markdown into an ordered list of (title, body) sections plus meta.

Returns (sections, meta) where:
- sections is a list of (title, body) tuples
- First section is the h1 (title may be "" if no h1)
- Subsequent sections are h2s
- meta is the front-matter dict (or {})

<a id="ganban.parser.serialize_sections"></a>

#### serialize\_sections

```python
def serialize_sections(sections: list[tuple[str, str]],
                       meta: dict | None = None) -> str
```

Serialize sections and meta back to markdown text.

First section becomes # heading, rest become ## headings.
Meta becomes YAML front-matter if non-empty.

<a id="ganban.parser.first_title"></a>

#### first\_title

```python
def first_title(sections) -> str
```

Get the title (first key) of a sections ListNode, or empty string.

<a id="ganban.parser.first_body"></a>

#### first\_body

```python
def first_body(sections) -> str
```

Get the body (first value) of a sections ListNode, or empty string.

