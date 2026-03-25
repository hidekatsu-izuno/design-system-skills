# Ant Design DESIGN.md

- **Provider:** Ant Group
- **Primary reference:** https://ant.design/
- **Primary product focus:** Enterprise web applications
- **Platforms:** Web-first enterprise UI, with secondary Ant Design Mobile variants for handheld contexts.
- **Status:** Active, v5-era system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Dense, task-first, and operational rather than atmospheric.
- Structured through predictable grids, explicit shells, and direct administrative affordances.
- Visually neutral by default, with color reserved for state and primary action emphasis.
- Best for dashboards, tables, forms, filters, and internal tooling where speed matters.
- Should feel systematic and scalable rather than custom-crafted per screen.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Primary (#1677FF):** Primary action and active interactive emphasis.
- **Success (#52C41A):** Success and positive status.
- **Warning (#FAAD14):** Caution and intermediate attention.
- **Error (#FF4D4F):** Errors and destructive emphasis.
- **Text (#1F1F1F):** Primary text on light surfaces.
- **Background (#FFFFFF):** Primary application surface.
- **Container (#F5F5F5):** Low-emphasis panels and grouped surfaces.
- **Border (#D9D9D9):** Input, table, and container borders.

## 3. Typography Rules
- Use a neutral enterprise sans stack with pragmatic hierarchy and compact spacing.
- Favor readable but efficient titles, section labels, table headers, and control text.
- Keep emphasis on clarity and scanability rather than display typography.
- Ant Design Icons are the default icon language; motion should feel brief and utilitarian.

## 4. Component Stylings
- **Buttons and actions:** Prefer clear primary, default, dashed, text, and link hierarchies. Keep the main CTA obvious and nearby secondary actions quiet but visible.
- **Inputs and form controls:** Use Input, Input.Search, Select, Cascader, AutoComplete, Checkbox, Radio, Switch, and DatePicker as explicit task-solving controls with visible status states.
- **Menus, tabs, breadcrumbs, and navigation:** Use Menu, Dropdown, Tabs, Steps, Breadcrumb, Header, and Sider patterns with literal labels and practical grouping. Avoid decorative navigation chrome.
- **Cards, lists, tables, badges:** Use Card, Table, List, Badge, and Tag patterns to structure dense operational information. Tables are first-class and should remain strong when comparison matters.
- **Dialogs, toasts, loading, pagination:** Use Modal, Drawer, Popconfirm, Message, Notification, Spin, Skeleton, Progress, and Pagination to support admin workflows without ambiguity.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.
- The default shell should read as `Layout` with `Header`, `Sider`, and `Content`, not as an abstract generic sidebar app.
- Preserve Ant’s strong Table, Form, and filter-toolbar rhythm: search, segmented filters, batch actions, and pagination should feel adjacent to the data area rather than detached hero controls.
- Use `Tag` and `Badge` as concise inline state markers and avoid oversized rounded summary chips that blur into other systems.

## 5. Layout Principles
- Use management shells with header, sider, and content regions when the information architecture is broad.
- Support dense table, filter, and form areas without collapsing hierarchy.
- Use moderate radii, regular panel spacing, and utilitarian shadows for overlays rather than soft consumer-style elevation.
- Prefer operational symmetry and explicit action bars over expressive composition.
- Keep dashboards grounded in filtering, summaries, and data display rather than hero surfaces.

- Keep the shell `Layout.Sider`-first and enterprise-web pragmatic rather than treating mobile navigation as a generic modal drawer pattern.
- Dense work areas, compact sections, and left-side navigation should define the page before decorative summary framing.
- Avoid a generic modal-drawer-plus-cards mobile shell; the small-screen pattern should still feel like collapsed `Sider` behavior with Ant-style structure and dense data-first organization.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Theming is token-driven and algorithmic; preserve seed/map/alias token thinking when generating new screens.
- Dark mode support is strong, but light enterprise shells remain the default reference.
- Ant-specific names such as `Input.Search`, `Drawer`, and `Sider` should be preserved when they materially affect prompt interpretation.

## Responsive and Navigation Notes
- **Mobile:** Collapse `Sider` navigation behind a compact trigger and reveal it as an overlay or drawer-like panel.
- **Tablet:** Allow partially collapsed side navigation with labels hidden or shortened, keeping header utilities visible.
- **Desktop:** Use the full `Layout` shell with persistent side navigation and dense content regions.
- **Navigation rule:** Treat navigation as a collapsible `Sider`, not as a permanently expanded mobile sidebar.
- **Table rule:** Preserve table density and filters through scroll, drawers, or stacked controls without losing operational clarity.

- **Dashboard note:** Use a collapsible `Layout.Sider` pattern with a zero-width trigger on smaller screens; do not replace Ant navigation with a generic app drawer shell.

## Official Sources
- https://ant.design/
- https://ant.design/docs/spec/introduce
- https://ant.design/docs/spec/colors
- https://ant.design/docs/spec/font
- https://ant.design/components/overview
