---
name: spectrum
description: Use when the task asks for UI design, frontend implementation, creative-tool interfaces, dashboards, or static mocks that should follow Adobe Spectrum.
---

# Spectrum Skill

Use this skill when the output should look and behave like Adobe Spectrum. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's workspace shell, trays, action menus, table views, and quiet creative-tool patterns before writing code.
- Adapt the requested information architecture into Spectrum patterns instead of defaulting to a generic dashboard shell.
- Prefer documented Spectrum component logic and naming whenever multiple solutions are plausible.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Choose shell, navigation, menus, tables, panels, and states from `./DESIGN.md`.
- Implement with documented Spectrum-style patterns first, especially for action menus, trays, table views, and polished workspace organization.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Output Rules

- Do not show design commentary or rationale as visible UI text.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if Spectrum implies a clearer workspace or tool surface.

## Copy Rules

- Write product UI copy, not design commentary.
- Use headings and labels that describe state, content, or action.
- Do not render phrases that describe the design system itself.

## Quality Bar

- Keep the result recognizably Spectrum at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
