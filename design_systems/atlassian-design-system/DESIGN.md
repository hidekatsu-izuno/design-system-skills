# Atlassian Design System DESIGN.md

- **Provider:** Atlassian
- **Primary reference:** https://atlassian.design/
- **Primary product focus:** Collaboration-heavy SaaS and work-management UI.
- **Platforms:** Web-first product UI for issue, project, and operational workflows.
- **Status:** Active core Atlassian system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Dense but readable, with strong inline status and collaboration-friendly scanning.
- Grounded in semantic tokens, practical spacing, and clear local hierarchy.
- Action-oriented rather than ornamental, with emphasis on work tracking and coordination.
- Best for projects, tickets, lists, workflows, and operational SaaS surfaces.
- Should feel calm, dependable, and ready for repeated daily use.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Blue (#0C66E4):** Primary action, active state, and key navigation emphasis.
- **Blue Subtle (#E9F2FF):** Selected backgrounds and supportive highlights.
- **Text (#172B4D):** Primary body and heading text.
- **Subtle Text (#44546F):** Secondary metadata and supporting labels.
- **Surface (#FFFFFF):** Base canvas and card surface.
- **Neutral Subtle (#F7F8F9):** Panels, low-emphasis containers, and row hover.
- **Danger (#CA3521):** Destructive and error emphasis.
- **Success (#1F845A):** Success states and positive completion.

## 3. Typography Rules
- Use Atlassian Sans and compact product hierarchy with excellent scanability.
- Treat headings, metadata, lozenges, and table text as tightly integrated working typography.
- Keep hierarchy clear in dense layouts without switching to display-heavy type.
- Atlassian iconography and lozenge/status language should remain recognizable in prompts.

## 4. Component Stylings
- **Buttons and actions:** Prefer practical primary buttons with quiet secondary and link-style actions. Inline actions should remain visible in dense product contexts.
- **Inputs and form controls:** Use Textfield, Select, Popup Select, Checkbox, Radio, Toggle, and date controls with direct labels and inline validation.
- **Menus, tabs, breadcrumbs, and navigation:** Use side navigation, in-product navigation, tabs, breadcrumbs, dropdown menus, and flags with literal labels and clear current-state emphasis.
- **Cards, lists, tables, badges:** Use cards and lists sparingly around strong tables. Prefer lozenges and inline status indicators over oversized pills or decorative chips.
- **Dialogs, toasts, loading, pagination:** Use Modal Dialog, Inline Dialog, Section Message, Flag, Spinner, Skeleton, and Pagination to support workflow continuity.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.

## 5. Layout Principles
- Use left navigation and product-level structure for larger SaaS shells.
- Keep content task-oriented and reduce decorative framing around data-heavy regions.
- Use compact spacing and semantic tokens before introducing bespoke styling.
- Rely on inline status, flags, lozenges, and page-level hierarchy more than large visual containers.
- Support issue, project, and object-based page structures cleanly.

- Prefer a side-navigation-first workspace with grouped sections, strong current-state indication, and inline lozenge status treatment.
- Avoid KPI hero rows and broad dashboard framing when a context-first navigation workflow is more appropriate.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Design tokens are foundational and should remain the dominant interpretation layer.
- Inline feedback is usually preferable to modal interruption unless the task is high-risk.
- Lozenge-style status handling should be preserved in generation prompts and outputs.

## Responsive and Navigation Notes
- **Mobile:** Move left navigation behind a compact trigger and reveal it as a panel or drawer, keeping global actions in the top area.
- **Tablet:** Keep navigation discoverable but collapsible, and reduce secondary chrome before compressing core content.
- **Desktop:** Restore the product shell with visible side navigation and clear lozenge-style status treatment.
- **Navigation rule:** Favor trigger-to-panel navigation on small widths rather than a permanently expanded list.
- **Table rule:** Let tables scroll and keep row actions concise; avoid replacing all data views with oversized cards.

- **Dashboard note:** Compact navigation should still feel like Atlassian side navigation and nested workspace context, not a generic drawer-plus-cards admin shell.

## Official Sources
- https://atlassian.design/
- https://atlassian.design/foundations/color-new
- https://atlassian.design/foundations/typography
- https://atlassian.design/foundations/layout
- https://atlassian.design/components
