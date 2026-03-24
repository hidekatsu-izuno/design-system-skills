# primer-product-ui Review

## Design system
Primer Product UI is GitHub's product-facing design system. The official guidance stresses focused, clean, accessible layouts, semantic landmarks, muted surfaces, restrained motion, and page structures that reduce cognitive load.

## Sources consulted
- https://primer.style/product/
- https://primer.style/product/getting-started/foundations/
- https://primer.style/product/getting-started/foundations/layout/
- https://primer.style/product/getting-started/foundations/typography/
- https://primer.style/product/getting-started/foundations/responsive/
- https://primer.style/product/getting-started/foundations/color-usage/
- https://primer.style/product/components/page-layout
- https://primer.style/product/components/page-layout/accessibility/
- https://primer.style/product/ui-patterns/navigation

## Overall assessment
The mock is structurally solid, but it is still too decorative and generic to feel like Primer Product UI. The page needs a calmer shell, more GitHub-like layout discipline, and less emphasis on rounded chrome.

## Matches
- The mock uses semantic regions for header, main content, pane-like content, and footer-like activity, which is consistent with Primer's PageLayout thinking.
- The palette stays in a GitHub-like blue, gray, and white range.
- The layout keeps data tables, filters, and related actions near the content they affect.

## Differences
- High: The left shell at `/home/hidek/git/design-system-skills/tests/sample1/primer-product-ui.html:42` feels heavier and more decorative than Primer's recommended clean, calm, uncluttered layout language.
- Medium: The global header and action area at `...:103` use large rounded controls and a soft "glass" treatment that do not match Primer's more restrained page header style.
- Medium: The repeated card treatment at `...:128` and `...:171` is too rounded and too shadowed. Primer guidance leans on muted containers, logical sectioning, and modest radii rather than soft dashboard tiles.
- Medium: The page does not yet feel like GitHub's PageLayout/PageHeader/NavList/UnderlineNav family. It has the right regions, but the styling and hierarchy are still closer to a generic admin UI.

## Severity / priority
- High: Simplify the shell so it reads as a focused GitHub product page rather than a branded dashboard.
- Medium: Tone down radius, shadows, and pill styling across headers, nav, and cards.
- Medium: Make the page hierarchy feel more like Primer's sectioned product layouts and less like a custom dashboard composition.

## Recommended HTML changes
- Rebuild the shell around a calmer PageLayout-like structure with a clearer PageHeader, main content, and side pane relationship.
- Reduce the visual weight of the sidebar and top actions; use muted surfaces and simpler controls.
- Replace the soft, heavily rounded cards with flatter panels and more restrained borders.
- Use more direct GitHub-like navigation patterns such as nav list / underline-style tabs where appropriate.
- Keep the activity and table regions, but present them with less ornament and more whitespace discipline.

## Recommended DESIGN.md changes
- Strengthen the guidance around focused, clean, uncluttered layouts and the use of semantic landmarks.
- Emphasize that Primer favors muted panels, logical page structure, and restrained rounding/shadows.
- Clarify that top-level navigation and page headers should feel product-oriented and not decorative.
- Add stronger guidance to prefer page layout, nav list, underline nav, and page header patterns over bespoke dashboard chrome.
