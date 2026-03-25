# Spindle Design System DESIGN.md

## Overview
Use this specification for Ameba-flavored web product UI that should feel friendly, respectful, and easy to understand without becoming noisy or overly promotional. Favor explicit labels, approachable surfaces, strong readability for Japanese content, and product decisions that balance emotional warmth with operational clarity.

- **Provider:** CyberAgent / Ameba
- **Primary reference:** https://spindle.ameba.design/
- **Primary product focus:** Ameba web product UI and brand-consistent digital experiences
- **Platforms:** Web: Yes | primary public guidance | iOS: Limited | catalog coverage exists but web-first public docs | Android: Limited | catalog coverage exists but web-first public docs | Desktop: Yes | strong browser product fit
- **Status:** Active | publicly maintained Spindle guidance
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Respect the user and avoid UI that feels pushy, abrupt, or self-centered.
- Add warmth and human tone, but keep interaction practical and easy to parse.
- Make first-time and repeat use feel welcoming rather than exclusive.
- Prefer simple structure, explicit labels, and readable spacing over clever novelty.
- Keep the interface lively through rhythm, color accents, and tone, not through visual clutter.

### Content & Accessibility
- Use direct, plain Japanese-friendly labels and guidance in product UI.
- Preserve alternatives for different abilities and interaction methods rather than assuming hover or pointer-only use.
- Do not rely on color alone for status or selection; pair color with borders, labels, or state styling.
- Keep validation, focus, and state changes explicit and easy to perceive.
- Favor clarity and flexibility so the interface remains resilient to user context changes.

- **Accessibility note:** Strong | Spindle aligns with Ameba Accessibility Guidelines and WCAG 2.1-based practice
- **Content note:** Strong | public guidance for brand voice, vocabulary, and UI labeling
- **Internationalization note:** Japanese-first product guidance
- **Localization / RTL note:** Limited | public guidance is Japanese-first
- **Validation note:** Public component guidance includes invalid and focus-aware states
- **State model note:** Strong | selection, visited, invalid, and focus behavior are explicitly discussed
- **Privacy / trust note:** Medium | respectful, user-centered tone is emphasized more than formal enterprise trust language

### Official Sources
- https://spindle.ameba.design/
- https://spindle.ameba.design/principles/design/
- https://spindle.ameba.design/principles/accessibility/
- https://spindle.ameba.design/styles/color/ui/
- https://spindle.ameba.design/styles/color/brand/
- https://spindle.ameba.design/styles/typography/ui/
- https://spindle.ameba.design/styles/typography/brand/
- https://spindle.ameba.design/styles/iconography/anatomy/
- https://spindle.ameba.design/styles/iconography/developer/
- https://spindle.ameba.design/components/
- https://spindle.ameba.design/components/status/

## Colors
Representative Spindle palette for generation based on the public UI color guidance. Favor UI colors for product interfaces and treat brand colors as communication accents rather than default UI paint.

- **Accent Blue `#0091FF`:** Primary accent for links, focus-led emphasis, and selected interactive states.
- **Text High `#08121A`:** Primary text on light surfaces.
- **Text Medium `#394148`:** Secondary text, helper copy, and supporting labels.
- **Text Low `#686E73`:** Quiet metadata and low-emphasis text.
- **Surface Base `#F5F6F6`:** Primary page background.
- **Surface Raised `#FFFFFF`:** Cards, panels, modals, and elevated content surfaces.
- **Surface Secondary `#EBECED`:** Subtle grouped sections and supporting containers.
- **Border Low `#D8D9DA`:** Dividers, field borders, and low-emphasis separators.
- **Border Quiet `#B5B8BA`:** Stronger neutral boundary for selected or separated regions.
- **Positive `#389E46`:** Positive status and success emphasis.
- **Danger `#D91C0B`:** Error and destructive emphasis.
- **Highlight Yellow `#F5E100`:** Highlight or marker-like emphasis in limited cases.
- **Expressive Pink `#F20076`:** Rare expressive accent; use only when green, gray, or red cannot serve the need and keep usage tightly limited.

- **Dark mode guidance:** Public site supports theme switching, but public usage guidance is still light-surface dominant
- **Theming guidance:** Medium | theme colors exist, but public product guidance emphasizes restrained UI usage
- **Semantic token guidance:** Strong | separate surface, text, object, border, highlight, focus, and brand roles

## Typography
- Use the published UI font stack for web by default: `"Helvetica Neue", Helvetica, Arial, "Segoe UI", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, "Yu Gothic Medium", sans-serif`.
- Use `bold` keyword weight for bold treatment rather than arbitrary numeric weight changes when following the official web guidance.
- Optimize for readability in Japanese UI first, especially in labels, controls, and dense operational lists.
- Treat brand typography such as Ameba Sans, UD Shin Maru Go, and AXIS as brand-expression tools, not default app UI type.
- Reserve Ameba Sans in product UI only for constrained numeric or expressive brand-led cases, not for general interface copy.

- **Official typography note:** Public UI typography guidance includes explicit web font-family recommendations
- **Iconography:** Spindle icons are first-party and documented separately
- **Motion direction:** Animation guidance exists, but typography should remain calm and readable rather than motion-led

