# Spectrum DESIGN.md

## Overview
Use this specification for Adobe-style product experiences, creative workflows, and polished application UI. Favor semantic tokens, refined typography, clear workflow containers, and branded but disciplined visual language.

- **Provider:** Adobe
- **Primary reference:** https://spectrum.adobe.com/
- **Primary product focus:** Adobe product and marketing flows
- **Platforms:** Web: Yes | web workflows | iOS: Limited | some mobile web patterns | Android: Limited | not Android-native guidance | Desktop: Yes | desktop creative workflows
- **Status:** Active | Adobe maintained
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
- Support creative and professional workflows without losing clarity.
- Use semantic tokens and reusable language across product families.
- Balance polish with systematic component behavior.
- Let workflow structure guide page composition.
- Keep themes expressive but controlled.

## Color System
Representative Spectrum palette for generation. Use official Spectrum tokens in implementation; these values are representative and tuned for UI generation.

- **Blue `#1473E6`:** Primary action and selected-state emphasis.
- **Purple `#6F5CFF`:** Expressive accent and branded secondary emphasis.
- **Green `#008F5D`:** Success and healthy completion.
- **Red `#D31510`:** Error and destructive emphasis.
- **Gray 900 `#2C2C2C`:** Primary dark text and dark-mode surface anchor.
- **Gray 50 `#FFFFFF`:** Light surface and content background.
- **Gray 100 `#F8F8F8`:** Subtle containers and low-emphasis panels.
- **Border `#D5D5D5`:** Field, panel, and overlay boundaries.

- **Dark mode guidance:** Strong | theming across products
- **Theming guidance:** High | tokenized theming across apps
- **Semantic token guidance:** Strong | Spectrum tokens across platforms

## Typography
- Use Adobe Clean or a close modern neutral sans stack.
- Keep hierarchy polished and workflow-aware rather than purely utilitarian.
- Use stronger title styling than enterprise admin systems, but stay disciplined.
- Preserve readable body text across dense creative tools and configuration panels.
- Use emphasis to support tool or asset hierarchy, not marketing flourish.

- **Official typography note:** Type system with expressive scales
- **Iconography:** Spectrum icons across families
- **Motion direction:** Motion and transitions in language system

## Spacing, Radius, Elevation
- Use a consistent spacing scale that supports panels, toolbars, and workflow regions.
- Use moderate radius and refined surfaces rather than severe sharpness.
- Use overlays and depth with control, especially for popovers, trays, and dialogs.
- Keep alignment precise in tools, panels, and asset-heavy layouts.

- **Spacing system note:** Spacing tokens
- **Radius / shape note:** Corner radius in component language
- **Elevation / shadow note:** Depth and overlay styling tokens

## Layout Rules
- Use workflow-centered composition with panels, tools, and content zones.
- Support both focused document-like screens and denser application shells.
- Use side panels, headers, and trays when they strengthen creation or review flows.
- Keep the interface polished, but avoid decorative clutter around work content.
- Use thematic consistency across surfaces and control families.

- **Official layout note:** Layout, workflow, and responsive guidance
- **Responsive behavior:** Responsive patterns across devices
- **App structure:** Workflow-centered page architecture
- **Data display guidance:** Charts less central than workflows

## Navigation Rules
- Use shell navigation, tabs, and side panels based on the product workflow.
- Use breadcrumbs or path indicators only when hierarchy truly matters.
- Keep local tool navigation close to the content it affects.
- Support both app-level and object-level navigation cleanly.

- **Official navigation note:** Workflow navigation and shell patterns
- **Pattern note:** Shell nav, side nav, tabs

## Component Rules
### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer polished but restrained button hierarchy with clear primary emphasis.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

### Text field
- **Official naming / aliases:** Text field
- **Preferred style:** Use refined text inputs with visible labels and clean helper or validation messaging.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

### Select/combobox
- **Official naming / aliases:** Picker and ComboBox in Spectrum family
- **Preferred style:** Use pickers and comboboxes that fit polished workflow surfaces and complex assets or options.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use selection controls that remain explicit and accessible without feeling heavy.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use selection controls that remain explicit and accessible without feeling heavy.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use selection controls that remain explicit and accessible without feeling heavy.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

### Date/time picker
- **Official naming / aliases:** DatePicker, Calendar in Spectrum family
- **Preferred style:** Use date and time inputs only when the workflow requires them, styled to match Spectrum fields.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

### Search
- **Official naming / aliases:** Search within workflows
- **Preferred style:** Use search as a strong workflow tool in headers, asset areas, or filtering contexts.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

### Menu
- **Official naming / aliases:** Menu and ActionMenu family
- **Preferred style:** Use menus and action menus with careful spacing and clear option grouping.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs to switch sibling workflows or subviews inside a larger shell.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs where workflow hierarchy or path context matters, not by default.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

### App bar/header
- **Official naming / aliases:** Top nav and headers
- **Preferred style:** Use polished headers that orient the user without overpowering the work surface.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

