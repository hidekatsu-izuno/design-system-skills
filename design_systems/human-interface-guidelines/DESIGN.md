# Human Interface Guidelines DESIGN.md

- **Provider:** Apple
- **Primary reference:** https://developer.apple.com/design/human-interface-guidelines/
- **Primary product focus:** Interfaces that should feel native to Apple platforms.
- **Platforms:** Apple platform apps and Apple-influenced web adaptations.
- **Status:** Active Apple guidance.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Native, restrained, and content-led.
- Familiar controls and platform metaphors matter more than brand-heavy styling.
- The interface should support the content quietly and precisely.
- Best for Apple-style settings, sidebars, split views, and grouped app surfaces.
- Custom ornament should stay subordinate to platform conventions.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **System Blue (#007AFF):** Primary action color and interactive emphasis.
- **System Green (#34C759):** Success and positive confirmation.
- **System Orange (#FF9500):** Caution and intermediate attention.
- **System Red (#FF3B30):** Destructive actions and errors.
- **Background (#FFFFFF):** Primary light background.
- **Secondary Background (#F2F2F7):** Grouped backgrounds and panels.
- **Label (#1C1C1E):** Primary text color on light surfaces.
- **Separator (#C6C6C8):** Dividers and low-emphasis strokes.

## 3. Typography Rules
- Use the San Francisco family or the closest Apple-native stack.
- Maintain a clear title/body/label hierarchy without forcing enterprise density.
- Group text, controls, and metadata in native-feeling spacing relationships.
- SF Symbols and subtle motion are the expected supporting languages.

## 4. Component Stylings
- **Buttons and actions:** Use native-looking filled, bordered, and plain actions with clear hierarchy and minimal over-branding.
- **Inputs and form controls:** Use text fields, pickers, toggles, segmented controls, radios, checkboxes where appropriate, and date pickers with platform-consistent behavior.
- **Menus, tabs, breadcrumbs, and navigation:** Use sidebars, split views, tab bars, segmented controls, toolbars, and sheets instead of generic web navigation constructs when possible.
- **Cards, lists, tables, badges:** Prefer grouped lists, inset tables, and calm summary containers over KPI-tile dashboards. Status should remain subtle.
- **Dialogs, toasts, loading, pagination:** Use alerts, sheets, banners, and progress indicators in a platform-native way and avoid noisy transient patterns.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.
- Prefer sidebar plus split-view selection patterns, grouped list sections, inset tables, and quiet toolbars as the primary component grammar for data-rich screens.
- In compact widths, switch view families with tab bars or segmented controls rather than inventing a generic web drawer.
- Keep status treatment subtle and native-feeling; avoid enterprise lozenges, large warning panels, or a dashboard row of equal KPI tiles.

## 5. Layout Principles
- Use content-first composition with grouped sections, split views, and quiet toolbars.
- Adjust layout, spacing, and control treatment by platform family rather than forcing one universal shell.
- Use blur and material only when it reads as platform-native structure.
- Avoid dashboard framing that overemphasizes metrics at the expense of content.
- Keep motion, depth, and hierarchy subtle and platform-consistent.

- Prefer sidebar + split view + grouped lists as the dominant composition, with native-feeling content groupings instead of KPI-tile dashboards.
- Let compact tab bars or segmented controls take over in compact widths instead of preserving a generic admin shell.
- The page should feel like an Apple app screen adapted to the web, not like an enterprise dashboard with Apple colors and typography.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Apple-native interaction metaphors should override generic web-admin patterns.
- SF Symbols and system color semantics are core interpretation anchors.
- Avoid forcing enterprise-style sidebar/dashboard treatment when a grouped native layout is a better fit.

## Responsive and Navigation Notes
- **Mobile:** Prefer compact tab bars, segmented controls, or toolbar-driven navigation over a generic admin drawer.
- **Tablet:** Sidebar and split-view patterns are appropriate, but they should collapse into compact top-level switching in compact width.
- **Desktop:** Restore native-feeling sidebars, split views, and quiet toolbars.
- **Navigation rule:** Compact widths should feel like Apple compact navigation, not like a web app forcing a persistent menu.
- **Table rule:** Use grouped lists, inset tables, or horizontal scroll as needed, while preserving native-feeling spacing.

- **Dashboard note:** Avoid dashboard hero cards and forced web-admin framing; compact widths should feel like Apple compact navigation rather than a shrunk desktop dashboard.

## Official Sources
- https://developer.apple.com/design/human-interface-guidelines/
- https://developer.apple.com/design/human-interface-guidelines/color
- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/layout
- https://developer.apple.com/design/human-interface-guidelines/controls
