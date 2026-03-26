# Material Design DESIGN.md

## Overview
Use this specification for adaptive product UI that should feel expressive, structured, and modern without becoming ornamental. Favor semantic color roles, clear hierarchy, and component choices that scale from mobile to desktop.

- **Provider:** Google
- **Primary reference:** https://m3.material.io/
- **Primary product focus:** Cross-platform product UI
- **Platforms:** Web: Yes | core web guidance | iOS: Yes | Android emphasis but adaptable | Android: Yes | Android canonical | Desktop: Yes | large-screen guidance
- **Status:** Active | Material 3 current
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Use semantic roles and emphasis levels rather than arbitrary decoration.
- Prefer adaptive layouts that respond cleanly to narrow, medium, and large screens.
- Use motion to clarify hierarchy and state changes, not to entertain.
- Keep surfaces layered and purposeful.
- Make primary actions obvious and secondary actions quiet.

### Content & Accessibility
- Use short labels and explicit helper text for form fields.
- Preserve visible focus, pressed, selected, disabled, and error states.
- Do not rely on color alone to convey meaning.
- Use accessible contrast on both tonal and neutral surfaces.
- Pair empty states with action-oriented copy and a clear next step.

- **Accessibility note:** Strong | accessibility foundations and alt text
- **Content note:** Writing and labels in guidance
- **Internationalization note:** Global writing guidance
- **Localization / RTL note:** Limited | not core Material 3 section
- **Validation note:** Error states in text fields and dialogs
- **State model note:** Hover, focus, pressed, disabled explicit
- **Privacy / trust note:** Security and permission patterns adjacent

### Official Sources
- https://m3.material.io/
- https://m3.material.io/styles/color/roles
- https://m3.material.io/styles/typography/overview
- https://m3.material.io/foundations/layout/understanding-layout/overview
- https://m3.material.io/components

## Colors
Representative Material 3 palette for generation. Use semantic roles in implementation; the values below are representative rather than exhaustive token exports.

- **Primary `#6750A4`:** Main action color and selected-state emphasis.
- **On Primary `#FFFFFF`:** Text and icons on primary-filled surfaces.
- **Secondary `#625B71`:** Supporting emphasis and alternate accents.
- **Tertiary `#7D5260`:** Expressive accent for supportive highlights.
- **Surface `#FFFBFE`:** Base app surface and page background.
- **Surface Variant `#E7E0EC`:** Container backgrounds, dividers, and low-emphasis grouping.
- **On Surface `#1C1B1F`:** Primary text and icon color on light surfaces.
- **Outline `#79747E`:** Borders, strokes, and inactive emphasis.

- **Dark mode guidance:** Strong | dynamic color and dark theme
- **Theming guidance:** High | color roles and dynamic schemes
- **Semantic token guidance:** Strong | color, type, shape, motion roles

## Typography
- Use Roboto or the platform-default Material type stack.
- Use a clear display/headline/title/body/label hierarchy rather than custom one-off sizes.
- Keep body text neutral and readable; use label styles for compact actions and metadata.
- Use medium weight for primary labels and buttons, regular weight for longer reading.
- Avoid mixing too many type scales in a single view.

- **Official typography note:** Type scale and roles
- **Iconography:** Material Symbols and icons
- **Motion direction:** Motion system and transitions

## Elevation
- Use a 4dp-based spacing rhythm with 8dp and 16dp as the most common steps.
- Use medium rounding by default; prefer 12px to 16px corners for cards, fields, and dialogs.
- Use elevation to separate surfaces, not to create dramatic shadows.
- Let spacing and tonal containers do more work than borders.

- **Spacing system note:** Layout spacing scale
- **Radius / shape note:** Shape scale is first-class
- **Elevation / shadow note:** Elevation levels and surfaces

