# Lightning Design System DESIGN.md

## Overview
Use this specification for CRM-style, record-centric business applications. Favor structured record pages, clear utility navigation, explicit statuses, and forms or tables that support object-heavy workflows.

- **Provider:** Salesforce
- **Primary reference:** https://v1.lightningdesignsystem.com/
- **Primary product focus:** Salesforce application UI
- **Platforms:** Web: Yes | responsive enterprise web | iOS: Limited | Salesforce mobile patterns separate | Android: Limited | mobile web and Salesforce apps | Desktop: Yes | desktop CRM workflows
- **Status:** Active | SLDS 1 public docs
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Design around records, lists, and business-object workflows.
- Keep page regions explicit and consistent.
- Use accessible business UI patterns rather than decorative surfaces.
- Support data-heavy tasks, filtering, and guided action flow.
- Make status and object metadata easy to scan.

### Content & Accessibility
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

### Official Sources
- https://v1.lightningdesignsystem.com/
- https://v1.lightningdesignsystem.com/design-tokens/
- https://v1.lightningdesignsystem.com/utilities/themes/
- https://v1.lightningdesignsystem.com/components/overview/
- https://v1.lightningdesignsystem.com/accessibility/overview/

## Colors
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

## Elevation
- Use utility spacing and region-based composition.
- Use subtle radius values and straightforward enterprise surfaces.
- Use depth sparingly and structurally, especially for overlays and utility panels.
- Keep record pages aligned and compartmentalized.

- **Spacing system note:** Spacing utilities
- **Radius / shape note:** Border radius utilities
- **Elevation / shadow note:** Utility shadows and depth tokens

## Components
### Navigation Rules
- Use global navigation, app launcher patterns, and object-level nav where needed.
- Use tabs within record pages and object areas.
- Use breadcrumbs lightly; object context often comes from shell and page titles.
- Keep utility actions near headers and record highlights.

- **Official navigation note:** Global nav and app launcher blueprints
- **Pattern note:** Global header, app launcher, breadcrumbs

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button blueprint
- **Preferred style:** Prefer direct business-action button hierarchy with clear primary and utility actions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#181818]">
  <button class="inline-flex h-10 items-center justify-center rounded-md bg-[#0176D3] px-4 text-sm font-medium text-white shadow-sm">New lead</button>
  <button class="inline-flex h-10 items-center justify-center rounded-md border border-[#C9C9C9] bg-[#FFFFFF] px-4 text-sm font-medium text-[#181818]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Input
- **Preferred style:** Use explicit enterprise fields with labels, required indicators, and nearby validation.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#181818]">
  <span class="font-medium">Project name</span>
  <input class="h-10 rounded-md border border-[#C9C9C9] bg-[#FFFFFF] px-4 text-sm text-[#181818] outline-none focus:border-[#0176D3] focus:ring-2 focus:ring-[#1B96FF]" value="North star workspace" />
  <span class="text-xs text-[#5C5C5C]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Combobox, picklist
