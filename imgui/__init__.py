# -*- coding: utf-8 -*-
VERSION = (1, 3, 1)  # PEP 386
__version__ = ".".join([str(x) for x in VERSION])

# from imgui.core import *  # noqa
# from imgui import core
from imgui.embedd import *  # noqa
from imgui import embedd
# from imgui.extra import *  # noqa
# from imgui import extra
from imgui import _compat
# from imgui import internal

# TODO: Complete and correcte doc text for ImGui v1.79

# VERTEX_BUFFER_POS_OFFSET = extra.vertex_buffer_vertex_pos_offset()
# VERTEX_BUFFER_UV_OFFSET = extra.vertex_buffer_vertex_uv_offset()
# VERTEX_BUFFER_COL_OFFSET = extra.vertex_buffer_vertex_col_offset()

# VERTEX_SIZE = extra.vertex_buffer_vertex_size()

# INDEX_SIZE = extra.index_buffer_index_size()

VERTEX_BUFFER_POS_OFFSET = embedd._py_vertex_buffer_vertex_pos_offset()
VERTEX_BUFFER_UV_OFFSET = embedd._py_vertex_buffer_vertex_uv_offset()
VERTEX_BUFFER_COL_OFFSET = embedd._py_vertex_buffer_vertex_col_offset()

VERTEX_SIZE = embedd._py_vertex_buffer_vertex_size()

INDEX_SIZE = embedd._py_index_buffer_index_size()

# ==== Condition constants (redefines for autodoc)
#: No condition (always set the variable), same as _Always
NONE = embedd.NONE
#: No condition (always set the variable)
ALWAYS = embedd.ALWAYS
#: Set the variable once per runtime session (only the first call will succeed)
ONCE = embedd.ONCE
#: Set the variable if the object/window has no persistently saved data (no entry in .ini file)
FIRST_USE_EVER = embedd.FIRST_USE_EVER
#: Set the variable if the object/window is appearing after being hidden/inactive (or the first time)
APPEARING = embedd.APPEARING


# === Key map constants (redefines for autodoc)
#: for tabbing through fields
KEY_TAB = embedd.KEY_TAB
#: for text edit
KEY_LEFT_ARROW = embedd.KEY_LEFT_ARROW
#: for text edit
KEY_RIGHT_ARROW = embedd.KEY_RIGHT_ARROW
#: for text edit
KEY_UP_ARROW = embedd.KEY_UP_ARROW
#: for text edit
KEY_DOWN_ARROW = embedd.KEY_DOWN_ARROW
KEY_PAGE_UP = embedd.KEY_PAGE_UP
KEY_PAGE_DOWN = embedd.KEY_PAGE_DOWN
#: for text edit
KEY_HOME = embedd.KEY_HOME
#: for text edit
KEY_END = embedd.KEY_END
#: for text edit
KEY_INSERT = embedd.KEY_INSERT
#: for text edit
KEY_DELETE = embedd.KEY_DELETE
#: for text edit
KEY_BACKSPACE = embedd.KEY_BACKSPACE
#: for text edit
KEY_SPACE = embedd.KEY_SPACE
#: for text edit
KEY_ENTER = embedd.KEY_ENTER
#: for text edit
KEY_ESCAPE = embedd.KEY_ESCAPE
#:
KEY_PAD_ENTER = embedd.KEY_PAD_ENTER
#: for text edit CTRL+A: select all
KEY_A = embedd.KEY_A
#: for text edit CTRL+C: copy
KEY_C = embedd.KEY_C
#: for text edit CTRL+V: paste
KEY_V = embedd.KEY_V
#: for text edit CTRL+X: cut
KEY_X = embedd.KEY_X
#: for text edit CTRL+Y: redo
KEY_Y = embedd.KEY_Y
#: for text edit CTRL+Z: undo
KEY_Z = embedd.KEY_Z

# === Nav Input (redefines for autodoc)
#: activate / open / toggle / tweak value        e.g. Cross  (PS4), A (Xbox), A (Switch), Space (Keyboard)
NAV_INPUT_ACTIVATE = embedd.NAV_INPUT_ACTIVATE
#: cancel / close / exit                         e.g. Circle (PS4), B (Xbox), B (Switch), Escape (Keyboard)
NAV_INPUT_CANCEL = embedd.NAV_INPUT_CANCEL
#: text input / on-screen keyboard               e.g. Triang.(PS4), Y (Xbox), X (Switch), Return (Keyboard)
NAV_INPUT_INPUT = embedd.NAV_INPUT_INPUT
#: tap: toggle menu / hold: focus, move, resize  e.g. Square (PS4), X (Xbox), Y (Switch), Alt (Keyboard)
NAV_INPUT_MENU = embedd.NAV_INPUT_MENU
#: move / tweak / resize window (w/ PadMenu)     e.g. D-pad Left/Right/Up/Down (Gamepads), Arrow keys (Keyboard)
NAV_INPUT_DPAD_LEFT = embedd.NAV_INPUT_DPAD_LEFT
#:
NAV_INPUT_DPAD_RIGHT = embedd.NAV_INPUT_DPAD_RIGHT
#:
NAV_INPUT_DPAD_UP = embedd.NAV_INPUT_DPAD_UP
#:
NAV_INPUT_DPAD_DOWN = embedd.NAV_INPUT_DPAD_DOWN
#: scroll / move window (w/ PadMenu)             e.g. Left Analog Stick Left/Right/Up/Down
NAV_INPUT_L_STICK_LEFT = embedd.NAV_INPUT_L_STICK_LEFT
#:
NAV_INPUT_L_STICK_RIGHT = embedd.NAV_INPUT_L_STICK_RIGHT
#:
NAV_INPUT_L_STICK_UP = embedd.NAV_INPUT_L_STICK_UP
#:
NAV_INPUT_L_STICK_DOWN = embedd.NAV_INPUT_L_STICK_DOWN
#: next window (w/ PadMenu)                      e.g. L1 or L2 (PS4), LB or LT (Xbox), L or ZL (Switch)
NAV_INPUT_FOCUS_PREV = embedd.NAV_INPUT_FOCUS_PREV
#: prev window (w/ PadMenu)                      e.g. R1 or R2 (PS4), RB or RT (Xbox), R or ZL (Switch)
NAV_INPUT_FOCUS_NEXT = embedd.NAV_INPUT_FOCUS_NEXT
#: slower tweaks                                 e.g. L1 or L2 (PS4), LB or LT (Xbox), L or ZL (Switch)
NAV_INPUT_TWEAK_SLOW = embedd.NAV_INPUT_TWEAK_SLOW
#: faster tweaks                                 e.g. R1 or R2 (PS4), RB or RT (Xbox), R or ZL (Switch)
NAV_INPUT_TWEAK_FAST    = embedd.NAV_INPUT_TWEAK_FAST


# === Key Mode Flags (redefines for autodoc)
KEY_MOD_NONE = embedd.KEY_MOD_NONE
KEY_MOD_CTRL = embedd.KEY_MOD_CTRL
KEY_MOD_SHIFT = embedd.KEY_MOD_SHIFT
KEY_MOD_ALT = embedd.KEY_MOD_ALT
KEY_MOD_SUPER = embedd.KEY_MOD_SUPER

# === Style var constants (redefines for autodoc)
#: associated type: ``float``.
STYLE_ALPHA = embedd.STYLE_ALPHA
#: associated type: ``Vec2``.
STYLE_WINDOW_PADDING = embedd.STYLE_WINDOW_PADDING
#: associated type: ``float``.
STYLE_WINDOW_ROUNDING = embedd.STYLE_WINDOW_ROUNDING
#: associated type: ``float``.
STYLE_WINDOW_BORDERSIZE = embedd.STYLE_WINDOW_BORDERSIZE
#: associated type: ``Vec2``.
STYLE_WINDOW_MIN_SIZE = embedd.STYLE_WINDOW_MIN_SIZE
#: associated type: ``Vec2``.
STYLE_WINDOW_TITLE_ALIGN = embedd.STYLE_WINDOW_TITLE_ALIGN
#: associated type: ``float``.
STYLE_CHILD_ROUNDING = embedd.STYLE_CHILD_ROUNDING
#: associated type: ``float``.
STYLE_CHILD_BORDERSIZE = embedd.STYLE_CHILD_BORDERSIZE
#: associated type: ``float``.
STYLE_POPUP_ROUNDING = embedd.STYLE_POPUP_ROUNDING
#: associated type: ``float``.
STYLE_POPUP_BORDERSIZE = embedd.STYLE_POPUP_BORDERSIZE
#: associated type: ``Vec2``.
STYLE_FRAME_PADDING = embedd.STYLE_FRAME_PADDING
#: associated type: ``float``.
STYLE_FRAME_ROUNDING = embedd.STYLE_FRAME_ROUNDING
#: associated type: ``float``.
STYLE_FRAME_BORDERSIZE = embedd.STYLE_FRAME_BORDERSIZE
#: associated type: ``Vec2``.
STYLE_ITEM_SPACING = embedd.STYLE_ITEM_SPACING
#: associated type: ``Vec2``.
STYLE_ITEM_INNER_SPACING = embedd.STYLE_ITEM_INNER_SPACING
#: associated type: ``float``.
STYLE_INDENT_SPACING = embedd.STYLE_INDENT_SPACING
#: associated type: ``Vec2``.
STYLE_CELL_PADDING = embedd.STYLE_CELL_PADDING
#: associated type: ``float``.
STYLE_SCROLLBAR_SIZE = embedd.STYLE_SCROLLBAR_SIZE
#: associated type: ``float``.
STYLE_SCROLLBAR_ROUNDING = embedd.STYLE_SCROLLBAR_ROUNDING
#: associated type: ``float``.
STYLE_GRAB_MIN_SIZE = embedd.STYLE_GRAB_MIN_SIZE
#: associated type: ``float``.
STYLE_GRAB_ROUNDING = embedd.STYLE_GRAB_ROUNDING
#: associated type: ``float``
STYLE_TAB_ROUNDING = embedd.STYLE_TAB_ROUNDING
#: associated type: flags ImGuiAlign_*.
STYLE_BUTTON_TEXT_ALIGN = embedd.STYLE_BUTTON_TEXT_ALIGN
#: associated type: Vec2
STYLE_SELECTABLE_TEXT_ALIGN = embedd.STYLE_SELECTABLE_TEXT_ALIGN

