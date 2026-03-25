# Sparkle Design DESIGN.md

- **Provider:** Goodpatch
- **Primary reference:** https://sparkle-design.goodpatch.com/sparkle-design
- **Primary product focus:** Digital products with stronger brand character than a pure utility system.
- **Platforms:** Web and product surfaces with reusable branding guidance.
- **Status:** Active public launch era system.
- **Implementation note:** This file is both a Stitch-style semantic design source and a standalone UI generation spec. Follow it directly when producing UI in this design system.

## 1. Visual Theme & Atmosphere
- Deliberate, branded, and expressive in a controlled way.
- The system should preserve personality without losing reusable product structure.
- Layouts and components should feel practical first, with expression layered on top.
- Best for branded digital products that still need repeatable quality.
- Brand warmth and clarity should coexist without overpowering utility.

## 2. Color Palette & Roles
Use semantic roles in implementation. The values below are representative generation anchors, not exhaustive token exports.

- **Primary (#111111):** Strong base text and key contrast anchor.
- **Accent (#FF6B3D):** Expressive action and branded highlight color.
- **Support (#FFC857):** Warm secondary accent for highlights and emphasis.
- **Background (#FFFFFF):** Base canvas and clean surface.
- **Subtle Surface (#F7F5F2):** Section grouping and quiet panel surface.
- **Border (#DDD6CE):** Light structure and field boundaries.
- **Muted Text (#5E5A55):** Secondary metadata and supporting labels.
- **Info Accent (#4A90E2):** Supplementary interactive or informational emphasis.

## 3. Typography Rules
- Use a confident but product-appropriate sans stack with stronger brand character than pure enterprise UI.
- Headings can carry more voice, but body text and labels should stay practical and readable.
- Use typography to support composition and personality without becoming a marketing page.
- Icons and emphasis treatments should remain subordinate to the product task flow.

## 4. Component Stylings
- **Buttons and actions:** Use branded primary actions and controlled secondary actions with warm, confident emphasis.
- **Inputs and form controls:** Use practical forms and controls with clear boundaries, while allowing modest branded tone in color and shape.
- **Menus, tabs, breadcrumbs, and navigation:** Use practical digital-product navigation, breadcrumbs, tabs, and menus without over-ornamenting the shell.
- **Cards, lists, tables, badges:** Use cards and grouped surfaces to add structure and personality, but keep tables and lists readable and useful.
- **Dialogs, toasts, loading, pagination:** Use overlays and transient feedback with controlled brand expression, not dramatic motion or heavy chrome.
- **Icons and symbolic affordances:** In static HTML mocks, use Font Awesome as the fallback icon set when the native design-system icon package is unavailable. Keep icons functional rather than decorative. Apply them to common affordance points such as menu triggers, search, notifications, primary and secondary actions, navigation items, status cues, and row-level actions. Prefer close semantic matches, keep visible labels, and avoid replacing text-only controls with icon-only controls unless the design system clearly expects that pattern.
- Add a showcase-like supporting area, branded highlight band, or warm editorial surface so the screen keeps a recognizably designed first impression.
- Let buttons, cards, section headers, and supporting modules carry controlled brand expression; tables and operational content still need to remain practical.
- Avoid stripping the system down to neutral SaaS admin primitives; Sparkle needs composition, warm surfaces, and expressive emphasis beyond color swaps alone.

## 5. Layout Principles
- Use coherent branding with reusable product structure rather than one-off visual flourishes.
- Allow more expressive accent and composition than pure utility systems, but keep layouts practical.
- Use controlled warmth in color and surface treatment instead of loud gradients or marketing hero framing.
- Support real product navigation and content density before decorative composition.
- Expression should sharpen the product identity without harming usability.

- Allow a more branded first impression and a showcase-like supporting area so the product still feels design-system-adjacent rather than neutral SaaS admin.
- Keep warm surfaces and expressive composition visible beyond color alone; do not flatten Sparkle into a generic enterprise dashboard.
- The page may be more editorial and brand-aware than the other systems, but it still needs a real product shell and actionable landmarks.

## Compatibility Notes
- When generating static mocks without the official icon library, approximate the system's iconography with Font Awesome icons that are semantically close and visually restrained.
- Use semantic guidance, atmosphere descriptions, and implementation notes as internal generation constraints only. Do not render them as visible UI labels, helper chips, taglines, or explanatory copy inside the product surface.
- Public component naming is thinner here, so keep the document semantically precise and conservative when certainty is low.
- Brand expression is part of the design system, but utility still governs the UI generation outcome.
- Use this file as a semantic prompt source rather than a formal token-export surrogate.

## Responsive and Navigation Notes
- **Mobile:** Collapse navigation into a branded but lightweight disclosure or menu trigger so the expressive shell does not consume the screen.
- **Tablet:** Keep brand accents, but reduce decorative framing before sacrificing utility content.
- **Desktop:** Restore the full branded shell with clear navigation and expressive but controlled surface treatment.
- **Navigation rule:** Small-screen navigation should be concise and intentional, not a permanent ornamental sidebar.
- **Table rule:** Let data views scroll and keep decorative treatments secondary to usability.

- **Dashboard note:** Compact navigation may stay light, but the page should preserve branded composition and supporting showcase structure instead of collapsing into the same dashboard scaffold as other systems.

## Official Sources
- https://sparkle-design.goodpatch.com/sparkle-design
- https://goodpatch.com/blog/2025-07-sparkle-design-3
- https://goodpatch.com/blog/2025-06-sparkle-design-1
