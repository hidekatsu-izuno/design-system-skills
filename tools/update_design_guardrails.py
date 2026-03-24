from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


GUARDRAILS = {
    "ant-design": [
        "Prefer functional management shells with literal sider or header navigation over decorative dashboard framing.",
        "Keep radii moderate and avoid glass, frosted, or overly soft consumer-style panels.",
        "Treat button hierarchy strictly: one primary action in a local group, with default, text, or link buttons for secondary work.",
        "Make table toolbars, sorting, filters, and row actions central to dashboard output rather than optional decoration.",
    ],
    "atlassian-design-system": [
        "Model the screen as a product workspace with top-level framing plus side navigation, not as an isolated generic admin page.",
        "Favor token-driven neutrals, lozenges, banners, and inline messaging over pill-heavy status styling.",
        "Keep typography practical and compact, with lightweight metadata rather than display-like page chrome.",
        "Reduce heavy dark shells and decorative shadows; Atlassian surfaces should feel light, layered, and operational.",
    ],
    "carbon-design-system": [
        "Use Carbon UI shell patterns with a persistent shell header and productive navigation instead of a decorative dark sidebar dashboard.",
        "Treat IBM Plex Sans productive hierarchy and a compact 14px-oriented rhythm as defining constraints.",
        "Enforce one-primary-action layouts and rely on secondary, tertiary, or ghost buttons for nearby actions.",
        "Make data-table toolbars, selection, sorting, and batch actions first-class parts of generated dashboards.",
    ],
    "digital-agency-design-system": [
        "Prefer plain service headers, conventional page flow, and simple navigation over branded app-shell chrome.",
        "Avoid blur, glossy effects, and heavily rounded card systems; public-service screens should feel direct and conventional.",
        "Keep search, labels, notices, and actions utility-oriented rather than hero-like or presentation-led.",
        "Favor readable sections and explicit borders over dashboard tile styling.",
    ],
    "fluent-2": [
        "Use calm token-driven surfaces with subtle dividers instead of decorative shells or glossy header treatments.",
        "Keep exactly one prominent primary action per task area and demote the rest to outline, subtle, or transparent styles.",
        "Use short task-oriented nav labels and support icon-led navigation where it helps recognition.",
        "Write status labels in short sentence-style language and keep badges semantically focused rather than ornamental.",
    ],
    "human-interface-guidelines": [
        "Favor Apple-native-feeling sidebars, split views, and toolbars over web-dashboard shells.",
        "Use materials and blur only when they read as platform-native structure, not as decorative frosting.",
        "Integrate search into the toolbar or title area instead of presenting it as a large standalone utility field.",
        "Keep grouped sections, buttons, and status indicators subtle and consistent with platform metaphors.",
    ],
    "lightning-design-system": [
        "Favor Salesforce global navigation, object context, page headers, highlights panels, and record-page segmentation over generic admin dashboards.",
        "Use flatter utility-first surfaces and avoid soft rounded dashboard chrome.",
        "Bring related lists, tabs, metric display, and explicit action regions into the default composition for dashboard-like pages.",
        "Prefer utility icons and explicit status/action patterns over bespoke pills and decorative labels.",
    ],
    "material-design": [
        "Make adaptive shell behavior explicit: use top app bars, navigation rails, drawers, and supporting panes based on width and complexity.",
        "Use semantic shape scale rather than repeating one large radius across every component.",
        "Lean on tonal containers and role-driven color emphasis instead of neutral enterprise panels.",
        "Do not default to a fixed desktop sidebar when generating Material dashboard screens.",
    ],
    "primer-product-ui": [
        "Favor calm PageLayout-style structure, clear page headers, and product-oriented navigation over bespoke dashboard framing.",
        "Keep radii, shadows, and surface treatment restrained, relying on muted containers and whitespace discipline.",
        "Prefer page header, nav list, and underline-nav style patterns before inventing custom chrome.",
        "Use semantic landmarks and focused hierarchy so the output feels like a GitHub product surface rather than a themed admin panel.",
    ],
    "smarthr-design-system": [
        "Use calm, approachable Japanese business-product surfaces with whitespace and borders doing more work than shadow or contrast-heavy shells.",
        "Prefer SmartHR's documented main blue as the primary action anchor in generated screens.",
        "Keep labels concise and operational, avoiding presentation-oriented English dashboard framing language.",
        "Make side navigation, cards, and data tables feel lightweight, practical, and accessible.",
    ],
    "sparkle-design": [
        "Preserve product personality and brand character instead of collapsing into a monochrome generic admin dashboard.",
        "Use controlled accent color, deliberate hierarchy, and polished composition to express system voice without harming usability.",
        "Treat reusable layout quality and crafted composition as part of the design output, not just component reuse.",
        "Where public guidance is thin, avoid speculative component/token claims and keep the spec explicit about inference.",
    ],
    "spectrum": [
        "Do not treat a dark utility shell as the default Spectrum expression; prefer lighter, refined workflow surfaces unless context clearly calls for dark framing.",
        "Express Adobe-like polish through typography, spacing, and detailed component hierarchy rather than generic enterprise density.",
        "Favor cohesive, approachable, contextual workflows over heavy admin-console styling.",
        "Use accent color and panel structure with restraint so the result feels modern, friendly, and detail-oriented.",
    ],
}


def apply_guardrail(slug: str) -> None:
    path = ROOT / "design_systems" / slug / "DESIGN.md"
    content = path.read_text(encoding="utf-8")
    section = "## Dashboard Mock Guardrails\n" + "\n".join(f"- {line}" for line in GUARDRAILS[slug]) + "\n\n"
    marker = "## Screen Generation Heuristics"
    if "## Dashboard Mock Guardrails" in content:
        head, tail = content.split("## Dashboard Mock Guardrails", 1)
        _, rest = tail.split(marker, 1)
        content = head + section + marker + rest
    else:
        content = content.replace(marker, section + marker, 1)
    path.write_text(content, encoding="utf-8")


def main():
    for slug in GUARDRAILS:
        apply_guardrail(slug)


if __name__ == "__main__":
    main()