# === Button Flags (redefines for autodoc)
BUTTON_NONE = embedd.BUTTON_NONE
#: React on left mouse button (default)
BUTTON_MOUSE_BUTTON_LEFT = embedd.BUTTON_MOUSE_BUTTON_LEFT
#: React on right mouse button
BUTTON_MOUSE_BUTTON_RIGHT = embedd.BUTTON_MOUSE_BUTTON_RIGHT
#: React on center mouse button
BUTTON_MOUSE_BUTTON_MIDDLE = embedd.BUTTON_MOUSE_BUTTON_MIDDLE

# === Window flag constants (redefines for autodoc)
#:
WINDOW_NONE = embedd.WINDOW_NONE
#: Disable title-bar.
WINDOW_NO_TITLE_BAR = embedd.WINDOW_NO_TITLE_BAR
#: Disable user resizing with the lower-right grip.
WINDOW_NO_RESIZE = embedd.WINDOW_NO_RESIZE
#: Disable user moving the window.
WINDOW_NO_MOVE = embedd.WINDOW_NO_MOVE
#: Disable scrollbars (window can still scroll with mouse or programmatically).
WINDOW_NO_SCROLLBAR = embedd.WINDOW_NO_SCROLLBAR
#: Disable user vertically scrolling with mouse wheel. On child window, mouse wheel will be forwarded to the parent unless NoScrollbar is also set.
WINDOW_NO_SCROLL_WITH_MOUSE = embedd.WINDOW_NO_SCROLL_WITH_MOUSE
#: Disable user collapsing window by double-clicking on it.
WINDOW_NO_COLLAPSE = embedd.WINDOW_NO_COLLAPSE
#: Resize every window to its content every frame.
WINDOW_ALWAYS_AUTO_RESIZE = embedd.WINDOW_ALWAYS_AUTO_RESIZE
#: Disable drawing background color (WindowBg, etc.) and outside border. Similar as using SetNextWindowBgAlpha(0.0f).
WINDOW_NO_BACKGROUND = embedd.WINDOW_NO_BACKGROUND
#: Never load/save settings in ``.ini`` file.
WINDOW_NO_SAVED_SETTINGS = embedd.WINDOW_NO_SAVED_SETTINGS
#: Disable catching mouse, hovering test with pass through.
WINDOW_NO_MOUSE_INPUTS = embedd.WINDOW_NO_MOUSE_INPUTS
#: Has a menu-bar.
WINDOW_MENU_BAR = embedd.WINDOW_MENU_BAR
#: Allow horizontal scrollbar to appear (off by default). You may use SetNextWindowContentSize(ImVec2(width,0.0f)); prior to calling Begin() to specify width. Read code in imgui_demo in the "Horizontal Scrolling" section.
WINDOW_HORIZONTAL_SCROLLING_BAR = embedd.WINDOW_HORIZONTAL_SCROLLING_BAR
#: Disable taking focus when transitioning from hidden to visible state.
WINDOW_NO_FOCUS_ON_APPEARING = embedd.WINDOW_NO_FOCUS_ON_APPEARING
#: Disable bringing window to front when taking focus (e.g. clicking on it or programmatically giving it focus).
WINDOW_NO_BRING_TO_FRONT_ON_FOCUS = embedd.WINDOW_NO_BRING_TO_FRONT_ON_FOCUS
#: Always show vertical scrollbar (even if ContentSize.y < Size.y).
WINDOW_ALWAYS_VERTICAL_SCROLLBAR = embedd.WINDOW_ALWAYS_VERTICAL_SCROLLBAR
#: Always show horizontal scrollbar (even if ContentSize.x < Size.x).
WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR = embedd.WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR
#: Ensure child windows without border uses style.WindowPadding (ignored by default for non-bordered child windows, because more convenient).
WINDOW_ALWAYS_USE_WINDOW_PADDING = embedd.WINDOW_ALWAYS_USE_WINDOW_PADDING
#: No gamepad/keyboard navigation within the window.
WINDOW_NO_NAV_INPUTS = embedd.WINDOW_NO_NAV_INPUTS
#: No focusing toward this window with gamepad/keyboard navigation (e.g. skipped by CTRL+TAB).
WINDOW_NO_NAV_FOCUS = embedd.WINDOW_NO_NAV_FOCUS
#: Append '*' to title without affecting the ID, as a convenience to avoid using the ### operator. When used in a tab/docking context, tab is selected on closure and closure is deferred by one frame to allow code to cancel the closure (with a confirmation popup, etc.) without flicker.
WINDOW_UNSAVED_DOCUMENT = embedd.WINDOW_UNSAVED_DOCUMENT
#: Shortcut: ``imgui.WINDOW_NO_NAV_INPUTS | imgui.WINDOW_NO_NAV_FOCUS``.
WINDOW_NO_NAV = embedd.WINDOW_NO_NAV
#: Shortcut: ``imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_SCROLLBAR | imgui.WINDOW_NO_COLLAPSE``.
WINDOW_NO_DECORATION = embedd.WINDOW_NO_DECORATION
#: Shortcut: ``imgui.WINDOW_NO_MOUSE_INPUTS | imgui.WINDOW_NO_NAV_INPUTS | imgui.WINDOW_NO_NAV_FOCUS``.
WINDOW_NO_INPUTS = embedd.WINDOW_NO_INPUTS

# === Color Edit Flags (redefines for autodoc)
#:
COLOR_EDIT_NONE = embedd.COLOR_EDIT_NONE
#: ColorEdit, ColorPicker, ColorButton: ignore Alpha component (will only read 3 components from the input pointer).
COLOR_EDIT_NO_ALPHA = embedd.COLOR_EDIT_NO_ALPHA
#: ColorEdit: disable picker when clicking on color square.
COLOR_EDIT_NO_PICKER = embedd.COLOR_EDIT_NO_PICKER
#: ColorEdit: disable toggling options menu when right-clicking on inputs/small preview.
COLOR_EDIT_NO_OPTIONS = embedd.COLOR_EDIT_NO_OPTIONS
#: ColorEdit, ColorPicker: disable color square preview next to the inputs. (e.g. to show only the inputs)
COLOR_EDIT_NO_SMALL_PREVIEW = embedd.COLOR_EDIT_NO_SMALL_PREVIEW
#: ColorEdit, ColorPicker: disable inputs sliders/text widgets (e.g. to show only the small preview color square).
COLOR_EDIT_NO_INPUTS = embedd.COLOR_EDIT_NO_INPUTS
#: ColorEdit, ColorPicker, ColorButton: disable tooltip when hovering the preview.
COLOR_EDIT_NO_TOOLTIP = embedd.COLOR_EDIT_NO_TOOLTIP
#: ColorEdit, ColorPicker: disable display of inline text label (the label is still forwarded to the tooltip and picker).
COLOR_EDIT_NO_LABEL = embedd.COLOR_EDIT_NO_LABEL
#: ColorPicker: disable bigger color preview on right side of the picker, use small color square preview instead.
COLOR_EDIT_NO_SIDE_PREVIEW = embedd.COLOR_EDIT_NO_SIDE_PREVIEW
#: ColorEdit: disable drag and drop target. ColorButton: disable drag and drop source.
COLOR_EDIT_NO_DRAG_DROP = embedd.COLOR_EDIT_NO_DRAG_DROP
#: ColorButton: disable border (which is enforced by default)
COLOR_EDIT_NO_BORDER = embedd.COLOR_EDIT_NO_BORDER

