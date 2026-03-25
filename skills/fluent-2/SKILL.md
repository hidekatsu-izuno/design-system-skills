---
name: fluent-2
description: Use when the task asks for UI design, frontend implementation, productivity apps, dashboards, or static mocks that should follow Fluent 2.
---

# Fluent 2 Skill

Use this skill when the output should look and behave like Fluent 2. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's productivity shell, nav pane or drawer, command surface, and soft surface hierarchy before writing code.
- Adapt the requested information architecture into Fluent 2 instead of defaulting to a generic dashboard shell.
- Prefer documented Fluent 2 component logic and naming whenever multiple solutions are plausible.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Choose shell, navigation, command surfaces, tables, forms, and states from `./DESIGN.md`.
- Implement with documented Fluent 2-style patterns first, especially for navigation panes, drawers, command bars, and calm productivity layouts.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Output Rules

- Do not show design commentary or rationale as visible UI text.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if Fluent 2 implies a more specific productivity workspace.

## Copy Rules

- Write product UI copy, not design commentary.
- Use headings and labels that describe state, content, or action.
- Do not render phrases that describe the design system itself.

## Quality Bar

- Keep the result recognizably Fluent 2 at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
