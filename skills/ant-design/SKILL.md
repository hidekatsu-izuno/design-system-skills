---
name: ant-design
description: Use when the task asks for UI design, frontend implementation, dashboards, forms, tables, or static mocks that should follow Ant Design rather than a generic product UI.
---

# Ant Design Skill

Use this skill when the output should look and behave like Ant Design. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's shell, navigation, density, table, form, and status patterns before writing code.
- Adapt the requested information architecture into Ant Design instead of defaulting to a generic dashboard shell.
- Prefer Ant Design component logic and naming whenever multiple solutions are plausible.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Choose shell, navigation, tables, cards, actions, and states from `./DESIGN.md`.
- Implement with documented Ant Design-style patterns first, especially for forms, data tables, filters, tags, and layout.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Output Rules

- Do not show design commentary or rationale as visible UI text.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if Ant Design implies a more specific shell or component treatment.

## Copy Rules

- Write product UI copy, not design commentary.
- Use headings and labels that describe state, content, or action.
- Do not render phrases that describe the design system itself.

## Quality Bar

- Keep the result recognizably Ant Design at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