### Side navigation/drawer
- **Official naming / aliases:** Side nav and rail patterns
- **Preferred style:** Use side panels or nav rails when workflow context benefits from persistent structure.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

### Card
- **Official naming / aliases:** Card and card view patterns
- **Preferred style:** Use cards and panels as controlled grouping surfaces, not as casual dashboard tiles.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use tables where precise asset or data scanning matters, with refined but readable density.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison.

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists for navigational, asset, or metadata workflows with clean structure.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and labels to communicate state and classification in a polished way.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips and coach marks for clarification in tool-dense areas.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

### Dialog/Modal
- **Official naming / aliases:** Dialog / tray
- **Preferred style:** Use dialogs, trays, and overlays for focused tasks and workflow interruptions.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

### Toast/Snackbar
- **Official naming / aliases:** Toast and coachmark family
- **Preferred style:** Use polished transient messaging that supports workflow continuity.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

### Progress/Loading
- **Official naming / aliases:** ProgressCircle, progress bar, skeleton
- **Preferred style:** Use progress indicators and skeletons that stay calm within content-heavy workflows.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination when dense result sets require explicit chunking; otherwise prefer filtering and navigation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.


## Content & Accessibility
- Use direct labels and avoid hiding critical state in pure iconography.
- Preserve contrast and state clarity across themes.
- Use supporting text and contextual help around complex tools or workflows.
- Keep terminology consistent across panels and actions.
- Use empty states and onboarding copy to guide the next creative action.

- **Accessibility note:** Strong | accessibility central across components
- **Content note:** Voice and tone is a first-class section
- **Internationalization note:** Global Adobe product support
- **Localization / RTL note:** Strong | localization and global products
- **Validation note:** Validation built into workflow and components
- **State model note:** Component states and variants explicit
- **Privacy / trust note:** Enterprise creative cloud trust context

## Do / Don't
### Do
- Do make the UI feel polished and systematized.
- Do use semantic colors and refined typography consistently.
- Do organize screens around workflows, tools, and content.
- Do keep panels and overlays clean and purposeful.
- Do let Adobe-style polish emerge through consistency, not ornament overload.

### Don't
- Do not turn Spectrum screens into generic enterprise admin dashboards.
- Do not overuse loud gradients, glossy cards, or decorative motion.
- Do not crowd creative workflows with unnecessary chrome.
- Do not flatten all hierarchy into one neutral gray layer.
- Do not use rough or mismatched component styling that breaks the polished system tone.

## Dashboard Mock Guardrails
- Do not treat a dark utility shell as the default Spectrum expression; prefer lighter, refined workflow surfaces unless context clearly calls for dark framing.
- Express Adobe-like polish through typography, spacing, and detailed component hierarchy rather than generic enterprise density.
- Favor cohesive, approachable, contextual workflows over heavy admin-console styling.
- Use accent color and panel structure with restraint so the result feels modern, friendly, and detail-oriented.
- Use lighter navigation framing and refined workflow chrome before falling back to console-like side rails.
- Include a light workflow toolbar or context strip before relying on dense dashboard cards so the page reads like a polished Adobe workspace.


## Responsive Behavior
- **Mobile:** Use an action-menu or tray-like navigation trigger with compact, polished controls rather than a broad admin drawer.
- **Tablet:** Preserve a calm workflow shell and collapse only secondary navigation before main workspace content.
- **Desktop:** Restore workspace-style navigation and utility chrome with restrained hierarchy.
- **Navigation rule:** Compact navigation should feel like Spectrum action or tray behavior, not a generic accordion menu.
- **Table rule:** Keep workspace data readable through scroll and grouped sections while maintaining a polished, low-noise shell.
## Screen Generation Heuristics
- **Default page structure:** Use a workflow shell with clear content region, supporting panels, and polished but restrained app chrome.
- **Default density:** Use medium density, allowing denser panels where workflow complexity requires it.
- **Default navigation model:** Use shell navigation, tabs, side panels, and contextual overlays according to the workflow.
- **Preferred form composition:** Use polished labeled fields with concise helper text and controlled validation.
- **Preferred feedback pattern:** Use toasts, dialogs, popovers, and inline status patterns with a calm but refined tone.
- **Preferred data-display pattern:** Use lists, asset grids, tables, and panel-based details depending on workflow fit.
- **Prompt bias:** Use prompts such as 'Adobe Spectrum workflow UI', 'refined panels', 'creative tool shell', and 'polished semantic tokens'.
- **Component naming consistency:** Medium | Adobe-specific family terms appear
- **Layout rule explicitness:** High | workflow layout is explicit
- **Theme describability:** High | visual language is richly named
- **Prompt-to-UI suitability:** High | strong for creative and content workflows

## Official Sources
- https://spectrum.adobe.com/
- https://spectrum.adobe.com/page/design-language/
- https://spectrum.adobe.com/page/color/
- https://spectrum.adobe.com/page/typography/
- https://spectrum.adobe.com/page/components/
