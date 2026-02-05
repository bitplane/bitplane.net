<a id="ganban"></a>

# ganban

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

Async wrappers around GitPython for non-blocking git operations.

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

<a id="ganban.__main__"></a>

# ganban.\_\_main\_\_

Entry point for ganban CLI.

<a id="ganban.loader"></a>

# ganban.loader

Load a ganban board from git tree.

<a id="ganban.loader.load_board"></a>

#### load\_board

```python
async def load_board(repo_path: str, branch: str = BRANCH_NAME) -> Board
```

Load a complete board from a git branch.

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

<a id="ganban.ui.menu.MenuList.get_focusable_items"></a>

#### get\_focusable\_items

```python
def get_focusable_items() -> list[MenuItem]
```

Return list of enabled menu items.

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

<a id="ganban.ui.menu.ContextMenu.action_select_or_enter"></a>

#### action\_select\_or\_enter

```python
def action_select_or_enter() -> None
```

Select leaf item or enter submenu.

<a id="ganban.ui.menu.ContextMenu.action_close_submenu"></a>

#### action\_close\_submenu

```python
def action_close_submenu() -> None
```

Move focus back to parent item.

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

<a id="ganban.ui"></a>

# ganban.ui

Textual UI for ganban.

<a id="ganban.ui.detail"></a>

# ganban.ui.detail

Detail modals for viewing and editing markdown content.

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
def action_quit() -> None
```

Quit the app.

<a id="ganban.ui.detail.CardDetailModal"></a>

## CardDetailModal Objects

```python
class CardDetailModal(DetailModal)
```

Modal screen showing full card details.

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

<a id="ganban.ui.edit.document.MarkdownDocEditor"></a>

## MarkdownDocEditor Objects

```python
class MarkdownDocEditor(Container)
```

Two-panel editor for MarkdownDoc content.

<a id="ganban.ui.edit.document.MarkdownDocEditor.Changed"></a>

## Changed Objects

```python
class Changed(Message)
```

Emitted when the document content changes.

<a id="ganban.ui.edit.document.MarkdownDocEditor.on_editable_text_changed"></a>

#### on\_editable\_text\_changed

```python
def on_editable_text_changed(event: EditableText.Changed) -> None
```

Update doc when title changes.

<a id="ganban.ui.edit.document.MarkdownDocEditor.on_section_editor_heading_changed"></a>

#### on\_section\_editor\_heading\_changed

```python
def on_section_editor_heading_changed(
        event: SectionEditor.HeadingChanged) -> None
```

Update doc when a section heading changes.

<a id="ganban.ui.edit.document.MarkdownDocEditor.on_section_editor_body_changed"></a>

#### on\_section\_editor\_body\_changed

```python
def on_section_editor_body_changed(event: SectionEditor.BodyChanged) -> None
```

Update doc when a body changes.

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
class MarkdownViewer(Container)
```

Markdown viewer container.

<a id="ganban.ui.edit.viewers.MarkdownViewer.update"></a>

#### update

```python
def update(value: str) -> None
```