#: ColorEdit, ColorPicker: show vertical alpha bar/gradient in picker.
COLOR_EDIT_ALPHA_BAR = embedd.COLOR_EDIT_ALPHA_BAR
#: ColorEdit, ColorPicker, ColorButton: display preview as a transparent color over a checkerboard, instead of opaque.
COLOR_EDIT_ALPHA_PREVIEW = embedd.COLOR_EDIT_ALPHA_PREVIEW
#: ColorEdit, ColorPicker, ColorButton: display half opaque / half checkerboard, instead of opaque.
COLOR_EDIT_ALPHA_PREVIEW_HALF = embedd.COLOR_EDIT_ALPHA_PREVIEW_HALF
#: (WIP) ColorEdit: Currently only disable 0.0f..1.0f limits in RGBA edition (note: you probably want to use ImGuiColorEditFlags_Float flag as well).
COLOR_EDIT_HDR = embedd.COLOR_EDIT_HDR
#: ColorEdit: override _display_ type among RGB/HSV/Hex. ColorPicker: select any combination using one or more of RGB/HSV/Hex.
COLOR_EDIT_DISPLAY_RGB = embedd.COLOR_EDIT_DISPLAY_RGB
#: ColorEdit: override _display_ type among RGB/HSV/Hex. ColorPicker: select any combination using one or more of RGB/HSV/Hex.
COLOR_EDIT_DISPLAY_HSV = embedd.COLOR_EDIT_DISPLAY_HSV
#: ColorEdit: override _display_ type among RGB/HSV/Hex. ColorPicker: select any combination using one or more of RGB/HSV/Hex.
COLOR_EDIT_DISPLAY_HEX = embedd.COLOR_EDIT_DISPLAY_HEX
#: ColorEdit, ColorPicker, ColorButton: _display_ values formatted as 0..255.
COLOR_EDIT_UINT8 = embedd.COLOR_EDIT_UINT8
#: ColorEdit, ColorPicker, ColorButton: _display_ values formatted as 0.0f..1.0f floats instead of 0..255 integers. No round-trip of value via integers.
COLOR_EDIT_FLOAT = embedd.COLOR_EDIT_FLOAT
#: ColorPicker: bar for Hue, rectangle for Sat/Value.
COLOR_EDIT_PICKER_HUE_BAR = embedd.COLOR_EDIT_PICKER_HUE_BAR
#: ColorPicker: wheel for Hue, triangle for Sat/Value.
COLOR_EDIT_PICKER_HUE_WHEEL = embedd.COLOR_EDIT_PICKER_HUE_WHEEL
#: ColorEdit, ColorPicker: input and output data in RGB format.
COLOR_EDIT_INPUT_RGB = embedd.COLOR_EDIT_INPUT_RGB
#: ColorEdit, ColorPicker: input and output data in HSV format.
COLOR_EDIT_INPUT_HSV = embedd.COLOR_EDIT_INPUT_HSV

#: Shortcut: ``imgui.COLOR_EDIT_UINT8 | imgui.COLOR_EDIT_DISPLAY_RGB | imgui.COLOR_EDIT_INPUT_RGB | imgui.COLOR_EDIT_PICKER_HUE_BAR``.
COLOR_EDIT_DEFAULT_OPTIONS = embedd.COLOR_EDIT_DEFAULT_OPTIONS

# === Tree node flag constants (redefines for autodoc)
#:
TREE_NODE_NONE = embedd.TREE_NODE_NONE
#: Draw as selected
TREE_NODE_SELECTED = embedd.TREE_NODE_SELECTED
#: Draw frame with background (e.g. for :func:`imgui.embedd.collapsing_header`).
TREE_NODE_FRAMED = embedd.TREE_NODE_FRAMED
#: Hit testing to allow subsequent widgets to overlap this one
TREE_NODE_ALLOW_ITEM_OVERLAP = embedd.TREE_NODE_ALLOW_ITEM_OVERLAP
#: Don't do a ``TreePush()`` when open
#: (e.g. for :func:`imgui.embedd.collapsing_header`).
#: No extra indent nor pushing on ID stack.
TREE_NODE_NO_TREE_PUSH_ON_OPEN = embedd.TREE_NODE_NO_TREE_PUSH_ON_OPEN
#: Don't automatically and temporarily open node when Logging is active
#: (by default logging will automatically open tree nodes).
TREE_NODE_NO_AUTO_OPEN_ON_LOG = embedd.TREE_NODE_NO_AUTO_OPEN_ON_LOG
#: Default node to be open
TREE_NODE_DEFAULT_OPEN = embedd.TREE_NODE_DEFAULT_OPEN
#: Need double-click to open node.
TREE_NODE_OPEN_ON_DOUBLE_CLICK = embedd.TREE_NODE_OPEN_ON_DOUBLE_CLICK
#: Only open when clicking on the arrow part. If
#: :py:data:`TREE_NODE_OPEN_ON_DOUBLE_CLICK` is also set,
#: single-click arrow or double-click all box to open.
TREE_NODE_OPEN_ON_ARROW = embedd.TREE_NODE_OPEN_ON_ARROW
#: No collapsing, no arrow (use as a convenience for leaf nodes).
TREE_NODE_LEAF = embedd.TREE_NODE_LEAF
#: Display a bullet instead of arrow.
TREE_NODE_BULLET = embedd.TREE_NODE_BULLET
#: Use FramePadding (even for an unframed text node) to vertically align
#: text baseline to regular widget height. Equivalent to calling
#: ``align_text_to_frame_padding()``
TREE_NODE_FRAME_PADDING = embedd.TREE_NODE_FRAME_PADDING
#: Extend hit box to the right-most edge, even if not framed. This is not the default in order to allow adding other items on the same line. In the future we may refactor the hit system to be front-to-back, allowing natural overlaps and then this can become the default.
TREE_NODE_SPAN_AVAILABLE_WIDTH = embedd.TREE_NODE_SPAN_AVAILABLE_WIDTH
#: Extend hit box to the left-most and right-most edges (bypass the indented area).
TREE_NODE_SPAN_FULL_WIDTH = embedd.TREE_NODE_SPAN_FULL_WIDTH
#: (WIP) Nav: left direction may move to this TreeNode() from any of its child (items submitted between TreeNode and TreePop)
TREE_NODE_NAV_LEFT_JUPS_BACK_HERE = embedd.TREE_NODE_NAV_LEFT_JUPS_BACK_HERE
#: Shortcut: ``imgui.TREE_NODE_FRAMED | imgui.TREE_NODE_NO_AUTO_OPEN_ON_LOG``.
TREE_NODE_COLLAPSING_HEADER = embedd.TREE_NODE_COLLAPSING_HEADER

# === Popup Flags (redefines for autodoc)
POPUP_NONE = embedd.POPUP_NONE
POPUP_MOUSE_BUTTON_LEFT = embedd.POPUP_MOUSE_BUTTON_LEFT
POPUP_MOUSE_BUTTON_RIGHT = embedd.POPUP_MOUSE_BUTTON_RIGHT
POPUP_MOUSE_BUTTON_MIDDLE = embedd.POPUP_MOUSE_BUTTON_MIDDLE
POPUP_MOUSE_BUTTON_MASK = embedd.POPUP_MOUSE_BUTTON_MASK
POPUP_MOUSE_BUTTON_DEFAULT = embedd.POPUP_MOUSE_BUTTON_DEFAULT
POPUP_NO_OPEN_OVER_EXISTING_POPUP = embedd.POPUP_NO_OPEN_OVER_EXISTING_POPUP
POPUP_NO_OPEN_OVER_ITEMS = embedd.POPUP_NO_OPEN_OVER_ITEMS
POPUP_ANY_POPUP_ID = embedd.POPUP_ANY_POPUP_ID
POPUP_ANY_POPUP_LEVEL = embedd.POPUP_ANY_POPUP_LEVEL
POPUP_ANY_POPUP = embedd.POPUP_ANY_POPUP

