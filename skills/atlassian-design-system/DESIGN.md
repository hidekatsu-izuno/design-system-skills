# Atlassian Design System DESIGN.md

## Overview
Use this specification for collaboration-heavy SaaS and work-management UI. Favor dense but readable layouts, semantic tokens, strong inline feedback, and patterns that support issues, projects, and operational workflows.

- **Provider:** Atlassian
- **Primary reference:** https://atlassian.design/
- **Primary product focus:** Atlassian cloud products
- **Platforms:** Web: Yes | cloud web apps | iOS: N/A | not a native iOS system | Android: N/A | web-first | Desktop: Yes | desktop web apps
- **Status:** Active | core Atlassian system
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Optimize for collaborative work and high-information screens.
- Use semantic tokens and predictable spacing before decorative styling.
- Make hierarchy readable in dense layouts.
- Keep patterns operational, practical, and action-oriented.
- Prefer inline feedback over unnecessary interruption.

### Content & Accessibility
- Use direct action labels and short explanatory helper text.
- Maintain strong focus and selected states in dense interfaces.
- Use inline validation and inline messaging where possible.
- Keep icon-only controls paired with accessible names.
- Use status lozenges, flags, and badges consistently.

- **Accessibility note:** Strong | dedicated accessibility content
- **Content note:** Dedicated content design guidance
- **Internationalization note:** International product patterns implied
- **Localization / RTL note:** Limited | not emphasized in top-level docs
- **Validation note:** Flags, inline messages, field errors
- **State model note:** Comprehensive interaction states via tokens
- **Privacy / trust note:** Enterprise trust and permissions implied

### Official Sources
- https://atlassian.design/
- https://atlassian.design/foundations/color-new
- https://atlassian.design/foundations/typography
- https://atlassian.design/foundations/layout
- https://atlassian.design/components

## Colors
Representative Atlassian palette for generation based on current public guidance and token usage. Use semantic tokens in implementation; these values are representative.

- **Blue `#0C66E4`:** Primary action, active state, and key navigation emphasis.
- **Blue Subtle `#E9F2FF`:** Selected backgrounds and supportive highlights.
- **Text `#172B4D`:** Primary body and heading text.
- **Subtle Text `#44546F`:** Secondary metadata and supporting labels.
- **Surface `#FFFFFF`:** Base canvas and card surface.
- **Neutral Subtle `#F7F8F9`:** Panels, low-emphasis containers, and row hover.
- **Danger `#CA3521`:** Destructive and error emphasis.
- **Success `#1F845A`:** Success states and positive completion.

- **Dark mode guidance:** Strong | design tokens support themes
- **Theming guidance:** High | tokens and theming infrastructure
- **Semantic token guidance:** Strong | design tokens core foundation

## Typography
- Use Atlassian Sans when available or a close neutral product sans stack.
- Keep hierarchy practical and product-oriented rather than editorial.
- Use concise headings and lightweight metadata styles.
- Favor strong alignment and rhythm over dramatic size contrast.
- Use semibold sparingly for anchors such as page titles, section titles, and primary actions.

- **Official typography note:** Typography tokens and guidance
- **Iconography:** Atlassian icons
- **Motion direction:** Motion guidance exists

## Elevation
- Use a tight but consistent spacing system suited to enterprise collaboration tools.
- Use moderate radius values and avoid overly soft consumer card styling.
- Use shadows minimally; rely on background value shifts and borders more than depth theatrics.
- Keep rows, tables, and side panels compact but readable.

- **Spacing system note:** Spacing tokens
- **Radius / shape note:** Border radius tokens
- **Elevation / shadow note:** Elevation via tokens where needed

## Components
### Navigation Rules
- Use left navigation and product-level top structure for app shells.
- Use tabs for content subviews inside a workspace or object page.
- Use breadcrumbs when users traverse deep project or object hierarchies.
- Keep navigation labels literal and task-oriented.

