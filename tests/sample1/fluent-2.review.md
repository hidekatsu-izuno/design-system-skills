# Fluent 2 Review

## Design system
Fluent 2

## Sources consulted
- Official: https://fluent2.microsoft.design/components/web/react/core/button/usage
- Official: https://fluent2.microsoft.design/components/web/react/core/nav/usage
- Official: https://fluent2.microsoft.design/components/web/react/core/card/usage
- Official: https://fluent2.microsoft.design/components/web/react/core/badge/usage
- Official: https://fluent2.microsoft.design/components/web/react/
- Official: https://fluent2.microsoft.design/components/web/react/core/tablist/usage
- Official: https://fluent2.microsoft.design/components/web/react/core/input/usage
- Official: https://fluent2.microsoft.design/components/web/react/core/text/usage

## Overall assessment
The mock is structurally close to a Fluent 2 productivity app, but the visual language is still too decorative and too generic. It uses a soft enterprise dashboard shell, but Fluent 2 expects clearer hierarchy, calmer composition, and stricter button and navigation discipline.

## Matches
- The mock uses a restrained neutral palette with a Microsoft-style blue accent.
- The page is organized into a shell, summary cards, alerts, approvals, and a data table, which fits a productivity-oriented app pattern.
- The content is mostly dense and work-focused rather than marketing-led.

## Differences
- The left navigation is plain text only; Fluent 2 nav guidance recommends brief, task-oriented labels and commonly uses icons for emphasis and recognition.
- The page uses several prominent actions at once, including the primary header action and repeated row actions, but Fluent 2 button guidance says to keep only one primary button prominent and use outline, subtle, or transparent appearances for minor actions.
- The `glass` treatment and rounded hero header make the mock feel softer and more branded than Fluent 2’s typically calm, token-driven surfaces.
- Badge text such as `Update`, `Approval`, and `Critical` is not written in Fluent 2 style; the docs prefer short, sentence-style labels and semantic use near the described component.
- The card and table areas are visually heavy, while Fluent 2 card guidance emphasizes bite-sized content and consistent use cases across experiences.
- The header search input behaves like a large static field, but Fluent 2 expects search to integrate into productivity workflows without taking visual priority.

## Severity / priority
- High: reduce the number of high-emphasis actions and convert secondary actions to subtle or outline treatment.
- High: add iconography and clearer task-oriented navigation semantics.
- Medium: remove decorative shell styling and flatten the surface treatment.
- Medium: rewrite badge and control labels to match Fluent 2’s sentence-style, utility-first tone.

## Recommended HTML changes
- Keep exactly one primary action in the header and demote other actions to subtle or outline buttons.
- Add icons to nav items and make the labels more task-oriented and brief.
- Replace the glassy header and soft dashboard chrome with flatter Fluent-style surfaces and clearer dividers.
- Make badges shorter and more semantically consistent, with sentence-style capitalization.
- Reduce visual weight in the card stack so summary data reads as content, not decoration.

## Recommended DESIGN.md changes
- Strengthen the component rules around one-primary-action layouts and subtle secondary actions.
- Add an explicit nav note that Fluent 2 favors icons, short labels, and task-oriented navigation.
- Clarify badge and status language, including sentence-style capitalization and short state labels.
- Tighten the layout guidance so shell treatments, cards, and tables stay calm and token-driven rather than decorative.
