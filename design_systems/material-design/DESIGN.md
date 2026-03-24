# Material Design DESIGN.md

## Overview
Use this specification for adaptive product UI that should feel expressive, structured, and modern without becoming ornamental. Favor semantic color roles, clear hierarchy, and component choices that scale from mobile to desktop.

- **Provider:** Google
- **Primary reference:** https://m3.material.io/
- **Primary product focus:** Cross-platform product UI
- **Platforms:** Web: Yes | core web guidance | iOS: Yes | Android emphasis but adaptable | Android: Yes | Android canonical | Desktop: Yes | large-screen guidance
- **Status:** Active | Material 3 current
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Use semantic roles and emphasis levels rather than arbitrary decoration.
- Prefer adaptive layouts that respond cleanly to narrow, medium, and large screens.
- Use motion to clarify hierarchy and state changes, not to entertain.
- Keep surfaces layered and purposeful.
- Make primary actions obvious and secondary actions quiet.

## Color System
Representative Material 3 palette for generation. Use semantic roles in implementation; the values below are representative rather than exhaustive token exports.

- **Primary `#6750A4`:** Main action color and selected-state emphasis.
- **On Primary `#FFFFFF`:** Text and icons on primary-filled surfaces.
- **Secondary `#625B71`:** Supporting emphasis and alternate accents.
- **Tertiary `#7D5260`:** Expressive accent for supportive highlights.
- **Surface `#FFFBFE`:** Base app surface and page background.
- **Surface Variant `#E7E0EC`:** Container backgrounds, dividers, and low-emphasis grouping.
- **On Surface `#1C1B1F`:** Primary text and icon color on light surfaces.
- **Outline `#79747E`:** Borders, strokes, and inactive emphasis.

- **Dark mode guidance:** Strong | dynamic color and dark theme
- **Theming guidance:** High | color roles and dynamic schemes
- **Semantic token guidance:** Strong | color, type, shape, motion roles

## Typography
- Use Roboto or the platform-default Material type stack.
- Use a clear display/headline/title/body/label hierarchy rather than custom one-off sizes.
- Keep body text neutral and readable; use label styles for compact actions and metadata.
- Use medium weight for primary labels and buttons, regular weight for longer reading.
- Avoid mixing too many type scales in a single view.

- **Official typography note:** Type scale and roles
- **Iconography:** Material Symbols and icons
- **Motion direction:** Motion system and transitions

## Spacing, Radius, Elevation
- Use a 4dp-based spacing rhythm with 8dp and 16dp as the most common steps.
- Use medium rounding by default; prefer 12px to 16px corners for cards, fields, and dialogs.
- Use elevation to separate surfaces, not to create dramatic shadows.
- Let spacing and tonal containers do more work than borders.

- **Spacing system note:** Layout spacing scale
- **Radius / shape note:** Shape scale is first-class
- **Elevation / shadow note:** Elevation levels and surfaces

## Layout Rules
- Use top app bars, navigation bars, rails, or drawers based on screen width and destination count.
- Prefer single-column composition on mobile and wider panes or supporting panels on desktop.
- Group related content into cards or tonal sections when it improves scanability.
- Use dense layouts only when task complexity requires them.
- Keep primary actions anchored near the end of the task flow or in persistent action regions.

- **Official layout note:** Responsive layout guidance
- **Responsive behavior:** Adaptive layouts by breakpoint and window class
- **App structure:** App bars, rails, sheets, panes
- **Data display guidance:** Charts and data display patterns limited

## Navigation Rules
- Use bottom navigation for a small number of top-level destinations on mobile.
- Use navigation rail for larger mobile and tablet layouts when persistent section switching helps.
- Use a drawer for broad information architecture or utility-heavy destinations.
- Use tabs for sibling content views inside a single destination.

- **Official navigation note:** Navigation bar, rail, drawer patterns
- **Pattern note:** Top app bar, nav bar, nav drawer, rail