- **Official navigation note:** Side navigation and in-app nav patterns
- **Pattern note:** Side nav, tabs, menus, breadcrumbs

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button component
- **Preferred style:** Prefer a practical primary button with quiet secondary and link-style low-emphasis actions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Textfield
- **Preferred style:** Use compact text fields and text areas with direct labels and inline messaging.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Select and popup select
- **Preferred style:** Use selects, popup selects, and autocomplete for operational filtering and assignment workflows.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use compact choice controls that remain legible in dense forms and filter panels.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use compact choice controls that remain legible in dense forms and filter panels.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Toggle
- **Preferred style:** Use compact choice controls that remain legible in dense forms and filter panels.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** Date and time fields adjacent
- **Preferred style:** Use date and time fields that fit object-editing and planning workflows.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Search field
- **Preferred style:** Use search fields that can support product-wide find, filtering, and command-like discovery.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Dropdown menu
- **Preferred style:** Use dropdown and overflow menus with clear grouping and low visual ornamentation.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs as practical sibling-view switches inside dense product areas.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs to support object and workspace hierarchy, not as decorative navigation.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Top navigation / page header
- **Preferred style:** Use a functional page header with title, metadata, and immediate actions.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Side navigation
- **Preferred style:** Use side navigation as a core app-shell pattern for larger products.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards and panels sparingly to group operational content without making the UI feel soft.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** DynamicTable
- **Preferred style:** Use dense, metadata-rich tables with clear statuses, row actions, and sortable structure.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

### List
- **Official naming / aliases:** List
- **Preferred style:** Use structured lists and object rows for issue, task, or item workflows.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge / lozenge
- **Preferred style:** Use lozenges, badges, and status marks to make workflow state instantly scannable.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips for clarification in dense action areas, not as a substitute for labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Modal dialog
- **Preferred style:** Use dialogs and drawers for focused edits or confirmations that should not overload the page.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Flag
- **Preferred style:** Use flags or equivalent transient messaging for operation feedback.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Spinner and progress indicator
- **Preferred style:** Use spinners and progress indicators as lightweight workflow feedback, not visual centerpiece.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination where table chunking improves orientation and performance.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

### Layout Rules
- Use persistent side navigation or workspace shells for complex products.
- Allow dense content regions with clear section headers and inline metadata.
- Use page-level banners, inline messages, and panel layouts to support workflows.
- Keep action placement predictable across issue, task, and project surfaces.
- Prefer operational clarity over decorative asymmetry.

- **Official layout note:** Page layout patterns and spacing tokens
- **Responsive behavior:** Responsive web app guidance
- **App structure:** App layouts for Jira/Confluence-like tools
- **Data display guidance:** Data display patterns, charts not central

### Screen Generation Heuristics
- **Default page structure:** Use a workspace shell with side navigation, a practical page header, and dense operational content blocks.
- **Default density:** Use medium-to-dense layout density.
- **Default navigation model:** Use side navigation, tabs, breadcrumbs, and in-context actions.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use structured sections, inline help, and strong field-level validation.
- **Preferred feedback pattern:** Use inline messages, flags, banners, and dialog confirmation for destructive changes.
- **Preferred data-display pattern:** Use tables, issue lists, cards, side panels, and metadata-rich rows.
- **Prompt bias:** Use prompts such as 'Atlassian-style admin screen', 'collaboration workspace', 'dense issue table', and 'semantic product tokens'.
- **Component naming consistency:** High | standard product naming
- **Layout rule explicitness:** High | page layout patterns are explicit
- **Theme describability:** High | brand and semantic themes clear
- **Prompt-to-UI suitability:** High | good for SaaS work-management prompts

## Do's and Don'ts
### Do
- Do build for dense collaboration workflows and long-lived work objects.
- Do keep tables, lists, and forms highly structured.
- Do use semantic tokens and subtle surfaces consistently.
- Do communicate status with strong inline messaging and lozenges.
- Do use layout patterns that feel like serious product tools, not marketing pages.

### Don't
- Do not use soft consumer-style cards, oversized whitespace, or lifestyle-brand hero layouts.
- Do not over-round controls or containers.
- Do not hide critical actions behind ambiguous overflow unless the workflow warrants it.
- Do not use novelty gradients or expressive illustration as the main hierarchy tool.
- Do not collapse dense workflows into overly sparse mobile-style compositions on desktop.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Atlassian patterns offer a clear stateful control.
