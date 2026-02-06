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

<a id="ganban.model.loader"></a>

# ganban.model.loader

Load a ganban board from git into a Node tree.

<a id="ganban.model.loader.load_board"></a>

#### load\_board

```python
def load_board(repo_path: str, branch: str = BRANCH_NAME) -> Node
```

Load a complete board from a git branch as a Node tree.

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

<a id="ganban.model.writer.create_card"></a>

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

<a id="ganban.model.writer.create_column"></a>

#### create\_column

```python
def create_column(board: Node,
                  name: str,
                  order: str | None = None,
                  hidden: bool = False) -> Node
```

Create a new column and add it to the board.

Returns the created column Node.

<a id="ganban.model.writer.slugify"></a>

#### slugify

```python
def slugify(text: str) -> str
```

Convert text to a URL-friendly slug.

<a id="ganban.model.writer.build_column_path"></a>

#### build\_column\_path

```python
def build_column_path(order: str, name: str, hidden: bool = False) -> str
```

Build column directory path from components.

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

<a id="ganban.ui.confirm"></a>

# ganban.ui.confirm

Compact inline confirmation widget.

<a id="ganban.ui.confirm.ConfirmButton"></a>

## ConfirmButton Objects

```python
class ConfirmButton(Static)
```

A button that shows a confirm/cancel menu on click.

Shows a single icon (default: 🗑️). When clicked, opens a context menu
with ❌ (cancel) and ✅ (confirm). Emits Confirmed message on confirm.

<a id="ganban.ui.confirm.ConfirmButton.Confirmed"></a>

## Confirmed Objects

```python
class Confirmed(Message)
```

Emitted when the action is confirmed.

<a id="ganban.ui.due"></a>

# ganban.ui.due

Due date widget with inline editing.

<a id="ganban.ui.due.DueDateLabel"></a>

## DueDateLabel Objects

```python
class DueDateLabel(Static)
```

Shows due date text, swaps to delete icon on hover.

<a id="ganban.ui.due.DueDateLabel.Confirmed"></a>

## Confirmed Objects

```python
class Confirmed(Message)
```

Emitted when delete is confirmed.

<a id="ganban.ui.due.DueDateWidget"></a>

## DueDateWidget Objects

```python
class DueDateWidget(Container)
```

Inline due date display with calendar picker.

<a id="ganban.ui.due.DueDateWidget.Changed"></a>

## Changed Objects

```python
class Changed(Message)
```

Emitted when due date changes.

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

<a id="ganban.ui.menu.MenuRow.active_item"></a>

#### active\_item

```python
@property
def active_item() -> MenuItem | None
```

The currently active (last-focused) item in this row.

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

Move active index by direction (+1/-1). Return new item, or None at edge.

<a id="ganban.ui.menu.MenuRow.activate"></a>

#### activate

```python
def activate(item: MenuItem) -> None
```

Set the given item as the active one.

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

Return list of items for vertical navigation.

Each MenuRow is collapsed to its active item.

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

<a id="ganban.ui.edit.document.DocHeader"></a>

## DocHeader Objects

```python
class DocHeader(Container)
```

Editable document title with rule underneath.

<a id="ganban.ui.edit.document.DocHeader.TitleChanged"></a>

## TitleChanged Objects

```python
class TitleChanged(Message)
```

Emitted when the title changes.

<a id="ganban.ui.edit.document.MarkdownDocEditor"></a>

## MarkdownDocEditor Objects

```python
class MarkdownDocEditor(Container)
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

Emitted when a date is selected.

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

Emitted when a date is selected.

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
def action_save() -> None
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
def action_quit() -> None
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

<a id="ganban.ui.column.ColumnWidget"></a>

## ColumnWidget Objects

```python
class ColumnWidget(DraggableMixin, Vertical)
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

