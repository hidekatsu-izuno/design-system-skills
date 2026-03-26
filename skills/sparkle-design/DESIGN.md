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
- **State model note:** Strong interaction states are discussed through reusable UI patterns and operational examples.
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
- **Iconography:** Brand and UI icon assets are part of the public Sparkle Design materials.
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

- **Official navigation note:** Navigation is presented as practical product structure with brand-aware visual treatment.
- **Pattern note:** Top navigation, tabs, side navigation, and grouped workspace navigation are consistent with the public examples.

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

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#111111]">
  <button class="inline-flex h-11 items-center justify-center rounded-xl bg-[#FF6B3D] px-4 text-sm font-medium text-white shadow-sm">Share concept</button>
  <button class="inline-flex h-11 items-center justify-center rounded-xl border border-[#DDD6CE] bg-[#FFFFFF] px-4 text-sm font-medium text-[#111111]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Text field pattern
- **Preferred style:** Use clean, readable fields with controlled brand styling and explicit labels.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#111111]">
  <span class="font-medium">Project name</span>
  <input class="h-11 rounded-xl border border-[#DDD6CE] bg-[#FFFFFF] px-4 text-sm text-[#111111] outline-none focus:border-[#FF6B3D] focus:ring-2 focus:ring-[#FFC857]" value="North star workspace" />
  <span class="text-xs text-[#5E5A55]">Client-facing planning board name.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Select and combobox patterns
- **Preferred style:** Use selects and comboboxes that feel integrated into the product language rather than generic browser controls.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#111111]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-11 w-full appearance-none rounded-xl border border-[#DDD6CE] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#111111] outline-none focus:border-[#FF6B3D] focus:ring-2 focus:ring-[#FFC857]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#5E5A55]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use clear choice controls with comfortable labels and visible state changes.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#111111]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#DDD6CE] text-[#FF6B3D] focus:ring-[#FFC857]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#5E5A55]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio pattern
- **Preferred style:** Use clear choice controls with comfortable labels and visible state changes.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#111111]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#DDD6CE] text-[#FF6B3D] focus:ring-[#FFC857]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#DDD6CE] text-[#FF6B3D] focus:ring-[#FFC857]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use clear choice controls with comfortable labels and visible state changes.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F7F5F2] p-3 text-sm text-[#111111]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#5E5A55]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#FF6B3D]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** Date and time picker patterns
- **Preferred style:** Use date and time controls only where the product workflow needs them, styled consistently with the broader product language.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#111111] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-11 rounded-xl border border-[#DDD6CE] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#FF6B3D] focus:ring-2 focus:ring-[#FFC857]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-11 rounded-xl border border-[#DDD6CE] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#FF6B3D] focus:ring-2 focus:ring-[#FFC857]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Search field
- **Preferred style:** Use search as a practical tool, not as a decorative centerpiece.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#111111]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#5E5A55]">⌕</span>
  <input class="h-11 w-full rounded-xl border border-[#DDD6CE] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#FF6B3D] focus:ring-2 focus:ring-[#FFC857]" placeholder="Search workspaces" />
