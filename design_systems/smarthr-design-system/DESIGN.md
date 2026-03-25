# SmartHR Design System DESIGN.md

- **Provider:** SmartHR
- **Primary reference:** https://smarthr.design/
- **Primary product focus:** Japanese business SaaS, HR workflows, and back-office tools.
- **Platforms:** Primary web product UI with desktop-heavy business use.
- **Status:** Active SmartHR-maintained system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Trustworthy, approachable, and operationally calm.
- The interface should feel dependable and readable for business workflows.
- Visual language is friendly but not casual or playful.
- Best for HR SaaS, forms, administrative flows, and daily back-office work.
- Clarity and accessibility should always outrank personality.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Primary (#00C4CC):** Main action and brand-led emphasis.
- **Primary Tint (#E5FAFB):** Soft highlight and selected-state background.
- **Text (#23221F):** Primary text color.
- **Background (#FFFFFF):** Base application surface.
- **Subtle Surface (#F8F7F6):** Panels, grouped sections, and low-emphasis containers.
- **Border (#D6D3D1):** Table, field, and section borders.
- **Warning (#FF9900):** Caution and pending attention.
- **Danger (#E5484D):** Error and destructive emphasis.

## 3. Typography Rules
- Use clear Japanese business-product typography with concise labels and straightforward hierarchy.
- Favor dependable body text, obvious labels, and readable form guidance.
- Avoid display-heavy hero type or overly playful metadata treatment.
- Icons and supporting motion should feel helpful and light, never busy.

## 4. Component Stylings
- **Buttons and actions:** Use practical primary and secondary actions with approachable but controlled styling.
- **Inputs and form controls:** Use explicit forms, search, selects, toggles, radios, checkboxes, and validation patterns with strong readability.
- **Menus, tabs, breadcrumbs, and navigation:** Use simple grouped navigation, tab bars, and business-product wayfinding. Keep labels explicit and easy to scan.
- **Cards, lists, tables, badges:** Use calm cards, tables, lists, and soft status chips to support back-office tasks without visual noise.
- **Dialogs, toasts, loading, pagination:** Use dialogs, notices, loading states, and pagination that preserve business-product trust and clarity.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.
- Treat `TabBar` as the primary screen-level switcher and use `Reel` behavior on mobile when tabs overflow.
- Prefer SmartHR-style feedback and support components such as `NotificationBar`, `ResponseMessage`, `InformationPanel`, `StatusLabel`, `Table`, and `AppNavi` / `SideNav` where relevant.
- Keep chips and badges soft and informational only; do not let chip-heavy navigation or generic dashboard tiles dominate the product shell.

## 5. Layout Principles
- Use straightforward business-product shells with stable grouping and minimal decorative chrome.
- Support form-heavy and back-office flows with clear labels and quiet hierarchy.
- Use gentle rounding and soft but restrained surfaces.
- Keep filters, table regions, and summary areas calm and legible.
- Avoid chip-heavy or overly playful dashboard framing.

- Use `TabBar` as the primary view-switching shell with a clear underline and a calm back-office product rhythm.
- Avoid drawer-first or sidebar-first admin framing and avoid generic overview-card dashboards when a tab-scoped product view is more appropriate.
- When data is dense, preserve SmartHR’s table readability and mobile stacking guidance rather than forcing desktop-style dashboard modules into small screens.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- SmartHR token guidance is important, but the higher-order rule is trust and readable business-product behavior.
- Japanese business-product clarity should remain a stronger signal than generic dashboard styling.
- Mobile navigation should stay low-friction and explicit rather than app-like.

## Responsive and Navigation Notes
- **Mobile:** Prefer an easy-to-scan horizontal top navigation strip or simple disclosure over a heavy application drawer.
- **Tablet:** Keep the shell quiet and back-office oriented, with restrained secondary navigation and stable form controls.
- **Desktop:** Restore side navigation or broader grouped navigation where it helps operational tasks.
- **Navigation rule:** Navigation on small screens should stay calm, explicit, and low-friction rather than feeling chip-heavy or overly app-like.
- **Table rule:** Preserve table readability with scroll and clear labels; avoid compressing text to chase density.

- **Dashboard note:** When tabs do not fit on mobile, render them as a Reel-style horizontal scroller rather than converting the product into a generic drawer shell.

## Official Sources
- https://smarthr.design/
- https://smarthr.design/products/design-tokens/color-palette/
- https://smarthr.design/products/design-tokens/typography/
- https://smarthr.design/products/design-tokens/media-query/
- https://smarthr.design/products/components/
