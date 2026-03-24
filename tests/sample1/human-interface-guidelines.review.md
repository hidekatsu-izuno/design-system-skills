# Human Interface Guidelines Review

## Design system
Human Interface Guidelines

## Sources consulted
- Official: https://developer.apple.com/design/human-interface-guidelines/
- Official: https://developer.apple.com/design/human-interface-guidelines/sidebars?changes=_9
- Official: https://developer.apple.com/design/human-interface-guidelines/buttons
- Official: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/SearchFields.html

## Overall assessment
The mock shows the right data categories, but it does not feel especially native to Apple platforms. The page is built like a web dashboard with a floating blur shell, dense utility rows, and custom controls, while the HIG favors platform conventions, clear hierarchy, and native-feeling containers such as sidebars, split views, toolbars, and search integrated into the toolbar.

## Matches
- The mock keeps the information hierarchy readable and avoids overly ornamental decoration beyond the shell styling.
- The layout uses a leading navigation region and a content area, which is directionally compatible with sidebar-based Apple app structure.
- The typography and color choices remain restrained rather than aggressively branded.

## Differences
- The full-height sidebar is treated as generic web app chrome, but the HIG sidebar guidance describes a floating sidebar that supports native hierarchy on Apple platforms and should be used with platform-appropriate spacing and behavior.
- The `glass` blur treatment is visually close to modern Apple materials, but here it is used as web ornamentation rather than a platform-native material treatment.
- The header search box is overly prominent and static; Apple’s search guidance expects search to be integrated into the toolbar or navigation stack, not presented as a large hero field.
- The page uses many custom rounded pills and badge-like labels, whereas the HIG favors native controls, subtle materials, and content-first presentation.
- The mock mixes several navigation and command metaphors in a single dashboard, while the HIG warns against mixing too many metaphors on one screen and emphasizes consistency.

## Severity / priority
- High: make the shell feel native by reducing web-dashboard styling and aligning navigation with Apple patterns.
- High: integrate search into the toolbar or title area instead of using a large custom field.
- Medium: reduce custom badge and pill styling in favor of simpler native-feeling controls.
- Medium: simplify the visual treatment of cards and tables so content leads.

## Recommended HTML changes
- Replace the dashboard-like shell with a more Apple-like split view or sidebar-plus-content layout.
- Move search into the header/toolbar region and reduce its visual dominance.
- Remove the heavy custom blur and soften the control chrome so the page feels like a platform interface rather than a branded web app.
- Use fewer custom capsules and more native-looking grouped sections, separators, and simple action buttons.
- Keep navigation and actions more consistent with one platform family at a time.

## Recommended DESIGN.md changes
- Strengthen the layout guidance to prefer sidebar, split view, toolbar, and tab-based patterns where appropriate.
- Add stronger wording around platform-native materials and avoiding web-dashboard chrome on Apple-oriented interfaces.
- Clarify that search should be integrated into the toolbar or navigation structure rather than treated as a standalone hero component.
- Tighten the component guidance so buttons, badges, and grouped sections stay subtle and native-feeling.
