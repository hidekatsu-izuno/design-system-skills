# Primer Product UI DESIGN.md

## Overview
Use this specification for GitHub-like product interfaces, developer tools, settings surfaces, and workflow-oriented applications. Favor utility, clarity, and quiet but strong structure.

- **Provider:** GitHub
- **Primary reference:** https://primer.style/product
- **Primary product focus:** GitHub product interfaces
- **Platforms:** Web: Yes | GitHub web app UI | iOS: Limited | not primary target | Android: N/A | not Android-native guidance | Desktop: Yes | desktop-heavy workflows
- **Status:** Active | GitHub maintained
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Let product utility and content hierarchy drive the screen.
- Use primitives and semantic variables to keep the interface systematic.
- Keep styling understated and developer-tool practical.
- Support both dense data and comfortable readability.
- Use component naming and layout patterns that feel familiar to serious software products.

## Color System
Representative Primer palette for generation based on current product UI primitives. Use variables in implementation; these hex values are representative.

- **Accent `#0969DA`:** Primary interactive emphasis and link/action color.
- **Success `#1F883D`:** Success and positive state.
- **Attention `#9A6700`:** Warning and needs-attention emphasis.
- **Danger `#CF222E`:** Error and destructive emphasis.
- **Canvas Default `#FFFFFF`:** Primary page background.
- **Canvas Subtle `#F6F8FA`:** Muted panels and section backgrounds.
- **Foreground Default `#1F2328`:** Primary text and icon color.
- **Border Default `#D0D7DE`:** Borders, table dividers, and field boundaries.

- **Dark mode guidance:** Strong | color modes through primitives
- **Theming guidance:** High | CSS variables and theme support
- **Semantic token guidance:** Strong | primitives for color, space, type

## Typography
- Use a neutral system sans stack appropriate for developer products.
- Keep headings functional and direct.
- Use monospace only for code, data snippets, and strongly technical labels.
- Preserve readable density in settings pages, forms, and table-like lists.
- Use weight changes modestly and let layout provide most hierarchy.

- **Official typography note:** Text styles and Primer primitives
- **Iconography:** Octicons
- **Motion direction:** Animation utilities minimal

## Spacing, Radius, Elevation
- Use a disciplined spacing scale with practical compactness.
- Use small-to-moderate radii and restrained shadows.
- Prefer borders, muted surfaces, and layout grouping over rich card effects.
- Keep row height, field spacing, and action spacing highly consistent.

- **Spacing system note:** Space primitives
- **Radius / shape note:** Border radius primitives
- **Elevation / shadow note:** Box-shadow tokens limited but present

## Layout Rules
- Use page layouts with clear header, side navigation, and content hierarchy when the product area is complex.
- Support split layouts, settings pages, and repository-style information density.
- Use sections, subheaders, and muted containers to organize complex screens.
- Keep actions near the data or task they affect.
- Favor compact clarity over ornamental whitespace.

- **Official layout note:** Layout primitives and page patterns
- **Responsive behavior:** Responsive layouts for GitHub pages
- **App structure:** Page layouts for product workflows
- **Data display guidance:** Data-rich GitHub tables more than charts

## Navigation Rules
- Use side nav, underline nav, and page-local patterns for clear product orientation.
- Use breadcrumbs only when nested hierarchy is genuinely helpful.
- Use tabs for sibling views and segmented content regions.
- Keep top-level navigation restrained and utility-first.

- **Official navigation note:** NavList, UnderlineNav, side nav patterns
- **Pattern note:** NavList, UnderlineNav, breadcrumbs

## Component Rules
### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer restrained button hierarchy with clear primary emphasis and quiet secondary actions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** TextInput
- **Preferred style:** Use practical text inputs with visible labels, concise help, and strong keyboard/focus support.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Select, SelectPanel, autocomplete-like patterns
- **Preferred style:** Use selects and select panels that fit settings and workflow contexts rather than decorative dropdowns.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use straightforward choice controls with explicit labels and compact spacing.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio / RadioGroup
- **Preferred style:** Use straightforward choice controls with explicit labels and compact spacing.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** ToggleSwitch
- **Preferred style:** Use straightforward choice controls with explicit labels and compact spacing.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** DatePicker relative time patterns
- **Preferred style:** Use date-related inputs when needed, styled to match a practical product surface.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** TextInput and command/search patterns
- **Preferred style:** Use search as a strong utility tool in headers, filters, and content lists.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** ActionMenu and menu patterns
- **Preferred style:** Use action menus and compact menus for contextual operations.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** UnderlineNav / tabs
- **Preferred style:** Use underline-style tabs or related navigation for sibling views.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs conservatively in nested product structures.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** PageHeader / header primitives
- **Preferred style:** Use practical page headers with clear title, metadata, and nearby actions.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** NavList / side nav
- **Preferred style:** Use side nav for durable product orientation in larger tools and settings areas.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards and muted panels to organize content without making the interface feel soft.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** DataTable / table patterns
- **Preferred style:** Use data tables and structured rows where developers or operators need quick scanning.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** ActionList / list
- **Preferred style:** Use action lists and metadata-rich rows for flexible workflow presentation.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Label / Counter
- **Preferred style:** Use labels, counters, and tokens to communicate state and categorization clearly.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips to support dense interfaces, not to compensate for vague labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Dialog
- **Preferred style:** Use dialogs and overlays for focused decisions and secondary tasks.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Flash / toast-like feedback
- **Preferred style:** Use flash-like transient messaging that stays practical and unobtrusive.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Spinner, skeleton, progress
- **Preferred style:** Use spinners, skeletons, and progress bars in a quiet utility style.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination when large result sets need explicit chunking and orientation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.


