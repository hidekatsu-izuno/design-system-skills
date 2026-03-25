---
name: ant-design
description: Use when the task asks for UI design, frontend implementation, dashboards, forms, tables, or static mocks that should follow Ant Design rather than a generic product UI.
---

# Ant Design Skill

Use this skill when the output should look and behave like Ant Design. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## Don't Rules

- Do not show design commentary or rationale as visible UI text.
- Do not render specification notes, implementation notes, or behavior explanations as visible UI text.
- Do not convert explanatory prose from `AGENTS.md` such as screen overviews, initial-state notes, validation notes, or interaction notes into visible UI copy.
- Treat explanatory text in `AGENTS.md` as author guidance unless it is explicitly specified as a user-facing label, helper text, message, sample value, table cell, or other UI string.
- Do not remove labels, item names, sample rows, status values, toast messages, dialog text, or other visible data that the request or source specification explicitly includes for the UI.
- Do not add sections, cards, notes, or headings that are not present in the request or source specification; if `AGENTS.md` does not define a block such as a memo or processing note, do not generate it.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if Ant Design implies a more specific shell or component treatment.
- Do not add taglines, promotional value statements, or landing-page style lead text unless explicitly requested.
- Do not add descriptive helper text for the whole screen, search area, table, or form unless the task explicitly requires it.
- Do not invent summary metrics, counts, status totals, badges, or other data points that are not present in the request or source specification.
- Do not render phrases that describe the design system itself.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's shell, navigation, density, table, form, and status patterns before writing code.
- Adapt the requested information architecture into Ant Design instead of defaulting to a generic dashboard shell.
- Prefer Ant Design component logic and naming whenever multiple solutions are plausible.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Distinguish user-facing strings from author guidance in `AGENTS.md`; if text explains the spec rather than the product UI, do not render it, but keep explicit UI labels, sample content, and messages.
- If the layout needs a drawer or mobile menu in static HTML, implement it as a CSS-only drawer controlled by `:checked`; do not rely on JavaScript-only menu toggles.
- In forms and search areas, place at most two primary input fields per row; only clearly secondary helper controls may break this rule.
- Choose shell, navigation, tables, cards, actions, and states from `./DESIGN.md`.
- Implement with documented Ant Design-style patterns first, especially for forms, data tables, filters, tags, and layout.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Copy Rules

- Write product UI copy, not design commentary.
- Default to operational system UI copy, not marketing copy.
- Use headings and labels that describe state, content, or action.
- When a string is not explicitly required as UI copy, prefer omitting it over summarizing specification text into subtitles, helper text, annotations, or status descriptions.
- If the specification includes concrete sample data or example content for visible fields, render it as UI content rather than deleting it as explanation text.
- Suppress wrapping for short strings of 8 characters or fewer in compact UI elements; use `white-space: nowrap` or an equivalent treatment so labels do not split awkwardly.

## Quality Bar

- Keep the result recognizably Ant Design at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
