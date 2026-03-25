# Digital Agency Design System (Beta) DESIGN.md

## Overview
Use this specification for Japanese public-service websites, form-heavy government flows, and trust-critical transactional screens. Favor plain language, conservative styling, explicit structure, and accessibility-first decisions.

- **Provider:** The digital agency
- **Primary reference:** https://design.digital.go.jp/
- **Primary product focus:** Japanese public service websites
- **Platforms:** Web: Yes | government websites | iOS: N/A | web-first guidance | Android: N/A | web-first guidance | Desktop: Yes | administrative web systems
- **Status:** Beta | public government rollout
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Design for trust, clarity, and public comprehension.
- Make accessibility and legal/service readability the default.
- Use conservative visual treatment and explicit interaction patterns.
- Prefer standardization over product-specific flourish.
- Keep forms and service flows obvious and low-ambiguity.

## Color System
Representative Digital Agency palette for generation based on public component examples and government web guidance. Use official values when implementing; the values below are representative for generation.

- **Primary Blue `#005AC2`:** Primary action, links, and core interactive emphasis.
- **Blue Hover `#00408A`:** Hover and active emphasis for primary controls.
- **Light Blue `#E8F1FF`:** Low-emphasis hover and outlined-button background.
- **Text `#1A1A1A`:** Primary readable text color.
- **Background `#FFFFFF`:** Primary document and service surface.
- **Subtle Surface `#F5F5F5`:** Section grouping and low-emphasis backgrounds.
- **Border `#C8C8C8`:** Field and section boundaries.
- **Danger `#B00020`:** Error and destructive emphasis.

- **Dark mode guidance:** Limited | public docs focus on baseline web
- **Theming guidance:** Low | standardization over customization
- **Semantic token guidance:** Medium | design foundations standardized

## Typography
- Use highly readable Japanese-capable sans-serif typography.
- Keep hierarchy simple, direct, and service-oriented.
- Avoid decorative display styling and compressed text treatment.
- Favor readability in long guidance text, labels, and form instructions.
- Use emphasis sparingly and only where comprehension improves.

- **Official typography note:** Readable Japanese web typography guidance
- **Iconography:** Icons in public components
- **Motion direction:** Motion restrained for service clarity

## Spacing, Radius, Elevation
- Use consistent spacing that supports long-form reading and form completion.
- Use conservative radius values and straightforward component geometry.
- Use minimal shadow; structure should come from order, not depth effects.
- Keep forms, notices, and templates aligned and explicit.

- **Spacing system note:** Consistent spacing in templates
- **Radius / shape note:** Conservative component shapes
- **Elevation / shadow note:** Minimal shadow usage for public trust

## Layout Rules
- Use simple page templates with clear header, content flow, and service structure.
- Support long-form guidance, forms, notices, and result pages without visual complexity.
- Use sections, headings, and notices to guide the user through the task.
- Keep primary actions explicit and easy to locate.
- Prefer stable, conventional layouts over experimental composition.

- **Official layout note:** Page templates and component layout examples
- **Responsive behavior:** Responsive government web guidance
- **App structure:** Templates for public information architecture
- **Data display guidance:** Tables and summaries more central than charts

## Navigation Rules
- Use straightforward global navigation, breadcrumbs, and side navigation where service scale requires them.
- Use local navigation only when it materially improves orientation.
- Keep navigation labels plain and official rather than branded.
- Avoid deep or playful navigation experiments.

- **Official navigation note:** Header, side nav, breadcrumb in public guidance
- **Pattern note:** Global nav, side nav, breadcrumbs