# === Color flag constants (redefines for autodoc)
COLOR_TEXT = embedd.COLOR_TEXT
COLOR_TEXT_DISABLED = embedd.COLOR_TEXT_DISABLED
COLOR_WINDOW_BACKGROUND = embedd.COLOR_WINDOW_BACKGROUND
COLOR_CHILD_BACKGROUND = embedd.COLOR_CHILD_BACKGROUND
COLOR_POPUP_BACKGROUND = embedd.COLOR_POPUP_BACKGROUND
COLOR_BORDER = embedd.COLOR_BORDER
COLOR_BORDER_SHADOW = embedd.COLOR_BORDER_SHADOW
COLOR_FRAME_BACKGROUND = embedd.COLOR_FRAME_BACKGROUND
COLOR_FRAME_BACKGROUND_HOVERED = embedd.COLOR_FRAME_BACKGROUND_HOVERED
COLOR_FRAME_BACKGROUND_ACTIVE = embedd.COLOR_FRAME_BACKGROUND_ACTIVE
COLOR_TITLE_BACKGROUND = embedd.COLOR_TITLE_BACKGROUND
COLOR_TITLE_BACKGROUND_ACTIVE = embedd.COLOR_TITLE_BACKGROUND_ACTIVE
COLOR_TITLE_BACKGROUND_COLLAPSED = embedd.COLOR_TITLE_BACKGROUND_COLLAPSED
COLOR_MENUBAR_BACKGROUND = embedd.COLOR_MENUBAR_BACKGROUND
COLOR_SCROLLBAR_BACKGROUND = embedd.COLOR_SCROLLBAR_BACKGROUND
COLOR_SCROLLBAR_GRAB = embedd.COLOR_SCROLLBAR_GRAB
COLOR_SCROLLBAR_GRAB_HOVERED = embedd.COLOR_SCROLLBAR_GRAB_HOVERED
COLOR_SCROLLBAR_GRAB_ACTIVE = embedd.COLOR_SCROLLBAR_GRAB_ACTIVE
COLOR_CHECK_MARK = embedd.COLOR_CHECK_MARK
COLOR_SLIDER_GRAB = embedd.COLOR_SLIDER_GRAB
COLOR_SLIDER_GRAB_ACTIVE = embedd.COLOR_SLIDER_GRAB_ACTIVE
COLOR_BUTTON = embedd.COLOR_BUTTON
COLOR_BUTTON_HOVERED = embedd.COLOR_BUTTON_HOVERED
COLOR_BUTTON_ACTIVE = embedd.COLOR_BUTTON_ACTIVE
COLOR_HEADER = embedd.COLOR_HEADER
COLOR_HEADER_HOVERED = embedd.COLOR_HEADER_HOVERED
COLOR_HEADER_ACTIVE = embedd.COLOR_HEADER_ACTIVE
COLOR_SEPARATOR = embedd.COLOR_SEPARATOR
COLOR_SEPARATOR_HOVERED = embedd.COLOR_SEPARATOR_HOVERED
COLOR_SEPARATOR_ACTIVE = embedd.COLOR_SEPARATOR_ACTIVE
COLOR_RESIZE_GRIP = embedd.COLOR_RESIZE_GRIP
COLOR_RESIZE_GRIP_HOVERED = embedd.COLOR_RESIZE_GRIP_HOVERED
COLOR_RESIZE_GRIP_ACTIVE = embedd.COLOR_RESIZE_GRIP_ACTIVE
COLOR_TAB = COLOR_TAB
COLOR_TAB_HOVERED = COLOR_TAB_HOVERED
COLOR_TAB_ACTIVE = COLOR_TAB_ACTIVE
COLOR_TAB_UNFOCUSED = COLOR_TAB_UNFOCUSED
COLOR_TAB_UNFOCUSED_ACTIVE = COLOR_TAB_UNFOCUSED_ACTIVE
COLOR_PLOT_LINES = embedd.COLOR_PLOT_LINES
COLOR_PLOT_LINES_HOVERED = embedd.COLOR_PLOT_LINES_HOVERED
COLOR_PLOT_HISTOGRAM = embedd.COLOR_PLOT_HISTOGRAM
COLOR_PLOT_HISTOGRAM_HOVERED = embedd.COLOR_PLOT_HISTOGRAM_HOVERED
COLOR_TABLE_HEADER_BACKGROUND = embedd.COLOR_TABLE_HEADER_BACKGROUND
COLOR_TABLE_BORDER_STRONG = embedd.COLOR_TABLE_BORDER_STRONG
COLOR_TABLE_BORDER_LIGHT = embedd.COLOR_TABLE_BORDER_LIGHT
COLOR_TABLE_ROW_BACKGROUND = embedd.COLOR_TABLE_ROW_BACKGROUND
COLOR_TABLE_ROW_BACKGROUND_ALT = embedd.COLOR_TABLE_ROW_BACKGROUND_ALT
COLOR_TEXT_SELECTED_BACKGROUND = embedd.COLOR_TEXT_SELECTED_BACKGROUND
COLOR_DRAG_DROP_TARGET = embedd.COLOR_DRAG_DROP_TARGET
COLOR_NAV_HIGHLIGHT = embedd.COLOR_NAV_HIGHLIGHT
COLOR_NAV_WINDOWING_HIGHLIGHT = embedd.COLOR_NAV_WINDOWING_HIGHLIGHT
COLOR_NAV_WINDOWING_DIM_BACKGROUND = embedd.COLOR_NAV_WINDOWING_DIM_BACKGROUND
COLOR_MODAL_WINDOW_DIM_BACKGROUND = embedd.COLOR_MODAL_WINDOW_DIM_BACKGROUND
COLOR_COUNT = embedd.COLOR_COUNT

# === Data Type (redefines for autodoc)
DATA_TYPE_S8     = embedd.DATA_TYPE_S8
DATA_TYPE_U8     = embedd.DATA_TYPE_U8
DATA_TYPE_S16    = embedd.DATA_TYPE_S16
DATA_TYPE_U16    = embedd.DATA_TYPE_U16
DATA_TYPE_S32    = embedd.DATA_TYPE_S32
DATA_TYPE_U32    = embedd.DATA_TYPE_U32
DATA_TYPE_S64    = embedd.DATA_TYPE_S64
DATA_TYPE_U64    = embedd.DATA_TYPE_U64
DATA_TYPE_FLOAT  = embedd.DATA_TYPE_FLOAT
DATA_TYPE_DOUBLE = embedd.DATA_TYPE_DOUBLE


# === Selectable flag constants (redefines for autodoc)
SELECTABLE_NONE = embedd.SELECTABLE_NONE
#: Clicking this don't close parent popup window.
SELECTABLE_DONT_CLOSE_POPUPS = embedd.SELECTABLE_DONT_CLOSE_POPUPS
#: Selectable frame can span all columns
#: (text will still fit in current column).
SELECTABLE_SPAN_ALL_COLUMNS = embedd.SELECTABLE_SPAN_ALL_COLUMNS
#: Generate press events on double clicks too.
SELECTABLE_ALLOW_DOUBLE_CLICK = embedd.SELECTABLE_ALLOW_DOUBLE_CLICK
SELECTABLE_DISABLED = embedd.SELECTABLE_DISABLED
SELECTABLE_ALLOW_ITEM_OVERLAP = embedd.SELECTABLE_ALLOW_ITEM_OVERLAP

# === Combo flag constants (redefines for autodoc)
COMBO_NONE = embedd.COMBO_NONE
#: Align the popup toward the left by default
COMBO_POPUP_ALIGN_LEFT = embedd.COMBO_POPUP_ALIGN_LEFT
#: Max ~4 items visible. Tip: If you want your combo popup to be a
#: specific size you can use SetNextWindowSizeConstraints() prior
#: to calling BeginCombo()
COMBO_HEIGHT_SMALL = embedd.COMBO_HEIGHT_SMALL
#: Max ~8 items visible (default)
COMBO_HEIGHT_REGULAR = embedd.COMBO_HEIGHT_REGULAR
#: Max ~20 items visible
COMBO_HEIGHT_LARGE = embedd.COMBO_HEIGHT_LARGE
#: As many fitting items as possible
COMBO_HEIGHT_LARGEST = embedd.COMBO_HEIGHT_LARGEST
#: Display on the preview box without the square arrow button
COMBO_NO_ARROW_BUTTON = embedd.COMBO_NO_ARROW_BUTTON
#: Display only a square arrow button
COMBO_NO_PREVIEW = embedd.COMBO_NO_PREVIEW
#: Shortcut: ``imgui.COMBO_HEIGHT_SMALL | imgui.COMBO_HEIGHT_REGULAR | imgui.COMBO_HEIGHT_LARGE | imgui.COMBO_HEIGHT_LARGEST``.
COMBO_HEIGHT_MASK = COMBO_HEIGHT_SMALL | COMBO_HEIGHT_REGULAR | COMBO_HEIGHT_LARGE | COMBO_HEIGHT_LARGEST

# === Tab Bar Flags (redefines for autodoc)
TAB_BAR_NONE = embedd.TAB_BAR_NONE
#: Allow manually dragging tabs to re-order them + New tabs are appended at the end of list
TAB_BAR_REORDERABLE = embedd.TAB_BAR_REORDERABLE
#: Automatically select new tabs when they appear
TAB_BAR_AUTO_SELECT_NEW_TABS = embedd.TAB_BAR_AUTO_SELECT_NEW_TABS
#: Disable buttons to open the tab list popup
TAB_BAR_TAB_LIST_POPUP_BUTTON = embedd.TAB_BAR_TAB_LIST_POPUP_BUTTON
#: Disable behavior of closing tabs (that are submitted with p_open != NULL) with middle mouse button. You can still repro this behavior on user's side with if (IsItemHovered() && IsMouseClicked(2)) *p_open = false.
TAB_BAR_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON = embedd.TAB_BAR_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON
#: Disable scrolling buttons (apply when fitting policy is ImGuiTabBarFlags_FittingPolicyScroll)
TAB_BAR_NO_TAB_LIST_SCROLLING_BUTTONS = embedd.TAB_BAR_NO_TAB_LIST_SCROLLING_BUTTONS
#: Disable tooltips when hovering a tab
TAB_BAR_NO_TOOLTIP = embedd.TAB_BAR_NO_TOOLTIP
#: Resize tabs when they don't fit
TAB_BAR_FITTING_POLICY_RESIZE_DOWN = embedd.TAB_BAR_FITTING_POLICY_RESIZE_DOWN
#: Add scroll buttons when tabs don't fit
TAB_BAR_FITTING_POLICY_SCROLL = embedd.TAB_BAR_FITTING_POLICY_SCROLL
#: TAB_BAR_FITTING_POLICY_RESIZE_DOWN | TAB_BAR_FITTING_POLICY_SCROLL
TAB_BAR_FITTING_POLICY_MASK = embedd.TAB_BAR_FITTING_POLICY_MASK
#: TAB_BAR_FITTING_POLICY_RESIZE_DOWN
TAB_BAR_FITTING_POLICY_DEFAULT = embedd.TAB_BAR_FITTING_POLICY_DEFAULT

