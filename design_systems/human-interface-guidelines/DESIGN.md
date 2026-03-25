# Human Interface Guidelines DESIGN.md

## Overview
Use this specification for interfaces that should feel native to Apple platforms. Favor clarity, restraint, familiar controls, and layouts that defer to content rather than brand-heavy UI treatment.

- **Provider:** Apple
- **Primary reference:** https://developer.apple.com/design/human-interface-guidelines/
- **Primary product focus:** Apple platform apps
- **Platforms:** Web: Yes | Safari/web adaptation | iOS: Yes | iPhone and iPad native | Android: N/A | Apple-only guidance | Desktop: Yes | macOS specific
- **Status:** Active | continuously updated by Apple
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Prioritize clarity in labels, icon use, and overall navigation structure.
- Let content lead; interface chrome should support, not dominate.
- Use native metaphors and control behavior whenever possible.
- Adjust layout, spacing, and control treatment by platform family.
- Keep motion and depth subtle and platform-consistent.

## Color System
Representative Apple system palette for generation. Use semantic system colors in implementation; these hex values are representative.

- **System Blue `#007AFF`:** Primary action color and interactive emphasis.
- **System Green `#34C759`:** Success and positive confirmation.
- **System Orange `#FF9500`:** Caution and intermediate attention.
- **System Red `#FF3B30`:** Destructive actions and errors.
- **Background `#FFFFFF`:** Primary light background.
- **Secondary Background `#F2F2F7`:** Grouped backgrounds and panels.
- **Label `#1C1C1E`:** Primary text color on light surfaces.
- **Separator `#C6C6C8`:** Dividers and low-emphasis strokes.

- **Dark mode guidance:** Strong | system dark mode guidance
- **Theming guidance:** Medium | platform appearance customization
- **Semantic token guidance:** Implicit via platform APIs and metrics

## Typography
- Use San Francisco as the primary typeface.
- Use Apple-style text roles rather than inventing a custom display system.
- Favor strong readability, generous line height, and restrained weight changes.
- Use platform-standard text styles for titles, body content, captions, and controls.
- Keep uppercase labels rare and functional.

- **Official typography note:** SF typography and text styles
- **Iconography:** SF Symbols and app icons
- **Motion direction:** Animation guidance by platform

## Spacing, Radius, Elevation
- Use platform-native spacing and alignment; prioritize optical balance over a rigid visible grid.
- Use rounded rectangles and materials that align with the target Apple platform.
- Use blur, translucency, and depth only in platform-native ways.
- Keep shadows subtle; depth should feel systemic rather than decorative.

- **Spacing system note:** System spacing through platform metrics
- **Radius / shape note:** Rounded rect conventions by platform
- **Elevation / shadow note:** Depth through materials and blur

## Layout Rules
- Use platform-appropriate containers such as split views, sidebars, tab bars, toolbars, and sheets.
- Respect safe areas, title regions, and expected control placement for each platform.
- Use grouped sections and inset panels where native patterns call for them.
- Avoid over-dense enterprise layouts unless the app category clearly supports them.
- When generating for macOS, allow more persistent side navigation and toolbar actions than on iPhone.

- **Official layout note:** Platform layout and safe-area guidance
- **Responsive behavior:** Canonical adaptations by device
- **App structure:** Tab bars, split views, sidebars
- **Data display guidance:** Charts available in platform frameworks

## Navigation Rules
- Use tab bars for a small number of top-level destinations on iPhone.
- Use sidebars and split views for iPadOS and macOS information architecture.
- Use back navigation and hierarchical drill-in patterns when content is naturally nested.
- Avoid mixing too many navigation metaphors in one screen.

- **Official navigation note:** Tab bars, sidebars, split views
- **Pattern note:** Sidebar, tab bar, navigation split

