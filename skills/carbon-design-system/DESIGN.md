# Carbon Design System DESIGN.md

## Overview
Use this specification for serious enterprise interfaces, operational dashboards, and products that require accessibility, structure, and a disciplined visual system. Favor grid logic, strong information hierarchy, and restrained styling.

- **Provider:** IBM
- **Primary reference:** https://carbondesignsystem.com/
- **Primary product focus:** Enterprise products and dashboards
- **Platforms:** Web: Yes | strong web focus | iOS: Limited | not primary focus | Android: Limited | not Android-native guidance | Desktop: Yes | enterprise dashboards
- **Status:** Active | IBM maintained
- **Reference note:** Use this file as the design-system reference for visual language, components, and layout decisions.

### Design Principles
- Optimize for clarity and enterprise-scale usability.
- Use the grid to create order before adding decoration.
- Keep motion restrained and purposeful.
- Use layered surfaces and theme-aware contrast carefully.
- Make dense information readable through structure and rhythm.

### Content & Accessibility
- Use explicit labels and strong state communication for fields and controls.
- Preserve visible focus and strong contrast in all themes.
- Use accessible component states as a non-negotiable baseline.
- Prefer inline explanation over hidden affordances.
- Use calm, direct content in error and empty-state messaging.

- **Accessibility note:** Strong | accessibility status per component
- **Content note:** Content and naming guidance
- **Internationalization note:** Global enterprise support implied
- **Localization / RTL note:** Strong | bidirectional support documented
- **Validation note:** Error messaging and inline validation guidance
- **State model note:** States documented in components
- **Privacy / trust note:** Enterprise governance context

### Official Sources
- https://carbondesignsystem.com/
- https://carbondesignsystem.com/guidelines/color/overview/
- https://carbondesignsystem.com/guidelines/typography/overview/
- https://carbondesignsystem.com/guidelines/2x-grid/overview/
- https://carbondesignsystem.com/components/overview/

## Colors
Representative Carbon palette for generation based on public themes and IBM blue emphasis. Use Carbon tokens in implementation; these values are representative.

- **Interactive `#0F62FE`:** Primary action and active emphasis.
- **Text Primary `#161616`:** Primary text and icon color.
- **Text Secondary `#525252`:** Secondary text and supporting metadata.
- **Background `#FFFFFF`:** Primary page background.
- **Layer 01 `#F4F4F4`:** First elevated or grouped layer.
- **Layer 02 `#E0E0E0`:** Additional layer separation and input backgrounds.
- **Success `#24A148`:** Success and positive confirmation.
- **Danger `#DA1E28`:** Error and destructive emphasis.

- **Dark mode guidance:** Strong | white and gray theme variants
- **Theming guidance:** High | tokens and themes for products
- **Semantic token guidance:** Strong | tokens and CSS custom properties

## Typography
- Use IBM Plex Sans as the primary interface typeface.
- Use a disciplined productive typographic hierarchy rather than expressive display-heavy treatment.
- Keep headings compact and functional.
- Use readable line length and restrained weight changes.
- Let tables, forms, and operational content stay crisp and efficient.

- **Official typography note:** Productive type styles and tokens
- **Iconography:** IBM iconography guidance
- **Motion direction:** Motion is limited and purposeful

## Elevation
- Use the Carbon spacing scale with a strong 2x Grid mindset.
- Use modest radius and avoid soft card-heavy consumer styling.
- Prefer layered backgrounds and subtle borders over dramatic shadow depth.
- Keep spacing highly consistent across sections, fields, and tables.

- **Spacing system note:** Spacing scale and grid
- **Radius / shape note:** Productive geometry and corner styles
- **Elevation / shadow note:** Layer model more central than shadows

## Components
### Navigation Rules
- Use side navigation and shell patterns for larger products.
- Use tabs for sibling content areas and view switching.
- Use breadcrumbs when navigating deep product hierarchies.
- Keep navigation labels literal and utility-oriented.