# === Tab Item Flags (redefines for autodoc)
TAB_ITEM_NONE = embedd.TAB_ITEM_NONE
#: Append '*' to title without affecting the ID, as a convenience to avoid using the ### operator. Also: tab is selected on closure and closure is deferred by one frame to allow code to undo it without flicker.
TAB_ITEM_UNSAVED_DOCUMENT = embedd.TAB_ITEM_UNSAVED_DOCUMENT
#: Trigger flag to programmatically make the tab selected when calling BeginTabItem()
TAB_ITEM_SET_SELECTED = embedd.TAB_ITEM_SET_SELECTED
#: Disable behavior of closing tabs (that are submitted with p_open != NULL) with middle mouse button. You can still repro this behavior on user's side with if (IsItemHovered() && IsMouseClicked(2)) *p_open = false.
TAB_ITEM_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON = embedd.TAB_ITEM_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON
#: Don't call PushID(tab->ID)/PopID() on BeginTabItem()/EndTabItem()
TAB_ITEM_NO_PUSH_ID = embedd.TAB_ITEM_NO_PUSH_ID
#: Disable tooltip for the given tab
TAB_ITEM_NO_TOOLTIP = embedd.TAB_ITEM_NO_TOOLTIP
#: Disable reordering this tab or having another tab cross over this tab
TAB_ITEM_NO_REORDER = embedd.TAB_ITEM_NO_REORDER
#: Enforce the tab position to the left of the tab bar (after the tab list popup button)
TAB_ITEM_LEADING = embedd.TAB_ITEM_LEADING
#: Enforce the tab position to the right of the tab bar (before the scrolling buttons)
TAB_ITEM_TRAILING = embedd.TAB_ITEM_TRAILING


# === Table Flags ===
#: # Features
#: None
TABLE_NONE                   = embedd.TABLE_NONE
#: Enable resizing columns.
TABLE_RESIZABLE              = embedd.TABLE_RESIZABLE
#: Enable reordering columns in header row (need calling TableSetupColumn() + TableHeadersRow() to display headers)
TABLE_REORDERABLE            = embedd.TABLE_REORDERABLE
#: Enable hiding/disabling columns in context menu.
TABLE_HIDEABLE               = embedd.TABLE_HIDEABLE
#: Enable sorting. Call TableGetSortSpecs() to obtain sort specs. Also see ImGuiTableFlags_SortMulti and ImGuiTableFlags_SortTristate.
TABLE_SORTABLE               = embedd.TABLE_SORTABLE
#: Disable persisting columns order, width and sort settings in the .ini file.
TABLE_NO_SAVED_SETTINGS      = embedd.TABLE_NO_SAVED_SETTINGS
#: Right-click on columns body/contents will display table context menu. By default it is available in TableHeadersRow().
TABLE_CONTEXT_MENU_IN_BODY   = embedd.TABLE_CONTEXT_MENU_IN_BODY
#: # Decorations
#: Set each RowBg color with ImGuiCol_TableRowBg or ImGuiCol_TableRowBgAlt (equivalent of calling TableSetBgColor with ImGuiTableBgFlags_RowBg0 on each row manually)
TABLE_ROW_BACKGROUND                    = embedd.TABLE_ROW_BACKGROUND
#: Draw horizontal borders between rows.
TABLE_BORDERS_INNER_HORIZONTAL          = embedd.TABLE_BORDERS_INNER_HORIZONTAL
#: Draw horizontal borders at the top and bottom.
TABLE_BORDERS_OUTER_HORIZONTAL          = embedd.TABLE_BORDERS_OUTER_HORIZONTAL
#: Draw vertical borders between columns.
TABLE_BORDERS_INNER_VERTICAL            = embedd.TABLE_BORDERS_INNER_VERTICAL
#: Draw vertical borders on the left and right sides.
TABLE_BORDERS_OUTER_VERTICAL            = embedd.TABLE_BORDERS_OUTER_VERTICAL
#: Draw horizontal borders.
TABLE_BORDERS_HORIZONTAL                = embedd.TABLE_BORDERS_HORIZONTAL
#: Draw vertical borders.
TABLE_BORDERS_VERTICAL                  = embedd.TABLE_BORDERS_VERTICAL
#: Draw inner borders.
TABLE_BORDERS_INNER                     = embedd.TABLE_BORDERS_INNER
#: Draw outer borders.
TABLE_BORDERS_OUTER                     = embedd.TABLE_BORDERS_OUTER
#: Draw all borders.
TABLE_BORDERS                           = embedd.TABLE_BORDERS
#: [ALPHA] Disable vertical borders in columns Body (borders will always appears in Headers). -> May move to style
TABLE_NO_BORDERS_IN_BODY                = embedd.TABLE_NO_BORDERS_IN_BODY
#: [ALPHA] Disable vertical borders in columns Body until hovered for resize (borders will always appears in Headers). -> May move to style
TABLE_NO_BORDERS_IN_BODY_UTIL_RESIZE    = embedd.TABLE_NO_BORDERS_IN_BODY_UTIL_RESIZE
#: # Sizing Policy (read above for defaults)
#: Columns default to _WidthFixed or _WidthAuto (if resizable or not resizable), matching contents width.
TABLE_SIZING_FIXED_FIT      = embedd.TABLE_SIZING_FIXED_FIT
#: Columns default to _WidthFixed or _WidthAuto (if resizable or not resizable), matching the maximum contents width of all columns. Implicitly enable ImGuiTableFlags_NoKeepColumnsVisible.
TABLE_SIZING_FIXED_SAME     = embedd.TABLE_SIZING_FIXED_SAME
#: Columns default to _WidthStretch with default weights proportional to each columns contents widths.
TABLE_SIZING_STRETCH_PROP   = embedd.TABLE_SIZING_STRETCH_PROP
#: Columns default to _WidthStretch with default weights all equal, unless overriden by TableSetupColumn().
TABLE_SIZING_STRETCH_SAME   = embedd.TABLE_SIZING_STRETCH_SAME
#: # Sizing Extra Options
#: Make outer width auto-fit to columns, overriding outer_size.x value. Only available when ScrollX/ScrollY are disabled and Stretch columns are not used.
TABLE_NO_HOST_EXTEND_X          = embedd.TABLE_NO_HOST_EXTEND_X
#: Make outer height stop exactly at outer_size.y (prevent auto-extending table past the limit). Only available when ScrollX/ScrollY are disabled. Data below the limit will be clipped and not visible.
TABLE_NO_HOST_EXTEND_Y          = embedd.TABLE_NO_HOST_EXTEND_Y
#: Disable keeping column always minimally visible when ScrollX is off and table gets too small. Not recommended if columns are resizable.
TABLE_NO_KEEP_COLUMNS_VISIBLE   = embedd.TABLE_NO_KEEP_COLUMNS_VISIBLE
#: Disable distributing remainder width to stretched columns (width allocation on a 100-wide table with 3 columns: Without this flag: 33,33,34. With this flag: 33,33,33). With larger number of columns, resizing will appear to be less smooth.
TABLE_PRECISE_WIDTHS            = embedd.TABLE_PRECISE_WIDTHS
#: # Clipping
#: Disable clipping rectangle for every individual columns (reduce draw command count, items will be able to overflow into other columns). Generally incompatible with TableSetupScrollFreeze().
TABLE_NO_CLIP = embedd.TABLE_NO_CLIP
#: # Padding
#: Default if BordersOuterV is on. Enable outer-most padding. Generally desirable if you have headers.
TABLE_PAD_OUTER_X       = embedd.TABLE_PAD_OUTER_X
#: Default if BordersOuterV is off. Disable outer-most padding.
TABLE_NO_PAD_OUTER_X    = embedd.TABLE_NO_PAD_OUTER_X
#: Disable inner padding between columns (double inner padding if BordersOuterV is on, single inner padding if BordersOuterV is off).
TABLE_NO_PAD_INNER_X    = embedd.TABLE_NO_PAD_INNER_X
#: # Scrolling
#: Enable horizontal scrolling. Require 'outer_size' parameter of BeginTable() to specify the container size. Changes default sizing policy. Because this create a child window, ScrollY is currently generally recommended when using ScrollX.
TABLE_SCROLL_X = embedd.TABLE_SCROLL_X
#: Enable vertical scrolling. Require 'outer_size' parameter of BeginTable() to specify the container size.
TABLE_SCROLL_Y = embedd.TABLE_SCROLL_Y
#: # Sorting
#: Hold shift when clicking headers to sort on multiple column. TableGetSortSpecs() may return specs where (SpecsCount > 1).
TABLE_SORT_MULTI    = embedd.TABLE_SORT_MULTI
#: Allow no sorting, disable default sorting. TableGetSortSpecs() may return specs where (SpecsCount == 0).
TABLE_SORT_TRISTATE = embedd.TABLE_SORT_TRISTATE