## Component Rules
### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** System button styles
- **Preferred style:** Prefer native filled or bordered button treatments and segmented controls that match Apple platform conventions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Text fields follow platform controls
- **Preferred style:** Use clean native text fields with visible labels when needed and subtle container styling.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Menus, pickers, pop-up buttons
- **Preferred style:** Use native menus, pop-up buttons, and pickers rather than heavily customized dropdowns.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use platform-native checkboxes, radio-like selections, and switches with familiar spacing and behavior.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio buttons
- **Preferred style:** Use platform-native checkboxes, radio-like selections, and switches with familiar spacing and behavior.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Toggle controls
- **Preferred style:** Use platform-native checkboxes, radio-like selections, and switches with familiar spacing and behavior.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** DatePicker and system pickers
- **Preferred style:** Use native date pickers, wheels, calendars, or compact pickers according to platform context.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Search field
- **Preferred style:** Use the native search field pattern integrated into the relevant container.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menus and pop-up menus
- **Preferred style:** Use menus and context menus that feel native and lightweight.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tab views
- **Preferred style:** Use tab bars or segmented controls depending on whether the switch is global or local.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Path controls where appropriate
- **Preferred style:** Use path-like navigation only where the platform supports it; otherwise prefer sidebars, back navigation, or split views.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Navigation bars and toolbars
- **Preferred style:** Use restrained navigation bars, toolbars, or title areas with minimal visual noise.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Sidebar and split view
- **Preferred style:** Use sidebars and split views instead of generic web-style drawers whenever possible.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Cards and collections
- **Preferred style:** Use grouped panels or inset sections before introducing generic cards.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Table / outline views via platform
- **Preferred style:** Use clean tables or outline views with strong text alignment and little decoration.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List and collection views
- **Preferred style:** Use lists and collections with platform-native spacing and separators.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge-like labels
- **Preferred style:** Use badges and status labels sparingly and semantically.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltips
- **Preferred style:** Use tooltips as supplemental help, especially on desktop.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Sheets and alerts
- **Preferred style:** Use alerts, sheets, and popovers with native structure and concise decisions.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Transient alerts
- **Preferred style:** Use transient feedback sparingly and in platform-native ways.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Progress indicators
- **Preferred style:** Use native progress bars, spinners, and activity indicators.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination where desktop fits
- **Preferred style:** Use pagination rarely; prefer content grouping, search, or hierarchical drill-in.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.


## Content & Accessibility
- Use concise, human labels and avoid jargon-heavy control text.
- Preserve dynamic type scalability and comfortable tap targets.
- Use semantic colors, not raw brand colors, for status whenever possible.
- Ensure controls read as native and predictable to VoiceOver users.
- Keep destructive actions explicit and visually separated from safe actions.

- **Accessibility note:** Strong | built into platform guidance
- **Content note:** Writing guidance included
- **Internationalization note:** Localization guidance across locales
- **Localization / RTL note:** Strong | locale-aware Apple controls
- **Validation note:** System alerts and validation via native controls
- **State model note:** Standard control states via platform behaviors
- **Privacy / trust note:** Privacy is a platform concern

## Do / Don't
### Do
- Do prefer native controls and familiar Apple patterns.
- Do keep chrome quiet and let content carry the screen.
- Do use system colors and typography roles before introducing custom branding.
- Do adapt layouts by platform family rather than forcing one universal shell.
- Do use SF Symbols for interface iconography when possible.

### Don't
- Do not add non-native ornamentation, loud shadows, or novelty gradients.
- Do not force Material- or enterprise-style app shells onto Apple screens.
- Do not crowd the screen with multiple simultaneous emphasis patterns.
- Do not replace native segmented controls, sheets, or menus with bespoke alternatives without reason.
- Do not use over-branded buttons or aggressively custom form fields.

## Screen Generation Heuristics
- **Default page structure:** Use content-first structure with native headers, grouped sections, and platform-appropriate sidebars or tab bars.
- **Default density:** Use comfortable density. Let breathing room and legibility outweigh data compression.
- **Default navigation model:** Use tab bars, sidebars, toolbars, split views, and sheets according to Apple platform conventions.
- **Preferred form composition:** Use clearly grouped fields, native pickers, and conservative validation messaging.
- **Preferred feedback pattern:** Use alerts, banners, inline validation, and native transient feedback sparingly.
- **Preferred data-display pattern:** Use lists, collections, and tables that prioritize readability over operational density.
- **Prompt bias:** Use prompts such as 'native iOS settings screen', 'macOS sidebar detail view', 'SF Symbols', and 'content-first Apple UI'.
- **Component naming consistency:** Medium | native names differ by platform
- **Layout rule explicitness:** High | device-specific rules are explicit
- **Theme describability:** Medium | appearance follows system settings
- **Prompt-to-UI suitability:** Medium | best when prompt targets Apple platforms

## Official Sources
- https://developer.apple.com/design/human-interface-guidelines/
- https://developer.apple.com/design/human-interface-guidelines/color
- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/layout
- https://developer.apple.com/design/human-interface-guidelines/controls
