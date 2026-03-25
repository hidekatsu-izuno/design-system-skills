# Digital Agency Design System (Beta) DESIGN.md

- **Provider:** The Digital Agency
- **Primary reference:** https://design.digital.go.jp/
- **Primary product focus:** Japanese public-service websites and trust-critical transactional screens.
- **Platforms:** Web-first government service guidance for desktop and mobile browsers.
- **Status:** Beta public government rollout.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Trustworthy, plainspoken, and conservative.
- Accessibility, legibility, and explicit interaction patterns come before style.
- The UI should feel official, comprehensible, and low-ambiguity.
- Best for forms, service flows, public portals, and administrative web systems.
- Brand expression should never compete with readability or legal clarity.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Primary Blue (#005AC2):** Primary action, links, and core interactive emphasis.
- **Blue Hover (#00408A):** Hover and active emphasis for primary controls.
- **Light Blue (#E8F1FF):** Low-emphasis hover and outlined-button background.
- **Text (#1A1A1A):** Primary readable text color.
- **Background (#FFFFFF):** Primary document and service surface.
- **Subtle Surface (#F5F5F5):** Section grouping and low-emphasis backgrounds.
- **Border (#C8C8C8):** Field and section boundaries.
- **Danger (#B00020):** Error and destructive emphasis.

## 3. Typography Rules
- Use highly readable Japanese web typography with conservative hierarchy and explicit labels.
- Favor service readability over brand personality or display-driven contrast.
- Keep text blocks, form labels, and instructions close to their controls.
- Motion and iconography should remain supportive, plain, and familiar.

## 4. Component Stylings
- **Buttons and actions:** Use clear filled, outlined, and text button hierarchies with obvious labels and conservative styling.
- **Inputs and form controls:** Use explicit text inputs, selects, radios, checkboxes, toggles, and date fields with visible labels, helper text, and nearby validation.
- **Menus, tabs, breadcrumbs, and navigation:** Use global navigation, breadcrumbs, and mobile menus in plain service language. Keep labels official, literal, and easy to understand.
- **Cards, lists, tables, badges:** Use sections, tables, and lists for structured information. Grouping should support comprehension rather than product personality.
- **Dialogs, toasts, loading, pagination:** Use dialogs, notices, progress, and pagination only when they reduce ambiguity in public-service flows.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.

## 5. Layout Principles
- Use straightforward headers, grouped sections, and explicit service flow structure.
- Favor plain backgrounds, visible borders, and conservative spacing over rich product shells.
- Use minimal rounding and minimal decorative depth.
- Keep forms, instructions, and state messaging explicit and nearby.
- Prioritize accessibility and public comprehension over visual novelty.

- Prefer a plain service-page shell with explicit labels and restrained grouping instead of a broad app-like dashboard scaffold.
- Avoid persistent app-style side rails and decorative hero/card framing when a literal service layout will communicate more clearly.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Customization is intentionally limited; standardization is more important than brand differentiation.
- Government-style clarity and legal/service readability should remain the interpretive default.
- A hamburger-driven mobile menu is part of the expected service pattern language.

## Responsive and Navigation Notes
- **Mobile:** Use a plain hamburger button that opens a left-side drawer / mobile menu, and keep utility items minimal.
- **Tablet:** Preserve straightforward top-level navigation with limited nesting and restrained secondary actions.
- **Desktop:** Allow a broader header/navigation presentation, but keep the shell simple and service-oriented.
- **Navigation rule:** Prefer an explicit hamburger button plus drawer / mobile menu over app-like persistent side rails.
- **Table rule:** Keep data readable with horizontal scroll and clear labels instead of compressing the interface aggressively.

- **Dashboard note:** Use one labeled hamburger trigger plus modal drawer/mobile menu as the primary compact navigation pattern and keep desktop navigation simple and literal.

## Official Sources
- https://design.digital.go.jp/
- https://design.digital.go.jp/dads/components/button/
- https://design.digital.go.jp/components/
- https://design.digital.go.jp/templates/
- https://design.digital.go.jp/guidelines/accessibility/
