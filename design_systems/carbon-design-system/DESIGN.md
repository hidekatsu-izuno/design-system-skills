# Carbon Design System DESIGN.md

- **Provider:** IBM
- **Primary reference:** https://carbondesignsystem.com/
- **Primary product focus:** Serious enterprise interfaces and operational dashboards.
- **Platforms:** Web-focused enterprise products with strong desktop dashboard usage.
- **Status:** Active IBM-maintained system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Disciplined, serious, and strongly structured.
- Grid logic, clarity, and accessibility matter more than softness or decoration.
- Enterprise density is acceptable when the hierarchy stays explicit.
- Best for operational products, IBM-style shells, and data-heavy workflows.
- Should feel industrial, rigorous, and stable.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Interactive (#0F62FE):** Primary action and active emphasis.
- **Text Primary (#161616):** Primary text and icon color.
- **Text Secondary (#525252):** Secondary text and supporting metadata.
- **Background (#FFFFFF):** Primary page background.
- **Layer 01 (#F4F4F4):** First elevated or grouped layer.
- **Layer 02 (#E0E0E0):** Additional layer separation and input backgrounds.
- **Success (#24A148):** Success and positive confirmation.
- **Danger (#DA1E28):** Error and destructive emphasis.

## 3. Typography Rules
- Use IBM Plex Sans with a disciplined hierarchy and strong data readability.
- Favor concise headings, stable body text, and consistent label treatment.
- Typography should reinforce the grid and structural rhythm rather than add personality.
- Motion is restrained; shell clarity and accessibility outweigh flourish.

## 4. Component Stylings
- **Buttons and actions:** Use primary, secondary, tertiary, and ghost-style hierarchies with clear intent. Buttons should feel direct and businesslike.
- **Inputs and form controls:** Use structured inputs, combo controls, toggles, date pickers, and search with explicit labels and crisp boundaries.
- **Menus, tabs, breadcrumbs, and navigation:** Use UI-shell header, side nav, tabs, breadcrumbs, and overflow menus in a strongly structured shell.
- **Cards, lists, tables, badges:** Use cards sparingly around strong layers and tables. Carbon tables, lists, and tags should remain explicit and disciplined.
- **Dialogs, toasts, loading, pagination:** Use modal, side panel, notification, inline loading, progress, skeleton, and pagination patterns with restrained chrome.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.

## 5. Layout Principles
- Use the 2x grid and layered shell logic to create order before decoration.
- Keep dense screens readable through rhythm, spacing, and strong section framing.
- Favor sharp or minimal radii and controlled shadows over soft, floating panels.
- Let layers and shells define depth rather than colorful cards.
- Use IBM-style shell logic for dashboards, administrative products, and structured workflows.

- Use a dark Gray 100 style UI shell header as the primary frame and keep the left panel structurally separate below it.
- Avoid soft floating dashboard framing; Carbon shells should read as layered IBM product structure first.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Carbon themes and tokens should remain the primary interpretation layer.
- Layer terminology matters; preserve layer-based reasoning in prompts.
- UI shell, side nav, left panel, and 2x grid language should be preserved where relevant.

## Responsive and Navigation Notes
- **Mobile:** Use the UI shell header with a menu trigger that collapses header items into the left side nav panel.
- **Tablet:** Preserve the shell hierarchy, but keep navigation collapsible and maintain IBM-like density.
- **Desktop:** Restore the full UI shell with visible side nav and layered regions.
- **Navigation rule:** The mobile pattern should read like Carbon header-plus-side-nav behavior, with header items collapsing into navigation.
- **Table rule:** Keep structured data views intact and allow horizontal scroll before rewriting them as loose cards.

- **Dashboard note:** Mobile should still feel like Carbon UI shell header plus side-nav/left-panel behavior, not a generic white sticky header and modal drawer.

## Official Sources
- https://carbondesignsystem.com/
- https://carbondesignsystem.com/guidelines/color/overview/
- https://carbondesignsystem.com/guidelines/typography/overview/
- https://carbondesignsystem.com/guidelines/2x-grid/overview/
- https://carbondesignsystem.com/components/overview/
