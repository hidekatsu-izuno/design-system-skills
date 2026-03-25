# Ant Design DESIGN.md

## Overview
Use this specification for enterprise web applications, dashboards, and internal tools. Favor information density, broad component coverage, predictable grids, and direct administrative workflows.

- **Provider:** Ant Group
- **Primary reference:** https://ant.design/
- **Primary product focus:** Enterprise web applications
- **Platforms:** Web: Yes | primary target | iOS: Limited | Ant Design Mobile exists | Android: Limited | Ant Design Mobile exists | Desktop: Yes | enterprise desktop web
- **Status:** Active | v5 current
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Design for efficient task completion in data-heavy environments.
- Use strong grid alignment and a clear page shell.
- Let components solve operational tasks directly.
- Keep theming systematic and algorithmic rather than handcrafted per screen.
- Support broad form, table, and filtering workflows.

### Content & Accessibility
- Use direct labels, placeholders only as hints, and strong field-level validation.
- Preserve clear hover, active, selected, disabled, and error states.
- Support RTL and localization-aware layout decisions.
- Use messages, notifications, and status color consistently.
- Keep icon usage secondary to readable labels.

- **Accessibility note:** Strong | WCAG-oriented component guidance
- **Content note:** Writing for enterprise flows
- **Internationalization note:** Internationalization support in components
- **Localization / RTL note:** Strong | direction and locale support in components
- **Validation note:** Status and feedback patterns strong
- **State model note:** Common control states standardized
- **Privacy / trust note:** Enterprise admin trust patterns

### Official Sources
- https://ant.design/
- https://ant.design/docs/spec/introduce
- https://ant.design/docs/spec/colors
- https://ant.design/docs/spec/font
- https://ant.design/components/overview

## Colors
Representative Ant Design palette for generation based on v5 semantics and common product usage. Use official token algorithms in implementation; these values are representative.

- **Primary `#1677FF`:** Primary action and active interactive emphasis.
- **Success `#52C41A`:** Success and positive status.
- **Warning `#FAAD14`:** Caution and intermediate attention.
- **Error `#FF4D4F`:** Errors and destructive emphasis.
- **Text `#1F1F1F`:** Primary text on light surfaces.
- **Background `#FFFFFF`:** Primary application surface.
- **Container `#F5F5F5`:** Low-emphasis panels and section surfaces.
- **Border `#D9D9D9`:** Input, table, and container borders.

- **Dark mode guidance:** Strong | algorithmic dark themes
- **Theming guidance:** High | seed tokens and algorithms
- **Semantic token guidance:** Strong | seed, map, alias tokens

## Typography
- Use a neutral enterprise sans stack, typically with system sans defaults.
- Keep hierarchy pragmatic and compact.
- Use page titles, section titles, body text, and compact control text without excessive variation.
- Favor dense tables and forms with readable but not loose line height.
- Use medium emphasis for buttons, labels, and data headers.

- **Official typography note:** Typography scale for enterprise UI
- **Iconography:** Ant Design Icons ecosystem
- **Motion direction:** Motion principles less central

## Elevation
- Use a clear grid system and regular panel spacing.
- Use moderate radii and avoid overly soft consumer rounded surfaces.
- Use shadows when surfacing overlays, drawers, and cards, but keep them utilitarian.
- Keep field spacing compact and consistent across form sections.

- **Spacing system note:** Spacing grid and spacing tokens
- **Radius / shape note:** Radius tokens and algorithm
- **Elevation / shadow note:** Shadows for layered surfaces

## Components
### Navigation Rules
- Use top navigation, side navigation, or a hybrid application shell for enterprise apps.
- Use tabs and steps for local workflow segmentation.
- Use breadcrumbs in deep admin structures and nested settings areas.
- Keep nav labels literal and easy to scan.

