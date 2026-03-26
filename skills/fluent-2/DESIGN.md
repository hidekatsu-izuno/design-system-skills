# Fluent 2 Design System DESIGN.md

## Overview
Use this specification for productive, cross-platform Microsoft-style applications. Favor approachable structure, strong tokenization, explicit states, and layouts that support work rather than spectacle.

- **Provider:** Microsoft
- **Primary reference:** https://fluent2.microsoft.design/
- **Primary product focus:** Cross-platform Microsoft product UI
- **Platforms:** Web: Yes | web first docs | iOS: Yes | cross-platform guidance | Android: Yes | Android support via Fluent UI | Desktop: Yes | Windows desktop heritage
- **Status:** Active | Fluent 2 current
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Design for productive tasks, not pure marketing impression.
- Use explicit states and accessible contrast throughout.
- Keep surfaces calm and theme-aware.
- Favor approachable geometry over severe sharpness.
- Let component behavior stay predictable across surfaces and themes.

### Content & Accessibility
- Use direct labels and task-oriented copy.
- Make focus, hover, pressed, selected, and disabled states explicit.
- Prefer inline validation and calm status messaging over modal interruption.
- Preserve readable contrast in both light and dark themes.
- Use icons to support labels, not replace them.

- **Accessibility note:** Strong | inclusive by default guidance
- **Content note:** Microcopy guidance present
- **Internationalization note:** Global products assumed
- **Localization / RTL note:** RTL support in Fluent UI ecosystem
- **Validation note:** Validation states standardized in components
- **State model note:** Rest, hover, pressed, selected explicit
- **Privacy / trust note:** Trust and privacy aligned with Microsoft products

### Official Sources
- https://fluent2.microsoft.design/
- https://fluent2.microsoft.design/color
- https://fluent2.microsoft.design/typography
- https://fluent2.microsoft.design/layout
- https://fluent2.microsoft.design/components/web/react/core/button/usage

## Colors
Representative Fluent 2 palette for generation. Use tokens in implementation; the hex values below capture the design language without claiming exhaustive token coverage.

- **Brand `#0F6CBD`:** Primary Microsoft-style action and brand emphasis.
- **Brand Pressed `#0C3B5E`:** Pressed or stronger action emphasis.
- **Brand Tint `#EBF3FC`:** Tinted selection, hover, and supportive surfaces.
- **Neutral Foreground `#242424`:** Primary text and icon color.
- **Neutral Background `#FFFFFF`:** Default canvas and card surfaces.
- **Neutral Subtle `#F5F5F5`:** Low-emphasis surface and section grouping.
- **Success `#107C10`:** Success and positive confirmation.
- **Danger `#D13438`:** Error and destructive emphasis.

- **Dark mode guidance:** Strong | light/dark theme built in
- **Theming guidance:** High | theme tokens and brand ramps
- **Semantic token guidance:** Strong | global and alias tokens

## Typography
- Use Segoe UI or the current Microsoft platform type stack.
- Use a clear ramp of display, title, subtitle, body, and caption roles.
- Favor functional, readable text over expressive editorial treatment.
- Use semibold strategically for headers and primary control labels.
- Keep tables and forms typographically compact but not cramped.

- **Official typography note:** Type ramp tokens
- **Iconography:** Fluent System Icons adjacent
- **Motion direction:** Motion tokens and transitions

## Elevation
- Use token-driven spacing with 4px and 8px cadence at the core.
- Use soft radii, typically around 4px to 8px for controls and 8px to 12px for containers.
- Use shadows and elevation quietly; structure should come mostly from spacing and surface value.
- Keep component spacing consistent across adjacent controls and panels.

- **Spacing system note:** Spacing tokens
- **Radius / shape note:** Border radius tokens
- **Elevation / shadow note:** Shadow tokens available

## Components
### Navigation Rules
- Use left-side navigation, top tabs, or app shell patterns for complex products.
- Use toolbar patterns for dense command surfaces.
- Use breadcrumbs when users move across deep hierarchies.
- Keep local navigation close to the content area it controls.

