# Atlassian Design System Review

## Design system
Atlassian Design System

## Sources consulted
- https://atlassian.design/foundations/color
- https://atlassian.design/foundations/typography/
- https://atlassian.design/foundations/tokens/design-tokens/
- https://atlassian.design/foundations/grid-beta/
- https://atlassian.design/components/lozenge/
- https://atlassian.design/components/navigation-system/side-navigation/

## Overall assessment
The mock captures the broad shape of a work-management dashboard, but it still reads as a generic admin screen. Atlassian’s system is more token-driven, lighter in surface treatment, and more explicit about workspace navigation and status presentation than this mock suggests.

## Matches
- The screen is dense, task-oriented, and collaboration-friendly, which is compatible with Atlassian’s product positioning.
- The mock uses compact labels, utility actions, and status emphasis, which fits Atlassian’s operational UI style.
- The page includes a side navigation area and content panels, which is directionally aligned with Atlassian application shells.

## Differences
- The layout is too generic and too isolated from Atlassian’s navigation model. Official guidance favors a product-level top structure with side navigation or the newer navigation system, while this mock only presents a flat sidebar and no top-level product framing.
- The palette is expressed as literal hex surfaces and a dark shell rather than as token-led color usage with neutrals, alpha values, and emphasis levels.
- The typography feels heavier and more display-like than Atlassian’s recommended readable, practical hierarchy with lightweight metadata styles.
- Status is expressed as rounded pills, but Atlassian uses lozenges as its characteristic status indicator pattern.
- The mock does not show inline banners or messaging patterns that Atlassian uses to support dense workflows with clear feedback.

## Severity / priority
Medium. The page structure works, but the navigation language, status presentation, and token usage should be more Atlassian-specific.

## Recommended HTML changes
- Replace the flat sidebar with a clearer Atlassian app shell that includes product-level framing and a more explicit workspace navigation model.
- Rework status badges into lozenge-like indicators with subtler emphasis.
- Lighten the visual treatment by reducing heavy borders, full-surface dark blocks, and overly decorative shadows.
- Make typography more compact and practical, with less emphasis on oversized page titling.
- Add a banner or inline message area to reflect Atlassian’s workflow-oriented feedback patterns.

## Recommended DESIGN.md changes
- Explicitly describe Atlassian’s app-shell structure, including top-level product framing and side navigation or navigation-system patterns.
- Emphasize token-driven color, spacing, elevation, and typography rather than hard-coded visual recipes.
- Add stronger guidance for lozenges, inline messages, and status presentation so the review output does not drift into generic pill badges.
- Clarify that typography should stay practical and readable, with lightweight metadata rather than prominent display-like page chrome.