## Component Rules
### Button
- **Official naming / aliases:** Filled, tonal, outlined, text buttons
- **Preferred style:** Prefer filled buttons for the primary action, tonal or outlined buttons for secondary actions, and text buttons for low-emphasis actions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Filled and outlined text field
- **Preferred style:** Use filled or outlined text fields with visible labels, helper text, and strong focus and error states.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Exposed dropdown menus and autocomplete
- **Preferred style:** Use exposed menus, dropdowns, and autocomplete patterns that align with Material input fields.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use compact, clearly labeled selection controls with explicit selected, disabled, and error states.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio button
- **Preferred style:** Use compact, clearly labeled selection controls with explicit selected, disabled, and error states.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use compact, clearly labeled selection controls with explicit selected, disabled, and error states.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** Date pickers and time pickers
- **Preferred style:** Use date and time pickers that match Material field styling and modal behavior.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Search bar
- **Preferred style:** Use a dedicated search bar or search view with clear focus and filtering affordances.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menus
- **Preferred style:** Use menus and sheets with clear option grouping and moderate rounding.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Primary and secondary tabs
- **Preferred style:** Use primary or secondary tabs with strong selected-state contrast and clear alignment to content panes.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs sparingly; prefer rail, drawer, or tabs before deep breadcrumb chains.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Top app bar
- **Preferred style:** Use top app bars with concise titles, contextual actions, and optional search or overflow.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Navigation drawer and rail
- **Preferred style:** Use rail or drawer patterns with strong current-destination emphasis.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Elevated, filled, outlined cards
- **Preferred style:** Use tonal or elevated cards to group related content and actions.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Data table
- **Preferred style:** Use data tables with clear row density, sortable headers, and restrained inline actions.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists for scanable item collections with avatars, metadata, or trailing actions only when useful.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and chips for status, filters, and lightweight metadata.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Plain and rich tooltip
- **Preferred style:** Use plain or rich tooltips only for supporting clarification.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Dialog and alert dialog
- **Preferred style:** Use dialogs and sheets for blocking choices, focused tasks, or supportive secondary flows.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Snackbar
- **Preferred style:** Use snackbars for transient non-blocking feedback.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Linear, circular, loading indicator
- **Preferred style:** Use circular or linear progress indicators and skeletons that match the surrounding surface hierarchy.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination less central in Material mobile
- **Preferred style:** Use pagination mainly in desktop data-heavy contexts; prefer infinite or chunked scrolling on mobile.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.


## Content & Accessibility
- Use short labels and explicit helper text for form fields.
- Preserve visible focus, pressed, selected, disabled, and error states.
- Do not rely on color alone to convey meaning.
- Use accessible contrast on both tonal and neutral surfaces.
- Pair empty states with action-oriented copy and a clear next step.

- **Accessibility note:** Strong | accessibility foundations and alt text
- **Content note:** Writing and labels in guidance
- **Internationalization note:** Global writing guidance
- **Localization / RTL note:** Limited | not core Material 3 section
- **Validation note:** Error states in text fields and dialogs
- **State model note:** Hover, focus, pressed, disabled explicit
- **Privacy / trust note:** Security and permission patterns adjacent

## Do / Don't
### Do
- Do use tonal hierarchy to distinguish importance levels.
- Do use chips for lightweight filtering and selection metadata.
- Do keep navigation patterns responsive to screen size.
- Do express brand through color roles and illustration accents, not through arbitrary chrome.
- Do use surface containers to chunk complex screens into readable groups.

### Don't
- Do not use glassmorphism, translucent blur-heavy panels, or frosted cards.
- Do not flatten all emphasis into a single filled-button style.
- Do not over-outline every container when tonal surfaces are sufficient.
- Do not use consumer-social styling such as oversized avatars and playful gradients by default.
- Do not invent custom control shapes that fight Material components.

## Dashboard Mock Guardrails
- Make adaptive shell behavior explicit: use top app bars, navigation rails, drawers, and supporting panes based on width and complexity.
- Use semantic shape scale rather than repeating one large radius across every component.
- Lean on tonal containers and role-driven color emphasis instead of neutral enterprise panels.
- Do not default to a fixed desktop sidebar when generating Material dashboard screens.
- Vary container shapes and corner sizes by component role instead of applying one universal rounded treatment.
- Let one higher-emphasis tonal container lead the page before secondary metric cards; avoid making every summary tile equal in weight.

## Screen Generation Heuristics
- **Default page structure:** Use a top app bar with one primary content column. Add navigation rail, drawer, or a supporting pane as complexity increases.
- **Default density:** Use medium density by default. Tighten spacing only for data-heavy enterprise screens.
- **Default navigation model:** Use app bar plus tabs, bottom nav, rail, or drawer depending on viewport size and destination count.
- **Preferred form composition:** Use stacked labeled fields with helper text, clear validation, and one dominant submit action.
- **Preferred feedback pattern:** Use snackbars for transient updates, inline errors for forms, and dialogs only for blocking decisions.
- **Preferred data-display pattern:** Use cards, lists, and data tables with clear row hierarchy and restrained inline actions.
- **Prompt bias:** Use prompts such as 'Material 3 dashboard', 'tonal surfaces', 'adaptive navigation rail', and 'filled / outlined / text button hierarchy'.
- **Component naming consistency:** High | mainstream names with variants
- **Layout rule explicitness:** High | adaptive layout rules are explicit
- **Theme describability:** High | dynamic color roles convert well from md
- **Prompt-to-UI suitability:** High | components + tokens + layout map well

## Official Sources
- https://m3.material.io/
- https://m3.material.io/styles/color/roles
- https://m3.material.io/styles/typography/overview
- https://m3.material.io/foundations/layout/understanding-layout/overview
- https://m3.material.io/components