- **Official navigation note:** Navigation patterns and shell guidance
- **Pattern note:** Side nav, header, switcher

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer direct, high-contrast button hierarchy with strong accessibility and limited ornament.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#161616]">
  <button class="inline-flex h-12 items-center justify-center rounded-none bg-[#0F62FE] px-4 text-sm font-medium text-white shadow-none">Save</button>
  <button class="inline-flex h-12 items-center justify-center rounded-none border border-[#C6C6C6] bg-[#FFFFFF] px-4 text-sm font-medium text-[#161616]">Add reviewer</button>
</div>
```

### Text field
- **Official naming / aliases:** Text input
- **Preferred style:** Use crisp text inputs with visible labels, helper text, and explicit invalid states.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#161616]">
  <span class="font-medium">Project name</span>
  <input class="h-12 rounded-none border border-[#C6C6C6] bg-[#FFFFFF] px-4 text-sm text-[#161616] outline-none focus:border-[#0F62FE] focus:ring-2 focus:ring-[#78A9FF]" value="North star workspace" />
  <span class="text-xs text-[#525252]">Shown in navigation and activity feeds.</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Dropdown, combo box, multiselect
- **Preferred style:** Use structured dropdown and multiselect patterns suited to enterprise forms and filters.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#161616]">
  <span class="font-medium">Owner</span>
  <div class="relative">
    <select class="h-12 w-full appearance-none rounded-none border border-[#C6C6C6] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#161616] outline-none focus:border-[#0F62FE] focus:ring-2 focus:ring-[#78A9FF]">
      <option>Design systems team</option>
      <option>Platform team</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#525252]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use compact, high-legibility choice controls with strong state feedback.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#161616]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#C6C6C6] text-[#0F62FE] focus:ring-[#78A9FF]" />
  <span>
    <span class="block font-medium">Notify collaborators</span>
    <span class="block text-xs text-[#525252]">Send a summary when this draft is published.</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio button
- **Preferred style:** Use compact, high-legibility choice controls with strong state feedback.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#161616]">
  <legend class="font-medium">Visibility</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#C6C6C6] text-[#0F62FE] focus:ring-[#78A9FF]" />Team only</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#C6C6C6] text-[#0F62FE] focus:ring-[#78A9FF]" />Public preview</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Toggle
- **Preferred style:** Use compact, high-legibility choice controls with strong state feedback.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F4F4F4] p-3 text-sm text-[#161616]">
  <div>
    <p class="font-medium">Auto-save updates</p>
    <p class="text-xs text-[#525252]">Apply the change immediately after toggling.</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#0F62FE]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** Date picker, time picker
- **Preferred style:** Use date and time inputs that align tightly with form grids and operational scheduling tasks.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#161616] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">Start date</span>
    <input type="date" class="h-12 rounded-none border border-[#C6C6C6] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0F62FE] focus:ring-2 focus:ring-[#78A9FF]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">Time</span>
    <input type="time" class="h-12 rounded-none border border-[#C6C6C6] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#0F62FE] focus:ring-2 focus:ring-[#78A9FF]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Search pattern with filtering
- **Preferred style:** Use search as a structured product function, often paired with filters and result management.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#161616]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#525252]">⌕</span>
  <input class="h-12 w-full rounded-none border border-[#C6C6C6] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#0F62FE] focus:ring-2 focus:ring-[#78A9FF]" placeholder="Search projects" />
</label>
```

