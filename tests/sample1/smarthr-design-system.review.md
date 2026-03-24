# SmartHR Design System Review

## Design system
SmartHR Design System

## Sources consulted
- Official: https://smarthr.design/
- Official: https://smarthr.design/products/design-tokens/
- Official: https://smarthr.design/products/design-tokens/color/
- Official: https://smarthr.design/products/design-tokens/typography/
- Official: https://smarthr.design/products/components/

## Overall assessment
The mock captures the broad business-dashboard shape reasonably well: side navigation, summary metrics, alerts, approvals, and a data table are all present. The main problem is that the visual language is still too generic and slightly over-styled compared with SmartHR’s documented emphasis on clarity, accessibility, calm surfaces, and practical composition.

## Matches
- The page is structured as an operational dashboard with navigation, summary cards, alerts, approvals, and a record table.
- The page uses a clearly defined primary accent rather than a random decorative palette, which is directionally consistent with SmartHR’s token-driven color system.
- The use of Japanese labels for the core workflow supports the product’s Japanese business context.
- The layout is readable and avoids excessive density, which is broadly consistent with SmartHR’s trust- and clarity-oriented positioning.

## Differences
- The primary accent is using `#00c4cc`, but the current official color token page puts `MAIN #0077c7` at the center of the system. The mock therefore uses the wrong visual anchor for the brand.
- The left rail is too dark and heavy. SmartHR’s public guidance emphasizes approachable, calm, practical UI language rather than a stark monochrome shell.
- The `glass` treatment and fairly strong shadows make the mock feel more decorative than the SmartHR system’s documented preference for whitespace, borders, and restrained surface hierarchy.
- The typography stack is a best-effort approximation, but the page still reads like a generic SaaS mock rather than a Japanese business product aligned with SmartHR’s typography guidance and OS-respecting approach.
- Several labels such as `Visual cues` and `Master Data Operations` are more presentation-oriented than the straightforward, operational tone implied by SmartHR’s product pages.
- The cards and table are functional, but the surface rhythm and border treatment could be tightened further to better match SmartHR’s accessible, businesslike component guidance.

## Severity / priority
- High: Fix the primary brand color so the mock uses SmartHR’s documented main token, not the lighter chart/accent teal.
- High: Reduce decorative styling in the shell and surfaces. This is the largest mismatch with the documented SmartHR tone.
- Medium: Adjust typography and label tone to feel more like a Japanese business SaaS product.
- Medium: Tighten component styling so cards, table, and badges feel more utilitarian and less presentation-driven.

## Recommended HTML changes
- Replace the current primary accent with `MAIN #0077c7`, and reserve `#00c4cc` only if the design needs a secondary chart-like accent.
- Replace the dark, glossy-looking sidebar treatment with a lighter, calmer shell and simpler hierarchy.
- Remove the `glass` effect and reduce shadow strength across header and cards.
- Use a more restrained visual rhythm with clearer borders and flatter panels.
- Align the header labels and supporting copy with concise operational language.
- Keep the same dashboard structure, but make the overall look less decorative and more product-utility focused.

## Recommended DESIGN.md changes
- Clarify that SmartHR mockups should favor calm, approachable surfaces and minimal visual flourish rather than any decorative or contrast-heavy shell treatment.
- Emphasize practical, readable Japanese business-product typography over generic enterprise sans assumptions.
- Strengthen the layout guidance around whitespace, borders, and clear content blocks.
- Add explicit wording that side navigation and record tables should feel lightweight and operational, not visually heavy.
