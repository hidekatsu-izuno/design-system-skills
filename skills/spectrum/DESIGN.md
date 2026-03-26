# Spectrum DESIGN.md

## Overview
Use this specification for Adobe-style product experiences, creative workflows, and polished application UI. Favor semantic tokens, refined typography, clear workflow containers, and branded but disciplined visual language.

- **Provider:** Adobe
- **Primary reference:** https://spectrum.adobe.com/
- **Primary product focus:** Adobe product and marketing flows
- **Platforms:** Web: Yes | web workflows | iOS: Limited | some mobile web patterns | Android: Limited | not Android-native guidance | Desktop: Yes | desktop creative workflows
- **Status:** Active | Adobe maintained
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

### Design Principles
- Support creative and professional workflows without losing clarity.
- Use semantic tokens and reusable language across product families.
- Balance polish with systematic component behavior.
- Let workflow structure guide page composition.
- Keep themes expressive but controlled.

### Content & Accessibility
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

### Official Sources
- https://spectrum.adobe.com/
- https://spectrum.adobe.com/page/design-language/
- https://spectrum.adobe.com/page/color/
- https://spectrum.adobe.com/page/typography/
- https://spectrum.adobe.com/page/components/

## Colors
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

## Elevation
- Use a consistent spacing scale that supports panels, toolbars, and workflow regions.
- Use moderate radius and refined surfaces rather than severe sharpness.
- Use overlays and depth with control, especially for popovers, trays, and dialogs.
- Keep alignment precise in tools, panels, and asset-heavy layouts.

- **Spacing system note:** Spacing tokens
- **Radius / shape note:** Corner radius in component language
- **Elevation / shadow note:** Depth and overlay styling tokens

## Components
### Navigation Rules
- Use shell navigation, tabs, and side panels based on the product workflow.
- Use breadcrumbs or path indicators only when hierarchy truly matters.
- Keep local tool navigation close to the content it affects.
- Support both app-level and object-level navigation cleanly.

- **Official navigation note:** Workflow navigation and shell patterns
- **Pattern note:** Shell nav, side nav, tabs

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer polished but restrained button hierarchy with clear primary emphasis.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#2C2C2C]">
  <button class="inline-flex h-10 items-center justify-center rounded-lg bg-[#1473E6] px-4 text-sm font-medium text-white shadow-sm">Create file</button>
  <button class="inline-flex h-10 items-center justify-center rounded-lg border border-[#D5D5D5] bg-[#FFFFFF] px-4 text-sm font-medium text-[#2C2C2C]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Text field
- **Preferred style:** Use refined text inputs with visible labels and clean helper or validation messaging.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#2C2C2C]">
  <span class="font-medium">Project name</span>
  <input class="h-10 rounded-lg border border-[#D5D5D5] bg-[#FFFFFF] px-4 text-sm text-[#2C2C2C] outline-none focus:border-[#1473E6] focus:ring-2 focus:ring-[#78BBFA]" value="North star workspace" />
  <span class="text-xs text-[#5C5C5C]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Picker and ComboBox in Spectrum family
- **Preferred style:** Use pickers and comboboxes that fit polished workflow surfaces and complex assets or options.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#2C2C2C]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-10 w-full appearance-none rounded-lg border border-[#D5D5D5] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#2C2C2C] outline-none focus:border-[#1473E6] focus:ring-2 focus:ring-[#78BBFA]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#5C5C5C]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use selection controls that remain explicit and accessible without feeling heavy.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#2C2C2C]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#D5D5D5] text-[#1473E6] focus:ring-[#78BBFA]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#5C5C5C]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use selection controls that remain explicit and accessible without feeling heavy.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#2C2C2C]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#D5D5D5] text-[#1473E6] focus:ring-[#78BBFA]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#D5D5D5] text-[#1473E6] focus:ring-[#78BBFA]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use selection controls that remain explicit and accessible without feeling heavy.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F8F8F8] p-3 text-sm text-[#2C2C2C]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#5C5C5C]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#1473E6]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** DatePicker, Calendar in Spectrum family
- **Preferred style:** Use date and time inputs only when the workflow requires them, styled to match Spectrum fields.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#2C2C2C] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-10 rounded-lg border border-[#D5D5D5] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#1473E6] focus:ring-2 focus:ring-[#78BBFA]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-10 rounded-lg border border-[#D5D5D5] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#1473E6] focus:ring-2 focus:ring-[#78BBFA]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Search within workflows
- **Preferred style:** Use search as a strong workflow tool in headers, asset areas, or filtering contexts.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#2C2C2C]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#5C5C5C]">⌕</span>
  <input class="h-10 w-full rounded-lg border border-[#D5D5D5] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#1473E6] focus:ring-2 focus:ring-[#78BBFA]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** Menu and ActionMenu family
