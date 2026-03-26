# Ant Design DESIGN.md

## Overview
Use this specification for enterprise web applications, dashboards, and internal tools. Favor information density, broad component coverage, predictable grids, and direct administrative workflows.

- **Provider:** Ant Group
- **Primary reference:** https://ant.design/
- **Primary product focus:** Enterprise web applications
- **Platforms:** Web: Yes | primary target | iOS: Limited | Ant Design Mobile exists | Android: Limited | Ant Design Mobile exists | Desktop: Yes | enterprise desktop web
- **Status:** Active | v5 current
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Design for efficient task completion in data-heavy environments.
- Use strong grid alignment and a clear page shell.
- Let components solve operational tasks directly.
- Keep theming systematic and algorithmic rather than handcrafted per screen.
- Support broad form, table, and filtering workflows.

### Content & Accessibility
- Use direct labels, placeholders only as hints, and strong field-level validation.
- Preserve clear hover, active, selected, disabled, and error states.
- Support RTL and localization-aware layout decisions.
- Use messages, notifications, and status color consistently.
- Keep icon usage secondary to readable labels.

- **Accessibility note:** Strong | WCAG-oriented component guidance
- **Content note:** Writing for enterprise flows
- **Internationalization note:** Internationalization support in components
- **Localization / RTL note:** Strong | direction and locale support in components
- **Validation note:** Status and feedback patterns strong
- **State model note:** Common control states standardized
- **Privacy / trust note:** Enterprise admin trust patterns

### Official Sources
- https://ant.design/
- https://ant.design/docs/spec/introduce
- https://ant.design/docs/spec/colors
- https://ant.design/docs/spec/font
- https://ant.design/components/overview

## Colors
Representative Ant Design palette for generation based on v5 semantics and common product usage. Use official token algorithms in implementation; these values are representative.

- **Primary `#1677FF`:** Primary action and active interactive emphasis.
- **Success `#52C41A`:** Success and positive status.
- **Warning `#FAAD14`:** Caution and intermediate attention.
- **Error `#FF4D4F`:** Errors and destructive emphasis.
- **Text `#1F1F1F`:** Primary text on light surfaces.
- **Background `#FFFFFF`:** Primary application surface.
- **Container `#F5F5F5`:** Low-emphasis panels and section surfaces.
- **Border `#D9D9D9`:** Input, table, and container borders.

- **Dark mode guidance:** Strong | algorithmic dark themes
- **Theming guidance:** High | seed tokens and algorithms
- **Semantic token guidance:** Strong | seed, map, alias tokens

## Typography
- Use a neutral enterprise sans stack, typically with system sans defaults.
- Keep hierarchy pragmatic and compact.
- Use page titles, section titles, body text, and compact control text without excessive variation.
- Favor dense tables and forms with readable but not loose line height.
- Use medium emphasis for buttons, labels, and data headers.

- **Official typography note:** Typography scale for enterprise UI
- **Iconography:** Ant Design Icons ecosystem
- **Motion direction:** Motion principles less central

## Elevation
- Use a clear grid system and regular panel spacing.
- Use moderate radii and avoid overly soft consumer rounded surfaces.
- Use shadows when surfacing overlays, drawers, and cards, but keep them utilitarian.
- Keep field spacing compact and consistent across form sections.

- **Spacing system note:** Spacing grid and spacing tokens
- **Radius / shape note:** Radius tokens and algorithm
- **Elevation / shadow note:** Shadows for layered surfaces

## Components
### Navigation Rules
- Use top navigation, side navigation, or a hybrid application shell for enterprise apps.
- Use tabs and steps for local workflow segmentation.
- Use breadcrumbs in deep admin structures and nested settings areas.
- Keep nav labels literal and easy to scan.

- **Official navigation note:** Navigation specs for enterprise apps
- **Pattern note:** Top nav, side nav, steps

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button with variants
- **Preferred style:** Prefer clear primary, default, dashed, text, and link hierarchies suited to enterprise tasks.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#1F1F1F]">
  <button class="inline-flex h-10 items-center justify-center rounded-lg bg-[#1677FF] px-4 text-sm font-medium text-white shadow-sm">Create project</button>
  <button class="inline-flex h-10 items-center justify-center rounded-lg border border-[#D9D9D9] bg-[#FFFFFF] px-4 text-sm font-medium text-[#1F1F1F]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Input
