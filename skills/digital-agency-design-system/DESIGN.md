# Digital Agency Design System (Beta) DESIGN.md

## Overview
Use this specification for Japanese public-service websites, form-heavy government flows, and trust-critical transactional screens. Favor plain language, conservative styling, explicit structure, and accessibility-first decisions.

- **Provider:** The digital agency
- **Primary reference:** https://design.digital.go.jp/
- **Primary product focus:** Japanese public service websites
- **Platforms:** Web: Yes | government websites | iOS: N/A | web-first guidance | Android: N/A | web-first guidance | Desktop: Yes | administrative web systems
- **Status:** Beta | public government rollout
- **Reference note:** Use this file as the design-system reference for visual language, components, and layout decisions.

### Design Principles
- Design for trust, clarity, and public comprehension.
- Make accessibility and legal/service readability the default.
- Use conservative visual treatment and explicit interaction patterns.
- Prefer standardization over product-specific flourish.
- Keep forms and service flows obvious and low-ambiguity.

### Content & Accessibility
- Use plain language and explicit procedural wording.
- Preserve strong contrast, visible focus, and accessible target sizes.
- Use helper text, error text, and notices close to the point of action.
- Do not rely on iconography alone to communicate state or instruction.
- Keep forms predictable and cognitively light.

- **Accessibility note:** Strong | public-sector accessibility emphasized
- **Content note:** Plain Japanese and service writing implied
- **Internationalization note:** Japanese government focus
- **Localization / RTL note:** N/A | Japanese public-sector context
- **Validation note:** Error and notice components for services
- **State model note:** Usage pages describe state behavior
- **Privacy / trust note:** Strong | public trust and legal accessibility

### Official Sources
- https://design.digital.go.jp/
- https://design.digital.go.jp/dads/components/button/
- https://design.digital.go.jp/components/
- https://design.digital.go.jp/templates/
- https://design.digital.go.jp/guidelines/accessibility/

## Colors
Representative Digital Agency palette for generation based on public component examples and government web guidance. Use official values when implementing; the values below are representative for generation.

- **Primary Blue `#005AC2`:** Primary action, links, and core interactive emphasis.
- **Blue Hover `#00408A`:** Hover and active emphasis for primary controls.
- **Light Blue `#E8F1FF`:** Low-emphasis hover and outlined-button background.
- **Text `#1A1A1A`:** Primary readable text color.
- **Background `#FFFFFF`:** Primary document and service surface.
- **Subtle Surface `#F5F5F5`:** Section grouping and low-emphasis backgrounds.
- **Border `#C8C8C8`:** Field and section boundaries.
- **Danger `#B00020`:** Error and destructive emphasis.

- **Dark mode guidance:** Limited | public docs focus on baseline web
- **Theming guidance:** Low | standardization over customization
- **Semantic token guidance:** Medium | design foundations standardized

## Typography
- Use highly readable Japanese-capable sans-serif typography.
- Keep hierarchy simple, direct, and service-oriented.
- Avoid decorative display styling and compressed text treatment.
- Favor readability in long guidance text, labels, and form instructions.
- Use emphasis sparingly and only where comprehension improves.

- **Official typography note:** Readable Japanese web typography guidance
- **Iconography:** Icons in public components
- **Motion direction:** Motion restrained for service clarity

## Elevation
- Use consistent spacing that supports long-form reading and form completion.
- Use conservative radius values and straightforward component geometry.
- Use minimal shadow; structure should come from order, not depth effects.
- Keep forms, notices, and templates aligned and explicit.

- **Spacing system note:** Consistent spacing in templates
- **Radius / shape note:** Conservative component shapes
- **Elevation / shadow note:** Minimal shadow usage for public trust

## Components
### Navigation Rules
- Use straightforward global navigation, breadcrumbs, and side navigation where service scale requires them.
- Use local navigation only when it materially improves orientation.
- Keep navigation labels plain and official rather than branded.
- Avoid deep or playful navigation experiments.

- **Official navigation note:** Header, side nav, breadcrumb in public guidance
- **Pattern note:** Global nav, side nav, breadcrumbs

### Icon usage in static mocks
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome icons as the fallback library.
- **Where to use icons:** Show icons in places where this design system normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions.
- **How to use icons:** Choose the closest semantic match to the official icon meaning, keep the visible text label, and avoid turning ordinary controls into icon-only controls unless the pattern is clearly icon-first.