# === Table Column Flags ===
#: # Input configuration flags
#: None
TABLE_COLUMN_NONE                   = embedd.TABLE_COLUMN_NONE
#: Default as a hidden/disabled column.
TABLE_COLUMN_DEFAULT_HIDE           = embedd.TABLE_COLUMN_DEFAULT_HIDE
#: Default as a sorting column.
TABLE_COLUMN_DEFAULT_SORT           = embedd.TABLE_COLUMN_DEFAULT_SORT
#: Column will stretch. Preferable with horizontal scrolling disabled (default if table sizing policy is _SizingStretchSame or _SizingStretchProp).
TABLE_COLUMN_WIDTH_STRETCH          = embedd.TABLE_COLUMN_WIDTH_STRETCH
#: Column will not stretch. Preferable with horizontal scrolling enabled (default if table sizing policy is _SizingFixedFit and table is resizable).
TABLE_COLUMN_WIDTH_FIXED            = embedd.TABLE_COLUMN_WIDTH_FIXED
#: Disable manual resizing.
TABLE_COLUMN_NO_RESIZE              = embedd.TABLE_COLUMN_NO_RESIZE
#: Disable manual reordering this column, this will also prevent other columns from crossing over this column.
TABLE_COLUMN_NO_REORDER             = embedd.TABLE_COLUMN_NO_REORDER
#: Disable ability to hide/disable this column.
TABLE_COLUMN_NO_HIDE                = embedd.TABLE_COLUMN_NO_HIDE
#: Disable clipping for this column (all NoClip columns will render in a same draw command).
TABLE_COLUMN_NO_CLIP                = embedd.TABLE_COLUMN_NO_CLIP
#: Disable ability to sort on this field (even if ImGuiTableFlags_Sortable is set on the table).
TABLE_COLUMN_NO_SORT                = embedd.TABLE_COLUMN_NO_SORT
#: Disable ability to sort in the ascending direction.
TABLE_COLUMN_NO_SORT_ASCENDING      = embedd.TABLE_COLUMN_NO_SORT_ASCENDING
#: Disable ability to sort in the descending direction.
TABLE_COLUMN_NO_SORT_DESCENDING     = embedd.TABLE_COLUMN_NO_SORT_DESCENDING
#: Disable header text width contribution to automatic column width.
TABLE_COLUMN_NO_HEADER_WIDTH        = embedd.TABLE_COLUMN_NO_HEADER_WIDTH
#: Make the initial sort direction Ascending when first sorting on this column (default).
TABLE_COLUMN_PREFER_SORT_ASCENDING  = embedd.TABLE_COLUMN_PREFER_SORT_ASCENDING
#: Make the initial sort direction Descending when first sorting on this column.
TABLE_COLUMN_PREFER_SORT_DESCENDING = embedd.TABLE_COLUMN_PREFER_SORT_DESCENDING
#: Use current Indent value when entering cell (default for column 0).
TABLE_COLUMN_INDENT_ENABLE          = embedd.TABLE_COLUMN_INDENT_ENABLE
#: Ignore current Indent value when entering cell (default for columns > 0). Indentation changes _within_ the cell will still be honored.
TABLE_COLUMN_INDENT_DISABLE         = embedd.TABLE_COLUMN_INDENT_DISABLE
#: # Output status flags, read-only via TableGetColumnFlags()
#: Status: is enabled == not hidden by user/api (referred to as "Hide" in _DefaultHide and _NoHide) flags.
TABLE_COLUMN_IS_ENABLED     = embedd.TABLE_COLUMN_IS_ENABLED
#: Status: is visible == is enabled AND not clipped by scrolling.
TABLE_COLUMN_IS_VISIBLE     = embedd.TABLE_COLUMN_IS_VISIBLE
#: Status: is currently part of the sort specs
TABLE_COLUMN_IS_SORTED      = embedd.TABLE_COLUMN_IS_SORTED
#: Status: is hovered by mouse
TABLE_COLUMN_IS_HOVERED     = embedd.TABLE_COLUMN_IS_HOVERED

# === Table Row Flags ===
#: None
TABLE_ROW_NONE      = embedd.TABLE_ROW_NONE
#: Identify header row (set default background color + width of its contents accounted different for auto column width)
TABLE_ROW_HEADERS   = embedd.TABLE_ROW_HEADERS

# === Table Background Target ===
#: None
TABLE_BACKGROUND_TARGET_NONE        = embedd.TABLE_BACKGROUND_TARGET_NONE
#: Set row background color 0 (generally used for background, automatically set when ImGuiTableFlags_RowBg is used)
TABLE_BACKGROUND_TARGET_ROW_BG0     = embedd.TABLE_BACKGROUND_TARGET_ROW_BG0
#: Set row background color 1 (generally used for selection marking)
TABLE_BACKGROUND_TARGET_ROW_BG1     = embedd.TABLE_BACKGROUND_TARGET_ROW_BG1
#: Set cell background color (top-most color)
TABLE_BACKGROUND_TARGET_CELL_BG     = embedd.TABLE_BACKGROUND_TARGET_CELL_BG

# === Focus flag constants (redefines for autodoc)
FOCUS_NONE = embedd.FOCUS_NONE
#: IsWindowFocused(): Return true if any children of the window is focused
FOCUS_CHILD_WINDOWS = embedd.FOCUS_CHILD_WINDOWS
#: IsWindowFocused(): Test from root window (top most parent of the current hierarchy)
FOCUS_ROOT_WINDOW = embedd.FOCUS_ROOT_WINDOW
#: IsWindowFocused(): Return true if any window is focused
FOCUS_ANY_WINDOW = embedd.FOCUS_ANY_WINDOW
#: Shortcut: ``imgui.FOCUS_CHILD_WINDOWS | imgui.FOCUS_ROOT_WINDOW``.
FOCUS_ROOT_AND_CHILD_WINDOWS = embedd.FOCUS_CHILD_WINDOWS | embedd.FOCUS_ROOT_WINDOW

# === Hovered flag constants (redefines for autodoc)
#: Return true if directly over the item/window, not obstructed by
#: another window, not obstructed by an active popup or modal
#: blocking inputs under them.
HOVERED_NONE = embedd.HOVERED_NONE
#: IsWindowHovered() only: Return true if any children of the window is hovered
HOVERED_CHILD_WINDOWS = embedd.HOVERED_CHILD_WINDOWS
#: IsWindowHovered() only: Test from root window (top most parent of the current hierarchy)
HOVERED_ROOT_WINDOW = embedd.HOVERED_ROOT_WINDOW
#: IsWindowHovered() only: Return true if any window is hovered
HOVERED_ANY_WINDOW = embedd.HOVERED_ANY_WINDOW
#: Return true even if a popup window is normally blocking access to this item/window
HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP = embedd.HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP
#: Return true even if an active item is blocking access to this item/window. Useful for Drag and Drop patterns.
HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM = embedd.HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM
#: Return true even if the position is overlapped by another window
HOVERED_ALLOW_WHEN_OVERLAPPED = embedd.HOVERED_ALLOW_WHEN_OVERLAPPED
HOVERED_ALLOW_WHEN_DISABLED = embedd.HOVERED_ALLOW_WHEN_DISABLED
#: Shortcut: ``imgui.HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP | imgui.HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM | imgui.HOVERED_ALLOW_WHEN_OVERLAPPED``.
HOVERED_RECT_ONLY = embedd.HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP | embedd.HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM | embedd.HOVERED_ALLOW_WHEN_OVERLAPPED
#: Shortcut: ``imgui.HOVERED_ROOT_WINDOW | imgui.HOVERED_CHILD_WINDOWS``.
HOVERED_ROOT_AND_CHILD_WINDOWS = embedd.HOVERED_ROOT_WINDOW | embedd.HOVERED_CHILD_WINDOWS