</label>
```

### Menu
- **Official naming / aliases:** Menu and action list patterns
- **Preferred style:** Use menus that feel polished and branded but remain easy to scan.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-[24px] border border-[#DDD6CE] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#111111] hover:bg-[#F7F5F2]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#111111] hover:bg-[#F7F5F2]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#C4493D] hover:bg-[#F7F5F2]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs where sibling content needs clear grouping with a stronger visual identity than bare utility tabs.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#DDD6CE] text-sm text-[#5E5A55]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#FF6B3D] px-3 font-medium text-[#111111]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-t-xl bg-[#FFFFFF] px-3 hover:text-[#111111]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#111111]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumbs
- **Preferred style:** Use breadcrumbs only when hierarchy needs explicit support.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#5E5A55]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#111111]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#111111]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#111111]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Header
- **Preferred style:** Use headers that can carry some brand expression while staying functional.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#DDD6CE] bg-[#FFFFFF] px-5 py-4 text-[#111111]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#5E5A55]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-11 items-center justify-center rounded-xl bg-[#FF6B3D] px-4 text-sm font-medium text-white">Share concept</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Side navigation
- **Preferred style:** Use side navigation when it helps complex products, but keep it structured and readable.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-[24px] border border-[#DDD6CE] bg-[#FFFFFF] p-3 text-sm text-[#5E5A55]">
  <a class="rounded-md bg-[#F7F5F2] px-3 py-2 font-medium text-[#111111]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F7F5F2] hover:text-[#111111]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F7F5F2] hover:text-[#111111]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Card and panel patterns
- **Preferred style:** Use cards and panels as a key part of polished modular composition.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-[24px] border border-[#DDD6CE] bg-[#FFFFFF] p-5 text-[#111111] shadow-sm">
  <p class="text-xs text-[#5E5A55]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#5E5A55]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#FF6B3D]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Table patterns
- **Preferred style:** Use tables when the workflow is data-heavy, but maintain stronger visual discipline than generic enterprise UI.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-[24px] border border-[#DDD6CE] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#111111]">
    <thead class="bg-[#F7F5F2] text-xs uppercase tracking-[0.08em] text-[#5E5A55]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#DDD6CE]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#2F8F5B]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#DDD6CE]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#5E5A55]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List pattern
- **Preferred style:** Use lists for flexible presentation when cards or tables would be too rigid.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#DDD6CE] rounded-[24px] border border-[#DDD6CE] bg-[#FFFFFF] text-sm text-[#111111]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#5E5A55]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#5E5A55]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge and tag patterns
- **Preferred style:** Use badges and tags to reinforce state and categorization with measured brand emphasis.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-xl bg-[#F7F5F2] px-3 py-1 text-xs font-semibold text-[#111111]">Featured</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips as supporting clarification, not as a stylish flourish.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#111111]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#DDD6CE] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-xl bg-[#111111] px-3 py-2 text-xs text-white shadow-sm">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Dialog and modal patterns
- **Preferred style:** Use dialogs for focused interruption and secondary tasks with polished but controlled styling.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-[24px] bg-[#FFFFFF] p-6 text-[#111111] shadow-sm">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#5E5A55]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-11 items-center justify-center rounded-xl border border-[#DDD6CE] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-11 items-center justify-center rounded-xl bg-[#C4493D] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Toast and feedback message patterns
- **Preferred style:** Use toast or notice patterns that align with the brand system without becoming noisy.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-[24px] border border-[#DDD6CE] bg-[#FFFFFF] px-4 py-3 text-sm text-[#111111] shadow-sm">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#2F8F5B]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#5E5A55]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Loading indicator patterns
- **Preferred style:** Use progress and loading states with calm clarity and subtle branded support.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#111111]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#5E5A55]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F7F5F2]">
    <div class="h-full w-[64%] bg-[#FF6B3D]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination when longer data or content sets need structure; avoid overusing it in narrative flows.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#111111]">
  <button class="inline-flex h-9 items-center justify-center rounded-xl border border-[#DDD6CE] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-xl bg-[#FF6B3D] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-xl border border-[#DDD6CE]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-xl border border-[#DDD6CE] px-3">Next</button>
</nav>
```

### Layout Rules
- Use clear page structure and a recognizable product shell.
- Allow stronger brand moments in headers, hero sections, or section transitions when the workflow supports them.
- Keep product areas practical and navigable even when visual identity is more pronounced.
- Use cards, sections, and modular panels to scale the system cleanly.
- Prefer deliberate composition over generic dashboard repetition.

- **Official layout note:** Information architecture and layout guidance
- **Responsive behavior:** Responsive rules follow modular branded layouts with consistent card and navigation behavior.
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
