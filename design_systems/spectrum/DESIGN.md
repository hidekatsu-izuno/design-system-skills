# Spectrum DESIGN.md

- **Provider:** Adobe
- **Primary reference:** https://spectrum.adobe.com/
- **Primary product focus:** Adobe-style product experiences and creative workflows.
- **Platforms:** Web workflows and desktop-leaning creative/productive applications.
- **Status:** Active Adobe-maintained system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Polished, disciplined, and workflow-oriented.
- The interface should support professional and creative work without losing clarity.
- Visual language is branded but controlled, never noisy.
- Best for asset workflows, professional tools, and polished application shells.
- Hierarchy should feel intentional and refined rather than merely dense.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Blue (#1473E6):** Primary action and selected-state emphasis.
- **Purple (#6F5CFF):** Expressive accent and branded secondary emphasis.
- **Green (#008F5D):** Success and healthy completion.
- **Red (#D31510):** Error and destructive emphasis.
- **Gray 900 (#2C2C2C):** Primary dark text and dark-mode surface anchor.
- **Gray 50 (#FFFFFF):** Light surface and content background.
- **Gray 100 (#F8F8F8):** Subtle containers and low-emphasis panels.
- **Border (#D5D5D5):** Field, panel, and overlay boundaries.

## 3. Typography Rules
- Use Spectrum typography with refined hierarchy and strong workflow readability.
- Headings should stay polished and quiet, while body text remains highly legible.
- Let typography support creative-professional calm rather than brand theater.
- Iconography and motion should feel precise and product-polished.

## 4. Component Stylings
- **Buttons and actions:** Use polished but restrained primary, secondary, and quiet action hierarchy.
- **Inputs and form controls:** Use Picker, ComboBox, TextField, Switch, Checkbox, Radio, DatePicker, and Search in a refined workflow context.
- **Menus, tabs, breadcrumbs, and navigation:** Use ActionMenu, Menu, Tabs, Breadcrumbs, side nav, and tray-like navigation to keep workflows clear and low-noise.
- **Cards, lists, tables, badges:** Use disciplined cards, lists, tables, and badges as workflow surfaces rather than casual dashboard tiles.
- **Dialogs, toasts, loading, pagination:** Use Dialog, Tray, Toast, ProgressCircle, Skeleton, and Pagination patterns with a polished but unobtrusive feel.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.

## 5. Layout Principles
- Use workflow containers, side panels, and polished shell framing to organize complex tasks.
- Keep hierarchy refined and low-noise even when the interface is information-rich.
- Use tokenized spacing, borders, and modest elevation instead of loud decorative treatment.
- Let workflow structure guide composition before brand expression does.
- Avoid generic admin-panel framing that ignores the Adobe-like workspace feel.

- Keep the shell polished and task-oriented with workflow emphasis, compact action surfaces, and deliberate iconography.
- Avoid generic admin dashboard framing; supporting trays, refined action areas, and product-workspace structure should do more of the organizing work.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Spectrum tokens and cross-platform naming are important and should remain visible in the semantic spec.
- ActionMenu and tray-like behavior are interpretation-critical for compact contexts.
- The system should feel polished and branded without relying on generic glossy cards.

## Responsive and Navigation Notes
- **Mobile:** Use an action-menu or tray-like navigation trigger with compact, polished controls rather than a broad admin drawer.
- **Tablet:** Preserve a calm workflow shell and collapse only secondary navigation before main workspace content.
- **Desktop:** Restore workspace-style navigation and utility chrome with restrained hierarchy.
- **Navigation rule:** Compact navigation should feel like Spectrum action or tray behavior, not a generic accordion menu.
- **Table rule:** Keep workspace data readable through scroll and grouped sections while maintaining a polished, low-noise shell.

- **Dashboard note:** Compact navigation should feel like Spectrum action/tray behavior, not like a generic accordion or dashboard drawer.

## Official Sources
- https://spectrum.adobe.com/
- https://spectrum.adobe.com/page/design-language/
- https://spectrum.adobe.com/page/color/
- https://spectrum.adobe.com/page/typography/
- https://spectrum.adobe.com/page/components/
