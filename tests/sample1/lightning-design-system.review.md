# lightning-design-system Review

## Design system
Salesforce Lightning Design System is optimized for record-centric enterprise apps. The official guidance emphasizes clear utility navigation, record pages, global navigation, accessible color hooks, data tables, and compact business workflows.

## Sources consulted
- https://v1.lightningdesignsystem.com/guidelines/color/our-color-system/
- https://v1.lightningdesignsystem.com/accessibility/global-color-styling-hooks/
- https://v1.lightningdesignsystem.com/components/global-navigation/
- https://v1.lightningdesignsystem.com/components/overview/
- https://v1.lightningdesignsystem.com/guidelines/data-visualization/metric-display/
- https://v1.lightningdesignsystem.com/accessibility/guidelines/keyboard/

## Overall assessment
The mock captures the broad enterprise intent, but it reads more like a generic admin dashboard than a Lightning page. The shell, navigation, and content hierarchy do not yet resemble Salesforce record-page patterns closely enough.

## Matches
- The UI uses a data-heavy structure with cards, alerts, approvals, and a table, which fits Lightning's enterprise/workflow focus.
- The palette is anchored in Salesforce blue and neutral grays, which is directionally consistent with the SLDS color system.
- The mock keeps actions near the data they affect, which aligns with Lightning's business-workflow orientation.

## Differences
- High: The left rail at `/home/hidek/git/design-system-skills/tests/sample1/lightning-design-system.html:42` and the generic top section at `...:103` do not resemble Salesforce's global navigation, app launcher, or record-page composition. The result is a custom dashboard frame instead of a Lightning-style app shell.
- High: The page has no Lightning-like highlights panel, page header pattern, or record-page/tab structure. The table and panels at `...:128` and `...:171` are useful, but they are arranged as a generic dashboard rather than a record-centric workspace.
- Medium: The mock relies on rounded pills, glass blur, and soft card treatment at `...:15` and `...:57`, which feels more decorative than the straightforward, utility-first surface treatment in SLDS.
- Medium: The status labels and controls use bespoke visual treatment instead of Lightning's more explicit utility icon, badge, and action patterns.

## Severity / priority
- High: Rework the overall shell and page hierarchy to look like a Lightning record/app page, not a generic enterprise dashboard.
- Medium: Reduce decorative softness and bring navigation, headers, and status presentation closer to SLDS conventions.
- Medium: Replace generic card and button styling with more explicit Lightning-like utility patterns.

## Recommended HTML changes
- Replace the current sidebar with a Salesforce-like global header and app navigation pattern.
- Introduce a record-page style header with object context, key metadata, and a highlights area.
- Add tabs or related-list segmentation for the main content instead of a single long dashboard stack.
- Use flatter, more utilitarian containers and less rounded corners.
- Swap emoji placeholders and generic pills for icon-driven, status-oriented labels and utility actions.

## Recommended DESIGN.md changes
- Strengthen the guidance around Salesforce global navigation, app launcher patterns, and record-page composition.
- State more explicitly that Lightning favors utility icons, related lists, page headers, and compartmentalized record workflows over decorative dashboards.
- Tighten the radius/shadow guidance so the spec discourages overly soft, consumer-style card treatment.
- Make the data-table and metric-display guidance more central, since those are core to the intended output shape.