- **Official navigation note:** Navigation specs for enterprise apps
- **Pattern note:** Top nav, side nav, steps

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button with variants
- **Preferred style:** Prefer clear primary, default, dashed, text, and link hierarchies suited to enterprise tasks.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Input
- **Preferred style:** Use compact but readable inputs with explicit labels and strong status borders.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Select, Cascader, AutoComplete
- **Preferred style:** Use selects, cascaders, autocompletes, and searchable dropdowns to handle complex choice sets.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use straightforward choice controls that integrate cleanly into filter bars and forms.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use straightforward choice controls that integrate cleanly into filter bars and forms.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use straightforward choice controls that integrate cleanly into filter bars and forms.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** DatePicker, TimePicker, Calendar
- **Preferred style:** Use date and time pickers that fit dense filter and scheduling workflows.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Input.Search
- **Preferred style:** Use search inputs as part of table filters, toolbars, and management headers.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menu, Dropdown
- **Preferred style:** Use menus and dropdowns with practical grouping and little visual flourish.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs for local task segmentation and steps for process-based flows.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs to anchor the user in deep administrative IA.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Layout.Header / page header
- **Preferred style:** Use practical page headers with title, metadata, actions, and optional breadcrumb context.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Drawer and sider
- **Preferred style:** Use sider navigation for persistent application structure on desktop.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards to modularize dashboards and related information groups.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use data tables as a first-class pattern with filters, row actions, and status tags.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists when the data is lighter-weight than a table or needs more flexible row content.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and tags for state, count, and categorization.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips to clarify dense controls or truncated labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Modal
- **Preferred style:** Use modals, drawers, and popconfirms for interruptive actions and secondary tasks.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Message / notification
- **Preferred style:** Use message and notification patterns for transient or global feedback.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Progress, Spin, Skeleton
- **Preferred style:** Use progress bars, spinners, and skeletons to keep busy states explicit in dense screens.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination heavily in tables and long administrative collections.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

### Layout Rules
- Use a dashboard or management shell with header, sider, and content regions when appropriate.
- Support dense table, filter, and form areas without collapsing hierarchy.
- Use cards and sections to organize related modules in larger screens.
- Keep admin workflows explicit through action bars, filters, and summaries.
- Prefer operational symmetry over expressive composition.

- **Official layout note:** Grid and layout spec
- **Responsive behavior:** Responsive grid and mobile variants
- **App structure:** Dashboard and management app structure
- **Data display guidance:** Ant Design Charts ecosystem

### Screen Generation Heuristics
- **Default page structure:** Use a management shell with optional sider, page header, filter region, and structured content blocks.
- **Default density:** Use medium-to-dense density by default.
- **Default navigation model:** Use top nav, sider, tabs, steps, and breadcrumbs depending on workflow depth.
- **Preferred form composition:** Use labeled fields, sectioned forms, inline validation, and clear submit/cancel actions.
- **Preferred feedback pattern:** Use message, notification, result, and modal patterns according to urgency.
- **Preferred data-display pattern:** Use tables, cards, lists, statistics, and charts with explicit filters and sorting.
- **Prompt bias:** Use prompts such as 'Ant Design admin dashboard', 'sider layout', 'dense enterprise table', and 'algorithmic token theme'.
- **Component naming consistency:** High | common web component names
- **Layout rule explicitness:** Medium | layout principles are broad
- **Theme describability:** High | algorithmic themes are easy to describe
- **Prompt-to-UI suitability:** High | rich web components for admin UIs

## Do's and Don'ts
### Do
- Do lean into the system's broad component coverage for enterprise tasks.
- Do use tables, filters, forms, and cards as primary building blocks.
- Do keep layouts structured and operational.
- Do use algorithmic theming rather than ad hoc color decisions.
- Do make workflow state obvious through status, tags, and notifications.

### Don't
- Do not style Ant screens like soft consumer landing pages.
- Do not overuse illustrations, gradients, or playful decorative surfaces.
- Do not create huge whitespace gaps that weaken dashboard scanability.
- Do not replace straightforward controls with overly bespoke alternatives.
- Do not bury key filters and table actions behind excessive nesting.