- **Preferred style:** Use compact but readable inputs with explicit labels and strong status borders.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1F1F1F]">
  <span class="font-medium">Project name</span>
  <input class="h-10 rounded-lg border border-[#D9D9D9] bg-[#FFFFFF] px-4 text-sm text-[#1F1F1F] outline-none focus:border-[#1677FF] focus:ring-2 focus:ring-[#91Caff]" value="North star workspace" />
  <span class="text-xs text-[#595959]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Select, Cascader, AutoComplete
- **Preferred style:** Use selects, cascaders, autocompletes, and searchable dropdowns to handle complex choice sets.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1F1F1F]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-10 w-full appearance-none rounded-lg border border-[#D9D9D9] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#1F1F1F] outline-none focus:border-[#1677FF] focus:ring-2 focus:ring-[#91Caff]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#595959]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use straightforward choice controls that integrate cleanly into filter bars and forms.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#1F1F1F]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#D9D9D9] text-[#1677FF] focus:ring-[#91Caff]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#595959]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use straightforward choice controls that integrate cleanly into filter bars and forms.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#1F1F1F]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#D9D9D9] text-[#1677FF] focus:ring-[#91Caff]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#D9D9D9] text-[#1677FF] focus:ring-[#91Caff]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use straightforward choice controls that integrate cleanly into filter bars and forms.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F5F5F5] p-3 text-sm text-[#1F1F1F]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#595959]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#1677FF]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** DatePicker, TimePicker, Calendar
- **Preferred style:** Use date and time pickers that fit dense filter and scheduling workflows.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#1F1F1F] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-10 rounded-lg border border-[#D9D9D9] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#1677FF] focus:ring-2 focus:ring-[#91Caff]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-10 rounded-lg border border-[#D9D9D9] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#1677FF] focus:ring-2 focus:ring-[#91Caff]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Input.Search
- **Preferred style:** Use search inputs as part of table filters, toolbars, and management headers.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#1F1F1F]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#595959]">⌕</span>
  <input class="h-10 w-full rounded-lg border border-[#D9D9D9] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#1677FF] focus:ring-2 focus:ring-[#91Caff]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** Menu, Dropdown
- **Preferred style:** Use menus and dropdowns with practical grouping and little visual flourish.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-xl border border-[#D9D9D9] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1F1F1F] hover:bg-[#F5F5F5]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1F1F1F] hover:bg-[#F5F5F5]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#FF4D4F] hover:bg-[#F5F5F5]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs for local task segmentation and steps for process-based flows.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#D9D9D9] text-sm text-[#595959]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#1677FF] px-3 font-medium text-[#1F1F1F]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-t-lg bg-[#FFFFFF] px-3 hover:text-[#1F1F1F]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#1F1F1F]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs to anchor the user in deep administrative IA.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#595959]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#1F1F1F]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#1F1F1F]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#1F1F1F]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Layout.Header / page header
- **Preferred style:** Use practical page headers with title, metadata, actions, and optional breadcrumb context. Prefer solid fills and clear borders over translucent or frosted glass effects.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions. Avoid using blur or translucency as the default header treatment.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#D9D9D9] bg-[#FFFFFF] px-5 py-4 text-[#1F1F1F]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#595959]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-10 items-center justify-center rounded-lg bg-[#1677FF] px-4 text-sm font-medium text-white">Create project</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Drawer and sider
- **Preferred style:** Use sider navigation for persistent application structure on desktop.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-xl border border-[#D9D9D9] bg-[#FFFFFF] p-3 text-sm text-[#595959]">
  <a class="rounded-md bg-[#F5F5F5] px-3 py-2 font-medium text-[#1F1F1F]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F5F5] hover:text-[#1F1F1F]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F5F5] hover:text-[#1F1F1F]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards to modularize dashboards and related information groups.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-xl border border-[#D9D9D9] bg-[#FFFFFF] p-5 text-[#1F1F1F] shadow-sm">
  <p class="text-xs text-[#595959]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#595959]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#1677FF]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use data tables as a first-class pattern with filters, row actions, and status tags.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-xl border border-[#D9D9D9] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#1F1F1F]">
    <thead class="bg-[#F5F5F5] text-xs uppercase tracking-[0.08em] text-[#595959]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#D9D9D9]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#52C41A]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#D9D9D9]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#595959]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists when the data is lighter-weight than a table or needs more flexible row content.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#D9D9D9] rounded-xl border border-[#D9D9D9] bg-[#FFFFFF] text-sm text-[#1F1F1F]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#595959]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#595959]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and tags for state, count, and categorization.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-lg bg-[#F5F5F5] px-3 py-1 text-xs font-semibold text-[#1677FF]">Active</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips to clarify dense controls or truncated labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#1F1F1F]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#D9D9D9] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-lg bg-[#1F1F1F] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Modal
- **Preferred style:** Use modals, drawers, and popconfirms for interruptive actions and secondary tasks.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-xl bg-[#FFFFFF] p-6 text-[#1F1F1F] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#595959]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-10 items-center justify-center rounded-lg border border-[#D9D9D9] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-10 items-center justify-center rounded-lg bg-[#FF4D4F] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Message / notification
- **Preferred style:** Use message and notification patterns for transient or global feedback.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-xl border border-[#D9D9D9] bg-[#FFFFFF] px-4 py-3 text-sm text-[#1F1F1F] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#52C41A]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#595959]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Progress, Spin, Skeleton
- **Preferred style:** Use progress bars, spinners, and skeletons to keep busy states explicit in dense screens.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#1F1F1F]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#595959]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F5F5F5]">
    <div class="h-full w-[64%] bg-[#1677FF]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination heavily in tables and long administrative collections.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#1F1F1F]">
  <button class="inline-flex h-9 items-center justify-center rounded-lg border border-[#D9D9D9] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-lg bg-[#1677FF] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-[#D9D9D9]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-lg border border-[#D9D9D9] px-3">Next</button>
</nav>
```

### Layout Rules
- Use a dashboard or management shell with header, sider, and content regions when appropriate.
- Support dense table, filter, and form areas without collapsing hierarchy.
- Use cards and sections to organize related modules in larger screens.
- Keep admin workflows explicit through action bars, filters, and summaries.
- Prefer operational symmetry over expressive composition.

- **Official layout note:** Grid and layout spec
- **Responsive behavior:** Responsive grid and mobile variants
- **App structure:** Dashboard and management app structure
- **Data display guidance:** Ant Design Charts ecosystem

### Screen Generation Heuristics
- **Default page structure:** Use a management shell with optional sider, page header, filter region, and structured content blocks.
- **Default density:** Use medium-to-dense density by default.
- **Default navigation model:** Use top nav, sider, tabs, steps, and breadcrumbs depending on workflow depth.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use labeled fields, sectioned forms, inline validation, and clear submit/cancel actions.
- **Preferred feedback pattern:** Use message, notification, result, and modal patterns according to urgency.
- **Preferred data-display pattern:** Use tables, cards, lists, statistics, and charts with explicit filters and sorting.
- **Prompt bias:** Use prompts such as 'Ant Design admin dashboard', 'sider layout', 'dense enterprise table', and 'algorithmic token theme'.
- **Component naming consistency:** High | common web component names
- **Layout rule explicitness:** Medium | layout principles are broad
- **Theme describability:** High | algorithmic themes are easy to describe
- **Prompt-to-UI suitability:** High | rich web components for admin UIs

## Do's and Don'ts
### Do
- Do lean into the system's broad component coverage for enterprise tasks.
- Do use tables, filters, forms, and cards as primary building blocks.
- Do keep layouts structured and operational.
- Do use algorithmic theming rather than ad hoc color decisions.
- Do make workflow state obvious through status, tags, and notifications.

### Don't
- Do not style Ant screens like soft consumer landing pages.
- Do not overuse illustrations, gradients, or playful decorative surfaces.
- Do not create huge whitespace gaps that weaken dashboard scanability.
- Do not replace straightforward controls with overly bespoke alternatives.
- Do not bury key filters and table actions behind excessive nesting.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Ant patterns offer a clear stateful control.
