# Fluent 2 Design System DESIGN.md

## Overview
Use this specification for productive, cross-platform Microsoft-style applications. Favor approachable structure, strong tokenization, explicit states, and layouts that support work rather than spectacle.

- **Provider:** Microsoft
- **Primary reference:** https://fluent2.microsoft.design/
- **Primary product focus:** Cross-platform Microsoft product UI
- **Platforms:** Web: Yes | web first docs | iOS: Yes | cross-platform guidance | Android: Yes | Android support via Fluent UI | Desktop: Yes | Windows desktop heritage
- **Status:** Active | Fluent 2 current
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Design for productive tasks, not pure marketing impression.
- Use explicit states and accessible contrast throughout.
- Keep surfaces calm and theme-aware.
- Favor approachable geometry over severe sharpness.
- Let component behavior stay predictable across surfaces and themes.

## Color System
Representative Fluent 2 palette for generation. Use tokens in implementation; the hex values below capture the design language without claiming exhaustive token coverage.

- **Brand `#0F6CBD`:** Primary Microsoft-style action and brand emphasis.
- **Brand Pressed `#0C3B5E`:** Pressed or stronger action emphasis.
- **Brand Tint `#EBF3FC`:** Tinted selection, hover, and supportive surfaces.
- **Neutral Foreground `#242424`:** Primary text and icon color.
- **Neutral Background `#FFFFFF`:** Default canvas and card surfaces.
- **Neutral Subtle `#F5F5F5`:** Low-emphasis surface and section grouping.
- **Success `#107C10`:** Success and positive confirmation.
- **Danger `#D13438`:** Error and destructive emphasis.

- **Dark mode guidance:** Strong | light/dark theme built in
- **Theming guidance:** High | theme tokens and brand ramps
- **Semantic token guidance:** Strong | global and alias tokens

## Typography
- Use Segoe UI or the current Microsoft platform type stack.
- Use a clear ramp of display, title, subtitle, body, and caption roles.
- Favor functional, readable text over expressive editorial treatment.
- Use semibold strategically for headers and primary control labels.
- Keep tables and forms typographically compact but not cramped.

- **Official typography note:** Type ramp tokens
- **Iconography:** Fluent System Icons adjacent
- **Motion direction:** Motion tokens and transitions

## Spacing, Radius, Elevation
- Use token-driven spacing with 4px and 8px cadence at the core.
- Use soft radii, typically around 4px to 8px for controls and 8px to 12px for containers.
- Use shadows and elevation quietly; structure should come mostly from spacing and surface value.
- Keep component spacing consistent across adjacent controls and panels.

- **Spacing system note:** Spacing tokens
- **Radius / shape note:** Border radius tokens
- **Elevation / shadow note:** Shadow tokens available

## Layout Rules
- Use app shells with clear header, navigation, and content regions.
- Support both simple single-column screens and multi-pane productivity layouts.
- Use compact density when task throughput matters, but preserve scanability.
- Group related content with subtle container separation rather than loud cards everywhere.
- Make state changes obvious through field messages, badges, and action feedback.

- **Official layout note:** Layout and spacing guidance
- **Responsive behavior:** Responsive/adaptive guidance across surfaces
- **App structure:** Shell, nav, windows, surfaces
- **Data display guidance:** Data viz not central in core Fluent 2

## Navigation Rules
- Use left-side navigation, top tabs, or app shell patterns for complex products.
- Use toolbar patterns for dense command surfaces.
- Use breadcrumbs when users move across deep hierarchies.
- Keep local navigation close to the content area it controls.

- **Official navigation note:** Nav, tabs, toolbar, app shell guidance
- **Pattern note:** Nav drawer, tabs, toolbar, breadcrumbs