- **Preferred style:** Use menus and action menus with careful spacing and clear option grouping.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-xl border border-[#D5D5D5] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#2C2C2C] hover:bg-[#F8F8F8]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#2C2C2C] hover:bg-[#F8F8F8]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#D31510] hover:bg-[#F8F8F8]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs to switch sibling workflows or subviews inside a larger shell.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#D5D5D5] text-sm text-[#5C5C5C]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#1473E6] px-3 font-medium text-[#2C2C2C]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-t-lg bg-[#FFFFFF] px-3 hover:text-[#2C2C2C]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#2C2C2C]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs where workflow hierarchy or path context matters, not by default.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#5C5C5C]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#2C2C2C]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#2C2C2C]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#2C2C2C]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Top nav and headers
- **Preferred style:** Use polished headers that orient the user without overpowering the work surface. Keep default header surfaces solid and crisp rather than frosted.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions. Avoid using backdrop blur as the standard header behavior.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#D5D5D5] bg-[#FFFFFF] px-5 py-4 text-[#2C2C2C]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#5C5C5C]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-10 items-center justify-center rounded-lg bg-[#1473E6] px-4 text-sm font-medium text-white">Create file</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Side nav and rail patterns
- **Preferred style:** Use side panels or nav rails when workflow context benefits from persistent structure.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-xl border border-[#D5D5D5] bg-[#FFFFFF] p-3 text-sm text-[#5C5C5C]">
  <a class="rounded-md bg-[#F8F8F8] px-3 py-2 font-medium text-[#2C2C2C]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F8F8F8] hover:text-[#2C2C2C]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F8F8F8] hover:text-[#2C2C2C]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Card and card view patterns
- **Preferred style:** Use cards and panels as controlled grouping surfaces, not as casual dashboard tiles.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-xl border border-[#D5D5D5] bg-[#FFFFFF] p-5 text-[#2C2C2C] shadow-sm">
  <p class="text-xs text-[#5C5C5C]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#5C5C5C]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#1473E6]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use tables where precise asset or data scanning matters, with refined but readable density.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-xl border border-[#D5D5D5] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#2C2C2C]">
    <thead class="bg-[#F8F8F8] text-xs uppercase tracking-[0.08em] text-[#5C5C5C]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#D5D5D5]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#008F5D]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#D5D5D5]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#5C5C5C]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists for navigational, asset, or metadata workflows with clean structure.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#D5D5D5] rounded-xl border border-[#D5D5D5] bg-[#FFFFFF] text-sm text-[#2C2C2C]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#5C5C5C]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#5C5C5C]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and labels to communicate state and classification in a polished way.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-lg bg-[#F8F8F8] px-3 py-1 text-xs font-semibold text-[#1473E6]">Active</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips and coach marks for clarification in tool-dense areas.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#2C2C2C]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#D5D5D5] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-lg bg-[#2C2C2C] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Dialog / tray
- **Preferred style:** Use dialogs, trays, and overlays for focused tasks and workflow interruptions.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-xl bg-[#FFFFFF] p-6 text-[#2C2C2C] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#5C5C5C]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-10 items-center justify-center rounded-lg border border-[#D5D5D5] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-10 items-center justify-center rounded-lg bg-[#D31510] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Toast and coachmark family
- **Preferred style:** Use polished transient messaging that supports workflow continuity.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-xl border border-[#D5D5D5] bg-[#FFFFFF] px-4 py-3 text-sm text-[#2C2C2C] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#008F5D]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#5C5C5C]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** ProgressCircle, progress bar, skeleton
- **Preferred style:** Use progress indicators and skeletons that stay calm within content-heavy workflows.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#2C2C2C]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#5C5C5C]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F8F8F8]">
    <div class="h-full w-[64%] bg-[#1473E6]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination when dense result sets require explicit chunking; otherwise prefer filtering and navigation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#2C2C2C]">
  <button class="inline-flex h-9 items-center justify-center rounded-lg border border-[#D5D5D5] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-lg bg-[#1473E6] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-[#D5D5D5]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-lg border border-[#D5D5D5] px-3">Next</button>
</nav>
```

### Layout Rules
- Use workflow-centered composition with panels, tools, and content zones.
- Support both focused document-like screens and denser application shells.
- Use side panels, headers, and trays when they strengthen creation or review flows.
- Keep the interface polished, but avoid decorative clutter around work content.
- Use thematic consistency across surfaces and control families.

- **Official layout note:** Layout, workflow, and responsive guidance
- **Responsive behavior:** Responsive patterns across devices
- **App structure:** Workflow-centered page architecture
- **Data display guidance:** Charts less central than workflows

### Screen Generation Heuristics
- **Default page structure:** Use a workflow shell with clear content region, supporting panels, and polished but restrained app chrome.
- **Default density:** Use medium density, allowing denser panels where workflow complexity requires it.
- **Default navigation model:** Use shell navigation, tabs, side panels, and contextual overlays according to the workflow.
- **Behavior-to-UI check:** Before writing visible copy, identify any spec lines that describe behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions, and express them as controls or selected states rather than literal text.
- **Preferred form composition:** Use polished labeled fields with concise helper text and controlled validation.
- **Preferred feedback pattern:** Use toasts, dialogs, popovers, and inline status patterns with a calm but refined tone.
- **Preferred data-display pattern:** Use lists, asset grids, tables, and panel-based details depending on workflow fit.
- **Prompt bias:** Use prompts such as 'Adobe Spectrum workflow UI', 'refined panels', 'creative tool shell', and 'polished semantic tokens'.
- **Component naming consistency:** Medium | Adobe-specific family terms appear
- **Layout rule explicitness:** High | workflow layout is explicit
- **Theme describability:** High | visual language is richly named
- **Prompt-to-UI suitability:** High | strong for creative and content workflows

## Do's and Don'ts
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
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Spectrum patterns offer a clear stateful control.
