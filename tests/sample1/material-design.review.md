# material-design Review

## Design system
Material Design 3 is a semantic, adaptive system built around color roles, typography scales, shape, elevation, and layout that changes with screen size. The official guidance favors top app bars, navigation rails or drawers, tonal containers, and clear role-driven emphasis.

## Sources consulted
- https://developer.android.com/develop/ui/compose/designsystems/material3
- https://developer.android.com/codelabs/m3-design-theming
- https://developer.android.com/design/ui/mobile/guides/components/material-overview
- https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary
- https://developer.android.com/reference/kotlin/androidx/compose/material3/TopAppBarColors
- https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationRailItemColors
- https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationRailDefaults

## Overall assessment
The mock is visually clean, but it is closer to a generic enterprise dashboard than to Material 3. The screen does not lean enough on semantic roles, adaptive shell patterns, or Material's shape and tonal surface language.

## Matches
- The layout uses cards, chips, and a data table, which are all compatible with Material's component family.
- The UI separates summary metrics, alerts, approvals, and tabular data into clear sections.
- The mock does use a distinct primary color and an explicit surface/background split.

## Differences
- High: The persistent left sidebar at `/home/hidek/git/design-system-skills/tests/sample1/material-design.html:42` is too static for Material 3's adaptive shell guidance. The spec expects the shell to shift between top app bars, rails, and drawers based on width, not stay locked to a desktop-admin layout.
- High: The page uses one large rounded shape language everywhere at `...:15` and `...:128`, which flattens Material's semantic shape scale into a single generic radius.
- Medium: The mock does not use tonal containers or role-based emphasis strongly enough. The cards, table shell, and action bars at `...:103`, `...:128`, and `...:171` all feel more like neutral enterprise panels than Material surfaces with surface/surface-variant hierarchy.
- Medium: The controls lean on outlined pills and a translucent "glass" treatment, which is not very Material 3. The official guidance favors clear color roles, adaptive containers, and concise emphasis patterns.

## Severity / priority
- High: Replace the fixed sidebar shell with an adaptive Material layout pattern.
- High: Rework shape and surface treatment so the screen uses Material's semantic shape and tonal hierarchy instead of one repeated radius.
- Medium: Make the color roles and button hierarchy more explicitly Material 3, especially for primary, secondary, and emphasis states.

## Recommended HTML changes
- Replace the current two-column admin shell with a Material app bar plus rail or drawer that changes with viewport width.
- Use tonal containers for the summary cards and supporting panels, with a clearer surface/surface-variant distinction.
- Reduce the repeated 20px radius and map corners more deliberately to the Material shape scale.
- Make buttons, chips, and selected states more role-driven: filled for primary, tonal/outlined for secondary, and chips for filters.
- Remove the glass blur treatment and keep elevation subtle and tonal.

## Recommended DESIGN.md changes
- Make adaptive shell behavior a stronger requirement, including when to use top app bars, navigation rails, drawers, and supporting panes.
- Tighten the shape guidance to reference Material's shape scale rather than a generic "medium rounding" description.
- Emphasize semantic color roles and tonal containers more clearly in the layout rules and component guidance.
- Add explicit guidance that dashboards should stay role-driven and adaptive rather than defaulting to a fixed enterprise sidebar pattern.