## Content & Accessibility
- Use clear technical language and avoid ambiguous marketing copy in product screens.
- Maintain strong focus treatment and keyboard navigability.
- Use icons to support labels and status, not replace readable text.
- Keep error and help copy concise and task-oriented.
- Use code or monospace treatment only where semantics justify it.

- **Accessibility note:** Strong | component-level accessibility docs
- **Content note:** Copy and UX writing within patterns
- **Internationalization note:** Global GitHub product support
- **Localization / RTL note:** Limited | GitHub product focus
- **Validation note:** FormControl validation and flash messages
- **State model note:** Default/hover/disabled/focus documented
- **Privacy / trust note:** GitHub trust and security context

## Do / Don't
### Do
- Do make the UI feel practical, reliable, and developer-friendly.
- Do use muted surfaces, borders, and strong alignment to manage complexity.
- Do use components and primitives consistently across settings and workflows.
- Do keep navigation and metadata explicit.
- Do let content and action structure drive the page.

### Don't
- Do not turn Primer screens into glossy marketing pages or soft consumer dashboards.
- Do not overuse large shadows, loud gradients, or decorative illustrations.
- Do not hide important settings and actions behind ambiguous icon-only patterns.
- Do not over-round containers or use whimsical control styling.
- Do not replace practical lists and tables with over-carded layouts without reason.

## Dashboard Mock Guardrails
- Favor calm PageLayout-style structure, clear page headers, and product-oriented navigation over bespoke dashboard framing.
- Keep radii, shadows, and surface treatment restrained, relying on muted containers and whitespace discipline.
- Prefer page header, nav list, and underline-nav style patterns before inventing custom chrome.
- Use semantic landmarks and focused hierarchy so the output feels like a GitHub product surface rather than a themed admin panel.
- Prefer flat borders and section grouping over repeated tile-like dashboard cards.
- Keep side navigation text-forward and quiet; avoid decorative icons, counters, or branded shell weight unless the workflow clearly needs them.


## Responsive Behavior
- **Mobile:** Collapse dense navigation into an ActionMenu-like trigger or overflow menu and keep the page header calm and text-forward.
- **Tablet:** Preserve PageLayout structure but allow nav and context panes to collapse before the main content does.
- **Desktop:** Restore side navigation, underline nav, and context panes as needed for product orientation.
- **Navigation rule:** Mobile navigation should feel like a GitHub product overflow or action menu, not a themed full-screen drawer.
- **Table rule:** Maintain practical tables and lists with scroll or compact controls rather than converting everything into tiles.
## Screen Generation Heuristics
- **Default page structure:** Use a utility-first product page with a clear title, optional side navigation, explicit section grouping, and practical action placement.
- **Default density:** Use medium density with compact tendencies for settings and tool screens.
- **Default navigation model:** Use side navigation, underline nav, tabs, and page headers for strong orientation.
- **Preferred form composition:** Use clearly labeled fields, concise help text, and practical action groups.
- **Preferred feedback pattern:** Use banners, flash messages, inline validation, and dialogs only when blocking is justified.
- **Preferred data-display pattern:** Use lists, tables, cards, and timelines in a calm, utility-first way.
- **Prompt bias:** Use prompts such as 'GitHub product settings page', 'Primer side nav', 'muted borders', and 'developer tool UI'.
- **Component naming consistency:** High | standard product UI names
- **Layout rule explicitness:** High | layout primitives and page patterns explicit
- **Theme describability:** High | color modes and primitives are clear
- **Prompt-to-UI suitability:** High | excellent for repository/productivity screens

## Official Sources
- https://primer.style/product
- https://primer.style/product/primitives/color
- https://primer.style/product/primitives/typography
- https://primer.style/product/components/page-layout
- https://primer.style/product/components
