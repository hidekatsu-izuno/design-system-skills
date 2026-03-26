# Spindle Design System DESIGN.md

## Overview
Use this specification for Ameba-flavored web product UI that should feel friendly, respectful, and easy to understand without becoming noisy or overly promotional. Favor explicit labels, approachable surfaces, strong readability for Japanese content, and product decisions that balance emotional warmth with operational clarity.

- **Provider:** CyberAgent / Ameba
- **Primary reference:** https://spindle.ameba.design/
- **Primary product focus:** Ameba web product UI and brand-consistent digital experiences
- **Platforms:** Web: Yes | primary public guidance | iOS: Limited | catalog coverage exists but web-first public docs | Android: Limited | catalog coverage exists but web-first public docs | Desktop: Yes | strong browser product fit
- **Status:** Active | publicly maintained Spindle guidance
- **Reference note:** Use this file as the design-system reference for visual language, components, and layout decisions.

### Design Principles
- Respect the user and avoid UI that feels pushy, abrupt, or self-centered.
- Add warmth and human tone, but keep interaction practical and easy to parse.
- Make first-time and repeat use feel welcoming rather than exclusive.
- Prefer simple structure, explicit labels, and readable spacing over clever novelty.
- Keep the interface lively through rhythm, color accents, and tone, not through visual clutter.

### Content & Accessibility
- Use direct, plain Japanese-friendly labels and guidance in product UI.
- Preserve alternatives for different abilities and interaction methods rather than assuming hover or pointer-only use.
- Do not rely on color alone for status or selection; pair color with borders, labels, or state styling.
- Keep validation, focus, and state changes explicit and easy to perceive.
- Favor clarity and flexibility so the interface remains resilient to user context changes.

- **Accessibility note:** Strong | Spindle aligns with Ameba Accessibility Guidelines and WCAG 2.1-based practice
- **Content note:** Strong | public guidance for brand voice, vocabulary, and UI labeling
- **Internationalization note:** Japanese-first product guidance
- **Localization / RTL note:** Limited | public guidance is Japanese-first
- **Validation note:** Public component guidance includes invalid and focus-aware states
- **State model note:** Strong | selection, visited, invalid, and focus behavior are explicitly discussed
- **Privacy / trust note:** Medium | respectful, user-centered tone is emphasized more than formal enterprise trust language

### Official Sources
- https://spindle.ameba.design/
- https://spindle.ameba.design/principles/design/
- https://spindle.ameba.design/principles/accessibility/
- https://spindle.ameba.design/styles/color/ui/
- https://spindle.ameba.design/styles/color/brand/
- https://spindle.ameba.design/styles/typography/ui/
- https://spindle.ameba.design/styles/typography/brand/
- https://spindle.ameba.design/styles/iconography/anatomy/
- https://spindle.ameba.design/styles/iconography/developer/
- https://spindle.ameba.design/components/
- https://spindle.ameba.design/components/status/

## Colors
Representative Spindle palette for generation based on the public UI color guidance. Favor UI colors for product interfaces and treat brand colors as communication accents rather than default UI paint.

- **Accent Blue `#0091FF`:** Primary accent for links, focus-led emphasis, and selected interactive states.
- **Text High `#08121A`:** Primary text on light surfaces.
- **Text Medium `#394148`:** Secondary text, helper copy, and supporting labels.
- **Text Low `#686E73`:** Quiet metadata and low-emphasis text.
- **Surface Base `#F5F6F6`:** Primary page background.
- **Surface Raised `#FFFFFF`:** Cards, panels, modals, and elevated content surfaces.
- **Surface Secondary `#EBECED`:** Subtle grouped sections and supporting containers.
- **Border Low `#D8D9DA`:** Dividers, field borders, and low-emphasis separators.
- **Border Quiet `#B5B8BA`:** Stronger neutral boundary for selected or separated regions.
- **Positive `#389E46`:** Positive status and success emphasis.
- **Danger `#D91C0B`:** Error and destructive emphasis.
- **Highlight Yellow `#F5E100`:** Highlight or marker-like emphasis in limited cases.
- **Expressive Pink `#F20076`:** Rare expressive accent; use only when green, gray, or red cannot serve the need and keep usage tightly limited.

- **Dark mode guidance:** Public site supports theme switching, but public usage guidance is still light-surface dominant
- **Theming guidance:** Medium | theme colors exist, but public product guidance emphasizes restrained UI usage
- **Semantic token guidance:** Strong | separate surface, text, object, border, highlight, focus, and brand roles

