---
name: material-design
description: Use when the task asks for UI design, frontend implementation, app surfaces, dashboards, or static mocks that should follow Material Design.
---

# Material Design Skill

Use this skill when the output should look and behave like Material Design. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## MUST

- If the request or source specification implies a side menu, implement it as a drawer pattern rather than a fixed sidebar-only layout.
- In static HTML, implement drawer open and close behavior with CSS-only state using `:checked`; do not rely on JavaScript-only toggles.
- Treat a side menu without an explicit open or close trigger as invalid.
- Implement the drawer shell before page-specific content whenever side navigation is required.
- Convert behavioral requirements such as sort order, filter state, pagination state, and view toggles into UI controls or visible state indicators rather than leaving them as raw specification text.

## Don't Rules

- Do not show design commentary or rationale as visible UI text.
- Do not render specification notes, implementation notes, or behavior explanations as visible UI text.
- Do not convert explanatory prose from `AGENTS.md` such as screen overviews, initial-state notes, validation notes, or interaction notes into visible UI copy.
- Treat explanatory text in `AGENTS.md` as author guidance unless it is explicitly specified as a user-facing label, helper text, message, sample value, table cell, or other UI string.
- Do not remove labels, item names, sample rows, status values, toast messages, dialog text, or other visible data that the request or source specification explicitly includes for the UI.
- Do not add sections, cards, notes, or headings that are not present in the request or source specification; if `AGENTS.md` does not define a block such as a memo or processing note, do not generate it.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if Material implies a clearer app shell or adaptive navigation pattern.
- Do not add taglines, promotional value statements, or landing-page style lead text unless explicitly requested.
- Do not add descriptive helper text for the whole screen, search area, table, or form unless the task explicitly requires it.
- Do not invent summary metrics, counts, status totals, badges, or other data points that are not present in the request or source specification.
- Do not leave lists, tables, or other collection views empty in a mockup just because live data is unavailable; use representative sample content unless the specification calls for an empty state.
- Do not render phrases that describe the design system itself.

## Explicit Failure Cases

- A left-side vertical menu that is always visible without drawer behavior does not satisfy a drawer requirement.
- A side menu with no trigger in the app bar or equivalent visible control is invalid.
- A side menu that behaves the same on mobile and desktop, without a closed-by-default mobile state, is invalid unless the specification explicitly requires otherwise.
- A layout that uses a narrow icon-stack rail as a substitute for a conventional side menu is invalid when the request expects a drawer.
- Raw strings such as `organization_code ASC` or `updated_at DESC` shown as plain body text are invalid when they describe sort behavior rather than user-facing copy.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's top app bar, drawer or rail, adaptive layout, tonal containers, and data patterns before writing code.
- Adapt the requested information architecture into Material patterns instead of defaulting to a generic dashboard shell.
- Prefer documented Material component logic and naming whenever multiple solutions are plausible.

## Pre-Implementation Checklist

Before writing HTML, explicitly confirm:

- Whether the screen requires a side menu or drawer.
- Whether that side menu must open and close as a drawer rather than remain a fixed sidebar.
- Whether the output is static HTML and therefore needs `:checked`-based CSS-only drawer control.
- Whether the top app bar needs a drawer trigger.
- Whether any specification text actually describes behavior or state that must be rendered as controls, chips, selected headers, segmented buttons, or similar UI.

If any answer is yes, implement the drawer shell before page-specific content.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Distinguish user-facing strings from author guidance in `AGENTS.md`; if text explains the spec rather than the product UI, do not render it, but keep explicit UI labels, sample content, and messages.
- Translate behavior specifications such as sorting, filtering, tabs, pagination, and selection state into appropriate interactive UI or stateful visual treatment instead of emitting raw text tokens.
- In mockups or static implementations, populate visible collections such as tables, lists, cards, and detail panes with representative sample data unless the request explicitly requires an empty state.
- If the layout needs a drawer or mobile menu in static HTML, implement it as a CSS-only drawer controlled by `:checked`; do not rely on JavaScript-only menu toggles.
- In forms and search areas, place at most two primary input fields per row; only clearly secondary helper controls may break this rule.
- Choose shell, navigation, cards, tables, forms, and states from `./DESIGN.md`.
- Implement with documented Material-style patterns first, especially for app bars, drawers, rails, tonal surfaces, and adaptive shells.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Acceptance Criteria For Drawer

A valid drawer implementation must include:

- A menu trigger in the app bar or equivalent top-level control.
- A hidden checkbox or equivalent CSS-only state control for static HTML.
- A label or equivalent control tied to that state.
- A drawer panel element.
- An overlay, backdrop, or equivalent dismissal surface.
- Responsive behavior where mobile is closed by default and desktop is open, pinned, or otherwise explicitly differentiated.

## Acceptance Criteria For Behavioral Specs

Behavioral requirements from the specification must be represented as UI structure, not raw prose.

- Sort requirements must appear as sortable headers, sort chips, segmented controls, menus, or another explicit sort-state pattern.
- Filter and toggle requirements must appear as controls with visible selected state.
- Pagination and view-mode requirements must appear as navigation or mode-switching controls.
- State changes such as default sort, alternate sort, selected tab, or active filter must be legible from the UI without relying on explanatory text.

## Copy Rules

- Write product UI copy, not design commentary.
- Default to operational system UI copy, not marketing copy.
- Use headings and labels that describe state, content, or action.
- When a string is not explicitly required as UI copy, prefer omitting it over summarizing specification text into subtitles, helper text, annotations, or status descriptions.
- Do not surface implementation-style tokens such as field names plus sort directions as plain text when they should be represented by UI state.
- If the specification includes concrete sample data or example content for visible fields, render it as UI content rather than deleting it as explanation text.
- For mockups, prefer realistic sample rows and values over blank placeholders in data views unless the intended state is explicitly empty.
- Suppress wrapping for short strings of 8 characters or fewer in compact UI elements; use `white-space: nowrap` or an equivalent treatment so labels do not split awkwardly.

## Final Audit

Before finalizing, verify:

- The result does not replace a required drawer with a fixed sidebar-only layout.
- A drawer trigger exists when side navigation is required.
- Static HTML drawer behavior works through `:checked`.
- Visible UI does not include explanatory prose from the specification.
- Behavioral requirements such as sort order or alternate ordering are expressed as UI state or controls, not dumped as raw strings.
- Explicit labels, actions, messages, and sample data from the specification remain present.

If any item fails, revise before returning.

## Quality Bar

- Keep the result recognizably Material at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
