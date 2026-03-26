# Primer Product UI DESIGN.md

## Overview
Use this specification for GitHub-like product interfaces, developer tools, settings surfaces, and workflow-oriented applications. Favor utility, clarity, and quiet but strong structure.

- **Provider:** GitHub
- **Primary reference:** https://primer.style/product
- **Primary product focus:** GitHub product interfaces
- **Platforms:** Web: Yes | GitHub web app UI | iOS: Limited | not primary target | Android: N/A | not Android-native guidance | Desktop: Yes | desktop-heavy workflows
- **Status:** Active | GitHub maintained
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Let product utility and content hierarchy drive the screen.
- Use primitives and semantic variables to keep the interface systematic.
- Keep styling understated and developer-tool practical.
- Support both dense data and comfortable readability.
- Use component naming and layout patterns that feel familiar to serious software products.

### Content & Accessibility
- Use clear technical language and avoid ambiguous marketing copy in product screens.
- Maintain strong focus treatment and keyboard navigability.
- Use icons to support labels and status, not replace readable text.
- Keep error and help copy concise and task-oriented.
- Use code or monospace treatment only where semantics justify it.

- **Accessibility note:** Strong | component-level accessibility docs
- **Content note:** Copy and UX writing within patterns
- **Internationalization note:** Global GitHub product support
- **Localization / RTL note:** Limited | GitHub product focus
- **Validation note:** FormControl validation and flash messages
- **State model note:** Default/hover/disabled/focus documented
- **Privacy / trust note:** GitHub trust and security context

### Official Sources
- https://primer.style/product
- https://primer.style/product/primitives/color
- https://primer.style/product/primitives/typography
- https://primer.style/product/components/page-layout
- https://primer.style/product/components

## Colors
Representative Primer palette for generation based on current product UI primitives. Use variables in implementation; these hex values are representative.

- **Accent `#0969DA`:** Primary interactive emphasis and link/action color.
- **Success `#1F883D`:** Success and positive state.
- **Attention `#9A6700`:** Warning and needs-attention emphasis.
- **Danger `#CF222E`:** Error and destructive emphasis.
- **Canvas Default `#FFFFFF`:** Primary page background.
- **Canvas Subtle `#F6F8FA`:** Muted panels and section backgrounds.
- **Foreground Default `#1F2328`:** Primary text and icon color.
- **Border Default `#D0D7DE`:** Borders, table dividers, and field boundaries.

- **Dark mode guidance:** Strong | color modes through primitives
- **Theming guidance:** High | CSS variables and theme support
- **Semantic token guidance:** Strong | primitives for color, space, type

## Typography
- Use a neutral system sans stack appropriate for developer products.
- Keep headings functional and direct.
- Use monospace only for code, data snippets, and strongly technical labels.
- Preserve readable density in settings pages, forms, and table-like lists.
- Use weight changes modestly and let layout provide most hierarchy.

- **Official typography note:** Text styles and Primer primitives
- **Iconography:** Octicons
- **Motion direction:** Animation utilities minimal

## Elevation
- Use a disciplined spacing scale with practical compactness.
- Use small-to-moderate radii and restrained shadows.
- Prefer borders, muted surfaces, and layout grouping over rich card effects.
- Keep row height, field spacing, and action spacing highly consistent.

- **Spacing system note:** Space primitives
- **Radius / shape note:** Border radius primitives
- **Elevation / shadow note:** Box-shadow tokens limited but present

## Components
### Navigation Rules
- Use side nav, underline nav, and page-local patterns for clear product orientation.
- Use breadcrumbs only when nested hierarchy is genuinely helpful.
- Use tabs for sibling views and segmented content regions.
- Keep top-level navigation restrained and utility-first.

