# Lightning Design System DESIGN.md

- **Provider:** Salesforce
- **Primary reference:** https://v1.lightningdesignsystem.com/
- **Primary product focus:** CRM-style, record-centric business applications.
- **Platforms:** Responsive enterprise web with desktop-heavy CRM workflows.
- **Status:** Active SLDS public docs.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Structured, object-oriented, and businesslike.
- Designed around record pages, related lists, utilities, and workflow status.
- The page shell should stay explicit and consistent rather than decorative.
- Best for CRM objects, account pages, lists, and guided action flows.
- Status, object metadata, and hierarchy should always be easy to scan.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Brand (#0176D3):** Primary interactive emphasis and brand-led action color.
- **Brand Dark (#032D60):** Stronger shell and enterprise emphasis.
- **Success (#2E844A):** Positive completion and healthy state.
- **Error (#BA0517):** Error and destructive action emphasis.
- **Background (#FFFFFF):** Primary page surface.
- **Canvas Alt (#F3F3F3):** Section and utility background.
- **Border (#C9C9C9):** Object, field, and table separators.
- **Text (#181818):** Primary readable text color.

## 3. Typography Rules
- Use Salesforce Sans or the closest enterprise sans stack.
- Keep object headers, field labels, and utility text readable and explicit.
- Favor business UI clarity over decorative type variation.
- Status chips, utility labels, and object metadata should feel stable and scannable.

## 4. Component Stylings
- **Buttons and actions:** Use obvious primary actions with strong business hierarchy and clear secondary utilities.
- **Inputs and form controls:** Use enterprise forms, comboboxes, picklists, toggles, search, and date controls with visible labels and validation.
- **Menus, tabs, breadcrumbs, and navigation:** Use global navigation, vertical navigation, record tabs, utility menus, and breadcrumbs around object context.
- **Cards, lists, tables, badges:** Use record headers, highlights panels, related lists, badges, and data tables that maintain object-page rhythm.
- **Dialogs, toasts, loading, pagination:** Use modals, prompt-style feedback, spinners, notifications, and pagination to support CRM operations.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.
- Treat `page header`, `record header`, `highlights panel`, `path`, `tabs`, `related list`, and `datatable` as the defining component set for this system.
- Primary content should feel like an object or record home: object identity and status first, related lists and support panels second, generic summary tiles last.
- Tabs and overflow should organize the major sections before any mobile drawer-like pattern is introduced.

## 5. Layout Principles
- Use record-page composition, object headers, highlights, related lists, and utility regions.
- Keep page regions explicit and stable across similar objects or workflows.
- Use accessible business UI patterns instead of consumer dashboard surfaces.
- Preserve strong status and metadata visibility near object context.
- Support data-heavy tasks with filtering, tabs, and related content sections.

- Use object or record-page composition with a persistent page header, main content area, and secondary sidebar rather than a generic dashboard hero row.
- Tabs should organize the primary sections and side panels should hold supporting record information.
- Avoid a top-bar-plus-cards admin shell; Lightning screens should read like CRM object pages with utility regions and related content.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Styling hooks and design tokens are interpretation-critical and should remain visible in the document logic.
- Object-page framing matters more than generic dashboard hero patterns.
- Compact navigation should preserve tabs and overflow before adopting a generic drawer.

## Responsive and Navigation Notes
- **Mobile:** Keep the page in a record-page rhythm: show a compact set of primary tabs first and move overflow destinations into a secondary menu.
- **Tablet:** Preserve object header context and visible tabs where possible, reducing only secondary navigation.
- **Desktop:** Restore the full object/page shell with highlights, related sections, and broader tab visibility.
- **Navigation rule:** Small-width navigation should behave like compact tab plus overflow navigation, not a generic left drawer unless the pattern truly demands it.
- **Table rule:** Related lists may scroll or stack, but object context and primary actions should remain visible.

- **Dashboard note:** Tabs should overflow before the experience collapses into a generic drawer; keep the shell record-oriented rather than dashboard-oriented.

## Official Sources
- https://v1.lightningdesignsystem.com/
- https://v1.lightningdesignsystem.com/design-tokens/
- https://v1.lightningdesignsystem.com/utilities/themes/
- https://v1.lightningdesignsystem.com/components/overview/
- https://v1.lightningdesignsystem.com/accessibility/overview/
