# Human Interface Guidelines DESIGN.md

## Overview
Use this specification for interfaces that should feel native to Apple platforms. Favor clarity, restraint, familiar controls, and layouts that defer to content rather than brand-heavy UI treatment.

- **Provider:** Apple
- **Primary reference:** https://developer.apple.com/design/human-interface-guidelines/
- **Primary product focus:** Apple platform apps
- **Platforms:** Web: Yes | Safari/web adaptation | iOS: Yes | iPhone and iPad native | Android: N/A | Apple-only guidance | Desktop: Yes | macOS specific
- **Status:** Active | continuously updated by Apple
- **Reference note:** Use this file as the design-system reference for visual language, components, and layout decisions.

### Design Principles
- Prioritize clarity in labels, icon use, and overall navigation structure.
- Let content lead; interface chrome should support, not dominate.
- Use native metaphors and control behavior whenever possible.
- Adjust layout, spacing, and control treatment by platform family.
- Keep motion and depth subtle and platform-consistent.

### Content & Accessibility
- Use concise, human labels and avoid jargon-heavy control text.
- Preserve dynamic type scalability and comfortable tap targets.
- Use semantic colors, not raw brand colors, for status whenever possible.
- Ensure controls read as native and predictable to VoiceOver users.
- Keep destructive actions explicit and visually separated from safe actions.

- **Accessibility note:** Strong | built into platform guidance
- **Content note:** Writing guidance included
- **Internationalization note:** Localization guidance across locales
- **Localization / RTL note:** Strong | locale-aware Apple controls
- **Validation note:** System alerts and validation via native controls
- **State model note:** Standard control states via platform behaviors
- **Privacy / trust note:** Privacy is a platform concern

### Official Sources
- https://developer.apple.com/design/human-interface-guidelines/
- https://developer.apple.com/design/human-interface-guidelines/color
- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/layout
- https://developer.apple.com/design/human-interface-guidelines/controls

## Colors
Representative Apple system palette for generation. Use semantic system colors in implementation; these hex values are representative.

- **System Blue `#007AFF`:** Primary action color and interactive emphasis.
- **System Green `#34C759`:** Success and positive confirmation.
- **System Orange `#FF9500`:** Caution and intermediate attention.
- **System Red `#FF3B30`:** Destructive actions and errors.
- **Background `#FFFFFF`:** Primary light background.
- **Secondary Background `#F2F2F7`:** Grouped backgrounds and panels.
- **Label `#1C1C1E`:** Primary text color on light surfaces.
- **Separator `#C6C6C8`:** Dividers and low-emphasis strokes.

- **Dark mode guidance:** Strong | system dark mode guidance
- **Theming guidance:** Medium | platform appearance customization
- **Semantic token guidance:** Implicit via platform APIs and metrics

## Typography
- Use San Francisco as the primary typeface.
- Use Apple-style text roles rather than inventing a custom display system.
- Favor strong readability, generous line height, and restrained weight changes.
- Use platform-standard text styles for titles, body content, captions, and controls.
- Keep uppercase labels rare and functional.

- **Official typography note:** SF typography and text styles
- **Iconography:** SF Symbols and app icons
- **Motion direction:** Animation guidance by platform

## Elevation
- Use platform-native spacing and alignment; prioritize optical balance over a rigid visible grid.
- Use rounded rectangles and materials that align with the target Apple platform.
- Use blur, translucency, and depth only in platform-native ways.
- Keep shadows subtle; depth should feel systemic rather than decorative.

- **Spacing system note:** System spacing through platform metrics
- **Radius / shape note:** Rounded rect conventions by platform
- **Elevation / shadow note:** Depth through materials and blur

## Components
### Navigation Rules
- Use tab bars for a small number of top-level destinations on iPhone.
- Use sidebars and split views for iPadOS and macOS information architecture.
- Use back navigation and hierarchical drill-in patterns when content is naturally nested.
- Avoid mixing too many navigation metaphors in one screen.

- **Official navigation note:** Tab bars, sidebars, split views
- **Pattern note:** Sidebar, tab bar, navigation split

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** System button styles
- **Preferred style:** Prefer native filled or bordered button treatments and segmented controls that match Apple platform conventions.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#1C1C1E]">
  <button class="inline-flex h-11 items-center justify-center rounded-xl bg-[#007AFF] px-4 text-sm font-medium text-white shadow-sm">Continue</button>
  <button class="inline-flex h-11 items-center justify-center rounded-xl border border-[#C6C6C8] bg-[#FFFFFF] px-4 text-sm font-medium text-[#1C1C1E]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Text fields follow platform controls
