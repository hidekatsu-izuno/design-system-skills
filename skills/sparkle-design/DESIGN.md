# Sparkle Design DESIGN.md

## Overview
Use this specification for digital products that need a deliberate visual system with stronger brand character than a pure utility system, while still staying reusable and scalable. Favor coherent branding, practical product structure, and controlled expressiveness.

- **Provider:** Goodpatch
- **Primary reference:** https://sparkle-design.goodpatch.com/sparkle-design
- **Primary product focus:** Client and in-house digital products
- **Platforms:** Web: Yes | website and app design | iOS: N/A | not publicly positioned for iOS | Android: N/A | not public Android system | Desktop: Yes | desktop productivity sites
- **Status:** Active | publicly launched 2025
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Use a reusable visual language that still preserves product personality.
- Favor scalable patterns over one-off visual flourishes.
- Let brand expression support product clarity, not overpower it.
- Keep layout and navigation practical for digital products.
- Use design-system thinking to make quality repeatable.

### Content & Accessibility
- Use readable contrast and explicit interaction states despite the stronger brand layer.
- Keep copy direct and useful; do not let tone undermine comprehension.
- Preserve accessible spacing and target sizes in branded components.
- Use imagery and iconography to support hierarchy, not to replace it.
- Keep form and validation guidance clear even in visually expressive screens.

- **Accessibility note:** Medium | public guidance exists but not deep yet
- **Content note:** Brand and communication guidance present
- **Internationalization note:** Global consulting context | docs mostly Japanese
- **Localization / RTL note:** N/A | Japanese-first documentation
- **Validation note:** Not a highlighted public section yet
- **State model note:** State guidance emerging
- **Privacy / trust note:** Client trust and brand quality focus

### Official Sources
- https://sparkle-design.goodpatch.com/sparkle-design
- https://goodpatch.com/blog/2025-07-sparkle-design-3
- https://goodpatch.com/blog/2025-06-sparkle-design-1

## Colors
Representative Sparkle palette inferred from public Sparkle Design examples and Goodpatch branding context. Treat these values as generation guidance, not as an official token export.

- **Primary `#111111`:** Strong base text and key contrast anchor.
- **Accent `#FF6B3D`:** Expressive action and branded highlight color.
- **Support `#FFC857`:** Warm secondary accent for highlights and emphasis.
- **Background `#FFFFFF`:** Base canvas and clean surface.
- **Subtle Surface `#F7F5F2`:** Section grouping and quiet panel surface.
- **Border `#DDD6CE`:** Light structure and field boundaries.
- **Muted Text `#5E5A55`:** Secondary metadata and supporting labels.
- **Info Accent `#4A90E2`:** Supplementary interactive or informational emphasis.

- **Dark mode guidance:** Medium | theming discussed at system level
- **Theming guidance:** Medium | reusable guidance, not a formal token engine
- **Semantic token guidance:** Medium | reusable style decisions, tokens not foregrounded

## Typography
- Use a clean modern sans stack with enough personality to support brand expression.
- Allow slightly more expressive heading contrast than a pure enterprise system.
- Keep body and interface text highly readable and product-oriented.
- Use brand expression through hierarchy and spacing before resorting to heavy decoration.
- Avoid overly quirky or fashion-editorial typography in product screens.

- **Official typography note:** Brand and UI typography guidance
- **Iconography:** Brand/icon assets likely included
- **Motion direction:** Motion not a primary public theme

## Elevation
- Use consistent spacing that keeps the product feeling polished and intentionally composed.
- Use moderate-to-soft radii when the brand direction supports it, but keep controls practical.
- Use depth selectively; avoid stacking gratuitous shadows everywhere.
- Let whitespace and composition express polish more than special effects.

- **Spacing system note:** Spacing guidance present
- **Radius / shape note:** Brand style decisions present
- **Elevation / shadow note:** Visual hierarchy guidance present

## Components
### Navigation Rules
- Use clear top-level navigation and local navigation patterns that feel product-specific but still familiar.
- Use tabs and side navigation when they simplify content grouping rather than for decoration.
- Keep labels literal even when visual styling is more expressive.
- Avoid hiding structure behind oversized visual branding elements.