### Button
- **Official naming / aliases:** Button
- **Preferred style:** Prefer clear filled, outlined, and text button hierarchy with conservative styling and obvious labels.
- **Use when:** Use for the single most important page action and nearby secondary actions.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading if the action can take time.
- **Avoid:** Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#1A1A1A]">
  <button class="inline-flex h-11 items-center justify-center rounded-md bg-[#005AC2] px-4 text-sm font-medium text-white shadow-none">申請を保存</button>
  <button class="inline-flex h-11 items-center justify-center rounded-md border border-[#C8C8C8] bg-[#FFFFFF] px-4 text-sm font-medium text-[#1A1A1A]">内容を確認</button>
</div>
```

### Text field
- **Official naming / aliases:** Text input
- **Preferred style:** Use explicit form fields with visible labels, helper text, and close-by validation.
- **Use when:** Use for short structured text entry with explicit labels and helper text.
- **Important states:** Rest, focus, filled, invalid, disabled, and helper/error text visibility.
- **Avoid:** Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1A1A1A]">
  <span class="font-medium">氏名</span>
  <input class="h-11 rounded-md border border-[#C8C8C8] bg-[#FFFFFF] px-4 text-sm text-[#1A1A1A] outline-none focus:border-[#005AC2] focus:ring-2 focus:ring-[#005FCC]" value="デジタル申請ポータル" />
  <span class="text-xs text-[#4A4A4A]">住民票と同じ表記で入力してください。</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** Select
- **Preferred style:** Use plain, accessible selects and comboboxes with low-ambiguity labeling.
- **Use when:** Use when the choice set is constrained, filterable, or too structured for free text.
- **Important states:** Closed, focused, expanded, selected, filtered, invalid, and disabled states.
- **Avoid:** Avoid replacing structured choice controls with free text when the choices are known.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#1A1A1A]">
  <span class="font-medium">担当チーム</span>
  <div class="relative">
    <select class="h-11 w-full appearance-none rounded-md border border-[#C8C8C8] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#1A1A1A] outline-none focus:border-[#005AC2] focus:ring-2 focus:ring-[#005FCC]">
      <option>デザインシステム担当</option>
      <option>プラットフォーム担当</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#4A4A4A]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use straightforward checkboxes, radios, and switches with enough space for clear Japanese labels.
- **Use when:** Use for non-exclusive multi-select or independent boolean options.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, and disabled.
- **Avoid:** Avoid using checkboxes for mutually exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#1A1A1A]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#C8C8C8] text-[#005AC2] focus:ring-[#005FCC]" />
  <span>
    <span class="block font-medium">メール通知を送る</span>
    <span class="block text-xs text-[#4A4A4A]">公開時に要約を送信します。</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio button
- **Preferred style:** Use straightforward checkboxes, radios, and switches with enough space for clear Japanese labels.
- **Use when:** Use for small exclusive option sets that should remain visible.
- **Important states:** Unchecked, checked, focus, disabled, and clear group labeling.
- **Avoid:** Avoid using radios for long or dynamic option sets better served by a select.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#1A1A1A]">
  <legend class="font-medium">公開範囲</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#C8C8C8] text-[#005AC2] focus:ring-[#005FCC]" />組織内のみ</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#C8C8C8] text-[#005AC2] focus:ring-[#005FCC]" />外部公開</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** Switch
- **Preferred style:** Use straightforward checkboxes, radios, and switches with enough space for clear Japanese labels.
- **Use when:** Use for immediate on/off states with direct effect or obvious persistence.
- **Important states:** Off, on, focus, disabled, and any paired status text.
- **Avoid:** Avoid using switches for actions that require confirmation or a final submit button.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F5F5F5] p-3 text-sm text-[#1A1A1A]">
  <div>
    <p class="font-medium">メール通知を受け取る</p>
    <p class="text-xs text-[#4A4A4A]">切り替えた直後に設定へ反映します。</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#005AC2]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Date/time picker
- **Official naming / aliases:** Date picker / calendar
- **Preferred style:** Use practical date inputs and calendars that favor comprehension over clever interaction.
- **Use when:** Use for scheduling, filtering, or structured temporal input.
- **Important states:** Empty, selected, invalid, focused, expanded, and disabled states.
- **Avoid:** Avoid ad hoc date text entry without clear format help when the system supports a picker.

**Tailwind implementation example:**
```html
<div class="grid max-w-md gap-2 text-sm text-[#1A1A1A] sm:grid-cols-2">
  <label class="grid gap-2">
    <span class="font-medium">利用開始日</span>
    <input type="date" class="h-11 rounded-md border border-[#C8C8C8] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#005AC2] focus:ring-2 focus:ring-[#005FCC]" value="2026-04-12" />
  </label>
  <label class="grid gap-2">
    <span class="font-medium">時刻</span>
    <input type="time" class="h-11 rounded-md border border-[#C8C8C8] bg-[#FFFFFF] px-4 text-sm outline-none focus:border-[#005AC2] focus:ring-2 focus:ring-[#005FCC]" value="09:30" />
  </label>