## Components
### Navigation Rules
- **MUST:** If the request or source specification implies a side menu, implement a navigation drawer rather than a fixed sidebar-only layout.
- **MUST:** In static HTML, implement drawer open and close behavior with CSS-only state using `:checked`.
- **MUST:** Provide a visible drawer trigger when side navigation is required.
- **MUST:** Translate behavioral requirements such as sort order, alternate sort, filtering, and toggle state into UI controls or visible state indicators rather than raw text.
- **MUST:** Treat the top app bar as an opaque surface by default on product and admin screens; do not apply backdrop blur or translucent backgrounds unless the request explicitly asks for that effect.
- Use bottom navigation for a small number of top-level destinations on mobile.
- Use navigation rail mainly for tablet or compact desktop layouts when persistent section switching helps and labels can remain secondary.
- Use a navigation drawer as the default side navigation pattern for desktop product and admin screens that need a recognizable side menu with visible labels.
- Keep drawer destinations in a vertical list with icon-leading, text-visible rows rather than centered icon stacks when the UI is presented as a side menu.
- Use tabs for sibling content views inside a single destination.

- **Official navigation note:** Navigation bar, rail, drawer patterns
- **Pattern note:** Top app bar, nav bar, nav drawer, rail

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Filled, tonal, outlined, text buttons
- **Preferred style:** Prefer filled buttons for the primary action, tonal or outlined buttons for secondary actions, and text buttons for low-emphasis actions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFBFE] p-2 text-[#1C1B1F]">
  <button class="inline-flex h-10 items-center justify-center rounded-full bg-[#6750A4] px-4 text-sm font-medium text-white shadow-sm">Save</button>
  <button class="inline-flex h-10 items-center justify-center rounded-full border border-[#79747E] bg-[#FFFBFE] px-4 text-sm font-medium text-[#1C1B1F]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Filled and outlined text field
- **Preferred style:** Use filled or outlined text fields with visible labels, helper text, and strong focus and error states.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1C1B1F]">
  <span class="font-medium">Project name</span>
  <input class="h-14 rounded-full border border-[#79747E] bg-[#FFFBFE] px-4 text-sm text-[#1C1B1F] outline-none focus:border-[#6750A4] focus:ring-2 focus:ring-[#D0BCFF]" value="North star workspace" />
  <span class="text-xs text-[#625B71]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Exposed dropdown menus and autocomplete