Update the displayed markdown.

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
def start_editing(value: str, x: int = 0, y: int = 0) -> None
```

Start editing. Called by EditableText.

<a id="ganban.ui.edit.editors.TextEditor"></a>

## TextEditor Objects

```python
class TextEditor(BaseEditor)
```

Single-line editor. Enter saves.

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

<a id="ganban.ui.board"></a>

# ganban.ui.board

Board screen showing kanban columns and cards.

<a id="ganban.ui.board.BoardScreen"></a>

## BoardScreen Objects

```python
class BoardScreen(Screen)
```

Main board screen showing all columns.

<a id="ganban.ui.board.BoardScreen.on_drag_started"></a>

#### on\_drag\_started

```python
def on_drag_started(event: DragStarted) -> None
```

Handle drag start from a card.

<a id="ganban.ui.board.BoardScreen.on_column_widget_drag_started"></a>

#### on\_column\_widget\_drag\_started

```python
def on_column_widget_drag_started(event: ColumnWidget.DragStarted) -> None
```

Handle the start of a column drag.

<a id="ganban.ui.board.BoardScreen.on_mouse_move"></a>

#### on\_mouse\_move

```python
def on_mouse_move(event) -> None
```

Update drag overlay position.

<a id="ganban.ui.board.BoardScreen.on_mouse_up"></a>

#### on\_mouse\_up

```python
def on_mouse_up(event) -> None
```

Complete the drag operation.

<a id="ganban.ui.board.BoardScreen.action_cancel_drag"></a>

#### action\_cancel\_drag

```python
def action_cancel_drag() -> None
```

Cancel the current drag operation.

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

Show context menu on right-click on board header.

<a id="ganban.ui.board.BoardScreen.action_save"></a>

#### action\_save

```python
async def action_save() -> None
```

Save the board to git.

<a id="ganban.ui.board.BoardScreen.on_card_widget_move_requested"></a>

#### on\_card\_widget\_move\_requested

```python
def on_card_widget_move_requested(event: CardWidget.MoveRequested) -> None
```

Handle card move request.

<a id="ganban.ui.board.BoardScreen.on_card_widget_delete_requested"></a>

#### on\_card\_widget\_delete\_requested

```python
def on_card_widget_delete_requested(event: CardWidget.DeleteRequested) -> None
```

Handle card delete request.

<a id="ganban.ui.board.BoardScreen.on_add_card_card_created"></a>

#### on\_add\_card\_card\_created

```python
def on_add_card_card_created(event: AddCard.CardCreated) -> None
```

Handle new card creation.

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

<a id="ganban.ui.board.BoardScreen.on_column_widget_delete_requested"></a>

#### on\_column\_widget\_delete\_requested

```python
def on_column_widget_delete_requested(
        event: ColumnWidget.DeleteRequested) -> None
```

Handle column delete request.

<a id="ganban.ui.card"></a>

# ganban.ui.card

Card widgets for ganban UI.

<a id="ganban.ui.card.CardWidget"></a>

## CardWidget Objects

```python
class CardWidget(DraggableMixin, Static)
```

A single card in a column.

<a id="ganban.ui.card.CardWidget.MoveRequested"></a>

## MoveRequested Objects

```python
class MoveRequested(Message)
```

Posted when card should be moved to another column.

<a id="ganban.ui.card.CardWidget.DeleteRequested"></a>

## DeleteRequested Objects

```python
class DeleteRequested(Message)
```

Posted when card should be deleted.

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

<a id="ganban.ui.drag.DragStarted"></a>

## DragStarted Objects

```python
class DragStarted(Message)
```

Posted when any draggable widget starts being dragged.

<a id="ganban.ui.drag.DragStarted.control"></a>

#### control

```python
@property
def control() -> Widget
```

The widget being dragged.

<a id="ganban.ui.drag.DraggableMixin"></a>

## DraggableMixin Objects

```python
class DraggableMixin()
```

Mixin for widgets that can be dragged.

Subclasses should:
- Call _init_draggable() in __init__
- Implement draggable_drag_started() to post appropriate messages
- Implement draggable_clicked() for click-without-drag behavior
- Optionally override DRAG_THRESHOLD and HORIZONTAL_ONLY

<a id="ganban.ui.drag.DraggableMixin.draggable_drag_started"></a>

#### draggable\_drag\_started

```python
def draggable_drag_started(mouse_pos: Offset) -> None
```

Called when drag threshold is exceeded. Override to post messages.

<a id="ganban.ui.drag.DraggableMixin.draggable_clicked"></a>

#### draggable\_clicked

```python
def draggable_clicked(click_pos: Offset) -> None
```

Called when mouse released without dragging. Override for click behavior.

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
async def action_quit() -> None
```

Save and quit.

<a id="ganban.ui.drag_managers"></a>

# ganban.ui.drag\_managers

Drag-and-drop managers for board elements.

<a id="ganban.ui.drag_managers.CardPlaceholder"></a>