- **Official navigation note:** Nav, tabs, toolbar, app shell guidance
- **Pattern note:** Nav drawer, tabs, toolbar, breadcrumbs

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button variants with appearance tokens
- **Preferred style:** Prefer clear primary, secondary, and subtle button hierarchy with strong state visibility.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#242424]">
  <button class="inline-flex h-10 items-center justify-center rounded-md bg-[#0F6CBD] px-4 text-sm font-medium text-white shadow-sm">Save changes</button>
  <button class="inline-flex h-10 items-center justify-center rounded-md border border-[#D1D1D1] bg-[#FFFFFF] px-4 text-sm font-medium text-[#242424]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Input field
- **Preferred style:** Use token-driven fields with explicit labels, helper text, and strong focus/error treatments.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#242424]">
  <span class="font-medium">Project name</span>
  <input class="h-10 rounded-md border border-[#D1D1D1] bg-[#FFFFFF] px-4 text-sm text-[#242424] outline-none focus:border-[#0F6CBD] focus:ring-2 focus:ring-[#82C7FF]" value="North star workspace" />
  <span class="text-xs text-[#616161]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Combobox, dropdown
- **Preferred style:** Use comboboxes and dropdowns that support productivity workflows and keyboard use.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#242424]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-10 w-full appearance-none rounded-md border border-[#D1D1D1] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#242424] outline-none focus:border-[#0F6CBD] focus:ring-2 focus:ring-[#82C7FF]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#616161]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use checkboxes, radios, and switches with compact but comfortable spacing and visible states.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#242424]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#D1D1D1] text-[#0F6CBD] focus:ring-[#82C7FF]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#616161]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use checkboxes, radios, and switches with compact but comfortable spacing and visible states.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#242424]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#D1D1D1] text-[#0F6CBD] focus:ring-[#82C7FF]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#D1D1D1] text-[#0F6CBD] focus:ring-[#82C7FF]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use checkboxes, radios, and switches with compact but comfortable spacing and visible states.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F5F5F5] p-3 text-sm text-[#242424]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#616161]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#0F6CBD]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** DatePicker, TimePicker adjacent in libraries
- **Preferred style:** Use date and time pickers that align with field composition and enterprise workflows.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#242424] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-10 rounded-md border border-[#D1D1D1] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0F6CBD] focus:ring-2 focus:ring-[#82C7FF]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-10 rounded-md border border-[#D1D1D1] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0F6CBD] focus:ring-2 focus:ring-[#82C7FF]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Searchbox
- **Preferred style:** Use search boxes that can expand into command or filtering workflows.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#242424]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#616161]">⌕</span>
  <input class="h-10 w-full rounded-md border border-[#D1D1D1] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#0F6CBD] focus:ring-2 focus:ring-[#82C7FF]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** Menu, MenuList