## Component Rules
### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer clear filled, outlined, and text button hierarchy with conservative styling and obvious labels.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Text input
- **Preferred style:** Use explicit form fields with visible labels, helper text, and close-by validation.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Select
- **Preferred style:** Use plain, accessible selects and comboboxes with low-ambiguity labeling.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use straightforward checkboxes, radios, and switches with enough space for clear Japanese labels.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio button
- **Preferred style:** Use straightforward checkboxes, radios, and switches with enough space for clear Japanese labels.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use straightforward checkboxes, radios, and switches with enough space for clear Japanese labels.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** Date picker / calendar
- **Preferred style:** Use practical date inputs and calendars that favor comprehension over clever interaction.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Search
- **Preferred style:** Use search as a service utility, not as a central visual motif.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menu
- **Preferred style:** Use menus only when they genuinely improve navigation or action grouping; keep them plain and direct.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs sparingly and only when sibling content views are clearly understood by users.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs to maintain orientation in multi-level public-service information architecture.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Header
- **Preferred style:** Use a straightforward header with service title, utility navigation, and minimal visual flourish.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Side navigation
- **Preferred style:** Use side navigation only for larger multi-section services, keeping labels explicit and official.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards and panels conservatively for summaries or grouped content, not as decorative layout tiles.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use plain, readable tables for summaries, result sets, and reference information.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists for steps, requirements, summaries, and straightforward content grouping.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and labels only when they improve comprehension of status or category.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips sparingly; essential guidance should remain visible.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Dialog
- **Preferred style:** Use dialogs for clear confirmation or interruption points, not for routine guidance.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Notice / snackbar-equivalent
- **Preferred style:** Use toast-like transient feedback rarely; prefer visible notices and confirmation content.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Loading and progress
- **Preferred style:** Use clear loading and progress states with explicit wording when the system is working.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination only where list length requires it and keep controls extremely explicit.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

## Content & Accessibility
- Use plain language and explicit procedural wording.
- Preserve strong contrast, visible focus, and accessible target sizes.
- Use helper text, error text, and notices close to the point of action.
- Do not rely on iconography alone to communicate state or instruction.
- Keep forms predictable and cognitively light.

- **Accessibility note:** Strong | public-sector accessibility emphasized
- **Content note:** Plain Japanese and service writing implied
- **Internationalization note:** Japanese government focus
- **Localization / RTL note:** N/A | Japanese public-sector context
- **Validation note:** Error and notice components for services
- **State model note:** Usage pages describe state behavior
- **Privacy / trust note:** Strong | public trust and legal accessibility

## Do / Don't
### Do
- Do make the interface feel trustworthy, official, and easy to understand.
- Do use plain language and visible procedural guidance.
- Do use clear buttons, notices, and form structures.
- Do prioritize accessibility and predictable service flow.
- Do keep customization limited and purposeful.

### Don't
- Do not over-customize the visual language or invent product-specific flourishes.
- Do not use glassmorphism, gradient-heavy surfaces, or trendy startup styling.
- Do not turn service screens into dashboard-like card mosaics without need.
- Do not hide critical instructions inside tooltips or tertiary UI.
- Do not use playful illustrations or novelty interactions in transactional service flows.

## Screen Generation Heuristics
- **Default page structure:** Use a conventional service page or form page with strong heading hierarchy, notices, and a clear primary action path.
- **Default density:** Use medium density with generous readability for text and forms.
- **Default navigation model:** Use straightforward header navigation, breadcrumbs, side navigation, and in-page section structure when needed.
- **Preferred form composition:** Use strongly labeled fields, clear required markers, helper text, and explicit error messaging.
- **Preferred feedback pattern:** Use notices, inline errors, confirmation pages, and dialogs only for essential interruption.
- **Preferred data-display pattern:** Use simple tables, lists, summaries, and result pages with conservative styling.
- **Prompt bias:** Use prompts such as 'Japanese public service form', 'official government service page', 'plain-language transaction flow', and 'accessible conservative UI'.
- **Component naming consistency:** High | generic public-service names
- **Layout rule explicitness:** High | usage and templates are explicit
- **Theme describability:** Low | customization is intentionally constrained
- **Prompt-to-UI suitability:** High | strong for public-service transaction screens

## Official Sources
- https://design.digital.go.jp/
- https://design.digital.go.jp/dads/components/button/
- https://design.digital.go.jp/components/
- https://design.digital.go.jp/templates/
- https://design.digital.go.jp/guidelines/accessibility/