### Menu
- **Official naming / aliases:** Overflow menu, menu button
- **Preferred style:** Use restrained menus and overflow patterns with clear grouping and accessible focus behavior.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-none border border-[#C6C6C6] bg-[#FFFFFF] p-2 shadow-none">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#161616] hover:bg-[#F4F4F4]">Rename</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#161616] hover:bg-[#F4F4F4]">Duplicate</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#DA1E28] hover:bg-[#F4F4F4]">Archive</button>
</div>
```

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs to segment major sibling views inside a larger enterprise shell.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#C6C6C6] text-sm text-[#525252]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#0F62FE] px-3 font-medium text-[#161616]">Overview</button>
  <button class="inline-flex h-10 items-center rounded-none bg-[#FFFFFF] px-3 hover:text-[#161616]">Activity</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#161616]">Settings</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs for complex hierarchy, not as decorative metadata.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#525252]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#161616]" href="#">Workspace</a></li>
    <li>/</li>
    <li><a class="hover:text-[#161616]" href="#">Campaigns</a></li>
    <li>/</li>
    <li class="font-medium text-[#161616]">Spring launch</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Header and masthead patterns
- **Preferred style:** Use clear page headers and shell headers that prioritize orientation and action clarity. Keep the header as an opaque layer or shell region, not a translucent glass bar.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions. Avoid backdrop blur or frosted treatments in default Carbon headers.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#C6C6C6] bg-[#FFFFFF] px-5 py-4 text-[#161616]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#525252]">Project</p>
    <h1 class="text-lg font-semibold">Spring launch</h1>
  </div>
  <button class="inline-flex h-12 items-center justify-center rounded-none bg-[#0F62FE] px-4 text-sm font-medium text-white">Save</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Side nav
- **Preferred style:** Use side nav confidently in desktop-oriented product shells.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-none border border-[#C6C6C6] bg-[#FFFFFF] p-3 text-sm text-[#525252]">
  <a class="rounded-md bg-[#F4F4F4] px-3 py-2 font-medium text-[#161616]" href="#">Overview</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F4F4F4] hover:text-[#161616]" href="#">Members</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F4F4F4] hover:text-[#161616]" href="#">Settings</a>
</aside>
```

### Card
- **Official naming / aliases:** Tile / structured containers
- **Preferred style:** Use tiles and panels for modular grouping without making the UI soft or consumer-like.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-none border border-[#C6C6C6] bg-[#FFFFFF] p-5 text-[#161616] shadow-none">
  <p class="text-xs text-[#525252]">Weekly summary</p>
  <h3 class="mt-1 text-lg font-semibold">24 tasks completed</h3>
  <p class="mt-2 text-sm text-[#525252]">Progress stays visible without turning the surface into a decorative hero card.</p>
  <button class="mt-4 text-sm font-medium text-[#0F62FE]">View details</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Data table
- **Preferred style:** Use tables as a flagship component with strong structure, sorting, status, and batch action support.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-none border border-[#C6C6C6] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#161616]">
    <thead class="bg-[#F4F4F4] text-xs uppercase tracking-[0.08em] text-[#525252]">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Status</th><th class="px-4 py-3">Owner</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#C6C6C6]"><td class="px-4 py-3 font-medium">Spring launch</td><td class="px-4 py-3 text-[#24A148]">Active</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#C6C6C6]"><td class="px-4 py-3 font-medium">Policy review</td><td class="px-4 py-3 text-[#525252]">Draft</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** Structured list / list group
- **Preferred style:** Use structured lists when table formality is unnecessary but hierarchy still matters.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#C6C6C6] rounded-none border border-[#C6C6C6] bg-[#FFFFFF] text-sm text-[#161616]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Design review</span><span class="text-[#525252]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">Approve copy deck</span><span class="text-[#525252]">Pending</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Tag / status indicator
- **Preferred style:** Use status indicators and tags to make workflow state scannable.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-none bg-[#F4F4F4] px-3 py-1 text-xs font-semibold text-[#0F62FE]">Draft</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips as clarification for dense product surfaces, not as a crutch for poor labels.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#161616]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#C6C6C6] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-none bg-[#161616] px-3 py-2 text-xs text-white shadow-none">Explain the setting without moving the user away from the task.</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Modal
- **Preferred style:** Use modals and side panels for focused tasks or confirmations that justify interruption.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-none bg-[#FFFFFF] p-6 text-[#161616] shadow-none">
    <h3 class="text-lg font-semibold">Discard changes?</h3>
    <p class="mt-2 text-sm text-[#525252]">Unsaved edits will be removed from this draft.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-12 items-center justify-center rounded-none border border-[#C6C6C6] px-4 text-sm font-medium">Cancel</button>
      <button class="inline-flex h-12 items-center justify-center rounded-none bg-[#DA1E28] px-4 text-sm font-medium text-white">Discard</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Toast notification
- **Preferred style:** Use concise toast or notification patterns for background process feedback.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-none border border-[#C6C6C6] bg-[#FFFFFF] px-4 py-3 text-sm text-[#161616] shadow-none">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#24A148]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">Changes saved</p>
    <p class="text-[#525252]">Your updates are now available to the team.</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Progress bar, loading, skeleton
- **Preferred style:** Use progress bars, loading states, and skeletons with a calm enterprise tone.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#161616]">
  <div class="flex items-center justify-between">
    <span class="font-medium">Uploading assets</span>
    <span class="text-[#525252]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F4F4F4]">
    <div class="h-full w-[64%] bg-[#0F62FE]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination in longer tables and data collections where chunking improves orientation.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#161616]">
  <button class="inline-flex h-9 items-center justify-center rounded-none border border-[#C6C6C6] px-3">Previous</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-none bg-[#0F62FE] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-none border border-[#C6C6C6]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-none border border-[#C6C6C6] px-3">Next</button>
</nav>
```

### Layout Rules
- Use the 2x Grid to create alignment, rhythm, and density control.
- Support structured enterprise shells with clear sections and utility actions.
- Use panels and grouped regions when task segmentation helps comprehension.
- Allow dense content, but keep rows, columns, and hierarchy crisp.
- Treat whitespace as a structural tool rather than a luxury aesthetic.

- **Official layout note:** 2x grid and layout principles
- **Responsive behavior:** Responsive by grid and layout tokens
- **App structure:** Enterprise shell and workflows
- **Data display guidance:** Carbon charts ecosystem official

### Screen Generation Heuristics
- **Default page structure:** Use an enterprise shell with side nav, precise sectioning, and structured content panes aligned to the grid.
- **Default density:** Use medium-to-dense density with strong alignment.
- **Default navigation model:** Use shell navigation, side nav, tabs, and breadcrumbs for complex product structures.
- **Behavior-to-UI expectation:** This design system expects behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions to appear as controls or selected states rather than literal text.
- **Preferred form composition:** Use labeled fields, strong validation, and orderly field groups that align tightly to the grid.
- **Preferred feedback pattern:** Use inline messaging, notifications, and modal confirmation only when a stronger interruption is justified.
- **Preferred data-display pattern:** Use tables, tiles, panels, and status-rich lists with disciplined hierarchy.
- **Prompt bias:** Use prompts such as 'Carbon enterprise console', 'IBM-style structured dashboard', '2x grid layout', and 'disciplined operational UI'.
- **Component naming consistency:** High | enterprise-standard names
- **Layout rule explicitness:** High | grid and shell guidance explicit
- **Theme describability:** High | layered theming is explicit
- **Prompt-to-UI suitability:** High | strong for complex enterprise workflows

## Do's and Don'ts
### Do
- Do build the page around grid structure and task clarity.
- Do use layered surfaces and type hierarchy to manage complex information.
- Do keep interactions explicit and accessible.
- Do use tables, forms, and panels confidently in enterprise contexts.
- Do make the UI feel stable and deliberate.

### Don't
- Do not style Carbon screens like soft consumer apps or startup marketing pages.
- Do not use oversized shadows, playful gradients, or decorative blobs.
- Do not over-round controls or turn every section into a floating card.
- Do not collapse dense workflows into excessively spacious layouts.
- Do not sacrifice grid discipline for asymmetrical flourish.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when Carbon patterns offer a clear stateful control.
