# Fluent 2 Design System DESIGN.md

- **Provider:** Microsoft
- **Primary reference:** https://fluent2.microsoft.design/
- **Primary product focus:** Productive cross-platform Microsoft-style applications.
- **Platforms:** Cross-platform web UI with Windows/productivity heritage and theme support.
- **Status:** Active Fluent 2 system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Productive, calm, and explicitly stateful.
- Approachable geometry and polished surfaces should support work rather than spectacle.
- The system should feel modern but not glossy or consumer-social.
- Best for productivity dashboards, enterprise tools, and Microsoft-style workflows.
- Theme-awareness and explicit states are part of the design language.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Brand (#0F6CBD):** Primary Microsoft-style action and brand emphasis.
- **Brand Pressed (#0C3B5E):** Pressed or stronger action emphasis.
- **Brand Tint (#EBF3FC):** Tinted selection, hover, and supportive surfaces.
- **Neutral Foreground (#242424):** Primary text and icon color.
- **Neutral Background (#FFFFFF):** Default canvas and card surfaces.
- **Neutral Subtle (#F5F5F5):** Low-emphasis surface and section grouping.
- **Success (#107C10):** Success and positive confirmation.
- **Danger (#D13438):** Error and destructive emphasis.

## 3. Typography Rules
- Use Segoe UI or the Fluent default stack with explicit task-oriented hierarchy.
- Text should stay readable in both compact and comfortable productivity layouts.
- Labels, metadata, and command surfaces should feel systematic and familiar to Microsoft products.
- Icons and motion should clarify focus, state, and layered navigation rather than decorate.

## 4. Component Stylings
- **Buttons and actions:** Use clear primary, secondary, subtle, and outline-emphasis hierarchies with strong state visibility.
- **Inputs and form controls:** Use token-driven inputs, dropdowns, comboboxes, switches, and date pickers with explicit labels and visible state treatment.
- **Menus, tabs, breadcrumbs, and navigation:** Use navigation panes, drawers, tabs, toolbars, and breadcrumbs that keep local controls close to the task area.
- **Cards, lists, tables, badges:** Use soft but disciplined cards, lists, tables, and badges to support productivity workflows without becoming decorative.
- **Dialogs, toasts, loading, pagination:** Use dialog, drawer, teaching bubble, toast, progress, skeleton, and loading patterns with explicit state transitions.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.
- Use `Nav` / navigation pane behavior explicitly: inline around medium and larger widths, overlay on compact widths, with plain-language labels and consistent leading icons.
- Keep command surfaces close to the work area through toolbars, split buttons, and subtle command groups rather than broad hero actions.
- Cards should stay softly rounded and token-driven, but avoid oversized glassy chrome or generic KPI-tile rows that erase Fluent’s productivity-shell character.

## 5. Layout Principles
- Use productivity-first shells with clear navigation, calm surfaces, and explicit local structure.
- Allow soft geometry, but keep layout logic more important than visual softness.
- Use subtle depth and theme-aware contrast rather than heavy shadows or blur.
- Keep commands near the work surface and preserve readable density.
- Favor polished workspaces over generic admin-panel framing.

- Keep navigation task-focused with plain-language labels, category icons, and only shallow nesting.
- Favor an inline productivity nav pane on larger widths instead of reusing a generic dashboard side shell.
- Avoid a consumer-style glossy dashboard or an oversized rounded shell; Fluent should read like Microsoft productivity software first.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Global and alias tokens remain the primary source of truth for interpretation.
- Fluent-specific navigation terms such as nav drawer and navigation pane should be preserved.
- Avoid consumer-style glassmorphism or oversized rounded dashboards when using this spec.

## Responsive and Navigation Notes
- **Mobile:** Use a compact navigation trigger that opens a panel or drawer and keep command-heavy controls close to the header.
- **Tablet:** Allow collapsible nav with strong focus and hover states, preserving productivity-oriented structure.
- **Desktop:** Restore visible navigation with calm surfaces and compact but readable spacing.
- **Navigation rule:** Navigation may be minimized, but should remain easy to expand and should not stay permanently open on narrow screens.
- **Table rule:** Keep lists and tables operationally dense, using scroll and compact command placement rather than over-carding.

- **Dashboard note:** Use an inline drawer around 260px above 640px and an overlay drawer below 640px; do not keep the same shell treatment across breakpoints.

## Official Sources
- https://fluent2.microsoft.design/
- https://fluent2.microsoft.design/color
- https://fluent2.microsoft.design/typography
- https://fluent2.microsoft.design/layout
- https://fluent2.microsoft.design/components/web/react/core/button/usage
