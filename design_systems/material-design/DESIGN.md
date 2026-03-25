# Material Design DESIGN.md

- **Provider:** Google
- **Primary reference:** https://m3.material.io/
- **Primary product focus:** Adaptive cross-platform product UI.
- **Platforms:** Cross-platform guidance with Android as the canonical reference and strong large-screen behavior.
- **Status:** Active Material 3 system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Expressive, structured, and modern without becoming ornamental.
- Semantic roles, adaptive shells, and layered surfaces define the visual language.
- Primary and secondary emphasis should be obvious through role, tone, and shape rather than decoration.
- Best for cross-platform product screens that must scale from mobile to desktop.
- The design should feel alive and responsive, but never playful for its own sake.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Primary (#6750A4):** Main action color and selected-state emphasis.
- **On Primary (#FFFFFF):** Text and icons on primary-filled surfaces.
- **Secondary (#625B71):** Supporting emphasis and alternate accents.
- **Tertiary (#7D5260):** Expressive accent for supportive highlights.
- **Surface (#FFFBFE):** Base app surface and page background.
- **Surface Variant (#E7E0EC):** Container backgrounds, dividers, and low-emphasis grouping.
- **On Surface (#1C1B1F):** Primary text and icon color on light surfaces.
- **Outline (#79747E):** Borders, strokes, and inactive emphasis.

## 3. Typography Rules
- Use Roboto or the platform-default Material stack with role-based type styles.
- Favor display/headline/title/body/label roles over one-off text sizing.
- Let labels, helper text, and metadata reinforce hierarchy rather than decorate surfaces.
- Material Symbols and motion guidance are core supporting systems.

## 4. Component Stylings
- **Buttons and actions:** Use filled, filled tonal, outlined, and text buttons with clear role-based hierarchy. Keep the primary action obvious and nearby secondary actions quiet.
- **Inputs and form controls:** Use filled or outlined text fields, exposed dropdown menus, autocomplete, checkbox, radio, switch, and picker patterns with visible labels and helper text.
- **Menus, tabs, breadcrumbs, and navigation:** Use navigation bar, rail, drawer, top app bar, tabs, and menus according to destination count and screen width.
- **Cards, lists, tables, badges:** Use tonal containers, cards, lists, tables, and chips to group content semantically. Avoid flattening every summary into identical tiles.
- **Dialogs, toasts, loading, pagination:** Use dialogs, bottom sheets, snackbars, progress, and loading states that clarify task flow without excessive interruption.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.
- Prefer Top App Bar plus modal navigation drawer on compact widths, then Navigation Rail plus supporting pane on wider widths; do not reuse the same sidebar shell at every breakpoint.
- Summary areas should read as tonal containers and elevated cards with Material shape scale, not as generic flat white admin tiles.
- Use chips, segmented filters, and list rows as secondary organization devices around tables instead of turning all status into large dashboard badges.

## 5. Layout Principles
- Use adaptive shells with top app bars, navigation rails, drawers, and supporting panes based on width and complexity.
- Prefer semantic color roles, tonal containers, and shape scale over arbitrary decoration.
- Use 4dp-based spacing, medium rounding, and measured elevation to separate surfaces.
- Mobile should stay single-column while larger screens may introduce rails and supporting panes.
- Let role-driven containers and adaptive hierarchy do more work than borders or generic enterprise panels.

- Prefer top app bar + drawer / rail transitions and tonal container hierarchy over a universal KPI-card dashboard row.
- Supporting panes and role-based containers should take precedence over one repeated four-card hero pattern.
- Avoid a flat white enterprise admin shell; Material surfaces should be separated by color roles, elevation, and shape rather than by heavy border grids alone.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- This file is both a semantic design source and a generation spec; preserve role-based language and concrete tokens together.
- Dynamic color, color roles, shape scale, and motion remain interpretation-critical concepts.
- Avoid glassmorphism, fixed desktop sidebars on mobile, or one-radius-fits-all dashboard styling.

## Responsive and Navigation Notes
- **Mobile:** Use a top app bar with a menu icon that opens a left-side temporary navigation drawer. Do not leave a rail or permanent drawer visible.
- **Tablet:** Prefer a navigation rail, optionally paired with a supporting pane, and let secondary content wrap under the app bar as needed.
- **Desktop:** Allow rail, drawer, and supporting pane combinations as adaptive shell elements rather than one fixed sidebar.
- **Navigation rule:** Material navigation should shift between drawer and rail by width; mobile access should be icon-triggered.
- **Table rule:** Dense tables may scroll horizontally, but important actions should stay reachable from cards or header actions.

- **Dashboard note:** Compact widths should open into a modal drawer from the top app bar; larger widths should switch to rail plus supporting-pane composition instead of preserving the same dashboard scaffold.

## Official Sources
- https://m3.material.io/
- https://m3.material.io/styles/color/roles
- https://m3.material.io/styles/typography/overview
- https://m3.material.io/foundations/layout/understanding-layout/overview
- https://m3.material.io/components
