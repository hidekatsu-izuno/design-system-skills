# Ant Design Review

## Design system
Ant Design

## Sources consulted
- https://ant.design/components/layout/
- https://ant.design/docs/spec/buttons/
- https://ant.design/components/table/
- https://ant.design/components/menu/
- https://ant.design/components/typography/
- https://4x.ant.design/docs/spec/colors

## Overall assessment
The mock is directionally correct for an enterprise dashboard, but it reads more like a generic Tailwind admin screen than an Ant Design page. The layout structure is acceptable, yet the visual language is too soft and decorative compared with Ant Design’s more direct, practical, and component-driven style.

## Matches
- Uses a classic dashboard shell with a left navigation region and a main content area, which is consistent with Ant Design’s dashboard and management layouts.
- Organizes the page into summary metrics, alerts, approvals, and a data table, matching Ant Design’s strength in dense operational screens.
- Keeps action labels literal and task-oriented, which aligns with Ant Design’s navigation and button guidance.

## Differences
- The mock relies on rounded-full controls, soft shadows, and a glass-like header treatment. Ant Design’s guidance is more utilitarian: moderate radii, predictable grid alignment, and restrained panel styling.
- The left navigation is flat and numbered, while Ant Design’s menu patterns support top or side navigation with literal labels and multi-level structure.
- The page uses a single prominent primary action plus several repeated call-to-action styles, but Ant Design’s button guidance emphasizes a clear hierarchy with one primary action per button group and lighter default/text/link alternatives.
- The table is rendered as a plain HTML table without the richer Ant Design table behaviors that are central to the system: sorting, filters, selection, row actions, and sticky handling.
- The mock’s badges and status pills are visually heavier than Ant Design’s more compact data-display patterns.

## Severity / priority
Medium. The information architecture is solid, but the visual styling and component hierarchy need tightening to look like Ant Design rather than a generic dashboard.

## Recommended HTML changes
- Replace the glass header and rounded-full controls with squarer, more utilitarian surfaces and standard Ant-style button hierarchy.
- Convert the sidebar into a more literal Ant-style menu with nested items and a clearer active state.
- Add a table toolbar with filter/sort affordances and more compact row actions.
- Reduce shadow use and soften the page less aggressively with cleaner borders and more neutral spacing.
- Make status indicators smaller and more system-like, with less emphasis on decorative pill styling.

## Recommended DESIGN.md changes
- Tighten the layout guidance around header + sider + content shells so the spec favors functional dashboards over decorative admin frames.
- Clarify the button hierarchy, especially that primary buttons should remain singular within a local action group and that text/default buttons should carry secondary work.
- Strengthen the table guidance to call out sorting, filtering, selection, and row actions as first-class Ant patterns.
- Reduce any language that implies soft consumer-style rounding or shadow-heavy composition; Ant is more restrained and operational.
