# Carbon Design System Review

## Design system
Carbon Design System

## Sources consulted
- https://carbondesignsystem.com/elements/color/tokens/
- https://carbondesignsystem.com/elements/typography/overview/
- https://carbondesignsystem.com/elements/typography/type-sets/
- https://carbondesignsystem.com/components/UI-shell-header/usage/
- https://carbondesignsystem.com/components/UI-shell-header/style/
- https://carbondesignsystem.com/components/button/usage/
- https://carbondesignsystem.com/components/data-table/usage/
- https://v10.carbondesignsystem.com/guidelines/2x-grid/overview/

## Overall assessment
This is the closest of the three mocks to its intended system at the structural level, but it still misses several defining Carbon traits. The shell, typography scale, button hierarchy, and data table behavior all feel more like a Tailwind admin dashboard than a Carbon enterprise interface.

## Matches
- The mock uses a disciplined enterprise dashboard structure with a persistent navigation region, content panels, and a data-heavy table.
- The visual tone is restrained compared with many generic dashboard mocks, which is a good starting point for Carbon.
- The use of strong contrast, explicit status states, and grouped content fits Carbon’s clarity-first approach.

## Differences
- Carbon’s UI shell header is a persistent header that spans the browser width and is part of a shell that works with left and right panels; the mock instead uses a tall dark sidebar and a decorative card panel, which does not reflect the Carbon shell model.
- The typography is too large and too display-like. Carbon’s productive type set is built around IBM Plex Sans and a 14px base, with emphasis on compact, task-oriented hierarchy.
- The page uses multiple primary-looking buttons, including the main CTA and several row-level actions. Carbon’s button guidance says each page should have only one primary button, with secondary and tertiary/ghost buttons handling the rest.
- The table lacks Carbon’s toolbar, sorting indicators, batch action bar, and clear selected-row behavior.
- The card surfaces are too rounded and decorative for Carbon, which prefers layered backgrounds, subtle borders, and productivity-oriented geometry over soft consumer-style cards.

## Severity / priority
High. The page structure is usable, but the shell, typography, and action hierarchy diverge from Carbon in ways that are immediately visible.

## Recommended HTML changes
- Replace the dark sidebar-heavy shell with a Carbon-style UI shell header and more literal product navigation.
- Reduce heading scale and tighten spacing to look like a productive 14px-based interface.
- Rework actions so there is one clear primary button on the page, with secondary or ghost actions for the rest.
- Add a data-table toolbar with search, filter, and batch-action affordances.
- Remove rounded consumer-style card treatment and lean on flatter layers, sharper geometry, and clearer grid rhythm.

## Recommended DESIGN.md changes
- Strengthen the shell section to reflect the Carbon UI shell header as a core pattern, including width, height, and responsive behavior.
- Tighten button guidance so the one-primary-per-page rule is explicit and the role of secondary, tertiary, and ghost buttons is unambiguous.
- Expand the table guidance to include toolbar, sorting, selection, and batch actions as core Carbon behaviors.
- Reinforce productive typography and the 2x Grid as defining constraints, not optional suggestions.