## Typography
- Use the published UI font stack for web by default: `"Helvetica Neue", Helvetica, Arial, "Segoe UI", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, "Yu Gothic Medium", sans-serif`.
- Use `bold` keyword weight for bold treatment rather than arbitrary numeric weight changes when following the official web guidance.
- Optimize for readability in Japanese UI first, especially in labels, controls, and dense operational lists.
- Treat brand typography such as Ameba Sans, UD Shin Maru Go, and AXIS as brand-expression tools, not default app UI type.
- Reserve Ameba Sans in product UI only for constrained numeric or expressive brand-led cases, not for general interface copy.

- **Official typography note:** Public UI typography guidance includes explicit web font-family recommendations
- **Iconography:** Spindle icons are first-party and documented separately
- **Motion direction:** Animation guidance exists, but typography should remain calm and readable rather than motion-led

## Elevation
- Prefer light surfaces, quiet borders, and modest card separation over heavy shadow stacks.
- Use rounded corners, but keep them controlled and product-like rather than oversized or glassy.
- Let whitespace and grouping establish hierarchy before adding stronger elevation.
- Keep lists, panels, and forms aligned to a simple, readable vertical rhythm.
- Use modal and panel elevation clearly when content overlays the current context.

- **Spacing system note:** Public style system covers UI typography, color, icons, and component rhythm even if spacing tokens are not foregrounded as a separate public chapter
- **Radius / shape note:** Rounded geometry is part of the Ameba visual character, but should stay disciplined in UI
- **Elevation / shadow note:** Surface layering exists, especially for cards and modals, but border-led grouping is common

## Components
### Navigation Rules
- Use navigation with explicit labels and approachable visual tone rather than abstract icon-only wayfinding.
- Prefer simple top navigation, local tabs, lists, or grouped menus over enterprise-heavy shell patterns unless the product scope clearly requires persistent side navigation.
- Keep destination structure shallow and friendly; avoid turning the interface into a cold admin shell.
- When navigation or selection appears inside a list, use border, background, or structural change in addition to color to indicate state.

- **Official navigation note:** Public guidance is component- and content-led rather than shell-heavy
- **Pattern note:** Lists, status, tabs, menus, and friendly top-level navigation fit better than rigid enterprise chrome

### Icon usage in static mocks
- **Native icon guidance:** Prefer the official Spindle icon set when available. The public developer guidance points to `@openameba/spindle-icons`.
- **Fallback icon rule:** When the native icon set is unavailable in a static HTML mock, use Font Awesome as the fallback icon library.
- **Where to use icons:** Show icons in places where Spindle normally expects them, especially menu triggers, search, notifications, primary and secondary actions, navigation items, state cues, and row-level actions.
- **How to use icons:** Choose simple geometric icons with readable 24px-oriented proportions, keep visible text labels, and avoid decorative multi-color icon treatments.

### Button
- **Official naming / aliases:** Button, LinkButton, TextButton, SubtleButton, BottomButton
- **Preferred style:** Use clean, approachable buttons with clear hierarchy and enough padding to feel friendly without becoming oversized.
- **Use when:** Use for primary actions, secondary follow-up actions, and inline action sets that should stay explicit.
- **Important states:** Rest, hover, focus, pressed, disabled, and loading when relevant.
- **Avoid:** Avoid overly glossy, overly shadowed, or aggressively enterprise-styled buttons.

**Tailwind implementation example:**
```html
<div class="flex items-center gap-3 bg-[#FFFFFF] p-2 text-[#08121A]">
  <button class="inline-flex h-11 items-center justify-center rounded-md bg-[#0091FF] px-4 text-sm font-medium text-white shadow-sm">保存する</button>
  <button class="inline-flex h-11 items-center justify-center rounded-md border border-[#D8D9DA] bg-[#FFFFFF] px-4 text-sm font-medium text-[#08121A]">あとで確認</button>
</div>
```

### Text field
- **Official naming / aliases:** TextField, TextArea, InputLabel, InvalidMessage
- **Preferred style:** Use clearly labeled fields with visible helper or invalid messaging and straightforward boundaries.
- **Use when:** Use for account, profile, settings, search, and content-entry tasks where direct text entry is expected.
- **Important states:** Empty, filled, focus, invalid, disabled, and helper/error visibility.
- **Avoid:** Avoid placeholder-only labeling or muted states that hide field purpose.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#08121A]">
  <span class="font-medium">ニックネーム</span>
  <input class="h-11 rounded-md border border-[#D8D9DA] bg-[#FFFFFF] px-4 text-sm text-[#08121A] outline-none focus:border-[#0091FF] focus:ring-2 focus:ring-[#8BD0FF]" value="アメーバ太郎" />
  <span class="text-xs text-[#394148]">他のユーザーに表示される名前です。</span>
