---
name: digital-agency-design-system
description: Use when the task asks for UI design, frontend implementation, service pages, dashboards, or static mocks that should follow the Japan Digital Agency Design System.
---

# Digital Agency Design System Skill

Use this skill when the output should look and behave like the Digital Agency Design System. Read [./DESIGN.md](./DESIGN.md) first and treat it as the source of truth for layout, components, colors, typography, and UI constraints.

## Working Model

- Read `./DESIGN.md` before making any visual or structural decision.
- Extract the system's public-service clarity, explicit labeling, border-led structure, and drawer or mobile-menu patterns before writing code.
- Adapt the requested information architecture into Digital Agency patterns instead of defaulting to a generic dashboard shell.
- Prefer documented Digital Agency component logic and naming whenever multiple solutions are plausible.

## Workflow

- Understand the user's content, task flow, and required screen regions first.
- Preserve the requested information architecture and labels unless the task explicitly changes them.
- Choose shell, navigation, sections, tables, notices, and states from `./DESIGN.md`.
- Implement with documented Digital Agency-style patterns first, especially for clear labels, strong borders, service-page structure, and plain operational UI.
- If a static mock needs icons and the native icon set is unavailable, follow the fallback guidance in `./DESIGN.md`.

## Output Rules

- Do not show design commentary or rationale as visible UI text.
- Do not render specification notes, implementation notes, or behavior explanations as visible UI text.
- Do not invent visual treatments that conflict with `./DESIGN.md`.
- Do not flatten the result into a generic enterprise dashboard if the service-oriented guidance implies a plainer public-service structure.

## Copy Rules

- Write product UI copy, not design commentary.
- Default to operational system UI copy, not marketing copy.
- Use headings and labels that describe state, content, or action.
- Do not add taglines, promotional value statements, or landing-page style lead text unless explicitly requested.
- Do not add descriptive helper text for the whole screen, search area, table, or form unless the task explicitly requires it.
- Do not invent summary metrics, counts, status totals, badges, or other data points that are not present in the request or source specification.
- Do not render phrases that describe the design system itself.

## Quality Bar

- Keep the result recognizably Digital Agency at the shell, component, spacing, and state level.
- Prefer stronger component fidelity over generic visual similarity.
