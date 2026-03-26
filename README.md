# design-system-skills

A collection of agent skills for generating UI mocks and frontend outputs in the style of specific design systems.

Each skill includes a `SKILL.md` and a `DESIGN.md`. Together, they help an agent choose layout patterns, navigation structures, components, tone, and copy style that match the target design system instead of falling back to a generic dashboard UI.

Unlike a general-purpose `frontend-design` skill, this repository is opinionated around specific design systems. Use `frontend-design` when you want broad frontend design and implementation help without locking the output to a named system; use these skills when the result should be recognizably aligned to Material Design, Ant Design, SmartHR Design System, and other concrete design languages.

## Included Skills

- [Ant Design](https://ant.design/)
- [Atlassian Design System](https://atlassian.design/)
- [Carbon Design System](https://carbondesignsystem.com/)
- [Digital Agency Design System](https://design.digital.go.jp/)
- [Fluent 2](https://fluent2.microsoft.design/)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Lightning Design System](https://v1.lightningdesignsystem.com/)
- [Material Design](https://m3.material.io/)
- [Primer Product UI](https://primer.style/product)
- [SmartHR Design System](https://smarthr.design/)
- [Sparkle Design](https://sparkle-design.goodpatch.com/sparkle-design)
- [Spectrum](https://spectrum.adobe.com/)
- [Spindle Design System](https://spindle.ameba.design/)

## Installation

This repository is intended to be installed with [`vercel-labs/skills`](https://github.com/vercel-labs/skills) using `npx skills add`.

### 1. List the available skills in this repository

```bash
npx skills add https://github.com/hidekatsu-izuno/design-system-skills --list
```

### 2. Install a specific skill

```bash
npx skills add https://github.com/hidekatsu-izuno/design-system-skills --skill material-design
```

Install multiple skills at once:

```bash
npx skills add https://github.com/hidekatsu-izuno/design-system-skills \
  --skill material-design \
  --skill ant-design \
  --skill smarthr-design-system
```

Install for a specific agent such as Codex:

```bash
npx skills add https://github.com/hidekatsu-izuno/design-system-skills \
  --agent codex \
  --skill material-design
```

Install globally:

```bash
npx skills add https://github.com/hidekatsu-izuno/design-system-skills \
  --global \
  --skill material-design
```

For the full set of options, see the [`vercel-labs/skills` README](https://github.com/vercel-labs/skills).

## Usage

After installation, invoke the skill by name when asking the agent to generate or modify UI.

Examples:

- `Use material-design to build an organization list screen`
- `Use smarthr-design-system for a Japanese back-office UI`
- `Use primer-product-ui for a developer-facing admin screen`

These skills are designed around the following assumptions:

- The agent should read `DESIGN.md` before making visual or structural decisions
- `SKILL.md` defines the behavior, layout, copy, and output constraints for that design system
- The agent should not invent visible sections or UI blocks that are not requested in the prompt or source spec such as `AGENTS.md`

## Directory Structure

```text
skills/
  <skill-name>/
    SKILL.md
    DESIGN.md

tests/
```

- `skills/`: the design-system skill definitions
- `tests/`: sample specs and generated HTML mocks used for validation

## Development Notes

- Each skill is maintained as a pair of `SKILL.md` and `DESIGN.md`
- UI generation behavior is validated against the sample specs under `tests/sample*/`
- Shared rules such as form layout, drawer behavior, and copy constraints are propagated across all relevant `SKILL.md` files

## License

This project is licensed under the MIT License.
See [LICENSE](./LICENSE) for details.
