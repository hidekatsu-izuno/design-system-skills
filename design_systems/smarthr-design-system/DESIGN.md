# SmartHR Design System DESIGN.md

## Overview
Use this specification for Japanese business SaaS, HR workflows, and back-office tools. Favor trust, clarity, and straightforward operational layouts with accessible defaults and minimal visual excess.

- **Provider:** SmartHR
- **Primary reference:** https://smarthr.design/
- **Primary product focus:** HR SaaS product UI
- **Platforms:** Web: Yes | primary product target | iOS: Limited | app-specific not central | Android: Limited | app-specific not public focus | Desktop: Yes | desktop web product
- **Status:** Active | SmartHR maintained
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Design for trust, clarity, and dependable business operation.
- Use concise labels and explicit guidance for form-heavy screens.
- Keep visual language approachable but not casual.
- Prefer practical layout and component choices over expressive experimentation.
- Support accessibility and Japanese business-product readability by default.

## Color System
Representative SmartHR palette for generation based on public design-token guidance and product styling. Use official tokens in implementation; these values are representative.

- **Primary `#00C4CC`:** Main action and brand-led emphasis.
- **Primary Tint `#E5FAFB`:** Soft highlight and selected-state background.
- **Text `#23221F`:** Primary text color.
- **Background `#FFFFFF`:** Base application surface.
- **Subtle Surface `#F8F7F6`:** Panels, grouped sections, and low-emphasis containers.
- **Border `#D6D3D1`:** Table, field, and section borders.
- **Warning `#FF9900`:** Caution and pending attention.
- **Danger `#E5484D`:** Error and destructive emphasis.

- **Dark mode guidance:** Strong | product supports themes
- **Theming guidance:** Medium | design tokens via SmartHR UI
- **Semantic token guidance:** Strong | design tokens in SmartHR UI

## Typography
- Use SmartHR Sans when available or a close readable sans stack that supports Japanese well.
- Keep hierarchy practical and approachable.
- Favor body readability and field clarity over large expressive headings.
- Use compact metadata styles but do not collapse readability in dense administrative screens.
- Preserve consistent rhythm between Japanese and Latin content.

- **Official typography note:** Typography tokens and usage
- **Iconography:** Icon guidance and assets
- **Motion direction:** Motion not heavily emphasized publicly

## Spacing, Radius, Elevation
- Use a practical spacing cadence that keeps forms and lists easy to scan.
- Use moderate rounding and calm surface hierarchy.
- Use shadows lightly and prefer whitespace plus borders for structure.
- Keep field spacing, labels, and section grouping highly consistent.

- **Spacing system note:** Spacing tokens in UI kit
- **Radius / shape note:** Shape decisions in UI kit
- **Elevation / shadow note:** Surface hierarchy guidance present

## Layout Rules
- Use straightforward page composition with clear title, navigation, and content blocks.
- Support form-heavy operational flows and list/detail patterns.
- Use cards, tables, and grouped sections to keep business content readable.
- Avoid ornamental asymmetry and aggressive visual flourishes.
- Favor trust-building clarity over trend-driven density extremes.

- **Official layout note:** Product layout guidance exists
- **Responsive behavior:** Responsive product design implied
- **App structure:** Product IA and screen composition
- **Data display guidance:** Data display in product guidance

## Navigation Rules
- Use simple, readable navigation with strong labels and modest hierarchy depth.
- Use tabs, side navigation, or local navigation only where task grouping benefits from it.
- Use breadcrumbs when the information architecture becomes deep enough to justify them.
- Keep navigation text explicit and low-ambiguity.

- **Official navigation note:** Product navigation guidance exists
- **Pattern note:** Header and local nav patterns