## Elevation
- Prefer light surfaces, quiet borders, and modest card separation over heavy shadow stacks.
- Use rounded corners, but keep them controlled and product-like rather than oversized or glassy.
- Let whitespace and grouping establish hierarchy before adding stronger elevation.
- Keep lists, panels, and forms aligned to a simple, readable vertical rhythm.
- Use modal and panel elevation clearly when content overlays the current context.

- **Spacing system note:** Public style system covers UI typography, color, icons, and component rhythm even if spacing tokens are not foregrounded as a separate public chapter
- **Radius / shape note:** Rounded geometry is part of the Ameba visual character, but should stay disciplined in UI
- **Elevation / shadow note:** Surface layering exists, especially for cards and modals, but border-led grouping is common

## Components
### Navigation Rules
- Use navigation with explicit labels and approachable visual tone rather than abstract icon-only wayfinding.
- Prefer simple top navigation, local tabs, lists, or grouped menus over enterprise-heavy shell patterns unless the product scope clearly requires persistent side navigation.
- Keep destination structure shallow and friendly; avoid turning the interface into a cold admin shell.
- When navigation or selection appears inside a list, use border, background, or structural change in addition to color to indicate state.

- **Official navigation note:** Public guidance is component- and content-led rather than shell-heavy
- **Pattern note:** Lists, status, tabs, menus, and friendly top-level navigation fit better than rigid enterprise chrome

### Icon usage in static mocks
- **Native icon guidance:** Prefer the official Spindle icon set when available. The public developer guidance points to `@openameba/spindle-icons`.
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome as the fallback icon library.
- **Where to use icons:** Show icons in places where Spindle normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, state cues, and row-level actions.
- **How to use icons:** Choose simple geometric icons with readable 24px-oriented proportions, keep visible text labels, and avoid decorative multi-color icon treatments.

### Button
- **Official naming / aliases:** Button, LinkButton, TextButton, SubtleButton, BottomButton
- **Preferred style:** Use clean, approachable buttons with clear hierarchy and enough padding to feel friendly without becoming oversized.
- **Use when:** Use for primary actions, secondary follow-up actions, and inline action sets that should stay explicit.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading when relevant.
- **Avoid:** Avoid overly glossy, overly shadowed, or aggressively enterprise-styled buttons.

### Text field
- **Official naming / aliases:** TextField, TextArea, InputLabel, InvalidMessage
- **Preferred style:** Use clearly labeled fields with visible helper or invalid messaging and straightforward boundaries.
- **Use when:** Use for account, profile, settings, search, and content-entry tasks where direct text entry is expected.
- **Important states:** Empty, filled, focus, invalid, disabled, and helper/error visibility.
- **Avoid:** Avoid placeholder-only labeling or muted states that hide field purpose.

### Select/combobox
- **Official naming / aliases:** DropDown, InlineDropDown
- **Preferred style:** Use simple dropdown patterns that align with surrounding text fields and list-based selection.
- **Use when:** Use when a known option set should stay compact or inline with other controls.
- **Important states:** Closed, open, focused, selected, invalid, and disabled.
- **Avoid:** Avoid visually overcomplicated custom pickers for ordinary option selection.

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use clear checkbox controls with enough label spacing and obvious selected state.
- **Use when:** Use for multi-select and independent opt-in or opt-out choices.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, invalid, and disabled.
- **Avoid:** Avoid using checkboxes for exclusive choices.

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use radios for small visible exclusive choice sets and align them cleanly within forms or lists.
- **Use when:** Use for one-of-many choices that benefit from full visibility.
- **Important states:** Unchecked, checked, focus, invalid, and disabled.
- **Avoid:** Avoid turning long option sets into radio groups when dropdown selection would be easier to scan.

### Switch
- **Official naming / aliases:** ToggleSwitch, Toggle inside List
- **Preferred style:** Use toggle switches inside list rows or settings groups when the change is immediate and understandable in place.
- **Use when:** Use for binary settings and lightweight immediate state changes.
- **Important states:** Off, on, focus, disabled, and any paired explanation.
- **Avoid:** Avoid switches for actions that still require later confirmation.

### Search
- **Official naming / aliases:** Search field using TextField patterns
- **Preferred style:** Use direct, readable search controls with explicit labels or clear search affordances.
- **Use when:** Use for filtering or finding content, people, records, or settings.
- **Important states:** Idle, focused, active query, clear/reset, loading, and empty-result states.
- **Avoid:** Avoid hero-style oversized search that overpowers the rest of the product UI.

### Menu
- **Official naming / aliases:** DropDownMenu, menus within lists and panels
- **Preferred style:** Use compact menus with direct labels and calm separators.
- **Use when:** Use for overflow actions, contextual actions, or dense utility choices.
- **Important states:** Closed, open, focus-visible item, selected item, and disabled item.
- **Avoid:** Avoid burying the primary task path behind menus.