- **Preferred style:** Use exposed menus, dropdowns, and autocomplete patterns that align with Material input fields.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1C1B1F]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-14 w-full appearance-none rounded-full border border-[#79747E] bg-[#FFFBFE] px-4 pr-10 text-sm text-[#1C1B1F] outline-none focus:border-[#6750A4] focus:ring-2 focus:ring-[#D0BCFF]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#625B71]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use compact, clearly labeled selection controls with explicit selected, disabled, and error states.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#1C1B1F]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#79747E] text-[#6750A4] focus:ring-[#D0BCFF]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#625B71]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio button
- **Preferred style:** Use compact, clearly labeled selection controls with explicit selected, disabled, and error states.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#1C1B1F]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#79747E] text-[#6750A4] focus:ring-[#D0BCFF]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#79747E] text-[#6750A4] focus:ring-[#D0BCFF]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use compact, clearly labeled selection controls with explicit selected, disabled, and error states.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#E7E0EC] p-3 text-sm text-[#1C1B1F]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#625B71]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#6750A4]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** Date pickers and time pickers
- **Preferred style:** Use date and time pickers that match Material field styling and modal behavior.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#1C1B1F] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-14 rounded-full border border-[#79747E] bg-[#FFFBFE] px-4 text-sm outline-none focus:border-[#6750A4] focus:ring-2 focus:ring-[#D0BCFF]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-14 rounded-full border border-[#79747E] bg-[#FFFBFE] px-4 text-sm outline-none focus:border-[#6750A4] focus:ring-2 focus:ring-[#D0BCFF]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Search bar
- **Preferred style:** Use a dedicated search bar or search view with clear focus and filtering affordances.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#1C1B1F]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#625B71]">⌕</span>
  <input class="h-14 w-full rounded-full border border-[#79747E] bg-[#FFFBFE] pl-11 pr-4 text-sm outline-none focus:border-[#6750A4] focus:ring-2 focus:ring-[#D0BCFF]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** Menus
- **Preferred style:** Use menus and sheets with clear option grouping and moderate rounding.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-[28px] border border-[#79747E] bg-[#FFFBFE] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1C1B1F] hover:bg-[#E7E0EC]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1C1B1F] hover:bg-[#E7E0EC]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#B3261E] hover:bg-[#E7E0EC]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** Primary and secondary tabs
- **Preferred style:** Use primary or secondary tabs with strong selected-state contrast and clear alignment to content panes.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#79747E] text-sm text-[#625B71]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#6750A4] px-3 font-medium text-[#1C1B1F]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-t-2xl bg-[#E7E0EC] px-3 hover:text-[#1C1B1F]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#1C1B1F]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs sparingly; prefer rail, drawer, or tabs before deep breadcrumb chains.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#625B71]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#1C1B1F]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#1C1B1F]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#1C1B1F]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Top app bar
- **Preferred style:** Use top app bars with concise titles, contextual actions, and optional search or overflow. Default to an opaque Material surface or container color rather than a frosted or translucent glass effect.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions. Avoid treating blur or translucency as the default top app bar treatment.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#79747E] bg-[#FFFBFE] px-5 py-4 text-[#1C1B1F]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#625B71]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-10 items-center justify-center rounded-full bg-[#6750A4] px-4 text-sm font-medium text-white">Save</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Navigation drawer and rail
- **Preferred style:** Prefer a standard navigation drawer with left-aligned icon-and-label rows for desktop side menus; use rail only when horizontal space is tight or the layout intentionally follows a compact adaptive pattern.
- **Use when:** Use a drawer for persistent destination structure, deeper information architecture, or ordinary enterprise-style side menus. Use a rail for fewer destinations in medium-width layouts where a compact shell is more appropriate.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure. Avoid using a rail as the default desktop side menu when users need always-visible destination labels.
- **Required structure for static HTML:** Include an app-bar trigger, a hidden checkbox or equivalent CSS-only state control, a drawer panel, and a dismissal surface such as a scrim or backdrop.
- **Explicit failure cases:** A permanently visible left menu with no drawer state is not a drawer. A side menu with no trigger is invalid. A narrow icon-stack rail is not a valid substitute when the request implies a conventional side menu.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-[28px] border border-[#79747E] bg-[#FFFBFE] p-3 text-sm text-[#625B71]">
  <a class="rounded-md bg-[#E7E0EC] px-3 py-2 font-medium text-[#1C1B1F]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#E7E0EC] hover:text-[#1C1B1F]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#E7E0EC] hover:text-[#1C1B1F]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Elevated, filled, outlined cards
- **Preferred style:** Use tonal or elevated cards to group related content and actions.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-[28px] border border-[#79747E] bg-[#FFFBFE] p-5 text-[#1C1B1F] shadow-sm">
  <p class="text-xs text-[#625B71]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#625B71]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#6750A4]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Data table
- **Preferred style:** Use data tables with clear row density, sortable headers, and restrained inline actions.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-[28px] border border-[#79747E] bg-[#FFFBFE]">
  <table class="min-w-full text-left text-sm text-[#1C1B1F]">
    <thead class="bg-[#E7E0EC] text-xs uppercase tracking-[0.08em] text-[#625B71]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#79747E]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#2E7D32]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#79747E]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#625B71]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists for scanable item collections with avatars, metadata, or trailing actions only when useful.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#79747E] rounded-[28px] border border-[#79747E] bg-[#FFFBFE] text-sm text-[#1C1B1F]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#625B71]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#625B71]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and chips for status, filters, and lightweight metadata.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-full bg-[#E7E0EC] px-3 py-1 text-xs font-semibold text-[#6750A4]">Active</span>
```

### Tooltip
- **Official naming / aliases:** Plain and rich tooltip
- **Preferred style:** Use plain or rich tooltips only for supporting clarification.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#1C1B1F]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#79747E] bg-[#FFFBFE]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-full bg-[#1C1B1F] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Dialog and alert dialog
- **Preferred style:** Use dialogs and sheets for blocking choices, focused tasks, or supportive secondary flows.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-[28px] bg-[#FFFBFE] p-6 text-[#1C1B1F] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#625B71]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-10 items-center justify-center rounded-full border border-[#79747E] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-10 items-center justify-center rounded-full bg-[#B3261E] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Snackbar
- **Preferred style:** Use snackbars for transient non-blocking feedback.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-[28px] border border-[#79747E] bg-[#FFFBFE] px-4 py-3 text-sm text-[#1C1B1F] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#2E7D32]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#625B71]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Linear, circular, loading indicator
- **Preferred style:** Use circular or linear progress indicators and skeletons that match the surrounding surface hierarchy.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#1C1B1F]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#625B71]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#E7E0EC]">
    <div class="h-full w-[64%] bg-[#6750A4]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination less central in Material mobile
- **Preferred style:** Use pagination mainly in desktop data-heavy contexts; prefer infinite or chunked scrolling on mobile.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#1C1B1F]">
  <button class="inline-flex h-9 items-center justify-center rounded-full border border-[#79747E] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-full bg-[#6750A4] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-full border border-[#79747E]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-full border border-[#79747E] px-3">Next</button>
</nav>
```

### Layout Rules
- Use top app bars, navigation bars, rails, or drawers based on screen width and destination count.
- Prefer single-column composition on mobile and wider panes or supporting panels on desktop.
- Group related content into cards or tonal sections when it improves scanability.
- Use dense layouts only when task complexity requires them.
- Keep primary actions anchored near the end of the task flow or in persistent action regions.

- **Official layout note:** Responsive layout guidance
- **Responsive behavior:** Adaptive layouts by breakpoint and window class
- **App structure:** App bars, rails, sheets, panes
- **Data display guidance:** Charts and data display patterns limited

### Screen Generation Heuristics
- **Default page structure:** Use a top app bar with one primary content column. On desktop product screens, add a navigation drawer before considering a rail; use a rail only for intentionally compact adaptive layouts.
- **Default density:** Use medium density by default. Tighten spacing only for data-heavy enterprise screens.
- **Default navigation model:** Use app bar plus bottom navigation on mobile, drawer on desktop side-menu layouts, and rail only for medium-width or compact adaptive shells.
- **Pre-implementation check:** Before writing page content, confirm whether the screen needs a drawer, whether static HTML requires `:checked` state, and whether the app bar needs a menu trigger. If yes, implement that shell first.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use stacked labeled fields with helper text, clear validation, and one dominant submit action.
- **Preferred feedback pattern:** Use snackbars for transient updates, inline errors for forms, and dialogs only for blocking decisions.
- **Preferred data-display pattern:** Use cards, lists, and data tables with clear row hierarchy and restrained inline actions.
- **Prompt bias:** Use prompts such as 'Material 3 dashboard', 'tonal surfaces', 'navigation drawer with selected container', and 'filled / outlined / text button hierarchy'.
- **Component naming consistency:** High | mainstream names with variants
- **Layout rule explicitness:** High | adaptive layout rules are explicit
- **Theme describability:** High | dynamic color roles convert well from md
- **Prompt-to-UI suitability:** High | components + tokens + layout map well

## Do's and Don'ts
### Do
- Do use tonal hierarchy to distinguish importance levels.
- Do use chips for lightweight filtering and selection metadata.
- Do keep navigation patterns responsive to screen size.
- Do prefer a labeled navigation drawer for standard desktop side menus in business applications.
- Do verify the drawer structure and trigger before finalizing any screen with side navigation.
- Do express brand through color roles and illustration accents, not through arbitrary chrome.
- Do use surface containers to chunk complex screens into readable groups.

### Don't
- Do not use glassmorphism, translucent blur-heavy panels, or frosted cards.
- Do not flatten all emphasis into a single filled-button style.
- Do not over-outline every container when tonal surfaces are sufficient.
- Do not use consumer-social styling such as oversized avatars and playful gradients by default.
- Do not invent custom control shapes that fight Material components.
- Do not default to a narrow icon-stack rail when the user asked for or clearly implies a conventional side menu.
- Do not treat drawer guidance as optional when the screen clearly requires a side menu.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Material patterns offer a clear stateful control.
