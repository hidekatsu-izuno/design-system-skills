# Digital Agency Design System Review

## Design system
Digital Agency Design System

## Sources consulted
- Official: https://design.digital.go.jp/dads/
- Official: https://design.digital.go.jp/dads/components/header-container/
- Official: https://design.digital.go.jp/dads/updates-code-snippet/

## Overall assessment
The mock captures the broad public-service intent, but it still reads more like a generic enterprise SaaS dashboard than a Digital Agency interface. The largest gap is the visual treatment: the current page uses a full-height app shell, translucent blur, highly rounded controls, and card-heavy composition that feels more product-branded than government-service oriented.

## Matches
- The mock uses a conservative blue primary color and mostly restrained surface colors.
- The layout keeps the core service information visible in sections for summary, alerts, approvals, and updates.
- The page includes utility search and global navigation concepts that are directionally compatible with the official guidance.

## Differences
- `tests/sample1/digital-agency-design-system.html` uses a persistent enterprise sidebar and dark shell, while the official site centers guidance around a header container, global menu, and service-oriented page structure rather than a branded application chrome.
- The `glass` blur effect and highly rounded pills are not supported by the official guidance and make the page feel less like a public-service UI.
- The mock overuses card treatment for every area, including summary metrics and activity items, while the official guidance favors clearer page structure and straightforward components.
- The search control is styled like a large hero input, but the official search box guidance is utility-oriented and intended to sit inside a service header.
- The action labels and data labels are more app-like than public-service-like; the official system consistently emphasizes plain, direct presentation.

## Severity / priority
- High: remove the decorative enterprise shell and glass styling.
- High: move the page closer to a plain service header with lighter component chrome.
- Medium: reduce rounded button and badge styling.
- Medium: simplify the card density and make the structure read more like a government service page.

## Recommended HTML changes
- Replace the full-height left sidebar chrome with a simpler service header plus lightweight global menu treatment.
- Remove `backdrop-filter` and tone down the rounded corners on buttons, cards, and badges.
- Flatten the hierarchy so the summary, alert, approval, and history areas read as plain sections rather than decorative dashboard tiles.
- Restyle the search control as a practical header utility instead of a prominent hero input.
- Reduce the visual emphasis of secondary actions and keep the primary action unmistakably simple.

## Recommended DESIGN.md changes
- Tighten the layout guidance to emphasize plain service headers, global menus, and simple page templates over dashboard-style app shells.
- Add stronger wording that discourages decorative blur, heavy rounding, and card-heavy composition.
- Clarify that search, labels, and status chips should read as utility elements, not branded UI ornaments.
- Make the guidance more explicit that public-service layouts should prioritize directness, readability, and conventional structure over product-like chrome.