</div>
```

### Search
- **Official naming / aliases:** Search
- **Preferred style:** Use search as a service utility, not as a central visual motif.
- **Use when:** Use for finding records, screens, or content, often paired with filters.
- **Important states:** Idle, focused, active query, loading, empty results, and clear/reset states.
- **Avoid:** Avoid styling search like a decorative hero input detached from the workflow.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#1A1A1A]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#4A4A4A]">⌕</span>
  <input class="h-11 w-full rounded-md border border-[#C8C8C8] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#005AC2] focus:ring-2 focus:ring-[#005FCC]" placeholder="申請番号を検索" />
</label>
```

### Menu
- **Official naming / aliases:** Menu
- **Preferred style:** Use menus only when they genuinely improve navigation or action grouping; keep them plain and direct.
- **Use when:** Use for contextual actions, option grouping, and compact command lists.
- **Important states:** Closed, open, focused item, selected item, disabled item, and submenu when needed.
- **Avoid:** Avoid burying primary actions inside menus when they should stay visible.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-md border border-[#C8C8C8] bg-[#FFFFFF] p-2 shadow-none">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1A1A1A] hover:bg-[#F5F5F5]">名前を変更</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#1A1A1A] hover:bg-[#F5F5F5]">複製する</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#B00020] hover:bg-[#F5F5F5]">アーカイブ</button>
</div>
```

### Tabs
- **Official naming / aliases:** Tabs
- **Preferred style:** Use tabs sparingly and only when sibling content views are clearly understood by users.
- **Use when:** Use for sibling views inside one destination or object context.
- **Important states:** Inactive, active, focus-visible, overflow if needed, and disabled when applicable.
- **Avoid:** Avoid using tabs for process steps or unrelated destinations.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#C8C8C8] text-sm text-[#4A4A4A]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#005AC2] px-3 font-medium text-[#1A1A1A]">概要</button>
  <button class="inline-flex h-10 items-center rounded-t-md bg-[#FFFFFF] px-3 hover:text-[#1A1A1A]">アクティビティ</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#1A1A1A]">設定</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** Breadcrumb
- **Preferred style:** Use breadcrumbs to maintain orientation in multi-level public-service information architecture.
- **Use when:** Use only when hierarchy depth needs visible orientation support.
- **Important states:** Normal, current page, truncated if space is tight, and focus-visible links.
- **Avoid:** Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#4A4A4A]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#1A1A1A]" href="#">ホーム</a></li>
    <li>/</li>
    <li><a class="hover:text-[#1A1A1A]" href="#">申請一覧</a></li>
    <li>/</li>
    <li class="font-medium text-[#1A1A1A]">詳細</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Header
- **Preferred style:** Use a straightforward header with service title, utility navigation, and minimal visual flourish. Use an opaque background for trust and readability rather than translucent or glass-like styling.
- **Use when:** Use to anchor the page title, context, and the most important actions.
- **Important states:** Default, scrolled where applicable, focus on actions, and overflow handling.
- **Avoid:** Avoid crowding the header with too many equal-weight actions. Avoid default frosted or blurred headers in public-service UI.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#C8C8C8] bg-[#FFFFFF] px-5 py-4 text-[#1A1A1A]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#4A4A4A]">案件</p>
    <h1 class="text-lg font-semibold">申請内容の確認</h1>
  </div>
  <button class="inline-flex h-11 items-center justify-center rounded-md bg-[#005AC2] px-4 text-sm font-medium text-white">申請を保存</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Side navigation
- **Preferred style:** Use side navigation only for larger multi-section services, keeping labels explicit and official.
- **Use when:** Use for persistent destination structure or deeper information architecture.
- **Important states:** Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.
- **Avoid:** Avoid introducing side navigation on small scopes that do not need persistent structure.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-md border border-[#C8C8C8] bg-[#FFFFFF] p-3 text-sm text-[#4A4A4A]">
  <a class="rounded-md bg-[#F5F5F5] px-3 py-2 font-medium text-[#1A1A1A]" href="#">概要</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F5F5] hover:text-[#1A1A1A]" href="#">メンバー</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F5F5] hover:text-[#1A1A1A]" href="#">設定</a>
</aside>
```

### Card
- **Official naming / aliases:** Card
- **Preferred style:** Use cards and panels conservatively for summaries or grouped content, not as decorative layout tiles.
- **Use when:** Use to group related content, metrics, or actions into a coherent module.
- **Important states:** Default, hover only if interactive, selected when applicable, and loading/skeleton states.
- **Avoid:** Avoid turning every section into a decorative floating card when simpler grouping would be clearer.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-md border border-[#C8C8C8] bg-[#FFFFFF] p-5 text-[#1A1A1A] shadow-none">
  <p class="text-xs text-[#4A4A4A]">今週の概要</p>
  <h3 class="mt-1 text-lg font-semibold">24 件の処理が完了</h3>
  <p class="mt-2 text-sm text-[#4A4A4A]">進捗を整理して見せつつ、情報面を装飾過多なカードにしない例です。</p>
  <button class="mt-4 text-sm font-medium text-[#005AC2]">詳細を見る</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use plain, readable tables for summaries, result sets, and reference information.
- **Use when:** Use when users need to compare rows, scan columns, sort, or act on collections.
- **Important states:** Default, hover, selected row, sorted column, loading, empty, and error states.
- **Avoid:** Avoid using a table when the user does not need row or column comparison. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-md border border-[#C8C8C8] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#1A1A1A]">
    <thead class="bg-[#F5F5F5] text-xs uppercase tracking-[0.08em] text-[#4A4A4A]">
      <tr><th class="px-4 py-3">名称</th><th class="px-4 py-3">状態</th><th class="px-4 py-3">担当</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#C8C8C8]"><td class="px-4 py-3 font-medium">春の申請更新</td><td class="px-4 py-3 text-[#2F7D32]">進行中</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#C8C8C8]"><td class="px-4 py-3 font-medium">制度見直し</td><td class="px-4 py-3 text-[#4A4A4A]">下書き</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### List
- **Official naming / aliases:** List
- **Preferred style:** Use lists for steps, requirements, summaries, and straightforward content grouping.
- **Use when:** Use for lighter-weight collections or rows that need more flexible content than a table.
- **Important states:** Default, hover if interactive, selected when needed, loading, and empty states.
- **Avoid:** Avoid lists when the task needs stable columns, sorting, or bulk data operations.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#C8C8C8] rounded-md border border-[#C8C8C8] bg-[#FFFFFF] text-sm text-[#1A1A1A]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">確認依頼</span><span class="text-[#4A4A4A]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">承認待ち</span><span class="text-[#4A4A4A]">保留中</span></li>
</ul>
```

### Badge
- **Official naming / aliases:** Badge
- **Preferred style:** Use badges and labels only when they improve comprehension of status or category.
- **Use when:** Use for status, counts, metadata, or lightweight categorization.
- **Important states:** Neutral, positive, warning, danger, and selected/filter-active where relevant.
- **Avoid:** Avoid using badges as the only way to communicate critical status.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-md bg-[#F5F5F5] px-3 py-1 text-xs font-semibold text-[#1A1A1A]">確認中</span>
```

### Tooltip
- **Official naming / aliases:** Tooltip
- **Preferred style:** Use tooltips sparingly; essential guidance should remain visible.
- **Use when:** Use for supporting clarification that should not interrupt the task flow.
- **Important states:** Hidden, visible, delayed appearance, and accessible trigger focus.
- **Avoid:** Avoid hiding required instructions or validation inside tooltips.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#1A1A1A]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#C8C8C8] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-md bg-[#1A1A1A] px-3 py-2 text-xs text-white shadow-none">必要な補足だけを、その場で伝える例です。</div>
</div>
```

### Dialog/Modal
- **Official naming / aliases:** Dialog
- **Preferred style:** Use dialogs for clear confirmation or interruption points, not for routine guidance.
- **Use when:** Use for blocking decisions, focused secondary tasks, or high-risk confirmation.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading/submit state.
- **Avoid:** Avoid using dialogs for routine inline edits that fit naturally in the page.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-md bg-[#FFFFFF] p-6 text-[#1A1A1A] shadow-none">
    <h3 class="text-lg font-semibold">変更を破棄しますか？</h3>
    <p class="mt-2 text-sm text-[#4A4A4A]">保存していない編集内容は削除されます。</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-11 items-center justify-center rounded-md border border-[#C8C8C8] px-4 text-sm font-medium">キャンセル</button>
      <button class="inline-flex h-11 items-center justify-center rounded-md bg-[#B00020] px-4 text-sm font-medium text-white">破棄する</button>
    </div>
  </div>
</div>
```

### Toast/Snackbar
- **Official naming / aliases:** Notice / snackbar-equivalent
- **Preferred style:** Use toast-like transient feedback rarely; prefer visible notices and confirmation content.
- **Use when:** Use for transient action feedback that should not block progress.
- **Important states:** Appearing, visible, dismissing, action available, and stacked if multiple are possible.
- **Avoid:** Avoid using transient feedback for critical errors that must remain visible.

**Tailwind implementation example:**
```html
<div class="inline-flex items-start gap-3 rounded-md border border-[#C8C8C8] bg-[#FFFFFF] px-4 py-3 text-sm text-[#1A1A1A] shadow-none">
  <span class="mt-0.5 h-2.5 w-2.5 rounded-full bg-[#2F7D32]" aria-hidden="true"></span>
  <div>
    <p class="font-medium">変更を保存しました</p>
    <p class="text-[#4A4A4A]">更新内容をすぐに共有できます。</p>
  </div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Loading and progress
- **Preferred style:** Use clear loading and progress states with explicit wording when the system is working.
- **Use when:** Use when background work, loading, or long-running actions need clear status.
- **Important states:** Idle, indeterminate, determinate, skeleton, and completion state.
- **Avoid:** Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#1A1A1A]">
  <div class="flex items-center justify-between">
    <span class="font-medium">ファイルをアップロード中</span>
    <span class="text-[#4A4A4A]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F5F5F5]">
    <div class="h-full w-[64%] bg-[#005AC2]"></div>
  </div>
</div>
```

### Pagination
- **Official naming / aliases:** Pagination
- **Preferred style:** Use pagination only where list length requires it and keep controls extremely explicit.
- **Use when:** Use when chunking long result sets improves orientation, performance, or control.
- **Important states:** Default, current page, hover/focus, disabled edge controls, and compact variants.
- **Avoid:** Avoid pagination when search, filtering, or progressive loading would better fit the workflow.

**Tailwind implementation example:**
```html
<nav aria-label="Pagination" class="flex items-center gap-2 text-sm text-[#1A1A1A]">
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#C8C8C8] px-3">前へ</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md bg-[#005AC2] text-white">1</button>
  <button class="inline-flex h-9 w-9 items-center justify-center rounded-md border border-[#C8C8C8]">2</button>
  <button class="inline-flex h-9 items-center justify-center rounded-md border border-[#C8C8C8] px-3">次へ</button>
</nav>
```

### Layout Rules
- Use simple page templates with clear header, content flow, and service structure.
- Support long-form guidance, forms, notices, and result pages without visual complexity.
- Use sections, headings, and notices to guide the user through the task.
- Keep primary actions explicit and easy to locate.
- Prefer stable, conventional layouts over experimental composition.

- **Official layout note:** Page templates and component layout examples
- **Responsive behavior:** Responsive government web guidance
- **App structure:** Templates for public information architecture
- **Data display guidance:** Tables and summaries more central than charts

### Screen Generation Heuristics
- **Default page structure:** Use a conventional service page or form page with strong heading hierarchy, notices, and a clear primary action path.
- **Default density:** Use medium density with generous readability for text and forms.
- **Default navigation model:** Use straightforward header navigation, breadcrumbs, side navigation, and in-page section structure when needed.
- **Behavior-to-UI expectation:** This design system expects behavior or state such as sorting, filtering, tab switching, pagination, or allowed transitions to appear as controls or selected states rather than literal text.
- **Preferred form composition:** Use strongly labeled fields, clear required markers, helper text, and explicit error messaging.
- **Preferred feedback pattern:** Use notices, inline errors, confirmation pages, and dialogs only for essential interruption.
- **Preferred data-display pattern:** Use simple tables, lists, summaries, and result pages with conservative styling.
- **Prompt bias:** Use prompts such as 'Japanese public service form', 'official government service page', 'plain-language transaction flow', and 'accessible conservative UI'.
- **Component naming consistency:** High | generic public-service names
- **Layout rule explicitness:** High | usage and templates are explicit
- **Theme describability:** Low | customization is intentionally constrained
- **Prompt-to-UI suitability:** High | strong for public-service transaction screens

## Do's and Don'ts
### Do
- Do make the interface feel trustworthy, official, and easy to understand.
- Do use plain language and visible procedural guidance.
- Do use clear buttons, notices, and form structures.
- Do prioritize accessibility and predictable service flow.
- Do keep customization limited and purposeful.

### Don't
- Do not over-customize the visual language or invent product-specific flourishes.
- Do not use glassmorphism, gradient-heavy surfaces, or trendy startup styling.
- Do not turn service screens into dashboard-like card mosaics without need.
- Do not hide critical instructions inside tooltips or tertiary UI.
- Do not use playful illustrations or novelty interactions in transactional service flows.
- Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when the system should express that behavior through explicit controls or state.