# === Drag Drop flag constants (redefines for autodoc)
DRAG_DROP_NONE = embedd.DRAG_DROP_NONE
#: By default, a successful call to BeginDragDropSource opens a tooltip
#: so you can display a preview or description of the source contents.
#: This flag disable this behavior.
DRAG_DROP_SOURCE_NO_PREVIEW_TOOLTIP = embedd.DRAG_DROP_SOURCE_NO_PREVIEW_TOOLTIP
#: By default, when dragging we clear data so that IsItemHovered() will
#: return true, to avoid subsequent user code submitting tooltips. This
#: flag disable this behavior so you can still call IsItemHovered() on
#: the source item.
DRAG_DROP_SOURCE_NO_DISABLE_HOVER = embedd.DRAG_DROP_SOURCE_NO_DISABLE_HOVER
#: Disable the behavior that allows to open tree nodes and collapsing
#: header by holding over them while dragging a source item.
DRAG_DROP_SOURCE_NO_HOLD_TO_OPEN_OTHERS = embedd.DRAG_DROP_SOURCE_NO_HOLD_TO_OPEN_OTHERS
#: Allow items such as Text(), Image() that have no unique identifier to
#: be used as drag source, by manufacturing a temporary identifier based
#: on their window-relative position. This is extremely unusual within the
#: dear imgui ecosystem and so we made it explicit.
DRAG_DROP_SOURCE_ALLOW_NULL_ID = embedd.DRAG_DROP_SOURCE_ALLOW_NULL_ID
#: External source (from outside of imgui), won't attempt to read current
#: item/window info. Will always return true. Only one Extern source can
#: be active simultaneously.
DRAG_DROP_SOURCE_EXTERN = embedd.DRAG_DROP_SOURCE_EXTERN
#: Automatically expire the payload if the source cease to be submitted
#: (otherwise payloads are persisting while being dragged)
DRAG_DROP_SOURCE_AUTO_EXPIRE_PAYLOAD = embedd.DRAG_DROP_SOURCE_AUTO_EXPIRE_PAYLOAD

# === Accept Drag Drop Payload flag constants (redefines for autodoc)
#: AcceptDragDropPayload() will returns true even before the mouse button
#: is released. You can then call IsDelivery() to test if the payload
#: needs to be delivered.
DRAG_DROP_ACCEPT_BEFORE_DELIVERY = embedd.DRAG_DROP_ACCEPT_BEFORE_DELIVERY
#: Do not draw the default highlight rectangle when hovering over target.
DRAG_DROP_ACCEPT_NO_DRAW_DEFAULT_RECT = embedd.DRAG_DROP_ACCEPT_NO_DRAW_DEFAULT_RECT
DRAG_DROP_ACCEPT_NO_PREVIEW_TOOLTIP = embedd.DRAG_DROP_ACCEPT_NO_PREVIEW_TOOLTIP
#: For peeking ahead and inspecting the payload before delivery.
DRAG_DROP_ACCEPT_PEEK_ONLY = embedd.DRAG_DROP_ACCEPT_PEEK_ONLY

# === Cardinal Direction
#: Direction None
DIRECTION_NONE = embedd.DIRECTION_NONE
#: Direction Left
DIRECTION_LEFT = embedd.DIRECTION_LEFT
#: Direction Right
DIRECTION_RIGHT = embedd.DIRECTION_RIGHT
#: Direction Up
DIRECTION_UP = embedd.DIRECTION_UP
#: Direction Down
DIRECTION_DOWN = embedd.DIRECTION_DOWN

# === Sorting direction
SORT_DIRECTION_NONE  = embedd.SORT_DIRECTION_NONE
#: Ascending = 0->9, A->Z etc.
SORT_DIRECTION_ASCENDING = embedd.SORT_DIRECTION_ASCENDING
#: Descending = 9->0, Z->A etc.
SORT_DIRECTION_DESCENDING = embedd.SORT_DIRECTION_DESCENDING

# === Mouse cursor flag constants (redefines for autodoc)
MOUSE_CURSOR_NONE = embedd.MOUSE_CURSOR_NONE
MOUSE_CURSOR_ARROW = embedd.MOUSE_CURSOR_ARROW
#: When hovering over InputText, etc.
MOUSE_CURSOR_TEXT_INPUT = embedd.MOUSE_CURSOR_TEXT_INPUT
#: Unused
MOUSE_CURSOR_RESIZE_ALL = embedd.MOUSE_CURSOR_RESIZE_ALL
#: When hovering over an horizontal border
MOUSE_CURSOR_RESIZE_NS = embedd.MOUSE_CURSOR_RESIZE_NS
#: When hovering over a vertical border or a column
MOUSE_CURSOR_RESIZE_EW = embedd.MOUSE_CURSOR_RESIZE_EW
#: When hovering over the bottom-left corner of a window
MOUSE_CURSOR_RESIZE_NESW = embedd.MOUSE_CURSOR_RESIZE_NESW
#: When hovering over the bottom-right corner of a window
MOUSE_CURSOR_RESIZE_NWSE = embedd.MOUSE_CURSOR_RESIZE_NWSE
#: (Unused by imgui functions. Use for e.g. hyperlinks)
MOUSE_CURSOR_HAND = embedd.MOUSE_CURSOR_HAND
MOUSE_CURSOR_NOT_ALLOWED = embedd.MOUSE_CURSOR_NOT_ALLOWED

# === Text input flag constants (redefines for autodoc)
INPUT_TEXT_NONE = embedd.INPUT_TEXT_NONE
#: Allow ``0123456789.+-*/``
INPUT_TEXT_CHARS_DECIMAL = embedd.INPUT_TEXT_CHARS_DECIMAL
#: Allow ``0123456789ABCDEFabcdef``
INPUT_TEXT_CHARS_HEXADECIMAL = embedd.INPUT_TEXT_CHARS_HEXADECIMAL
#: Turn a..z into A..Z
INPUT_TEXT_CHARS_UPPERCASE = embedd.INPUT_TEXT_CHARS_UPPERCASE
#: Filter out spaces, tabs
INPUT_TEXT_CHARS_NO_BLANK = embedd.INPUT_TEXT_CHARS_NO_BLANK
#: Select entire text when first taking mouse focus
INPUT_TEXT_AUTO_SELECT_ALL = embedd.INPUT_TEXT_AUTO_SELECT_ALL
#: Return 'true' when Enter is pressed (as opposed to when the
#: value was modified)
INPUT_TEXT_ENTER_RETURNS_TRUE = embedd.INPUT_TEXT_ENTER_RETURNS_TRUE
#: Call user function on pressing TAB (for completion handling)
INPUT_TEXT_CALLBACK_COMPLETION = embedd.INPUT_TEXT_CALLBACK_COMPLETION
#: Call user function on pressing Up/Down arrows (for history handling)
INPUT_TEXT_CALLBACK_HISTORY = embedd.INPUT_TEXT_CALLBACK_HISTORY
#: Call user function every time. User code may query cursor position,
#: modify text buffer.
INPUT_TEXT_CALLBACK_ALWAYS = embedd.INPUT_TEXT_CALLBACK_ALWAYS
#: Call user function to filter character. Modify data->EventChar to
#: replace/filter input, or return 1 to discard character.
INPUT_TEXT_CALLBACK_CHAR_FILTER = embedd.INPUT_TEXT_CALLBACK_CHAR_FILTER
#: Pressing TAB input a '\t' character into the text field
INPUT_TEXT_ALLOW_TAB_INPUT = embedd.INPUT_TEXT_ALLOW_TAB_INPUT
#: In multi-line mode, allow exiting edition by pressing Enter.
#: Ctrl+Enter to add new line (by default adds new lines with Enter).
INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE = embedd.INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE
#: Disable following the cursor horizontally
INPUT_TEXT_NO_HORIZONTAL_SCROLL = embedd.INPUT_TEXT_NO_HORIZONTAL_SCROLL
#: Overwrite mode
INPUT_TEXT_ALWAYS_OVERWRITE = embedd.INPUT_TEXT_ALWAYS_OVERWRITE
#: OBSOLETED in 1.82 (from Mars 2021)
INPUT_TEXT_ALWAYS_INSERT_MODE = embedd.INPUT_TEXT_ALWAYS_INSERT_MODE
#: Read-only mode
INPUT_TEXT_READ_ONLY = embedd.INPUT_TEXT_READ_ONLY
#: Password mode, display all characters as '*'
INPUT_TEXT_PASSWORD = embedd.INPUT_TEXT_PASSWORD
#: Disable undo/redo. Note that input text owns the text data while
#: active, if you want to provide your own undo/redo stack you need
#: e.g. to call clear_active_id().
INPUT_TEXT_NO_UNDO_REDO = embedd.INPUT_TEXT_NO_UNDO_REDO
INPUT_TEXT_CHARS_SCIENTIFIC = embedd.INPUT_TEXT_CHARS_SCIENTIFIC
INPUT_TEXT_CALLBACK_RESIZE = embedd.INPUT_TEXT_CALLBACK_RESIZE
INPUT_TEXT_CALLBACK_EDIT = embedd.INPUT_TEXT_CALLBACK_EDIT