## Component Rules
### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer clear primary and secondary buttons with calm brand color emphasis.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Text field
- **Preferred style:** Use practical fields with explicit labels, helper text, and readable validation.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Select and combobox in SmartHR UI
- **Preferred style:** Use straightforward selects and comboboxes for business configuration and data entry.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use readable choice controls with enough spacing for Japanese labels and explanatory text.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio button
- **Preferred style:** Use readable choice controls with enough spacing for Japanese labels and explanatory text.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use readable choice controls with enough spacing for Japanese labels and explanatory text.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** Date picker in SmartHR UI
- **Preferred style:** Use date inputs that feel businesslike and integrate cleanly with operational forms.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Search
- **Preferred style:** Use search as a direct utility for finding records, people, or settings.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menu
- **Preferred style:** Use menus with explicit labels and restrained visual treatment.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs when sibling business views need fast switching without adding confusion.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs when deeper administrative IA needs orientation support.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Header
- **Preferred style:** Use practical page headers with title, summary, and a small action set.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Side navigation
- **Preferred style:** Use side navigation for larger business products, but keep structure simple and readable.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards and sections to keep back-office information grouped and approachable.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use tables confidently for records, settings, and administrative data.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists where the content is lighter-weight or more narrative than a full table.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Status label
- **Preferred style:** Use badges and labels for status, state, and lightweight categorization.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips sparingly to clarify controls without hiding essential guidance.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Dialog
- **Preferred style:** Use dialogs for confirmations and focused secondary tasks, not for routine validation.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Toast / notification
- **Preferred style:** Use toast or notice patterns for non-blocking business feedback.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Loader and progress
- **Preferred style:** Use loading and progress indicators calmly and clearly.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination in longer administrative lists and records where chunking helps orientation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.


## Content & Accessibility
- Use plain, direct interface language suited to business and HR operations.
- Make validation and required fields explicit.
- Preserve accessible contrast and focus treatment across all controls.
- Use icons and illustrations as support, not as the main communication layer.
- Keep forms calm, readable, and easy to complete in sequence.

- **Accessibility note:** Strong | checklist and alt-text guidance
- **Content note:** Communication content category exists
- **Internationalization note:** Japanese product focus | global not primary
- **Localization / RTL note:** N/A | Japanese-first documentation
- **Validation note:** Product guidance includes error states
- **State model note:** State handling in SmartHR UI components
- **Privacy / trust note:** HR data sensitivity strongly implied

## Do / Don't
### Do
- Do make the interface feel dependable and business-ready.
- Do prioritize form clarity, list readability, and explicit feedback.
- Do use subtle brand color accents rather than over-branding the full shell.
- Do support Japanese text comfortably in labels, tables, and help text.
- Do keep the experience calm and operational.

### Don't
- Do not turn SmartHR screens into flashy startup landing pages.
- Do not use overly dark or dramatic visual treatment by default.
- Do not hide validation or rely on placeholder-only labeling.
- Do not over-pack screens with dense micro-panels if simple sections will do.
- Do not use playful novelty components that weaken trust.

## Screen Generation Heuristics
- **Default page structure:** Use a calm business shell with a readable header, practical navigation, and content grouped into forms, lists, and sections.
- **Default density:** Use medium density with readable spacing.
- **Default navigation model:** Use straightforward navigation, tabs, and side navigation only where task organization benefits.
- **Preferred form composition:** Use stacked or well-aligned labeled fields with explicit validation and helper text.
- **Preferred feedback pattern:** Use inline validation, notices, toasts, and dialogs with clear business wording.
- **Preferred data-display pattern:** Use tables, cards, and lists for employee data, settings, and administrative workflows.
- **Prompt bias:** Use prompts such as 'SmartHR business app', 'Japanese HR workflow', 'calm teal accents', and 'clear back-office form layout'.
- **Component naming consistency:** High | straightforward Japanese and OSS names
- **Layout rule explicitness:** Medium | guidance exists but not always condensed
- **Theme describability:** Medium | themes exist but docs are product-specific
- **Prompt-to-UI suitability:** High | good for Japanese business app screens

## Official Sources
- https://smarthr.design/
- https://smarthr.design/products/design-tokens/color-palette/
- https://smarthr.design/products/design-tokens/typography/
- https://smarthr.design/products/design-tokens/media-query/
- https://smarthr.design/products/components/