- **Official navigation note:** NavList, UnderlineNav, side nav patterns
- **Pattern note:** NavList, UnderlineNav, breadcrumbs

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer restrained button hierarchy with clear primary emphasis and quiet secondary actions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#1F2328]">
  <button class="inline-flex h-9 items-center justify-center rounded-md bg-[#0969DA] px-4 text-sm font-medium text-white shadow-sm">Merge pull request</button>
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#D0D7DE] bg-[#FFFFFF] px-4 text-sm font-medium text-[#1F2328]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** TextInput
- **Preferred style:** Use practical text inputs with visible labels, concise help, and strong keyboard/focus support.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1F2328]">
  <span class="font-medium">Project name</span>
  <input class="h-9 rounded-md border border-[#D0D7DE] bg-[#FFFFFF] px-4 text-sm text-[#1F2328] outline-none focus:border-[#0969DA] focus:ring-2 focus:ring-[#54AEFF]" value="North star workspace" />
  <span class="text-xs text-[#57606A]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Select, SelectPanel, autocomplete-like patterns
- **Preferred style:** Use selects and select panels that fit settings and workflow contexts rather than decorative dropdowns.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1F2328]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-9 w-full appearance-none rounded-md border border-[#D0D7DE] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#1F2328] outline-none focus:border-[#0969DA] focus:ring-2 focus:ring-[#54AEFF]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#57606A]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use straightforward choice controls with explicit labels and compact spacing.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#1F2328]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#D0D7DE] text-[#0969DA] focus:ring-[#54AEFF]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#57606A]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio / RadioGroup
- **Preferred style:** Use straightforward choice controls with explicit labels and compact spacing.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#1F2328]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#D0D7DE] text-[#0969DA] focus:ring-[#54AEFF]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#D0D7DE] text-[#0969DA] focus:ring-[#54AEFF]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** ToggleSwitch
- **Preferred style:** Use straightforward choice controls with explicit labels and compact spacing.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F6F8FA] p-3 text-sm text-[#1F2328]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#57606A]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#0969DA]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** DatePicker relative time patterns
- **Preferred style:** Use date-related inputs when needed, styled to match a practical product surface.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#1F2328] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-9 rounded-md border border-[#D0D7DE] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0969DA] focus:ring-2 focus:ring-[#54AEFF]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-9 rounded-md border border-[#D0D7DE] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0969DA] focus:ring-2 focus:ring-[#54AEFF]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** TextInput and command/search patterns
- **Preferred style:** Use search as a strong utility tool in headers, filters, and content lists.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#1F2328]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#57606A]">⌕</span>
  <input class="h-9 w-full rounded-md border border-[#D0D7DE] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#0969DA] focus:ring-2 focus:ring-[#54AEFF]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** ActionMenu and menu patterns
- **Preferred style:** Use action menus and compact menus for contextual operations.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-xl border border-[#D0D7DE] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1F2328] hover:bg-[#F6F8FA]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1F2328] hover:bg-[#F6F8FA]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#CF222E] hover:bg-[#F6F8FA]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** UnderlineNav / tabs
- **Preferred style:** Use underline-style tabs or related navigation for sibling views.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#D0D7DE] text-sm text-[#57606A]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#0969DA] px-3 font-medium text-[#1F2328]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-t-md bg-[#FFFFFF] px-3 hover:text-[#1F2328]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#1F2328]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs conservatively in nested product structures.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#57606A]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#1F2328]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#1F2328]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#1F2328]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** PageHeader / header primitives
- **Preferred style:** Use practical page headers with clear title, metadata, and nearby actions.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#D0D7DE] bg-[#F6F8FA] px-5 py-4 text-[#1F2328]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#57606A]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-9 items-center justify-center rounded-md bg-[#0969DA] px-4 text-sm font-medium text-white">Merge pull request</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** NavList / side nav
- **Preferred style:** Use side nav for durable product orientation in larger tools and settings areas.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-xl border border-[#D0D7DE] bg-[#FFFFFF] p-3 text-sm text-[#57606A]">
  <a class="rounded-md bg-[#F6F8FA] px-3 py-2 font-medium text-[#1F2328]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F6F8FA] hover:text-[#1F2328]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F6F8FA] hover:text-[#1F2328]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards and muted panels to organize content without making the interface feel soft.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-xl border border-[#D0D7DE] bg-[#FFFFFF] p-5 text-[#1F2328] shadow-sm">
  <p class="text-xs text-[#57606A]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#57606A]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#0969DA]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** DataTable / table patterns
- **Preferred style:** Use data tables and structured rows where developers or operators need quick scanning.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-xl border border-[#D0D7DE] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#1F2328]">
    <thead class="bg-[#F6F8FA] text-xs uppercase tracking-[0.08em] text-[#57606A]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#D0D7DE]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#1F883D]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#D0D7DE]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#57606A]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** ActionList / list
- **Preferred style:** Use action lists and metadata-rich rows for flexible workflow presentation.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#D0D7DE] rounded-xl border border-[#D0D7DE] bg-[#FFFFFF] text-sm text-[#1F2328]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#57606A]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#57606A]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Label / Counter
- **Preferred style:** Use labels, counters, and tokens to communicate state and categorization clearly.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-md bg-[#F6F8FA] px-3 py-1 text-xs font-semibold text-[#0969DA]">Beta</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips to support dense interfaces, not to compensate for vague labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#1F2328]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#D0D7DE] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-md bg-[#1F2328] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Dialog
- **Preferred style:** Use dialogs and overlays for focused decisions and secondary tasks.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-xl bg-[#FFFFFF] p-6 text-[#1F2328] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#57606A]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#D0D7DE] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-9 items-center justify-center rounded-md bg-[#CF222E] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Flash / toast-like feedback
- **Preferred style:** Use flash-like transient messaging that stays practical and unobtrusive.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-xl border border-[#D0D7DE] bg-[#FFFFFF] px-4 py-3 text-sm text-[#1F2328] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#1F883D]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#57606A]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Spinner, skeleton, progress
- **Preferred style:** Use spinners, skeletons, and progress bars in a quiet utility style.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#1F2328]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#57606A]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F6F8FA]">
    <div class="h-full w-[64%] bg-[#0969DA]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination when large result sets need explicit chunking and orientation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#1F2328]">
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#D0D7DE] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md bg-[#0969DA] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md border border-[#D0D7DE]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#D0D7DE] px-3">Next</button>
</nav>
```

### Layout Rules
- Use page layouts with clear header, side navigation, and content hierarchy when the product area is complex.
- Support split layouts, settings pages, and repository-style information density.
- Use sections, subheaders, and muted containers to organize complex screens.
- Keep actions near the data or task they affect.
- Favor compact clarity over ornamental whitespace.

- **Official layout note:** Layout primitives and page patterns
- **Responsive behavior:** Responsive layouts for GitHub pages
- **App structure:** Page layouts for product workflows
- **Data display guidance:** Data-rich GitHub tables more than charts

### Screen Generation Heuristics
- **Default page structure:** Use a utility-first product page with a clear title, optional side navigation, explicit section grouping, and practical action placement.
- **Default density:** Use medium density with compact tendencies for settings and tool screens.
- **Default navigation model:** Use side navigation, underline nav, tabs, and page headers for strong orientation.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use clearly labeled fields, concise help text, and practical action groups.
- **Preferred feedback pattern:** Use banners, flash messages, inline validation, and dialogs only when blocking is justified.
- **Preferred data-display pattern:** Use lists, tables, cards, and timelines in a calm, utility-first way.
- **Prompt bias:** Use prompts such as 'GitHub product settings page', 'Primer side nav', 'muted borders', and 'developer tool UI'.
- **Component naming consistency:** High | standard product UI names
- **Layout rule explicitness:** High | layout primitives and page patterns explicit
- **Theme describability:** High | color modes and primitives are clear
- **Prompt-to-UI suitability:** High | excellent for repository/productivity screens

## Do's and Don'ts
### Do
- Do make the UI feel practical, reliable, and developer-friendly.
- Do use muted surfaces, borders, and strong alignment to manage complexity.
- Do use components and primitives consistently across settings and workflows.
- Do keep navigation and metadata explicit.
- Do let content and action structure drive the page.

### Don't
- Do not turn Primer screens into glossy marketing pages or soft consumer dashboards.
- Do not overuse large shadows, loud gradients, or decorative illustrations.
- Do not hide important settings and actions behind ambiguous icon-only patterns.
- Do not over-round containers or use whimsical control styling.
- Do not replace practical lists and tables with over-carded layouts without reason.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Primer patterns offer a clear stateful control.