- **Preferred style:** Use comboboxes and picklists for structured object workflows and form completion.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#181818]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-10 w-full appearance-none rounded-md border border-[#C9C9C9] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#181818] outline-none focus:border-[#0176D3] focus:ring-2 focus:ring-[#1B96FF]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#5C5C5C]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use enterprise-friendly selection controls with readable spacing and explicit states.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#181818]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#C9C9C9] text-[#0176D3] focus:ring-[#1B96FF]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#5C5C5C]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio group
- **Preferred style:** Use enterprise-friendly selection controls with readable spacing and explicit states.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#181818]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#C9C9C9] text-[#0176D3] focus:ring-[#1B96FF]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#C9C9C9] text-[#0176D3] focus:ring-[#1B96FF]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Checkbox toggle / switch
- **Preferred style:** Use enterprise-friendly selection controls with readable spacing and explicit states.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F3F3F3] p-3 text-sm text-[#181818]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#5C5C5C]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#0176D3]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** Datepicker, timepicker blueprints
- **Preferred style:** Use date and time controls that work inside record-editing and scheduling flows.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#181818] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-10 rounded-md border border-[#C9C9C9] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0176D3] focus:ring-2 focus:ring-[#1B96FF]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-10 rounded-md border border-[#C9C9C9] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0176D3] focus:ring-2 focus:ring-[#1B96FF]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Global search / lookup
- **Preferred style:** Use global or object-level search fields with strong utility placement.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#181818]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#5C5C5C]">⌕</span>
  <input class="h-10 w-full rounded-md border border-[#C9C9C9] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#0176D3] focus:ring-2 focus:ring-[#1B96FF]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** Menus
- **Preferred style:** Use action menus and utility menus with explicit grouping and object relevance.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-lg border border-[#C9C9C9] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#181818] hover:bg-[#F3F3F3]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#181818] hover:bg-[#F3F3F3]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#BA0517] hover:bg-[#F3F3F3]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs as a core local-navigation pattern inside record and object pages.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#C9C9C9] text-sm text-[#5C5C5C]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#0176D3] px-3 font-medium text-[#181818]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-t-md bg-[#FFFFFF] px-3 hover:text-[#181818]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#181818]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs only where the shell and page context do not already provide sufficient orientation.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#5C5C5C]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#181818]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#181818]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#181818]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Global header
- **Preferred style:** Use object or page headers that surface key metadata and immediate actions. Keep headers as solid enterprise surfaces, not translucent glass bars.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions. Avoid frosted or blurred headers as a default SLDS pattern.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#C9C9C9] bg-[#F3F3F3] px-5 py-4 text-[#181818]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#5C5C5C]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-10 items-center justify-center rounded-md bg-[#0176D3] px-4 text-sm font-medium text-white">New lead</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Global navigation, vertical nav
- **Preferred style:** Use enterprise shell navigation and object context panes instead of consumer drawers.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-lg border border-[#C9C9C9] bg-[#FFFFFF] p-3 text-sm text-[#5C5C5C]">
  <a class="rounded-md bg-[#F3F3F3] px-3 py-2 font-medium text-[#181818]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F3F3F3] hover:text-[#181818]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F3F3F3] hover:text-[#181818]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Cards
- **Preferred style:** Use cards for modular business summaries, but prioritize page-region logic over card galleries.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-lg border border-[#C9C9C9] bg-[#FFFFFF] p-5 text-[#181818] shadow-sm">
  <p class="text-xs text-[#5C5C5C]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#5C5C5C]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#0176D3]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Data table
- **Preferred style:** Use data tables as a core pattern for records, related items, and result sets.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-lg border border-[#C9C9C9] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#181818]">
    <thead class="bg-[#F3F3F3] text-xs uppercase tracking-[0.08em] text-[#5C5C5C]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#C9C9C9]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#2E844A]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#C9C9C9]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#5C5C5C]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List views
- **Preferred style:** Use list views and record rows for object collections and quick scanning.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#C9C9C9] rounded-lg border border-[#C9C9C9] bg-[#FFFFFF] text-sm text-[#181818]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#5C5C5C]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#5C5C5C]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and status indicators to encode record state, object type, or count.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-md bg-[#F3F3F3] px-3 py-1 text-xs font-semibold text-[#0176D3]">Qualified</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips to support compact enterprise controls without replacing clear labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#181818]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#C9C9C9] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-md bg-[#181818] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Modal
- **Preferred style:** Use prompts, modals, and panels for record edits or critical confirmations.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-lg bg-[#FFFFFF] p-6 text-[#181818] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#5C5C5C]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-10 items-center justify-center rounded-md border border-[#C9C9C9] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-10 items-center justify-center rounded-md bg-[#BA0517] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Toast / scoped notification
- **Preferred style:** Use scoped or global notifications for action outcomes and background updates.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-lg border border-[#C9C9C9] bg-[#FFFFFF] px-4 py-3 text-sm text-[#181818] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#2E844A]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#5C5C5C]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Spinners and progress indicators
- **Preferred style:** Use spinners and progress indicators to keep long-running business actions legible.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#181818]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#5C5C5C]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F3F3F3]">
    <div class="h-full w-[64%] bg-[#0176D3]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination in data tables and list views when chunking improves enterprise throughput.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#181818]">
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#C9C9C9] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md bg-[#0176D3] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md border border-[#C9C9C9]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#C9C9C9] px-3">Next</button>
</nav>
```

### Layout Rules
- Use record-page composition with header, highlights panel, tabs, and related lists when appropriate.
- Use utility bars, object actions, and supporting panels for dense workflows.
- Support responsive desktop-first enterprise layouts rather than mobile-social composition.
- Keep filter, table, and form structures explicit and region-based.
- Use blueprint-like page segmentation whenever the workflow benefits from it.

- **Official layout note:** Responsive grid utilities and page regions
- **Responsive behavior:** Responsive and adaptive tags on blueprints
- **App structure:** Record pages and app shell
- **Data display guidance:** Analytics and report UI patterns

### Screen Generation Heuristics
- **Default page structure:** Use an app shell or record-page shell with utility navigation, object header, tabs, and related content regions.
- **Default density:** Use medium-to-dense density with strong business scanability.
- **Default navigation model:** Use global app navigation, object context, tabs, and contextual utility actions.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use sectioned enterprise forms with explicit labels, validation, and record-level actions.
- **Preferred feedback pattern:** Use prompts, scoped notifications, and inline field messaging for business actions.
- **Preferred data-display pattern:** Use data tables, record lists, related lists, and object summaries as primary patterns.
- **Prompt bias:** Use prompts such as 'Salesforce-style record page', 'object highlights panel', 'related list table', and 'SLDS business shell'.
- **Component naming consistency:** Medium | Salesforce-specific names appear
- **Layout rule explicitness:** High | blueprint regions and adaptivity explicit
- **Theme describability:** High | styling hooks describe visual variance
- **Prompt-to-UI suitability:** High | strong for CRM and record-centric screens

## Do's and Don'ts
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
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Lightning patterns offer a clear stateful control.