### Tabs
- **Official naming / aliases:** UnderlineTab, SegmentedControl
- **Preferred style:** Use underline tabs or segmented controls for sibling views with a lightweight, web-native feel.
- **Use when:** Use for nearby peer views inside one destination.
- **Important states:** Inactive, active, focus-visible, and overflow handling where necessary.
- **Avoid:** Avoid turning tabs into deep information architecture or complex workflow steps.

### Breadcrumb
- **Official naming / aliases:** BreadCrumb
- **Preferred style:** Use breadcrumbs only when the product hierarchy genuinely needs orientation help.
- **Use when:** Use for deeper destinations where the user benefits from visible location context.
- **Important states:** Default, current page, truncated if necessary, and focus-visible links.
- **Avoid:** Avoid breadcrumbs in shallow experiences where titles and local navigation are enough.

### App bar/header
- **Official naming / aliases:** Header and local page header patterns
- **Preferred style:** Use light, readable headers with clear titles, concise support copy, and a modest action set.
- **Use when:** Use to anchor the page context and expose a small number of important controls.
- **Important states:** Default, focused action, and compact behavior on small screens.
- **Avoid:** Avoid sticky chrome that feels heavier than the page content.

### Side navigation/drawer
- **Official naming / aliases:** Local navigation patterns rather than a strongly prescribed global shell
- **Preferred style:** If side navigation is necessary, keep it lightweight, label-first, and friendlier than a classic enterprise admin rail.
- **Use when:** Use only when the product truly has multiple persistent destinations that benefit from constant visibility.
- **Important states:** Hidden or compact, expanded, selected destination, and focus-visible state.
- **Avoid:** Avoid forcing a rigid dashboard shell onto content that is better served by top navigation, tabs, or lists.

### List
- **Official naming / aliases:** List, Collection List, Selection, Visited, Add
- **Preferred style:** Use lists as a core structural primitive. Support state with borders, backgrounds, and row structure rather than color alone.
- **Use when:** Use for settings, row actions, navigation-like collections, selectable rows, and content browsing.
- **Important states:** Default, selected, visited where relevant, toggled, focused, and disabled.
- **Avoid:** Avoid reducing list state to color-only differences.

### Card
- **Official naming / aliases:** Panel or card-like grouped container
- **Preferred style:** Use soft grouped surfaces with visible borders or subtle elevation.
- **Use when:** Use to group related information or supporting actions without turning every region into a floating tile.
- **Important states:** Default, interactive hover when clickable, selected when needed, and loading.
- **Avoid:** Avoid overly ornamental card stacks or exaggerated dashboard tiles.

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use practical tables with readable row spacing and quiet borders.
- **Use when:** Use when comparison across rows and columns is the main task.
- **Important states:** Default, sorted, selected, loading, empty, and error.
- **Avoid:** Avoid using a table when a simpler list better supports the content.

### Badge
- **Official naming / aliases:** Status, InlineNotification, StackNotificationManager, Toast, SnackBar
- **Preferred style:** Use small status labels and notification surfaces with explicit text and clear contrast.
- **Use when:** Use for state, inline feedback, pending work, or transient results.
- **Important states:** Neutral, positive, warning, danger, active, and dismissed where relevant.
- **Avoid:** Avoid replacing explanatory text with color chips alone.

### Dialog/Modal
- **Official naming / aliases:** Modal, Dialog, SemiModal, AppealModal
- **Preferred style:** Use light, rounded overlays with clear hierarchy, readable body copy, and one obvious primary action.
- **Use when:** Use for confirmation, focused secondary tasks, or interruption-worthy flows.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading or submitting state.
- **Avoid:** Avoid oversized or theatrically layered modal presentations.

### Tooltip
- **Official naming / aliases:** Tooltip-like helper usage where needed
- **Preferred style:** Use only for supplementary clarification.
- **Use when:** Use for secondary help that should not interrupt the task.
- **Important states:** Hidden, shown, keyboard-focus trigger, and dismissal.
- **Avoid:** Avoid putting required instructions only in a tooltip.

### Progress/Loading
- **Official naming / aliases:** Loading and notification-related progress states
- **Preferred style:** Use quiet loading indicators and skeletons that do not dominate the layout.
- **Use when:** Use for async updates, content fetches, and submission feedback.
- **Important states:** Idle, loading, partial progress where available, and completion.
- **Avoid:** Avoid flashy loading treatments that compete with content.

## Do's and Don'ts
- **Do:** Keep UI product-facing, warm, and readable with explicit labels and approachable spacing.
- **Do:** Prefer UI colors over brand colors for normal product surfaces and controls.
- **Do:** Use lists, tabs, fields, and notifications as the main building blocks before inventing new shells.
- **Do:** Preserve Japanese readability and a friendly tone without sounding childish.
- **Do:** Use borders, state shape, and labels in addition to color to communicate selection and status.
- **Do not:** Do not turn the interface into a generic enterprise admin dashboard with heavy chrome.
- **Do not:** Do not overuse brand green or expressive pink as default UI paint.
- **Do not:** Do not use glassmorphism, oversized blur, or decorative gradients as the main visual language.
- **Do not:** Do not replace clear copy with icon-only or color-only communication.
- **Do not:** Do not expose brand typography as the default font for routine web UI text.