- **Preferred style:** Use clean native text fields with visible labels when needed and subtle container styling.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1C1C1E]">
  <span class="font-medium">Project name</span>
  <input class="h-11 rounded-xl border border-[#C6C6C8] bg-[#FFFFFF] px-4 text-sm text-[#1C1C1E] outline-none focus:border-[#007AFF] focus:ring-2 focus:ring-[#8EC5FF]" value="North star workspace" />
  <span class="text-xs text-[#636366]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Menus, pickers, pop-up buttons
- **Preferred style:** Use native menus, pop-up buttons, and pickers rather than heavily customized dropdowns.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1C1C1E]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-11 w-full appearance-none rounded-xl border border-[#C6C6C8] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#1C1C1E] outline-none focus:border-[#007AFF] focus:ring-2 focus:ring-[#8EC5FF]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#636366]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use platform-native checkboxes, radio-like selections, and switches with familiar spacing and behavior.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#1C1C1E]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#C6C6C8] text-[#007AFF] focus:ring-[#8EC5FF]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#636366]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio buttons
- **Preferred style:** Use platform-native checkboxes, radio-like selections, and switches with familiar spacing and behavior.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#1C1C1E]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#C6C6C8] text-[#007AFF] focus:ring-[#8EC5FF]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#C6C6C8] text-[#007AFF] focus:ring-[#8EC5FF]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Toggle controls
- **Preferred style:** Use platform-native checkboxes, radio-like selections, and switches with familiar spacing and behavior.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F2F2F7] p-3 text-sm text-[#1C1C1E]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#636366]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#007AFF]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** DatePicker and system pickers
- **Preferred style:** Use native date pickers, wheels, calendars, or compact pickers according to platform context.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#1C1C1E] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-11 rounded-xl border border-[#C6C6C8] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#007AFF] focus:ring-2 focus:ring-[#8EC5FF]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-11 rounded-xl border border-[#C6C6C8] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#007AFF] focus:ring-2 focus:ring-[#8EC5FF]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Search field
- **Preferred style:** Use the native search field pattern integrated into the relevant container.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#1C1C1E]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#636366]">⌕</span>
  <input class="h-11 w-full rounded-xl border border-[#C6C6C8] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#007AFF] focus:ring-2 focus:ring-[#8EC5FF]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** Menus and pop-up menus
- **Preferred style:** Use menus and context menus that feel native and lightweight.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-[20px] border border-[#C6C6C8] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1C1C1E] hover:bg-[#F2F2F7]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1C1C1E] hover:bg-[#F2F2F7]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#FF3B30] hover:bg-[#F2F2F7]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** Tab views
- **Preferred style:** Use tab bars or segmented controls depending on whether the switch is global or local.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#C6C6C8] text-sm text-[#636366]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#007AFF] px-3 font-medium text-[#1C1C1E]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-full bg-[#F2F2F7] px-3 hover:text-[#1C1C1E]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#1C1C1E]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Path controls where appropriate
- **Preferred style:** Use path-like navigation only where the platform supports it; otherwise prefer sidebars, back navigation, or split views.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#636366]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#1C1C1E]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#1C1C1E]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#1C1C1E]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Navigation bars and toolbars
- **Preferred style:** Use restrained navigation bars, toolbars, or title areas with minimal visual noise. Translucent or material-based headers are acceptable when they match Apple platform conventions, but they should still read as native system chrome rather than decorative blur.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#C6C6C8] bg-[#FFFFFF] px-5 py-4 text-[#1C1C1E]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#636366]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-11 items-center justify-center rounded-xl bg-[#007AFF] px-4 text-sm font-medium text-white">Continue</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Sidebar and split view
- **Preferred style:** Use sidebars and split views instead of generic web-style drawers whenever possible.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-[20px] border border-[#C6C6C8] bg-[#FFFFFF] p-3 text-sm text-[#636366]">
  <a class="rounded-md bg-[#F2F2F7] px-3 py-2 font-medium text-[#1C1C1E]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F2F2F7] hover:text-[#1C1C1E]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F2F2F7] hover:text-[#1C1C1E]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Cards and collections
- **Preferred style:** Use grouped panels or inset sections before introducing generic cards.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-[20px] border border-[#C6C6C8] bg-[#FFFFFF] p-5 text-[#1C1C1E] shadow-sm">
  <p class="text-xs text-[#636366]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#636366]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#007AFF]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Table / outline views via platform
- **Preferred style:** Use clean tables or outline views with strong text alignment and little decoration.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-[20px] border border-[#C6C6C8] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#1C1C1E]">
    <thead class="bg-[#F2F2F7] text-xs uppercase tracking-[0.08em] text-[#636366]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#C6C6C8]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#34C759]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#C6C6C8]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#636366]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List and collection views
- **Preferred style:** Use lists and collections with platform-native spacing and separators.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#C6C6C8] rounded-[20px] border border-[#C6C6C8] bg-[#FFFFFF] text-sm text-[#1C1C1E]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#636366]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#636366]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge-like labels
- **Preferred style:** Use badges and status labels sparingly and semantically.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-xl bg-[#F2F2F7] px-3 py-1 text-xs font-semibold text-[#007AFF]">Active</span>
```

### Tooltip
- **Official naming / aliases:** Tooltips
- **Preferred style:** Use tooltips as supplemental help, especially on desktop.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#1C1C1E]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#C6C6C8] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-xl bg-[#1C1C1E] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Sheets and alerts
- **Preferred style:** Use alerts, sheets, and popovers with native structure and concise decisions.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-[20px] bg-[#FFFFFF] p-6 text-[#1C1C1E] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#636366]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-11 items-center justify-center rounded-xl border border-[#C6C6C8] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-11 items-center justify-center rounded-xl bg-[#FF3B30] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Transient alerts
- **Preferred style:** Use transient feedback sparingly and in platform-native ways.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-[20px] border border-[#C6C6C8] bg-[#FFFFFF] px-4 py-3 text-sm text-[#1C1C1E] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#34C759]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#636366]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Progress indicators
- **Preferred style:** Use native progress bars, spinners, and activity indicators.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#1C1C1E]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#636366]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F2F2F7]">
    <div class="h-full w-[64%] bg-[#007AFF]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination where desktop fits
- **Preferred style:** Use pagination rarely; prefer content grouping, search, or hierarchical drill-in.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#1C1C1E]">
  <button class="inline-flex h-9 items-center justify-center rounded-xl border border-[#C6C6C8] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-xl bg-[#007AFF] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-xl border border-[#C6C6C8]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-xl border border-[#C6C6C8] px-3">Next</button>
</nav>
```

### Layout Rules
- Use platform-appropriate containers such as split views, sidebars, tab bars, toolbars, and sheets.
- Respect safe areas, title regions, and expected control placement for each platform.
- Use grouped sections and inset panels where native patterns call for them.
- Avoid over-dense enterprise layouts unless the app category clearly supports them.
- When generating for macOS, allow more persistent side navigation and toolbar actions than on iPhone.

- **Official layout note:** Platform layout and safe-area guidance
- **Responsive behavior:** Canonical adaptations by device
- **App structure:** Tab bars, split views, sidebars
- **Data display guidance:** Charts available in platform frameworks

### Screen Generation Heuristics
- **Default page structure:** Use content-first structure with native headers, grouped sections, and platform-appropriate sidebars or tab bars.
- **Default density:** Use comfortable density. Let breathing room and legibility outweigh data compression.
- **Default navigation model:** Use tab bars, sidebars, toolbars, split views, and sheets according to Apple platform conventions.
- **Behavior-to-UI expectation:** This design system expects behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions to appear as controls or selected states rather than literal text.
- **Preferred form composition:** Use clearly grouped fields, native pickers, and conservative validation messaging.
- **Preferred feedback pattern:** Use alerts, banners, inline validation, and native transient feedback sparingly.
- **Preferred data-display pattern:** Use lists, collections, and tables that prioritize readability over operational density.
- **Prompt bias:** Use prompts such as 'native iOS settings screen', 'macOS sidebar detail view', 'SF Symbols', and 'content-first Apple UI'.
- **Component naming consistency:** Medium | native names differ by platform
- **Layout rule explicitness:** High | device-specific rules are explicit
- **Theme describability:** Medium | appearance follows system settings
- **Prompt-to-UI suitability:** Medium | best when prompt targets Apple platforms

## Do's and Don'ts
### Do
- Do prefer native controls and familiar Apple patterns.
- Do keep chrome quiet and let content carry the screen.
- Do use system colors and typography roles before introducing custom branding.
- Do adapt layouts by platform family rather than forcing one universal shell.
- Do use SF Symbols for interface iconography when possible.

### Don't
- Do not add non-native ornamentation, loud shadows, or novelty gradients.
- Do not force Material- or enterprise-style app shells onto Apple screens.
- Do not crowd the screen with multiple simultaneous emphasis patterns.
- Do not replace native segmented controls, sheets, or menus with bespoke alternatives without reason.
- Do not use over-branded buttons or aggressively custom form fields.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when native controls should carry the state.
