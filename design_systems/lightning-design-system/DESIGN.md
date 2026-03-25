# Lightning Design System DESIGN.md

## Overview
Use this specification for CRM-style, record-centric business applications. Favor structured record pages, clear utility navigation, explicit statuses, and forms or tables that support object-heavy workflows.

- **Provider:** Salesforce
- **Primary reference:** https://v1.lightningdesignsystem.com/
- **Primary product focus:** Salesforce application UI
- **Platforms:** Web: Yes | responsive enterprise web | iOS: Limited | Salesforce mobile patterns separate | Android: Limited | mobile web and Salesforce apps | Desktop: Yes | desktop CRM workflows
- **Status:** Active | SLDS 1 public docs
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Design around records, lists, and business-object workflows.
- Keep page regions explicit and consistent.
- Use accessible business UI patterns rather than decorative surfaces.
- Support data-heavy tasks, filtering, and guided action flow.
- Make status and object metadata easy to scan.

## Color System
Representative Lightning palette for generation based on public SLDS guidance and Salesforce product styling. Use official tokens in implementation; these values are representative.

- **Brand `#0176D3`:** Primary interactive emphasis and brand-led action color.
- **Brand Dark `#032D60`:** Stronger shell and enterprise emphasis.
- **Success `#2E844A`:** Positive completion and healthy state.
- **Error `#BA0517`:** Error and destructive action emphasis.
- **Background `#FFFFFF`:** Primary page surface.
- **Canvas Alt `#F3F3F3`:** Section and utility background.
- **Border `#C9C9C9`:** Object, field, and table separators.
- **Text `#181818`:** Primary readable text color.

- **Dark mode guidance:** Strong | styling hooks and themes
- **Theming guidance:** High | styling hooks and design tokens
- **Semantic token guidance:** Strong | design tokens + styling hooks

## Typography
- Use Salesforce Sans or a close humanist enterprise sans stack.
- Favor practical hierarchy over expressive typography.
- Keep object labels, section headers, and data metadata crisp.
- Use compact text in forms and tables without reducing readability.
- Avoid over-styled headings and editorial display text.

- **Official typography note:** SLDS typography utilities
- **Iconography:** Utility icons in SLDS
- **Motion direction:** Motion guidance light but present

## Spacing, Radius, Elevation
- Use utility spacing and region-based composition.
- Use subtle radius values and straightforward enterprise surfaces.
- Use depth sparingly and structurally, especially for overlays and utility panels.
- Keep record pages aligned and compartmentalized.

- **Spacing system note:** Spacing utilities
- **Radius / shape note:** Border radius utilities
- **Elevation / shadow note:** Utility shadows and depth tokens

## Layout Rules
- Use record-page composition with header, highlights panel, tabs, and related lists when appropriate.
- Use utility bars, object actions, and supporting panels for dense workflows.
- Support responsive desktop-first enterprise layouts rather than mobile-social composition.
- Keep filter, table, and form structures explicit and region-based.
- Use blueprint-like page segmentation whenever the workflow benefits from it.

- **Official layout note:** Responsive grid utilities and page regions
- **Responsive behavior:** Responsive and adaptive tags on blueprints
- **App structure:** Record pages and app shell
- **Data display guidance:** Analytics and report UI patterns

## Navigation Rules
- Use global navigation, app launcher patterns, and object-level nav where needed.
- Use tabs within record pages and object areas.
- Use breadcrumbs lightly; object context often comes from shell and page titles.
- Keep utility actions near headers and record highlights.

- **Official navigation note:** Global nav and app launcher blueprints
- **Pattern note:** Global header, app launcher, breadcrumbs

## Component Rules
### Button
- **Official naming / aliases:** Button blueprint
- **Preferred style:** Prefer direct business-action button hierarchy with clear primary and utility actions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Input
- **Preferred style:** Use explicit enterprise fields with labels, required indicators, and nearby validation.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Combobox, picklist
- **Preferred style:** Use comboboxes and picklists for structured object workflows and form completion.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use enterprise-friendly selection controls with readable spacing and explicit states.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio group
- **Preferred style:** Use enterprise-friendly selection controls with readable spacing and explicit states.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Checkbox toggle / switch
- **Preferred style:** Use enterprise-friendly selection controls with readable spacing and explicit states.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** Datepicker, timepicker blueprints
- **Preferred style:** Use date and time controls that work inside record-editing and scheduling flows.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Global search / lookup
- **Preferred style:** Use global or object-level search fields with strong utility placement.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menus
- **Preferred style:** Use action menus and utility menus with explicit grouping and object relevance.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs as a core local-navigation pattern inside record and object pages.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs only where the shell and page context do not already provide sufficient orientation.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Global header
- **Preferred style:** Use object or page headers that surface key metadata and immediate actions.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Global navigation, vertical nav
- **Preferred style:** Use enterprise shell navigation and object context panes instead of consumer drawers.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Cards
- **Preferred style:** Use cards for modular business summaries, but prioritize page-region logic over card galleries.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Data table
- **Preferred style:** Use data tables as a core pattern for records, related items, and result sets.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List views
- **Preferred style:** Use list views and record rows for object collections and quick scanning.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and status indicators to encode record state, object type, or count.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips to support compact enterprise controls without replacing clear labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Modal
- **Preferred style:** Use prompts, modals, and panels for record edits or critical confirmations.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Toast / scoped notification
- **Preferred style:** Use scoped or global notifications for action outcomes and background updates.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Spinners and progress indicators
- **Preferred style:** Use spinners and progress indicators to keep long-running business actions legible.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination in data tables and list views when chunking improves enterprise throughput.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.