- **Official navigation note:** Navigation guidance emerging with system assets
- **Pattern note:** System-level nav guidance likely present

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button guidance
- **Preferred style:** Prefer a strong primary button and a carefully branded secondary treatment without losing clarity.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Text field pattern
- **Preferred style:** Use clean, readable fields with controlled brand styling and explicit labels.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Selection patterns likely present
- **Preferred style:** Use selects and comboboxes that feel integrated into the product language rather than generic browser controls.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use clear choice controls with comfortable labels and visible state changes.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio pattern
- **Preferred style:** Use clear choice controls with comfortable labels and visible state changes.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Switch guidance likely present
- **Preferred style:** Use clear choice controls with comfortable labels and visible state changes.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** Date/time selection likely present
- **Preferred style:** Use date and time controls only where the product workflow needs them, styled consistently with the broader product language.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Search pattern likely present
- **Preferred style:** Use search as a practical tool, not as a decorative centerpiece.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menu guidance likely present
- **Preferred style:** Use menus that feel polished and branded but remain easy to scan.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tabs likely present
- **Preferred style:** Use tabs where sibling content needs clear grouping with a stronger visual identity than bare utility tabs.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumb guidance likely present
- **Preferred style:** Use breadcrumbs only when hierarchy needs explicit support.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Header guidance likely present
- **Preferred style:** Use headers that can carry some brand expression while staying functional.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Side navigation likely present
- **Preferred style:** Use side navigation when it helps complex products, but keep it structured and readable.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card patterns likely present
- **Preferred style:** Use cards and panels as a key part of polished modular composition.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Table patterns likely present
- **Preferred style:** Use tables when the workflow is data-heavy, but maintain stronger visual discipline than generic enterprise UI.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

### List
- **Official naming / aliases:** List pattern
- **Preferred style:** Use lists for flexible presentation when cards or tables would be too rigid.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge likely present
- **Preferred style:** Use badges and tags to reinforce state and categorization with measured brand emphasis.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip likely present
- **Preferred style:** Use tooltips as supporting clarification, not as a stylish flourish.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Dialog guidance likely present
- **Preferred style:** Use dialogs for focused interruption and secondary tasks with polished but controlled styling.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Feedback message likely present
- **Preferred style:** Use toast or notice patterns that align with the brand system without becoming noisy.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** Loading guidance likely present
- **Preferred style:** Use progress and loading states with calm clarity and subtle branded support.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination likely present
- **Preferred style:** Use pagination when longer data or content sets need structure; avoid overusing it in narrative flows.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

### Layout Rules
- Use clear page structure and a recognizable product shell.
- Allow stronger brand moments in headers, hero sections, or section transitions when the workflow supports them.
- Keep product areas practical and navigable even when visual identity is more pronounced.
- Use cards, sections, and modular panels to scale the system cleanly.
- Prefer deliberate composition over generic dashboard repetition.

- **Official layout note:** Information architecture and layout guidance
- **Responsive behavior:** Responsive guidance likely included
- **App structure:** Consulting patterns for digital services
- **Data display guidance:** Not a major public system axis

### Screen Generation Heuristics
- **Default page structure:** Use a clear product shell with opportunities for brand expression in selected anchor areas, while keeping operational content practical.
- **Default density:** Use medium density with enough breathing room to let the visual system read clearly.
- **Default navigation model:** Use familiar top-level nav, tabs, and side navigation in a product-specific but readable way.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use clean, well-labeled forms with branded restraint rather than decorative novelty.
- **Preferred feedback pattern:** Use notices, toasts, and dialogs that match the system's visual voice without becoming theatrical.
- **Preferred data-display pattern:** Use cards, lists, and tables with stronger composition than generic admin UI, but keep them operational.
- **Prompt bias:** Use prompts such as 'brand-conscious product UI', 'Goodpatch-style design system', 'controlled expressive accents', and 'polished reusable layout'.
- **Component naming consistency:** Medium | some brand-led naming likely remains
- **Layout rule explicitness:** Medium | reusable rules still maturing publicly
- **Theme describability:** Medium | style direction is strong but less formalized
- **Prompt-to-UI suitability:** Medium | useful as a visual direction source

## Do's and Don'ts
### Do
- Do let the product feel intentionally branded and well composed.
- Do keep reusable patterns stronger than one-off art direction.
- Do use expressive accent color selectively for emphasis.
- Do keep product shells and forms practical and scalable.
- Do allow stronger visual moments only where they support product identity.

### Don't
- Do not turn Sparkle screens into generic monochrome enterprise dashboards.
- Do not over-decorate every section with gradients, stickers, or visual noise.
- Do not let branding weaken form clarity or navigation comprehension.
- Do not use playful consumer gimmicks if the product context is serious.
- Do not treat expressive accents as a substitute for hierarchy and layout discipline.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Sparkle patterns offer a clear stateful control.