# === Draw Corner Flags (redefines for autodoc)
DRAW_CORNER_NONE = embedd.DRAW_CORNER_NONE
DRAW_CORNER_TOP_LEFT = embedd.DRAW_CORNER_TOP_LEFT
DRAW_CORNER_TOP_RIGHT = embedd.DRAW_CORNER_TOP_RIGHT
DRAW_CORNER_BOTTOM_LEFT = embedd.DRAW_CORNER_BOTTOM_LEFT
DRAW_CORNER_BOTTOM_RIGHT = embedd.DRAW_CORNER_BOTTOM_RIGHT
DRAW_CORNER_TOP = embedd.DRAW_CORNER_TOP
DRAW_CORNER_BOTTOM = embedd.DRAW_CORNER_BOTTOM
DRAW_CORNER_LEFT = embedd.DRAW_CORNER_LEFT
DRAW_CORNER_RIGHT = embedd.DRAW_CORNER_RIGHT
DRAW_CORNER_ALL = embedd.DRAW_CORNER_ALL

# === Draw Flags (redifines for autodoc)
#: None
DRAW_NONE                        = embedd.DRAW_NONE
#: path_stroke(), add_polyline(): specify that shape should be closed (Important: this is always == 1 for legacy reason)
DRAW_CLOSED                      = embedd.DRAW_CLOSED
#: add_rect(), add_rect_filled(), path_rect(): enable rounding top-left corner only (when rounding > 0.0f, we default to all corners). Was 0x01.
DRAW_ROUND_CORNERS_TOP_LEFT      = embedd.DRAW_ROUND_CORNERS_TOP_LEFT
#: add_rect(), add_rect_filled(), path_rect(): enable rounding top-right corner only (when rounding > 0.0f, we default to all corners). Was 0x02.
DRAW_ROUND_CORNERS_TOP_RIGHT     = embedd.DRAW_ROUND_CORNERS_TOP_RIGHT
#: add_rect(), add_rect_filled(), path_rect(): enable rounding bottom-left corner only (when rounding > 0.0f, we default to all corners). Was 0x04.
DRAW_ROUND_CORNERS_BOTTOM_LEFT   = embedd.DRAW_ROUND_CORNERS_BOTTOM_LEFT
#: add_rect(), add_rect_filled(), path_rect(): enable rounding bottom-right corner only (when rounding > 0.0f, we default to all corners). Wax 0x08.
DRAW_ROUND_CORNERS_BOTTOM_RIGHT  = embedd.DRAW_ROUND_CORNERS_BOTTOM_RIGHT
#: add_rect(), add_rect_filled(), path_rect(): disable rounding on all corners (when rounding > 0.0f). This is NOT zero, NOT an implicit flag!
DRAW_ROUND_CORNERS_NONE          = embedd.DRAW_ROUND_CORNERS_NONE
#: DRAW_ROUND_CORNERS_TOP_LEFT | DRAW_ROUND_CORNERS_TOP_RIGHT
DRAW_ROUND_CORNERS_TOP           = embedd.DRAW_ROUND_CORNERS_TOP
#: DRAW_ROUND_CORNERS_BOTTOM_LEFT | DRAW_ROUND_CORNERS_BOTTOM_RIGHT
DRAW_ROUND_CORNERS_BOTTOM        = embedd.DRAW_ROUND_CORNERS_BOTTOM
#: DRAW_ROUND_CORNERS_BOTTOM_LEFT | DRAW_ROUND_CORNERS_TOP_LEFT
DRAW_ROUND_CORNERS_LEFT          = embedd.DRAW_ROUND_CORNERS_LEFT
#: DRAW_ROUND_CORNERS_BOTTOM_RIGHT | DRAW_ROUND_CORNERS_TOP_RIGHT
DRAW_ROUND_CORNERS_RIGHT         = embedd.DRAW_ROUND_CORNERS_RIGHT
#: DRAW_ROUND_CORNERS_TOP_LEFT | DRAW_ROUND_CORNERS_TOP_RIGHT | DRAW_ROUND_CORNERS_BOTTOM_LEFT | DRAW_ROUND_CORNERS_BOTTOM_RIGHT
DRAW_ROUND_CORNERS_ALL           = embedd.DRAW_ROUND_CORNERS_ALL

# === Draw List Flags (redefines for autodoc)
DRAW_LIST_NONE = embedd.DRAW_LIST_NONE
DRAW_LIST_ANTI_ALIASED_LINES = embedd.DRAW_LIST_ANTI_ALIASED_LINES
DRAW_LIST_ANTI_ALIASED_LINES_USE_TEX = embedd.DRAW_LIST_ANTI_ALIASED_LINES_USE_TEX
DRAW_LIST_ANTI_ALIASED_FILL = embedd.DRAW_LIST_ANTI_ALIASED_FILL
DRAW_LIST_ALLOW_VTX_OFFSET = embedd.DRAW_LIST_ALLOW_VTX_OFFSET

# === Font Atlas Flags (redefines for autodoc)
FONT_ATLAS_NONE = embedd.FONT_ATLAS_NONE
FONT_ATLAS_NO_POWER_OF_TWO_HEIGHT = embedd.FONT_ATLAS_NO_POWER_OF_TWO_HEIGHT
FONT_ATLAS_NO_MOUSE_CURSOR = embedd.FONT_ATLAS_NO_MOUSE_CURSOR
FONT_ATLAS_NO_BAKED_LINES = embedd.FONT_ATLAS_NO_BAKED_LINES

# === Config Flags (redefines for autodoc)
CONFIG_NONE = embedd.CONFIG_NONE
CONFIG_NAV_ENABLE_KEYBOARD = embedd.CONFIG_NAV_ENABLE_KEYBOARD
CONFIG_NAV_ENABLE_GAMEPAD = embedd.CONFIG_NAV_ENABLE_GAMEPAD
CONFIG_NAV_ENABLE_SET_MOUSE_POS = embedd.CONFIG_NAV_ENABLE_SET_MOUSE_POS
CONFIG_NAV_NO_CAPTURE_KEYBOARD = embedd.CONFIG_NAV_NO_CAPTURE_KEYBOARD
CONFIG_NO_MOUSE = embedd.CONFIG_NO_MOUSE
CONFIG_NO_MOUSE_CURSOR_CHARGE = embedd.CONFIG_NO_MOUSE_CURSOR_CHARGE
CONFIG_IS_RGB = embedd.CONFIG_IS_RGB
CONFIG_IS_TOUCH_SCREEN = embedd.CONFIG_IS_TOUCH_SCREEN

# === Backend Flags (redefines for autodoc)
BACKEND_NONE = embedd.BACKEND_NONE
BACKEND_HAS_GAMEPAD = embedd.BACKEND_HAS_GAMEPAD
BACKEND_HAS_MOUSE_CURSORS = embedd.BACKEND_HAS_MOUSE_CURSORS
BACKEND_HAS_SET_MOUSE_POS = embedd.BACKEND_HAS_SET_MOUSE_POS
BACKEND_RENDERER_HAS_VTX_OFFSET = embedd.BACKEND_RENDERER_HAS_VTX_OFFSET

# === Slider flag (redefines for autodoc)
SLIDER_FLAGS_NONE
#: Clamp value to min/max bounds when input manually with CTRL+Click. By default CTRL+Click allows going out of bounds.
SLIDER_FLAGS_ALWAYS_CLAMP
#: Make the widget logarithmic (linear otherwise). Consider using ImGuiSliderFlags_NoRoundToFormat with this if using a format-string with small amount of digits.
SLIDER_FLAGS_LOGARITHMIC
#: Disable rounding underlying value to match precision of the display format string (e.g. %.3f values are rounded to those 3 digits)
SLIDER_FLAGS_NO_ROUND_TO_FORMAT
#: Disable CTRL+Click or Enter key allowing to input text directly into the widget
SLIDER_FLAGS_NO_INPUT

# === Mouse Button (redefines for autodoc)
MOUSE_BUTTON_LEFT = embedd.MOUSE_BUTTON_LEFT
MOUSE_BUTTON_RIGHT = embedd.MOUSE_BUTTON_RIGHT
MOUSE_BUTTON_MIDDLE = embedd.MOUSE_BUTTON_MIDDLE

# === Viewport Flags (redifines for autodoc)
#: None
VIEWPORT_FLAGS_NONE                = embedd.VIEWPORT_FLAGS_NONE
#: Represent a Platform Window
VIEWPORT_FLAGS_IS_PLATFORM_WINDOW  = embedd.VIEWPORT_FLAGS_IS_PLATFORM_WINDOW
#: Represent a Platform Monitor (unused yet)
VIEWPORT_FLAGS_IS_PLATFORM_MONITOR = embedd.VIEWPORT_FLAGS_IS_PLATFORM_MONITOR
#: Platform Window: is created/managed by the application (rather than a dear imgui backend)
VIEWPORT_FLAGS_OWNED_BY_APP        = embedd.VIEWPORT_FLAGS_OWNED_BY_APP