## Content & Accessibility
- Use direct labels and business-readable terminology.
- Preserve explicit states in forms, tables, prompts, and alerts.
- Use iconography to support object identification, not replace text labels.
- Keep validation close to the field or record action that caused it.
- Use accessible table and form patterns for enterprise workflows.

- **Accessibility note:** Strong | accessible blueprints emphasized
- **Content note:** Voice and tone guidance limited
- **Internationalization note:** Global Salesforce product support
- **Localization / RTL note:** Limited | not prominent in public docs
- **Validation note:** Alerts, prompts, validation in blueprints
- **State model note:** Interaction states per blueprint
- **Privacy / trust note:** CRM trust and data-sensitive workflows

## Do / Don't
### Do
- Do design around record objects, related lists, and guided business workflows.
- Do use page regions and object headers to structure screens.
- Do make status and metadata immediately visible.
- Do use tables, prompts, and utility actions confidently.
- Do keep the experience efficient and scanable for repeat work.

### Don't
- Do not make Lightning screens look like generic consumer dashboards.
- Do not overuse decorative cards, heavy gradients, or glassy panels.
- Do not hide record context or key actions behind ambiguous navigation.
- Do not replace business tables with card mosaics unless the use case clearly needs it.
- Do not soften the system into a lifestyle-brand aesthetic.

## Dashboard Mock Guardrails
- Favor Salesforce global navigation, object context, page headers, highlights panels, and record-page segmentation over generic admin dashboards.
- Use flatter utility-first surfaces and avoid soft rounded dashboard chrome.
- Bring related lists, tabs, metric display, and explicit action regions into the default composition for dashboard-like pages.
- Prefer utility icons and explicit status/action patterns over bespoke pills and decorative labels.
- Do not lead with a generic hero card; start from an object/page header plus highlights panel and related-list structure when generating CRM-like dashboards.


## Responsive Behavior
- **Mobile:** Keep the page in a record-page rhythm: show a compact set of primary tabs first and move overflow destinations into a secondary menu.
- **Tablet:** Preserve object header context and visible tabs where possible, reducing only secondary navigation.
- **Desktop:** Restore the full object/page shell with highlights, related sections, and broader tab visibility.
- **Navigation rule:** Small-width navigation should behave like compact tab plus overflow navigation, not a generic left drawer unless the pattern truly demands it.
- **Table rule:** Related lists may scroll or stack, but object context and primary actions should remain visible.
## Screen Generation Heuristics
- **Default page structure:** Use an app shell or record-page shell with utility navigation, object header, tabs, and related content regions.
- **Default density:** Use medium-to-dense density with strong business scanability.
- **Default navigation model:** Use global app navigation, object context, tabs, and contextual utility actions.
- **Preferred form composition:** Use sectioned enterprise forms with explicit labels, validation, and record-level actions.
- **Preferred feedback pattern:** Use prompts, scoped notifications, and inline field messaging for business actions.
- **Preferred data-display pattern:** Use data tables, record lists, related lists, and object summaries as primary patterns.
- **Prompt bias:** Use prompts such as 'Salesforce-style record page', 'object highlights panel', 'related list table', and 'SLDS business shell'.
- **Component naming consistency:** Medium | Salesforce-specific names appear
- **Layout rule explicitness:** High | blueprint regions and adaptivity explicit
- **Theme describability:** High | styling hooks describe visual variance
- **Prompt-to-UI suitability:** High | strong for CRM and record-centric screens

## Official Sources
- https://v1.lightningdesignsystem.com/
- https://v1.lightningdesignsystem.com/design-tokens/
- https://v1.lightningdesignsystem.com/utilities/themes/
- https://v1.lightningdesignsystem.com/components/overview/
- https://v1.lightningdesignsystem.com/accessibility/overview/