</label>
```

### Select/combobox
- **Official naming / aliases:** DropDown, InlineDropDown
- **Preferred style:** Use simple dropdown patterns that align with surrounding text fields and list-based selection.
- **Use when:** Use when a known option set should stay compact or inline with other controls.
- **Important states:** Closed, open, focused, selected, invalid, and disabled.
- **Avoid:** Avoid visually overcomplicated custom pickers for ordinary option selection.

**Tailwind implementation example:**
```html
<label class="grid max-w-sm gap-2 text-sm text-[#08121A]">
  <span class="font-medium">担当チーム</span>
  <div class="relative">
    <select class="h-11 w-full appearance-none rounded-md border border-[#D8D9DA] bg-[#FFFFFF] px-4 pr-10 text-sm text-[#08121A] outline-none focus:border-[#0091FF] focus:ring-2 focus:ring-[#8BD0FF]">
      <option>デザインシステム担当</option>
      <option>プラットフォーム担当</option>
    </select>
    <span class="pointer-events-none absolute inset-y-0 right-3 flex items-center text-[#394148]">▾</span>
  </div>
</label>
```

### Checkbox
- **Official naming / aliases:** Checkbox
- **Preferred style:** Use clear checkbox controls with enough label spacing and obvious selected state.
- **Use when:** Use for multi-select and independent opt-in or opt-out choices.
- **Important states:** Unchecked, checked, indeterminate when relevant, focus, invalid, and disabled.
- **Avoid:** Avoid using checkboxes for exclusive choices.

**Tailwind implementation example:**
```html
<label class="flex items-start gap-3 text-sm text-[#08121A]">
  <input type="checkbox" checked class="mt-1 h-4 w-4 rounded border-[#D8D9DA] text-[#0091FF] focus:ring-[#8BD0FF]" />
  <span>
    <span class="block font-medium">メール通知を送る</span>
    <span class="block text-xs text-[#394148]">公開時に要約を送信します。</span>
  </span>