## CardPlaceholder Objects

```python
class CardPlaceholder(Static)
```

Placeholder showing where a dragged card will drop.

<a id="ganban.ui.drag_managers.DragGhost"></a>

## DragGhost Objects

```python
class DragGhost(Static)
```

Floating overlay showing the card being dragged.

<a id="ganban.ui.drag_managers.ColumnPlaceholder"></a>

## ColumnPlaceholder Objects

```python
class ColumnPlaceholder(Static)
```

Placeholder showing where a dragged column will drop.

<a id="ganban.ui.drag_managers.renumber_links"></a>

#### renumber\_links

```python
def renumber_links(column) -> None
```

Renumber all links in a column to sequential zero-padded positions.

<a id="ganban.ui.drag_managers.CardDragManager"></a>

## CardDragManager Objects

```python
class CardDragManager()
```

Manages card drag-and-drop state and operations.

<a id="ganban.ui.drag_managers.ColumnDragManager"></a>

## ColumnDragManager Objects

```python
class ColumnDragManager()
```

Manages column drag-and-drop state and operations.

<a id="ganban.ui.column"></a>

# ganban.ui.column

Column widgets for ganban UI.

<a id="ganban.ui.column.ColumnHeader"></a>

## ColumnHeader Objects

```python
class ColumnHeader(DraggableMixin, Static)
```

Draggable column header.

<a id="ganban.ui.column.ColumnWidget"></a>

## ColumnWidget Objects

```python
class ColumnWidget(Vertical)
```

A single column on the board.

<a id="ganban.ui.column.ColumnWidget.DragStarted"></a>

## DragStarted Objects

```python
class DragStarted(Message)
```

Posted when a column drag begins.

<a id="ganban.ui.column.ColumnWidget.DragStarted.control"></a>

#### control

```python
@property
def control() -> "ColumnWidget"
```

The column widget being dragged.

<a id="ganban.ui.column.ColumnWidget.MoveRequested"></a>

## MoveRequested Objects

```python
class MoveRequested(Message)
```

Posted when column should be moved.

<a id="ganban.ui.column.ColumnWidget.DeleteRequested"></a>

## DeleteRequested Objects

```python
class DeleteRequested(Message)
```

Posted when column should be deleted.

<a id="ganban.ui.column.ColumnWidget.on_drag_started"></a>

#### on\_drag\_started

```python
def on_drag_started(event: DragStarted) -> None
```

Convert header DragStarted to ColumnWidget.DragStarted.

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

<a id="ganban.writer"></a>

# ganban.writer

Save a ganban board to git without touching the working tree.

<a id="ganban.writer.MergeRequired"></a>

## MergeRequired Objects

```python
@dataclass
class MergeRequired()
```

Returned by check_for_merge when the branch has diverged.

<a id="ganban.writer.MergeRequired.base"></a>

#### base

common ancestor commit

<a id="ganban.writer.MergeRequired.ours"></a>

#### ours

our commit (what board was loaded from)

<a id="ganban.writer.MergeRequired.theirs"></a>

#### theirs

their commit (current branch tip)

<a id="ganban.writer.check_for_merge"></a>

#### check\_for\_merge

```python
def check_for_merge(board: Board,
                    branch: str = BRANCH_NAME) -> MergeRequired | None
```

Check if saving would require a merge.

Returns MergeRequired with the 3 commit hashes if branch has diverged,
or None if a simple save is possible.

The caller can then:
1. Load all 3 boards: load_board(repo, commit=base/ours/theirs)
2. Compare them to find conflicts
3. Build a resolved board
4. Save with: save_board(resolved, parents=[ours, theirs])

<a id="ganban.writer.check_remote_for_merge"></a>

#### check\_remote\_for\_merge

```python
def check_remote_for_merge(board: Board,
                           remote: str = "origin",
                           branch: str = BRANCH_NAME) -> MergeRequired | None
```

Check if a remote has changes that need merging.

Call this after fetching to see if the remote tracking branch has diverged
from the board's current commit.

