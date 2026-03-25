# Primer Product UI DESIGN.md

- **Provider:** GitHub
- **Primary reference:** https://primer.style/product
- **Primary product focus:** GitHub-like product interfaces and developer tools.
- **Platforms:** Web-first product UI for desktop-heavy engineering workflows.
- **Status:** Active GitHub-maintained system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Quiet, practical, and developer-tool oriented.
- Utility and content hierarchy should dominate over decoration.
- The surface language should feel systematic, understated, and trustworthy.
- Best for settings, repositories, management tools, and workflow-heavy product pages.
- Should read like a serious software product, not a themed dashboard.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Accent (#0969DA):** Primary interactive emphasis and link/action color.
- **Success (#1F883D):** Success and positive state.
- **Attention (#9A6700):** Warning and needs-attention emphasis.
- **Danger (#CF222E):** Error and destructive emphasis.
- **Canvas Default (#FFFFFF):** Primary page background.
- **Canvas Subtle (#F6F8FA):** Muted panels and section backgrounds.
- **Foreground Default (#1F2328):** Primary text and icon color.
- **Border Default (#D0D7DE):** Borders, table dividers, and field boundaries.

## 3. Typography Rules
- Use GitHub-style product typography with restrained hierarchy and strong metadata clarity.
- Keep headings, section labels, and body text practical rather than expressive.
- Developer-facing text should remain calm, compact, and highly readable.
- Octicon/Primer naming conventions should remain preserved where they materially clarify behavior.

## 4. Component Stylings
- **Buttons and actions:** Use calm primary and secondary action hierarchy with flat borders and modest emphasis.
- **Inputs and form controls:** Use text inputs, search, selects, toggles, and validation patterns that feel practical and explicit.
- **Menus, tabs, breadcrumbs, and navigation:** Use PageLayout, NavList, underline nav, ActionMenu, breadcrumbs, and context panes to orient larger product surfaces.
- **Cards, lists, tables, badges:** Use flat borders, muted containers, tables, timelines, and compact status labels rather than decorative dashboard tiles.
- **Dialogs, toasts, loading, pagination:** Use dialogs, flash messages, loading states, and pagination in a restrained product-oriented way.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.

## 5. Layout Principles
- Use page headers, page layout primitives, side nav, and context panes to organize work.
- Favor flat borders, muted surfaces, and whitespace discipline over repeated heavy cards.
- Keep layout calm and semantically landmarked so product structure is obvious.
- Avoid glossy shells and over-rounded surfaces.
- Support both settings-style pages and denser data displays cleanly.

- Use `PageLayout` as a real sidebar/main/pane relationship with `NavList` as a vertical grouped navigation primitive.
- Avoid broad KPI-card dashboard framing; the page should read like a GitHub product surface with breadcrumbs, panes, and content landmarks.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Primer primitives and semantic variables remain the most important interpretation layer.
- PageLayout and ActionMenu-style navigation behavior should remain visible in prompts and HTML generation.
- Quiet text-forward navigation is more correct than icon-heavy shells for this system.

## Responsive and Navigation Notes
- **Mobile:** Collapse dense navigation into an ActionMenu-like trigger or overflow menu and keep the page header calm and text-forward.
- **Tablet:** Preserve PageLayout structure but allow nav and context panes to collapse before the main content does.
- **Desktop:** Restore side navigation, underline nav, and context panes as needed for product orientation.
- **Navigation rule:** Mobile navigation should feel like a GitHub product overflow or action menu, not a themed full-screen drawer.
- **Table rule:** Maintain practical tables and lists with scroll or compact controls rather than converting everything into tiles.

- **Dashboard note:** Compact widths should rely on `ActionMenu`/overflow plus preserved page landmarks, not on a universal dashboard shell.

## Official Sources
- https://primer.style/product
- https://primer.style/product/primitives/color
- https://primer.style/product/primitives/typography
- https://primer.style/product/components/page-layout
- https://primer.style/product/components