</label>
```

### Radio
- **Official naming / aliases:** Radio
- **Preferred style:** Use radios for small visible exclusive choice sets and align them cleanly within forms or lists.
- **Use when:** Use for one-of-many choices that benefit from full visibility.
- **Important states:** Unchecked, checked, focus, invalid, and disabled.
- **Avoid:** Avoid turning long option sets into radio groups when dropdown selection would be easier to scan.

**Tailwind implementation example:**
```html
<fieldset class="grid gap-2 text-sm text-[#08121A]">
  <legend class="font-medium">公開範囲</legend>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" checked class="h-4 w-4 border-[#D8D9DA] text-[#0091FF] focus:ring-[#8BD0FF]" />組織内のみ</label>
  <label class="flex items-center gap-3"><input type="radio" name="visibility" class="h-4 w-4 border-[#D8D9DA] text-[#0091FF] focus:ring-[#8BD0FF]" />外部公開</label>
</fieldset>
```

### Switch
- **Official naming / aliases:** ToggleSwitch, Toggle inside List
- **Preferred style:** Use toggle switches inside list rows or settings groups when the change is immediate and understandable in place.
- **Use when:** Use for binary settings and lightweight immediate state changes.
- **Important states:** Off, on, focus, disabled, and any paired explanation.
- **Avoid:** Avoid switches for actions that still require later confirmation.

**Tailwind implementation example:**
```html
<div class="flex items-center justify-between gap-4 rounded-xl bg-[#F5F6F6] p-3 text-sm text-[#08121A]">
  <div>
    <p class="font-medium">更新を通知する</p>
    <p class="text-xs text-[#394148]">切り替えた直後に設定へ反映します。</p>
  </div>
  <button type="button" role="switch" aria-checked="true" class="relative h-7 w-12 rounded-full bg-[#0091FF]">
    <span class="absolute right-1 top-1 h-5 w-5 rounded-full bg-white"></span>
  </button>
</div>
```

### Search
- **Official naming / aliases:** Search field using TextField patterns
- **Preferred style:** Use direct, readable search controls with explicit labels or clear search affordances.
- **Use when:** Use for filtering or finding content, people, records, or settings.
- **Important states:** Idle, focused, active query, clear/reset, loading, and empty-result states.
- **Avoid:** Avoid hero-style oversized search that overpowers the rest of the product UI.

**Tailwind implementation example:**
```html
<label class="relative block max-w-md text-sm text-[#08121A]">
  <span class="sr-only">Search</span>
  <span class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-[#394148]">⌕</span>
  <input class="h-11 w-full rounded-md border border-[#D8D9DA] bg-[#FFFFFF] pl-11 pr-4 text-sm outline-none focus:border-[#0091FF] focus:ring-2 focus:ring-[#8BD0FF]" placeholder="ブログを検索" />
</label>
```

### Menu
- **Official naming / aliases:** DropDownMenu, menus within lists and panels
- **Preferred style:** Use compact menus with direct labels and calm separators.
- **Use when:** Use for overflow actions, contextual actions, or dense utility choices.
- **Important states:** Closed, open, focus-visible item, selected item, and disabled item.
- **Avoid:** Avoid burying the primary task path behind menus.

**Tailwind implementation example:**
```html
<div class="inline-grid min-w-56 gap-1 rounded-2xl border border-[#D8D9DA] bg-[#FFFFFF] p-2 shadow-sm">
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#08121A] hover:bg-[#F5F6F6]">名前を変更</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#08121A] hover:bg-[#F5F6F6]">複製する</button>
  <button class="rounded-md px-3 py-2 text-left text-sm text-[#D91C0B] hover:bg-[#F5F6F6]">アーカイブ</button>
</div>
```

### Tabs
- **Official naming / aliases:** UnderlineTab, SegmentedControl
- **Preferred style:** Use underline tabs or segmented controls for sibling views with a lightweight, web-native feel.
- **Use when:** Use for nearby peer views inside one destination.
- **Important states:** Inactive, active, focus-visible, and overflow handling where necessary.
- **Avoid:** Avoid turning tabs into deep information architecture or complex workflow steps.

**Tailwind implementation example:**
```html
<nav class="flex gap-2 border-b border-[#D8D9DA] text-sm text-[#394148]">
  <button class="-mb-px inline-flex h-10 items-center border-b-2 border-[#0091FF] px-3 font-medium text-[#08121A]">概要</button>
  <button class="inline-flex h-10 items-center rounded-t-lg bg-[#FFFFFF] px-3 hover:text-[#08121A]">アクティビティ</button>
  <button class="inline-flex h-10 items-center px-3 hover:text-[#08121A]">設定</button>
</nav>
```

### Breadcrumb
- **Official naming / aliases:** BreadCrumb
- **Preferred style:** Use breadcrumbs only when the product hierarchy genuinely needs orientation help.
- **Use when:** Use for deeper destinations where the user benefits from visible location context.
- **Important states:** Default, current page, truncated if necessary, and focus-visible links.
- **Avoid:** Avoid breadcrumbs in shallow experiences where titles and local navigation are enough.

**Tailwind implementation example:**
```html
<nav aria-label="Breadcrumb" class="text-sm text-[#394148]">
  <ol class="flex items-center gap-2">
    <li><a class="hover:text-[#08121A]" href="#">ホーム</a></li>
    <li>/</li>
    <li><a class="hover:text-[#08121A]" href="#">申請一覧</a></li>
    <li>/</li>
    <li class="font-medium text-[#08121A]">詳細</li>
  </ol>
</nav>
```

### App bar/header
- **Official naming / aliases:** Header and local page header patterns
- **Preferred style:** Use light, readable headers with clear titles, concise support copy, and a modest action set. Keep the header surface opaque and calm rather than frosted or translucent.
- **Use when:** Use to anchor the page context and expose a small number of important controls.
- **Important states:** Default, focused action, and compact behavior on small screens.
- **Avoid:** Avoid sticky chrome that feels heavier than the page content. Avoid defaulting to blur-heavy glass effects for headers.

**Tailwind implementation example:**
```html
<header class="flex items-center justify-between gap-4 border-b border-[#D8D9DA] bg-[#FFFFFF] px-5 py-4 text-[#08121A]">
  <div>
    <p class="text-xs uppercase tracking-[0.12em] text-[#394148]">案件</p>
    <h1 class="text-lg font-semibold">ブログ設定</h1>
  </div>
  <button class="inline-flex h-11 items-center justify-center rounded-md bg-[#0091FF] px-4 text-sm font-medium text-white">保存する</button>
</header>
```

### Side navigation/drawer
- **Official naming / aliases:** Local navigation patterns rather than a strongly prescribed global shell
- **Preferred style:** If side navigation is necessary, keep it lightweight, label-first, and friendlier than a classic enterprise admin rail.
- **Use when:** Use only when the product truly has multiple persistent destinations that benefit from constant visibility.
- **Important states:** Hidden or compact, expanded, selected destination, and focus-visible state.
- **Avoid:** Avoid forcing a rigid dashboard shell onto content that is better served by top navigation, tabs, or lists.

**Tailwind implementation example:**
```html
<aside class="flex w-64 flex-col gap-1 rounded-2xl border border-[#D8D9DA] bg-[#FFFFFF] p-3 text-sm text-[#394148]">
  <a class="rounded-md bg-[#F5F6F6] px-3 py-2 font-medium text-[#08121A]" href="#">概要</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F6F6] hover:text-[#08121A]" href="#">メンバー</a>
  <a class="rounded-md px-3 py-2 hover:bg-[#F5F6F6] hover:text-[#08121A]" href="#">設定</a>
</aside>
```

### List
- **Official naming / aliases:** List, Collection List, Selection, Visited, Add
- **Preferred style:** Use lists as a core structural primitive. Support state with borders, backgrounds, and row structure rather than color alone.
- **Use when:** Use for settings, row actions, navigation-like collections, selectable rows, and content browsing.
- **Important states:** Default, selected, visited where relevant, toggled, focused, and disabled.
- **Avoid:** Avoid reducing list state to color-only differences.

**Tailwind implementation example:**
```html
<ul class="max-w-md divide-y divide-[#D8D9DA] rounded-2xl border border-[#D8D9DA] bg-[#FFFFFF] text-sm text-[#08121A]">
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">確認依頼</span><span class="text-[#394148]">10:30</span></li>
  <li class="flex items-center justify-between px-4 py-3"><span class="font-medium">承認待ち</span><span class="text-[#394148]">保留中</span></li>
</ul>
```

### Card
- **Official naming / aliases:** Panel or card-like grouped container
- **Preferred style:** Use soft grouped surfaces with visible borders or subtle elevation.
- **Use when:** Use to group related information or supporting actions without turning every region into a floating tile.
- **Important states:** Default, interactive hover when clickable, selected when needed, and loading.
- **Avoid:** Avoid overly ornamental card stacks or exaggerated dashboard tiles.

**Tailwind implementation example:**
```html
<section class="max-w-sm rounded-2xl border border-[#D8D9DA] bg-[#FFFFFF] p-5 text-[#08121A] shadow-sm">
  <p class="text-xs text-[#394148]">今週の概要</p>
  <h3 class="mt-1 text-lg font-semibold">24 件の処理が完了</h3>
  <p class="mt-2 text-sm text-[#394148]">進捗を整理して見せつつ、情報面を装飾過多なカードにしない例です。</p>
  <button class="mt-4 text-sm font-medium text-[#0091FF]">詳細を見る</button>
</section>
```

### Table/Data grid
- **Official naming / aliases:** Table
- **Preferred style:** Use practical tables with readable row spacing and quiet borders.
- **Use when:** Use when comparison across rows and columns is the main task.
- **Important states:** Default, sorted, selected, loading, empty, and error.
- **Avoid:** Avoid using a table when a simpler list better supports the content. Avoid showing sort instructions like `organization_code ASC` as plain text when the state should be attached to headers or sort controls.

**Tailwind implementation example:**
```html
<div class="overflow-hidden rounded-2xl border border-[#D8D9DA] bg-[#FFFFFF]">
  <table class="min-w-full text-left text-sm text-[#08121A]">
    <thead class="bg-[#F5F6F6] text-xs uppercase tracking-[0.08em] text-[#394148]">
      <tr><th class="px-4 py-3">名称</th><th class="px-4 py-3">状態</th><th class="px-4 py-3">担当</th></tr>
    </thead>
    <tbody>
      <tr class="border-t border-[#D8D9DA]"><td class="px-4 py-3 font-medium">特集ページ</td><td class="px-4 py-3 text-[#389E46]">公開中</td><td class="px-4 py-3">A. Chen</td></tr>
      <tr class="border-t border-[#D8D9DA]"><td class="px-4 py-3 font-medium">制度見直し</td><td class="px-4 py-3 text-[#394148]">下書き</td><td class="px-4 py-3">M. Sato</td></tr>
    </tbody>
  </table>
</div>
```

### Badge
- **Official naming / aliases:** Status, InlineNotification, StackNotificationManager, Toast, SnackBar
- **Preferred style:** Use small status labels and notification surfaces with explicit text and clear contrast.
- **Use when:** Use for state, inline feedback, pending work, or transient results.
- **Important states:** Neutral, positive, warning, danger, active, and dismissed where relevant.
- **Avoid:** Avoid replacing explanatory text with color chips alone.

**Tailwind implementation example:**
```html
<span class="inline-flex items-center rounded-md bg-[#F5F6F6] px-3 py-1 text-xs font-semibold text-[#0091FF]">注目</span>
```

### Dialog/Modal
- **Official naming / aliases:** Modal, Dialog, SemiModal, AppealModal
- **Preferred style:** Use light, rounded overlays with clear hierarchy, readable body copy, and one obvious primary action.
- **Use when:** Use for confirmation, focused secondary tasks, or interruption-worthy flows.
- **Important states:** Closed, open, focus trapped, destructive confirmation, and loading or submitting state.
- **Avoid:** Avoid oversized or theatrically layered modal presentations.

**Tailwind implementation example:**
```html
<div class="flex min-h-[240px] items-center justify-center bg-black/30 p-6">
  <div class="w-full max-w-md rounded-2xl bg-[#FFFFFF] p-6 text-[#08121A] shadow-sm">
    <h3 class="text-lg font-semibold">変更を破棄しますか？</h3>
    <p class="mt-2 text-sm text-[#394148]">保存していない編集内容は削除されます。</p>
    <div class="mt-6 flex justify-end gap-3">
      <button class="inline-flex h-11 items-center justify-center rounded-md border border-[#D8D9DA] px-4 text-sm font-medium">キャンセル</button>
      <button class="inline-flex h-11 items-center justify-center rounded-md bg-[#D91C0B] px-4 text-sm font-medium text-white">破棄する</button>
    </div>
  </div>
</div>
```

### Tooltip
- **Official naming / aliases:** Tooltip-like helper usage where needed
- **Preferred style:** Use only for supplementary clarification.
- **Use when:** Use for secondary help that should not interrupt the task.
- **Important states:** Hidden, shown, keyboard-focus trigger, and dismissal.
- **Avoid:** Avoid putting required instructions only in a tooltip.

**Tailwind implementation example:**
```html
<div class="relative inline-flex items-center gap-2 text-sm text-[#08121A]">
  <button class="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[#D8D9DA] bg-[#FFFFFF]">i</button>
  <div class="absolute left-10 top-1/2 w-48 -translate-y-1/2 rounded-md bg-[#08121A] px-3 py-2 text-xs text-white shadow-sm">必要な補足だけを、その場で伝える例です。</div>
</div>
```

### Progress/Loading
- **Official naming / aliases:** Loading and notification-related progress states
- **Preferred style:** Use quiet loading indicators and skeletons that do not dominate the layout.
- **Use when:** Use for async updates, content fetches, and submission feedback.
- **Important states:** Idle, loading, partial progress where available, and completion.
- **Avoid:** Avoid flashy loading treatments that compete with content.

## Do's and Don'ts
- **Do:** Keep UI product-facing, warm, and readable with explicit labels and approachable spacing.
- **Do:** Prefer UI colors over brand colors for normal product surfaces and controls.
- **Do:** Use lists, tabs, fields, and notifications as the main building blocks before inventing new shells.
- **Do:** Preserve Japanese readability and a friendly tone without sounding childish.
- **Do:** Use borders, state shape, and labels in addition to color to communicate selection and status.
- **Do not:** Do not turn the interface into a generic enterprise admin dashboard with heavy chrome.
- **Do not:** Do not overuse brand green or expressive pink as default UI paint.
- **Do not:** Do not use glassmorphism, oversized blur, or decorative gradients as the main visual language.
- **Do not:** Do not replace clear copy with icon-only or color-only communication.
- **Do not:** Do not expose brand typography as the default font for routine web UI text.
- **Do not:** Do not leave behavioral spec tokens such as field names plus sort directions visible as raw text when the UI should communicate that state structurally.

**Tailwind implementation example:**
```html
<div class="max-w-sm space-y-2 text-sm text-[#08121A]">
  <div class="flex items-center justify-between">
    <span class="font-medium">ファイルをアップロード中</span>
    <span class="text-[#394148]">64%</span>
  </div>
  <div class="h-2 overflow-hidden rounded-full bg-[#F5F6F6]">
    <div class="h-full w-[64%] bg-[#0091FF]"></div>
  </div>
</div>
```