**Arguments**:

- `board` - The current board state
- `remote` - Remote name (e.g., "origin")
- `branch` - Branch name on the remote
  

**Returns**:

  MergeRequired if remote has diverged, None if up to date.

<a id="ganban.writer.save_board"></a>

#### save\_board

```python
async def save_board(board: Board,
                     message: str = "Update board",
                     branch: str = BRANCH_NAME,
                     parents: list[str] | None = None) -> str
```

Save a board to git and return the new commit hash.

This creates blobs, trees, and a commit without modifying the working tree.

**Arguments**:

- `board` - The board state to save
- `message` - Commit message
- `branch` - Branch name to update
- `parents` - Explicit parent commits. If None, uses board.commit.
  For merge commits, pass [ours_commit, theirs_commit].
  

**Returns**:

  The new commit hash

<a id="ganban.writer.try_auto_merge"></a>

#### try\_auto\_merge

```python
def try_auto_merge(board: Board,
                   merge_info: MergeRequired,
                   message: str = "Merge changes",
                   branch: str = BRANCH_NAME) -> str | None
```

Attempt an automatic merge if there are no conflicts.

**Arguments**:

- `board` - The board with our changes
- `merge_info` - The MergeRequired from check_for_merge
- `message` - Commit message for the merge
- `branch` - Branch to update
  

**Returns**:

  The new merge commit hash if successful, None if there are conflicts.

<a id="ganban.writer.create_card"></a>

#### create\_card

```python
def create_card(board: Board,
                title: str,
                body: str = "",
                column: Column | None = None,
                position: int | None = None) -> Card
```

Create a new card and add it to the board.

**Arguments**:

- `board` - The board to add the card to
- `title` - Card title
- `body` - Card body text
- `column` - Column to add the card to (default: first column)
- `position` - Position in column (default: end of column)
  

**Returns**:

  The created Card

<a id="ganban.writer.create_column"></a>

#### create\_column

```python
def create_column(board: Board,
                  name: str,
                  order: str | None = None,
                  hidden: bool = False) -> Column
```

Create a new column and add it to the board.

**Arguments**:

- `board` - The board to add the column to
- `name` - Column display name
- `order` - Sort order prefix (default: auto-increment from highest)
- `hidden` - Whether column is hidden (prefix with .)
  

**Returns**:

  The created Column

<a id="ganban.writer.slugify"></a>

#### slugify

```python
def slugify(text: str) -> str
```

Convert text to a URL-friendly slug.

<a id="ganban.writer.build_column_path"></a>

#### build\_column\_path

```python
def build_column_path(order: str, name: str, hidden: bool = False) -> str
```

Build column directory path from components.

<a id="ganban.parser"></a>

# ganban.parser

Parse markdown documents with front-matter.

<a id="ganban.parser.parse_markdown"></a>

#### parse\_markdown

```python
def parse_markdown(text: str) -> MarkdownDoc
```

Parse a markdown document into a MarkdownDoc.

<a id="ganban.parser.serialize_markdown"></a>

#### serialize\_markdown

```python
def serialize_markdown(doc: MarkdownDoc) -> str
```

Serialize a MarkdownDoc back to markdown text.

<a id="ganban.models"></a>

# ganban.models

Data models for ganban boards.

<a id="ganban.models.MarkdownDoc"></a>

## MarkdownDoc Objects

```python
@dataclass
class MarkdownDoc()
```

Parsed markdown document with optional front-matter.

<a id="ganban.models.Card"></a>

## Card Objects

```python
@dataclass
class Card()
```

A card file in .all/

<a id="ganban.models.CardLink"></a>

## CardLink Objects

```python
@dataclass
class CardLink()
```

A symlink in a column pointing to a card.

<a id="ganban.models.Column"></a>

## Column Objects

```python
@dataclass
class Column()
```

A column directory on the board.

<a id="ganban.models.Board"></a>

## Board Objects

```python
@dataclass
class Board()
```

The full board state.