## Component Rules
### Button
- **Official naming / aliases:** Button variants with appearance tokens
- **Preferred style:** Prefer clear primary, secondary, and subtle button hierarchy with strong state visibility.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Input field
- **Preferred style:** Use token-driven fields with explicit labels, helper text, and strong focus/error treatments.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Combobox, dropdown
- **Preferred style:** Use comboboxes and dropdowns that support productivity workflows and keyboard use.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use checkboxes, radios, and switches with compact but comfortable spacing and visible states.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use checkboxes, radios, and switches with compact but comfortable spacing and visible states.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use checkboxes, radios, and switches with compact but comfortable spacing and visible states.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** DatePicker, TimePicker adjacent in libraries
- **Preferred style:** Use date and time pickers that align with field composition and enterprise workflows.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Searchbox
- **Preferred style:** Use search boxes that can expand into command or filtering workflows.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menu, MenuList
- **Preferred style:** Use compact menus with clear grouping and keyboard-friendly behavior.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** TabList / tabs
- **Preferred style:** Use tabs and tablists for local view switching in app and panel contexts.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs when deep app hierarchy needs persistent orientation.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Toolbar / app shell header
- **Preferred style:** Use page headers and command bars that prioritize task controls.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Drawer and navigation pane
- **Preferred style:** Use left navigation or pane-based navigation for persistent product structure.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use quiet cards and panels to organize related information blocks.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Table, DataGrid in ecosystem
- **Preferred style:** Use dense but readable tables and grids with visible column hierarchy and state cues.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List
- **Preferred style:** Use structured lists with metadata, avatars, and utility actions where appropriate.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and status pills for state, category, or lightweight metadata.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips for supporting clarification, especially in command-dense interfaces.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Dialog
- **Preferred style:** Use dialogs for focused decisions and side panels for longer secondary tasks.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Toast / message bar
- **Preferred style:** Use toast or message bar feedback without overusing interruption.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Spinner, progress bar
- **Preferred style:** Use spinners, progress bars, and skeletons with explicit surrounding context.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination in web libraries
- **Preferred style:** Use pagination in dense data views when chunking improves throughput and orientation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.


## Content & Accessibility
- Use direct labels and task-oriented copy.
- Make focus, hover, pressed, selected, and disabled states explicit.
- Prefer inline validation and calm status messaging over modal interruption.
- Preserve readable contrast in both light and dark themes.
- Use icons to support labels, not replace them.

- **Accessibility note:** Strong | inclusive by default guidance
- **Content note:** Microcopy guidance present
- **Internationalization note:** Global products assumed
- **Localization / RTL note:** RTL support in Fluent UI ecosystem
- **Validation note:** Validation states standardized in components
- **State model note:** Rest, hover, pressed, selected explicit
- **Privacy / trust note:** Trust and privacy aligned with Microsoft products

## Do / Don't
### Do
- Do make states highly legible and easy to scan.
- Do keep productivity tasks front and center.
- Do use theme-aware surfaces and semantic color roles.
- Do structure dense screens with clear hierarchy and predictable alignment.
- Do use compact controls when the workflow demands efficiency.

### Don't
- Do not make Fluent screens overly playful, bubbly, or consumer-social.
- Do not use oversized shadows or high-gloss surfaces.
- Do not hide state changes behind subtle color-only differences.
- Do not over-brand the shell when the product task should dominate.
- Do not replace standard productivity components with experimental shapes.

## Dashboard Mock Guardrails
- Use calm token-driven surfaces with subtle dividers instead of decorative shells or glossy header treatments.
- Keep exactly one prominent primary action per task area and demote the rest to outline, subtle, or transparent styles.
- Use short task-oriented nav labels and support icon-led navigation where it helps recognition.
- Write status labels in short sentence-style language and keep badges semantically focused rather than ornamental.

## Screen Generation Heuristics
- **Default page structure:** Use a productivity shell with persistent navigation, clear page title, command region, and structured content panes.
- **Default density:** Use medium-to-compact density by default.
- **Default navigation model:** Use left navigation, tabs, toolbars, and contextual command surfaces.
- **Preferred form composition:** Use aligned labeled fields, strong helper text, inline validation, and clearly grouped actions.
- **Preferred feedback pattern:** Use message bars, toasts, inline status, and dialogs only when interruption is necessary.
- **Preferred data-display pattern:** Use structured tables, lists, cards, and panels with visible status metadata.
- **Prompt bias:** Use prompts such as 'Fluent 2 productivity app', 'Microsoft admin console', 'calm neutral surfaces', and 'explicit stateful controls'.
- **Component naming consistency:** High | conventional names
- **Layout rule explicitness:** High | spacing and layout tokens explicit
- **Theme describability:** High | theme tokens map cleanly to prompts
- **Prompt-to-UI suitability:** High | strong for cross-platform enterprise prompts

## Official Sources
- https://fluent2.microsoft.design/
- https://fluent2.microsoft.design/color
- https://fluent2.microsoft.design/typography
- https://fluent2.microsoft.design/layout
- https://fluent2.microsoft.design/components/web/react/core/button/usage