- **Preferred style:** Use compact menus with clear grouping and keyboard-friendly behavior.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-xl border border-[#D1D1D1] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#242424] hover:bg-[#F5F5F5]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#242424] hover:bg-[#F5F5F5]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#D13438] hover:bg-[#F5F5F5]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** TabList / tabs
- **Preferred style:** Use tabs and tablists for local view switching in app and panel contexts.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#D1D1D1] text-sm text-[#616161]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#0F6CBD] px-3 font-medium text-[#242424]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-t-lg bg-[#FFFFFF] px-3 hover:text-[#242424]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#242424]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs when deep app hierarchy needs persistent orientation.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#616161]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#242424]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#242424]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#242424]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Toolbar / app shell header
- **Preferred style:** Use page headers and command bars that prioritize task controls.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#D1D1D1] bg-[#FFFFFF] px-5 py-4 text-[#242424]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#616161]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-10 items-center justify-center rounded-md bg-[#0F6CBD] px-4 text-sm font-medium text-white">Save changes</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Drawer and navigation pane
- **Preferred style:** Use left navigation or pane-based navigation for persistent product structure.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-xl border border-[#D1D1D1] bg-[#FFFFFF] p-3 text-sm text-[#616161]">
  <a class="rounded-md bg-[#F5F5F5] px-3 py-2 font-medium text-[#242424]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F5F5] hover:text-[#242424]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F5F5] hover:text-[#242424]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use quiet cards and panels to organize related information blocks.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-xl border border-[#D1D1D1] bg-[#FFFFFF] p-5 text-[#242424] shadow-sm">
  <p class="text-xs text-[#616161]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#616161]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#0F6CBD]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Table, DataGrid in ecosystem
- **Preferred style:** Use dense but readable tables and grids with visible column hierarchy and state cues.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-xl border border-[#D1D1D1] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#242424]">
    <thead class="bg-[#F5F5F5] text-xs uppercase tracking-[0.08em] text-[#616161]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#D1D1D1]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#107C10]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#D1D1D1]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#616161]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List
- **Preferred style:** Use structured lists with metadata, avatars, and utility actions where appropriate.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#D1D1D1] rounded-xl border border-[#D1D1D1] bg-[#FFFFFF] text-sm text-[#242424]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#616161]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#616161]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and status pills for state, category, or lightweight metadata.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-md bg-[#F5F5F5] px-3 py-1 text-xs font-semibold text-[#0F6CBD]">Active</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips for supporting clarification, especially in command-dense interfaces.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#242424]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#D1D1D1] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-md bg-[#242424] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Dialog
- **Preferred style:** Use dialogs for focused decisions and side panels for longer secondary tasks.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-xl bg-[#FFFFFF] p-6 text-[#242424] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#616161]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-10 items-center justify-center rounded-md border border-[#D1D1D1] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-10 items-center justify-center rounded-md bg-[#D13438] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Toast / message bar
- **Preferred style:** Use toast or message bar feedback without overusing interruption.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-xl border border-[#D1D1D1] bg-[#FFFFFF] px-4 py-3 text-sm text-[#242424] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#107C10]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#616161]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Spinner, progress bar
- **Preferred style:** Use spinners, progress bars, and skeletons with explicit surrounding context.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#242424]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#616161]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F5F5F5]">
    <div class="h-full w-[64%] bg-[#0F6CBD]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination in web libraries
- **Preferred style:** Use pagination in dense data views when chunking improves throughput and orientation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#242424]">
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#D1D1D1] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md bg-[#0F6CBD] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md border border-[#D1D1D1]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#D1D1D1] px-3">Next</button>
</nav>
```

### Layout Rules
- Use app shells with clear header, navigation, and content regions.
- Support both simple single-column screens and multi-pane productivity layouts.
- Use compact density when task throughput matters, but preserve scanability.
- Group related content with subtle container separation rather than loud cards everywhere.
- Make state changes obvious through field messages, badges, and action feedback.

- **Official layout note:** Layout and spacing guidance
- **Responsive behavior:** Responsive/adaptive guidance across surfaces
- **App structure:** Shell, nav, windows, surfaces
- **Data display guidance:** Data viz not central in core Fluent 2

### Screen Generation Heuristics
- **Default page structure:** Use a productivity shell with persistent navigation, clear page title, command region, and structured content panes.
- **Default density:** Use medium-to-compact density by default.
- **Default navigation model:** Use left navigation, tabs, toolbars, and contextual command surfaces.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use aligned labeled fields, strong helper text, inline validation, and clearly grouped actions.
- **Preferred feedback pattern:** Use message bars, toasts, inline status, and dialogs only when interruption is necessary.
- **Preferred data-display pattern:** Use structured tables, lists, cards, and panels with visible status metadata.
- **Prompt bias:** Use prompts such as 'Fluent 2 productivity app', 'Microsoft admin console', 'calm neutral surfaces', and 'explicit stateful controls'.
- **Component naming consistency:** High | conventional names
- **Layout rule explicitness:** High | spacing and layout tokens explicit
- **Theme describability:** High | theme tokens map cleanly to prompts
- **Prompt-to-UI suitability:** High | strong for cross-platform enterprise prompts

## Do's and Don'ts
### Do
- Do make states highly legible and easy to scan.
- Do keep productivity tasks front and center.
- Do use theme-aware surfaces and semantic color roles.
- Do structure dense screens with clear hierarchy and predictable alignment.
- Do use compact controls when the workflow demands efficiency.

### Don't
- Do not make Fluent screens overly playful, bubbly, or consumer-social.
- Do not use oversized shadows or high-gloss surfaces.
- Do not hide state changes behind subtle color-only differences.
- Do not over-brand the shell when the product task should dominate.
- Do not replace standard productivity components with experimental shapes.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Fluent patterns offer a clear stateful control.
