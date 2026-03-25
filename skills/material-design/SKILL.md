---
name: material-design
description: Use when the task asks for UI design, frontend implementation, app surfaces, dashboards, or static mocks that should follow Material Design.
---

# Material Design Skill

Use this skill when the output should look and behave like Material Design. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's top app bar, drawer or rail, adaptive layout, tonal containers, and data patterns before writing code.
- Adapt the requested information architecture into Material patterns instead of defaulting to a generic dashboard shell.
- Prefer documented Material component logic and naming whenever multiple solutions are plausible.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Choose shell, navigation, cards, tables, forms, and states from `./DESIGN.md`.
- Implement with documented Material-style patterns first, especially for app bars, drawers, rails, tonal surfaces, and adaptive shells.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Output Rules

- Do not show design commentary or rationale as visible UI text.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if Material implies a clearer app shell or adaptive navigation pattern.

## Copy Rules

- Write product UI copy, not design commentary.
- Use headings and labels that describe state, content, or action.
- Do not render phrases that describe the design system itself.

## Quality Bar

- Keep the result recognizably Material at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
