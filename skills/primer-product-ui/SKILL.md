---
name: primer-product-ui
description: Use when the task asks for UI design, frontend implementation, developer tools, dashboards, or static mocks that should follow Primer Product UI.
---

# Primer Product UI Skill

Use this skill when the output should look and behave like Primer Product UI. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's PageLayout, NavList, UnderlineNav, ActionMenu, and quiet workspace patterns before writing code.
- Adapt the requested information architecture into Primer patterns instead of defaulting to a generic dashboard shell.
- Prefer documented Primer component logic and naming whenever multiple solutions are plausible.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Choose shell, navigation, lists, tables, panes, and states from `./DESIGN.md`.
- Implement with documented Primer-style patterns first, especially for page layout, navigation lists, action menus, and restrained developer-product surfaces.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Output Rules

- Do not show design commentary or rationale as visible UI text.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if Primer implies a quieter product workspace.

## Copy Rules

- Write product UI copy, not design commentary.
- Use headings and labels that describe state, content, or action.
- Do not render phrases that describe the design system itself.

## Quality Bar

- Keep the result recognizably Primer Product UI at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
