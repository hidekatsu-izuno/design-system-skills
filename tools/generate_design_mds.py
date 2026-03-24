#!/usr/bin/env python3

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "research" / "design_system_list.csv"
OUT_DIR = ROOT / "design_systems"


COMPONENT_ORDER = [
    "Button",
    "Text field",
    "Select/combobox",
    "Checkbox",
    "Radio",
    "Switch",
    "Date/time picker",
    "Search",
    "Menu",
    "Tabs",
    "Breadcrumb",
    "App bar/header",
    "Side navigation/drawer",
    "Card",
    "Table/Data grid",
    "List",
    "Badge",
    "Tooltip",
    "Dialog/Modal",
    "Toast/Snackbar",
    "Progress/Loading",
    "Pagination",
]


SYSTEM_CONFIG = {
    "Material Design": {
        "slug": "material-design",
        "title": "Material Design",
        "overview": "Use this specification for adaptive product UI that should feel expressive, structured, and modern without becoming ornamental. Favor semantic color roles, clear hierarchy, and component choices that scale from mobile to desktop.",
        "principles": [
            "Use semantic roles and emphasis levels rather than arbitrary decoration.",
            "Prefer adaptive layouts that respond cleanly to narrow, medium, and large screens.",
            "Use motion to clarify hierarchy and state changes, not to entertain.",
            "Keep surfaces layered and purposeful.",
            "Make primary actions obvious and secondary actions quiet.",
        ],
        "palette_note": "Representative Material 3 palette for generation. Use semantic roles in implementation; the values below are representative rather than exhaustive token exports.",
        "colors": [
            ("Primary", "#6750A4", "Main action color and selected-state emphasis."),
            ("On Primary", "#FFFFFF", "Text and icons on primary-filled surfaces."),
            ("Secondary", "#625B71", "Supporting emphasis and alternate accents."),
            ("Tertiary", "#7D5260", "Expressive accent for supportive highlights."),
            ("Surface", "#FFFBFE", "Base app surface and page background."),
            ("Surface Variant", "#E7E0EC", "Container backgrounds, dividers, and low-emphasis grouping."),
            ("On Surface", "#1C1B1F", "Primary text and icon color on light surfaces."),
            ("Outline", "#79747E", "Borders, strokes, and inactive emphasis."),
        ],
        "typography": [
            "Use Roboto or the platform-default Material type stack.",
            "Use a clear display/headline/title/body/label hierarchy rather than custom one-off sizes.",
            "Keep body text neutral and readable; use label styles for compact actions and metadata.",
            "Use medium weight for primary labels and buttons, regular weight for longer reading.",
            "Avoid mixing too many type scales in a single view.",
        ],
        "spacing": [
            "Use a 4dp-based spacing rhythm with 8dp and 16dp as the most common steps.",
            "Use medium rounding by default; prefer 12px to 16px corners for cards, fields, and dialogs.",
            "Use elevation to separate surfaces, not to create dramatic shadows.",
            "Let spacing and tonal containers do more work than borders.",
        ],
        "layout_rules": [
            "Use top app bars, navigation bars, rails, or drawers based on screen width and destination count.",
            "Prefer single-column composition on mobile and wider panes or supporting panels on desktop.",
            "Group related content into cards or tonal sections when it improves scanability.",
            "Use dense layouts only when task complexity requires them.",
            "Keep primary actions anchored near the end of the task flow or in persistent action regions.",
        ],
        "navigation_rules": [
            "Use bottom navigation for a small number of top-level destinations on mobile.",
            "Use navigation rail for larger mobile and tablet layouts when persistent section switching helps.",
            "Use a drawer for broad information architecture or utility-heavy destinations.",
            "Use tabs for sibling content views inside a single destination.",
        ],
        "content_accessibility": [
            "Use short labels and explicit helper text for form fields.",
            "Preserve visible focus, pressed, selected, disabled, and error states.",
            "Do not rely on color alone to convey meaning.",
            "Use accessible contrast on both tonal and neutral surfaces.",
            "Pair empty states with action-oriented copy and a clear next step.",
        ],
        "dos": [
            "Do use tonal hierarchy to distinguish importance levels.",
            "Do use chips for lightweight filtering and selection metadata.",
            "Do keep navigation patterns responsive to screen size.",
            "Do express brand through color roles and illustration accents, not through arbitrary chrome.",
            "Do use surface containers to chunk complex screens into readable groups.",
        ],
        "donts": [
            "Do not use glassmorphism, translucent blur-heavy panels, or frosted cards.",
            "Do not flatten all emphasis into a single filled-button style.",
            "Do not over-outline every container when tonal surfaces are sufficient.",
            "Do not use consumer-social styling such as oversized avatars and playful gradients by default.",
            "Do not invent custom control shapes that fight Material components.",
        ],
        "screen_generation": {
            "page_structure": "Use a top app bar with one primary content column. Add navigation rail, drawer, or a supporting pane as complexity increases.",
            "density": "Use medium density by default. Tighten spacing only for data-heavy enterprise screens.",
            "navigation_model": "Use app bar plus tabs, bottom nav, rail, or drawer depending on viewport size and destination count.",
            "form_composition": "Use stacked labeled fields with helper text, clear validation, and one dominant submit action.",
            "feedback_pattern": "Use snackbars for transient updates, inline errors for forms, and dialogs only for blocking decisions.",
            "data_display_pattern": "Use cards, lists, and data tables with clear row hierarchy and restrained inline actions.",
            "prompt_bias": "Use prompts such as 'Material 3 dashboard', 'tonal surfaces', 'adaptive navigation rail', and 'filled / outlined / text button hierarchy'.",
        },
        "styles": {
            "button": "Prefer filled buttons for the primary action, tonal or outlined buttons for secondary actions, and text buttons for low-emphasis actions.",
            "text_field": "Use filled or outlined text fields with visible labels, helper text, and strong focus and error states.",
            "select": "Use exposed menus, dropdowns, and autocomplete patterns that align with Material input fields.",
            "choice": "Use compact, clearly labeled selection controls with explicit selected, disabled, and error states.",
            "date": "Use date and time pickers that match Material field styling and modal behavior.",
            "search": "Use a dedicated search bar or search view with clear focus and filtering affordances.",
            "menu": "Use menus and sheets with clear option grouping and moderate rounding.",
            "tabs": "Use primary or secondary tabs with strong selected-state contrast and clear alignment to content panes.",
            "breadcrumb": "Use breadcrumbs sparingly; prefer rail, drawer, or tabs before deep breadcrumb chains.",
            "header": "Use top app bars with concise titles, contextual actions, and optional search or overflow.",
            "sidenav": "Use rail or drawer patterns with strong current-destination emphasis.",
            "card": "Use tonal or elevated cards to group related content and actions.",
            "table": "Use data tables with clear row density, sortable headers, and restrained inline actions.",
            "list": "Use lists for scanable item collections with avatars, metadata, or trailing actions only when useful.",
            "badge": "Use badges and chips for status, filters, and lightweight metadata.",
            "tooltip": "Use plain or rich tooltips only for supporting clarification.",
            "dialog": "Use dialogs and sheets for blocking choices, focused tasks, or supportive secondary flows.",
            "toast": "Use snackbars for transient non-blocking feedback.",
            "progress": "Use circular or linear progress indicators and skeletons that match the surrounding surface hierarchy.",
            "pagination": "Use pagination mainly in desktop data-heavy contexts; prefer infinite or chunked scrolling on mobile.",
        },
        "sources": [
            "https://m3.material.io/",
            "https://m3.material.io/styles/color/roles",
            "https://m3.material.io/styles/typography/overview",
            "https://m3.material.io/foundations/layout/understanding-layout/overview",
            "https://m3.material.io/components",
        ],
    },
    "Human Interface Guidelines": {
        "slug": "human-interface-guidelines",
        "title": "Human Interface Guidelines",
        "overview": "Use this specification for interfaces that should feel native to Apple platforms. Favor clarity, restraint, familiar controls, and layouts that defer to content rather than brand-heavy UI treatment.",
        "principles": [
            "Prioritize clarity in labels, icon use, and overall navigation structure.",
            "Let content lead; interface chrome should support, not dominate.",
            "Use native metaphors and control behavior whenever possible.",
            "Adjust layout, spacing, and control treatment by platform family.",
            "Keep motion and depth subtle and platform-consistent.",
        ],
        "palette_note": "Representative Apple system palette for generation. Use semantic system colors in implementation; these hex values are representative.",
        "colors": [
            ("System Blue", "#007AFF", "Primary action color and interactive emphasis."),
            ("System Green", "#34C759", "Success and positive confirmation."),
            ("System Orange", "#FF9500", "Caution and intermediate attention."),
            ("System Red", "#FF3B30", "Destructive actions and errors."),
            ("Background", "#FFFFFF", "Primary light background."),
            ("Secondary Background", "#F2F2F7", "Grouped backgrounds and panels."),
            ("Label", "#1C1C1E", "Primary text color on light surfaces."),
            ("Separator", "#C6C6C8", "Dividers and low-emphasis strokes."),
        ],
        "typography": [
            "Use San Francisco as the primary typeface.",
            "Use Apple-style text roles rather than inventing a custom display system.",
            "Favor strong readability, generous line height, and restrained weight changes.",
            "Use platform-standard text styles for titles, body content, captions, and controls.",
            "Keep uppercase labels rare and functional.",
        ],
        "spacing": [
            "Use platform-native spacing and alignment; prioritize optical balance over a rigid visible grid.",
            "Use rounded rectangles and materials that align with the target Apple platform.",
            "Use blur, translucency, and depth only in platform-native ways.",
            "Keep shadows subtle; depth should feel systemic rather than decorative.",
        ],
        "layout_rules": [
            "Use platform-appropriate containers such as split views, sidebars, tab bars, toolbars, and sheets.",
            "Respect safe areas, title regions, and expected control placement for each platform.",
            "Use grouped sections and inset panels where native patterns call for them.",
            "Avoid over-dense enterprise layouts unless the app category clearly supports them.",
            "When generating for macOS, allow more persistent side navigation and toolbar actions than on iPhone.",
        ],
        "navigation_rules": [
            "Use tab bars for a small number of top-level destinations on iPhone.",
            "Use sidebars and split views for iPadOS and macOS information architecture.",
            "Use back navigation and hierarchical drill-in patterns when content is naturally nested.",
            "Avoid mixing too many navigation metaphors in one screen.",
        ],
        "content_accessibility": [
            "Use concise, human labels and avoid jargon-heavy control text.",
            "Preserve dynamic type scalability and comfortable tap targets.",
            "Use semantic colors, not raw brand colors, for status whenever possible.",
            "Ensure controls read as native and predictable to VoiceOver users.",
            "Keep destructive actions explicit and visually separated from safe actions.",
        ],
        "dos": [
            "Do prefer native controls and familiar Apple patterns.",
            "Do keep chrome quiet and let content carry the screen.",
            "Do use system colors and typography roles before introducing custom branding.",
            "Do adapt layouts by platform family rather than forcing one universal shell.",
            "Do use SF Symbols for interface iconography when possible.",
        ],
        "donts": [
            "Do not add non-native ornamentation, loud shadows, or novelty gradients.",
            "Do not force Material- or enterprise-style app shells onto Apple screens.",
            "Do not crowd the screen with multiple simultaneous emphasis patterns.",
            "Do not replace native segmented controls, sheets, or menus with bespoke alternatives without reason.",
            "Do not use over-branded buttons or aggressively custom form fields.",
        ],
        "screen_generation": {
            "page_structure": "Use content-first structure with native headers, grouped sections, and platform-appropriate sidebars or tab bars.",
            "density": "Use comfortable density. Let breathing room and legibility outweigh data compression.",
            "navigation_model": "Use tab bars, sidebars, toolbars, split views, and sheets according to Apple platform conventions.",
            "form_composition": "Use clearly grouped fields, native pickers, and conservative validation messaging.",
            "feedback_pattern": "Use alerts, banners, inline validation, and native transient feedback sparingly.",
            "data_display_pattern": "Use lists, collections, and tables that prioritize readability over operational density.",
            "prompt_bias": "Use prompts such as 'native iOS settings screen', 'macOS sidebar detail view', 'SF Symbols', and 'content-first Apple UI'.",
        },
        "styles": {
            "button": "Prefer native filled or bordered button treatments and segmented controls that match Apple platform conventions.",
            "text_field": "Use clean native text fields with visible labels when needed and subtle container styling.",
            "select": "Use native menus, pop-up buttons, and pickers rather than heavily customized dropdowns.",
            "choice": "Use platform-native checkboxes, radio-like selections, and switches with familiar spacing and behavior.",
            "date": "Use native date pickers, wheels, calendars, or compact pickers according to platform context.",
            "search": "Use the native search field pattern integrated into the relevant container.",
            "menu": "Use menus and context menus that feel native and lightweight.",
            "tabs": "Use tab bars or segmented controls depending on whether the switch is global or local.",
            "breadcrumb": "Use path-like navigation only where the platform supports it; otherwise prefer sidebars, back navigation, or split views.",
            "header": "Use restrained navigation bars, toolbars, or title areas with minimal visual noise.",
            "sidenav": "Use sidebars and split views instead of generic web-style drawers whenever possible.",
            "card": "Use grouped panels or inset sections before introducing generic cards.",
            "table": "Use clean tables or outline views with strong text alignment and little decoration.",
            "list": "Use lists and collections with platform-native spacing and separators.",
            "badge": "Use badges and status labels sparingly and semantically.",
            "tooltip": "Use tooltips as supplemental help, especially on desktop.",
            "dialog": "Use alerts, sheets, and popovers with native structure and concise decisions.",
            "toast": "Use transient feedback sparingly and in platform-native ways.",
            "progress": "Use native progress bars, spinners, and activity indicators.",
            "pagination": "Use pagination rarely; prefer content grouping, search, or hierarchical drill-in.",
        },
        "sources": [
            "https://developer.apple.com/design/human-interface-guidelines/",
            "https://developer.apple.com/design/human-interface-guidelines/color",
            "https://developer.apple.com/design/human-interface-guidelines/typography",
            "https://developer.apple.com/design/human-interface-guidelines/layout",
            "https://developer.apple.com/design/human-interface-guidelines/controls",
        ],
    },
    "Fluent 2 Design System": {
        "slug": "fluent-2",
        "title": "Fluent 2 Design System",
        "overview": "Use this specification for productive, cross-platform Microsoft-style applications. Favor approachable structure, strong tokenization, explicit states, and layouts that support work rather than spectacle.",
        "principles": [
            "Design for productive tasks, not pure marketing impression.",
            "Use explicit states and accessible contrast throughout.",
            "Keep surfaces calm and theme-aware.",
            "Favor approachable geometry over severe sharpness.",
            "Let component behavior stay predictable across surfaces and themes.",
        ],
        "palette_note": "Representative Fluent 2 palette for generation. Use tokens in implementation; the hex values below capture the design language without claiming exhaustive token coverage.",
        "colors": [
            ("Brand", "#0F6CBD", "Primary Microsoft-style action and brand emphasis."),
            ("Brand Pressed", "#0C3B5E", "Pressed or stronger action emphasis."),
            ("Brand Tint", "#EBF3FC", "Tinted selection, hover, and supportive surfaces."),
            ("Neutral Foreground", "#242424", "Primary text and icon color."),
            ("Neutral Background", "#FFFFFF", "Default canvas and card surfaces."),
            ("Neutral Subtle", "#F5F5F5", "Low-emphasis surface and section grouping."),
            ("Success", "#107C10", "Success and positive confirmation."),
            ("Danger", "#D13438", "Error and destructive emphasis."),
        ],
        "typography": [
            "Use Segoe UI or the current Microsoft platform type stack.",
            "Use a clear ramp of display, title, subtitle, body, and caption roles.",
            "Favor functional, readable text over expressive editorial treatment.",
            "Use semibold strategically for headers and primary control labels.",
            "Keep tables and forms typographically compact but not cramped.",
        ],
        "spacing": [
            "Use token-driven spacing with 4px and 8px cadence at the core.",
            "Use soft radii, typically around 4px to 8px for controls and 8px to 12px for containers.",
            "Use shadows and elevation quietly; structure should come mostly from spacing and surface value.",
            "Keep component spacing consistent across adjacent controls and panels.",
        ],
        "layout_rules": [
            "Use app shells with clear header, navigation, and content regions.",
            "Support both simple single-column screens and multi-pane productivity layouts.",
            "Use compact density when task throughput matters, but preserve scanability.",
            "Group related content with subtle container separation rather than loud cards everywhere.",
            "Make state changes obvious through field messages, badges, and action feedback.",
        ],
        "navigation_rules": [
            "Use left-side navigation, top tabs, or app shell patterns for complex products.",
            "Use toolbar patterns for dense command surfaces.",
            "Use breadcrumbs when users move across deep hierarchies.",
            "Keep local navigation close to the content area it controls.",
        ],
        "content_accessibility": [
            "Use direct labels and task-oriented copy.",
            "Make focus, hover, pressed, selected, and disabled states explicit.",
            "Prefer inline validation and calm status messaging over modal interruption.",
            "Preserve readable contrast in both light and dark themes.",
            "Use icons to support labels, not replace them.",
        ],
        "dos": [
            "Do make states highly legible and easy to scan.",
            "Do keep productivity tasks front and center.",
            "Do use theme-aware surfaces and semantic color roles.",
            "Do structure dense screens with clear hierarchy and predictable alignment.",
            "Do use compact controls when the workflow demands efficiency.",
        ],
        "donts": [
            "Do not make Fluent screens overly playful, bubbly, or consumer-social.",
            "Do not use oversized shadows or high-gloss surfaces.",
            "Do not hide state changes behind subtle color-only differences.",
            "Do not over-brand the shell when the product task should dominate.",
            "Do not replace standard productivity components with experimental shapes.",
        ],
        "screen_generation": {
            "page_structure": "Use a productivity shell with persistent navigation, clear page title, command region, and structured content panes.",
            "density": "Use medium-to-compact density by default.",
            "navigation_model": "Use left navigation, tabs, toolbars, and contextual command surfaces.",
            "form_composition": "Use aligned labeled fields, strong helper text, inline validation, and clearly grouped actions.",
            "feedback_pattern": "Use message bars, toasts, inline status, and dialogs only when interruption is necessary.",
            "data_display_pattern": "Use structured tables, lists, cards, and panels with visible status metadata.",
            "prompt_bias": "Use prompts such as 'Fluent 2 productivity app', 'Microsoft admin console', 'calm neutral surfaces', and 'explicit stateful controls'.",
        },
        "styles": {
            "button": "Prefer clear primary, secondary, and subtle button hierarchy with strong state visibility.",
            "text_field": "Use token-driven fields with explicit labels, helper text, and strong focus/error treatments.",
            "select": "Use comboboxes and dropdowns that support productivity workflows and keyboard use.",
            "choice": "Use checkboxes, radios, and switches with compact but comfortable spacing and visible states.",
            "date": "Use date and time pickers that align with field composition and enterprise workflows.",
            "search": "Use search boxes that can expand into command or filtering workflows.",
            "menu": "Use compact menus with clear grouping and keyboard-friendly behavior.",
            "tabs": "Use tabs and tablists for local view switching in app and panel contexts.",
            "breadcrumb": "Use breadcrumbs when deep app hierarchy needs persistent orientation.",
            "header": "Use page headers and command bars that prioritize task controls.",
            "sidenav": "Use left navigation or pane-based navigation for persistent product structure.",
            "card": "Use quiet cards and panels to organize related information blocks.",
            "table": "Use dense but readable tables and grids with visible column hierarchy and state cues.",
            "list": "Use structured lists with metadata, avatars, and utility actions where appropriate.",
            "badge": "Use badges and status pills for state, category, or lightweight metadata.",
            "tooltip": "Use tooltips for supporting clarification, especially in command-dense interfaces.",
            "dialog": "Use dialogs for focused decisions and side panels for longer secondary tasks.",
            "toast": "Use toast or message bar feedback without overusing interruption.",
            "progress": "Use spinners, progress bars, and skeletons with explicit surrounding context.",
            "pagination": "Use pagination in dense data views when chunking improves throughput and orientation.",
        },
        "sources": [
            "https://fluent2.microsoft.design/",
            "https://fluent2.microsoft.design/color",
            "https://fluent2.microsoft.design/typography",
            "https://fluent2.microsoft.design/layout",
            "https://fluent2.microsoft.design/components/web/react/core/button/usage",
        ],
    },
    "Atlassian Design System": {
        "slug": "atlassian-design-system",
        "title": "Atlassian Design System",
        "overview": "Use this specification for collaboration-heavy SaaS and work-management UI. Favor dense but readable layouts, semantic tokens, strong inline feedback, and patterns that support issues, projects, and operational workflows.",
        "principles": [
            "Optimize for collaborative work and high-information screens.",
            "Use semantic tokens and predictable spacing before decorative styling.",
            "Make hierarchy readable in dense layouts.",
            "Keep patterns operational, practical, and action-oriented.",
            "Prefer inline feedback over unnecessary interruption.",
        ],
        "palette_note": "Representative Atlassian palette for generation based on current public guidance and token usage. Use semantic tokens in implementation; these values are representative.",
        "colors": [
            ("Blue", "#0C66E4", "Primary action, active state, and key navigation emphasis."),
            ("Blue Subtle", "#E9F2FF", "Selected backgrounds and supportive highlights."),
            ("Text", "#172B4D", "Primary body and heading text."),
            ("Subtle Text", "#44546F", "Secondary metadata and supporting labels."),
            ("Surface", "#FFFFFF", "Base canvas and card surface."),
            ("Neutral Subtle", "#F7F8F9", "Panels, low-emphasis containers, and row hover."),
            ("Danger", "#CA3521", "Destructive and error emphasis."),
            ("Success", "#1F845A", "Success states and positive completion."),
        ],
        "typography": [
            "Use Atlassian Sans when available or a close neutral product sans stack.",
            "Keep hierarchy practical and product-oriented rather than editorial.",
            "Use concise headings and lightweight metadata styles.",
            "Favor strong alignment and rhythm over dramatic size contrast.",
            "Use semibold sparingly for anchors such as page titles, section titles, and primary actions.",
        ],
        "spacing": [
            "Use a tight but consistent spacing system suited to enterprise collaboration tools.",
            "Use moderate radius values and avoid overly soft consumer card styling.",
            "Use shadows minimally; rely on background value shifts and borders more than depth theatrics.",
            "Keep rows, tables, and side panels compact but readable.",
        ],
        "layout_rules": [
            "Use persistent side navigation or workspace shells for complex products.",
            "Allow dense content regions with clear section headers and inline metadata.",
            "Use page-level banners, inline messages, and panel layouts to support workflows.",
            "Keep action placement predictable across issue, task, and project surfaces.",
            "Prefer operational clarity over decorative asymmetry.",
        ],
        "navigation_rules": [
            "Use left navigation and product-level top structure for app shells.",
            "Use tabs for content subviews inside a workspace or object page.",
            "Use breadcrumbs when users traverse deep project or object hierarchies.",
            "Keep navigation labels literal and task-oriented.",
        ],
        "content_accessibility": [
            "Use direct action labels and short explanatory helper text.",
            "Maintain strong focus and selected states in dense interfaces.",
            "Use inline validation and inline messaging where possible.",
            "Keep icon-only controls paired with accessible names.",
            "Use status lozenges, flags, and badges consistently.",
        ],
        "dos": [
            "Do build for dense collaboration workflows and long-lived work objects.",
            "Do keep tables, lists, and forms highly structured.",
            "Do use semantic tokens and subtle surfaces consistently.",
            "Do communicate status with strong inline messaging and lozenges.",
            "Do use layout patterns that feel like serious product tools, not marketing pages.",
        ],
        "donts": [
            "Do not use soft consumer-style cards, oversized whitespace, or lifestyle-brand hero layouts.",
            "Do not over-round controls or containers.",
            "Do not hide critical actions behind ambiguous overflow unless the workflow warrants it.",
            "Do not use novelty gradients or expressive illustration as the main hierarchy tool.",
            "Do not collapse dense workflows into overly sparse mobile-style compositions on desktop.",
        ],
        "screen_generation": {
            "page_structure": "Use a workspace shell with side navigation, a practical page header, and dense operational content blocks.",
            "density": "Use medium-to-dense layout density.",
            "navigation_model": "Use side navigation, tabs, breadcrumbs, and in-context actions.",
            "form_composition": "Use structured sections, inline help, and strong field-level validation.",
            "feedback_pattern": "Use inline messages, flags, banners, and dialog confirmation for destructive changes.",
            "data_display_pattern": "Use tables, issue lists, cards, side panels, and metadata-rich rows.",
            "prompt_bias": "Use prompts such as 'Atlassian-style admin screen', 'collaboration workspace', 'dense issue table', and 'semantic product tokens'.",
        },
        "styles": {
            "button": "Prefer a practical primary button with quiet secondary and link-style low-emphasis actions.",
            "text_field": "Use compact text fields and text areas with direct labels and inline messaging.",
            "select": "Use selects, popup selects, and autocomplete for operational filtering and assignment workflows.",
            "choice": "Use compact choice controls that remain legible in dense forms and filter panels.",
            "date": "Use date and time fields that fit object-editing and planning workflows.",
            "search": "Use search fields that can support product-wide find, filtering, and command-like discovery.",
            "menu": "Use dropdown and overflow menus with clear grouping and low visual ornamentation.",
            "tabs": "Use tabs as practical sibling-view switches inside dense product areas.",
            "breadcrumb": "Use breadcrumbs to support object and workspace hierarchy, not as decorative navigation.",
            "header": "Use a functional page header with title, metadata, and immediate actions.",
            "sidenav": "Use side navigation as a core app-shell pattern for larger products.",
            "card": "Use cards and panels sparingly to group operational content without making the UI feel soft.",
            "table": "Use dense, metadata-rich tables with clear statuses, row actions, and sortable structure.",
            "list": "Use structured lists and object rows for issue, task, or item workflows.",
            "badge": "Use lozenges, badges, and status marks to make workflow state instantly scannable.",
            "tooltip": "Use tooltips for clarification in dense action areas, not as a substitute for labels.",
            "dialog": "Use dialogs and drawers for focused edits or confirmations that should not overload the page.",
            "toast": "Use flags or equivalent transient messaging for operation feedback.",
            "progress": "Use spinners and progress indicators as lightweight workflow feedback, not visual centerpiece.",
            "pagination": "Use pagination where table chunking improves orientation and performance.",
        },
        "sources": [
            "https://atlassian.design/",
            "https://atlassian.design/foundations/color-new",
            "https://atlassian.design/foundations/typography",
            "https://atlassian.design/foundations/layout",
            "https://atlassian.design/components",
        ],
    },
    "Ant Design": {
        "slug": "ant-design",
        "title": "Ant Design",
        "overview": "Use this specification for enterprise web applications, dashboards, and internal tools. Favor information density, broad component coverage, predictable grids, and direct administrative workflows.",
        "principles": [
            "Design for efficient task completion in data-heavy environments.",
            "Use strong grid alignment and a clear page shell.",
            "Let components solve operational tasks directly.",
            "Keep theming systematic and algorithmic rather than handcrafted per screen.",
            "Support broad form, table, and filtering workflows.",
        ],
        "palette_note": "Representative Ant Design palette for generation based on v5 semantics and common product usage. Use official token algorithms in implementation; these values are representative.",
        "colors": [
            ("Primary", "#1677FF", "Primary action and active interactive emphasis."),
            ("Success", "#52C41A", "Success and positive status."),
            ("Warning", "#FAAD14", "Caution and intermediate attention."),
            ("Error", "#FF4D4F", "Errors and destructive emphasis."),
            ("Text", "#1F1F1F", "Primary text on light surfaces."),
            ("Background", "#FFFFFF", "Primary application surface."),
            ("Container", "#F5F5F5", "Low-emphasis panels and section surfaces."),
            ("Border", "#D9D9D9", "Input, table, and container borders."),
        ],
        "typography": [
            "Use a neutral enterprise sans stack, typically with system sans defaults.",
            "Keep hierarchy pragmatic and compact.",
            "Use page titles, section titles, body text, and compact control text without excessive variation.",
            "Favor dense tables and forms with readable but not loose line height.",
            "Use medium emphasis for buttons, labels, and data headers.",
        ],
        "spacing": [
            "Use a clear grid system and regular panel spacing.",
            "Use moderate radii and avoid overly soft consumer rounded surfaces.",
            "Use shadows when surfacing overlays, drawers, and cards, but keep them utilitarian.",
            "Keep field spacing compact and consistent across form sections.",
        ],
        "layout_rules": [
            "Use a dashboard or management shell with header, sider, and content regions when appropriate.",
            "Support dense table, filter, and form areas without collapsing hierarchy.",
            "Use cards and sections to organize related modules in larger screens.",
            "Keep admin workflows explicit through action bars, filters, and summaries.",
            "Prefer operational symmetry over expressive composition.",
        ],
        "navigation_rules": [
            "Use top navigation, side navigation, or a hybrid application shell for enterprise apps.",
            "Use tabs and steps for local workflow segmentation.",
            "Use breadcrumbs in deep admin structures and nested settings areas.",
            "Keep nav labels literal and easy to scan.",
        ],
        "content_accessibility": [
            "Use direct labels, placeholders only as hints, and strong field-level validation.",
            "Preserve clear hover, active, selected, disabled, and error states.",
            "Support RTL and localization-aware layout decisions.",
            "Use messages, notifications, and status color consistently.",
            "Keep icon usage secondary to readable labels.",
        ],
        "dos": [
            "Do lean into the system's broad component coverage for enterprise tasks.",
            "Do use tables, filters, forms, and cards as primary building blocks.",
            "Do keep layouts structured and operational.",
            "Do use algorithmic theming rather than ad hoc color decisions.",
            "Do make workflow state obvious through status, tags, and notifications.",
        ],
        "donts": [
            "Do not style Ant screens like soft consumer landing pages.",
            "Do not overuse illustrations, gradients, or playful decorative surfaces.",
            "Do not create huge whitespace gaps that weaken dashboard scanability.",
            "Do not replace straightforward controls with overly bespoke alternatives.",
            "Do not bury key filters and table actions behind excessive nesting.",
        ],
        "screen_generation": {
            "page_structure": "Use a management shell with optional sider, page header, filter region, and structured content blocks.",
            "density": "Use medium-to-dense density by default.",
            "navigation_model": "Use top nav, sider, tabs, steps, and breadcrumbs depending on workflow depth.",
            "form_composition": "Use labeled fields, sectioned forms, inline validation, and clear submit/cancel actions.",
            "feedback_pattern": "Use message, notification, result, and modal patterns according to urgency.",
            "data_display_pattern": "Use tables, cards, lists, statistics, and charts with explicit filters and sorting.",
            "prompt_bias": "Use prompts such as 'Ant Design admin dashboard', 'sider layout', 'dense enterprise table', and 'algorithmic token theme'.",
        },
        "styles": {
            "button": "Prefer clear primary, default, dashed, text, and link hierarchies suited to enterprise tasks.",
            "text_field": "Use compact but readable inputs with explicit labels and strong status borders.",
            "select": "Use selects, cascaders, autocompletes, and searchable dropdowns to handle complex choice sets.",
            "choice": "Use straightforward choice controls that integrate cleanly into filter bars and forms.",
            "date": "Use date and time pickers that fit dense filter and scheduling workflows.",
            "search": "Use search inputs as part of table filters, toolbars, and management headers.",
            "menu": "Use menus and dropdowns with practical grouping and little visual flourish.",
            "tabs": "Use tabs for local task segmentation and steps for process-based flows.",
            "breadcrumb": "Use breadcrumbs to anchor the user in deep administrative IA.",
            "header": "Use practical page headers with title, metadata, actions, and optional breadcrumb context.",
            "sidenav": "Use sider navigation for persistent application structure on desktop.",
            "card": "Use cards to modularize dashboards and related information groups.",
            "table": "Use data tables as a first-class pattern with filters, row actions, and status tags.",
            "list": "Use lists when the data is lighter-weight than a table or needs more flexible row content.",
            "badge": "Use badges and tags for state, count, and categorization.",
            "tooltip": "Use tooltips to clarify dense controls or truncated labels.",
            "dialog": "Use modals, drawers, and popconfirms for interruptive actions and secondary tasks.",
            "toast": "Use message and notification patterns for transient or global feedback.",
            "progress": "Use progress bars, spinners, and skeletons to keep busy states explicit in dense screens.",
            "pagination": "Use pagination heavily in tables and long administrative collections.",
        },
        "sources": [
            "https://ant.design/",
            "https://ant.design/docs/spec/introduce",
            "https://ant.design/docs/spec/colors",
            "https://ant.design/docs/spec/font",
            "https://ant.design/components/overview",
        ],
    },
    "Carbon Design System": {
        "slug": "carbon-design-system",
        "title": "Carbon Design System",
        "overview": "Use this specification for serious enterprise interfaces, operational dashboards, and products that require accessibility, structure, and a disciplined visual system. Favor grid logic, strong information hierarchy, and restrained styling.",
        "principles": [
            "Optimize for clarity and enterprise-scale usability.",
            "Use the grid to create order before adding decoration.",
            "Keep motion restrained and purposeful.",
            "Use layered surfaces and theme-aware contrast carefully.",
            "Make dense information readable through structure and rhythm.",
        ],
        "palette_note": "Representative Carbon palette for generation based on public themes and IBM blue emphasis. Use Carbon tokens in implementation; these values are representative.",
        "colors": [
            ("Interactive", "#0F62FE", "Primary action and active emphasis."),
            ("Text Primary", "#161616", "Primary text and icon color."),
            ("Text Secondary", "#525252", "Secondary text and supporting metadata."),
            ("Background", "#FFFFFF", "Primary page background."),
            ("Layer 01", "#F4F4F4", "First elevated or grouped layer."),
            ("Layer 02", "#E0E0E0", "Additional layer separation and input backgrounds."),
            ("Success", "#24A148", "Success and positive confirmation."),
            ("Danger", "#DA1E28", "Error and destructive emphasis."),
        ],
        "typography": [
            "Use IBM Plex Sans as the primary interface typeface.",
            "Use a disciplined productive typographic hierarchy rather than expressive display-heavy treatment.",
            "Keep headings compact and functional.",
            "Use readable line length and restrained weight changes.",
            "Let tables, forms, and operational content stay crisp and efficient.",
        ],
        "spacing": [
            "Use the Carbon spacing scale with a strong 2x Grid mindset.",
            "Use modest radius and avoid soft card-heavy consumer styling.",
            "Prefer layered backgrounds and subtle borders over dramatic shadow depth.",
            "Keep spacing highly consistent across sections, fields, and tables.",
        ],
        "layout_rules": [
            "Use the 2x Grid to create alignment, rhythm, and density control.",
            "Support structured enterprise shells with clear sections and utility actions.",
            "Use panels and grouped regions when task segmentation helps comprehension.",
            "Allow dense content, but keep rows, columns, and hierarchy crisp.",
            "Treat whitespace as a structural tool rather than a luxury aesthetic.",
        ],
        "navigation_rules": [
            "Use side navigation and shell patterns for larger products.",
            "Use tabs for sibling content areas and view switching.",
            "Use breadcrumbs when navigating deep product hierarchies.",
            "Keep navigation labels literal and utility-oriented.",
        ],
        "content_accessibility": [
            "Use explicit labels and strong state communication for fields and controls.",
            "Preserve visible focus and strong contrast in all themes.",
            "Use accessible component states as a non-negotiable baseline.",
            "Prefer inline explanation over hidden affordances.",
            "Use calm, direct content in error and empty-state messaging.",
        ],
        "dos": [
            "Do build the page around grid structure and task clarity.",
            "Do use layered surfaces and type hierarchy to manage complex information.",
            "Do keep interactions explicit and accessible.",
            "Do use tables, forms, and panels confidently in enterprise contexts.",
            "Do make the UI feel stable and deliberate.",
        ],
        "donts": [
            "Do not style Carbon screens like soft consumer apps or startup marketing pages.",
            "Do not use oversized shadows, playful gradients, or decorative blobs.",
            "Do not over-round controls or turn every section into a floating card.",
            "Do not collapse dense workflows into excessively spacious layouts.",
            "Do not sacrifice grid discipline for asymmetrical flourish.",
        ],
        "screen_generation": {
            "page_structure": "Use an enterprise shell with side nav, precise sectioning, and structured content panes aligned to the grid.",
            "density": "Use medium-to-dense density with strong alignment.",
            "navigation_model": "Use shell navigation, side nav, tabs, and breadcrumbs for complex product structures.",
            "form_composition": "Use labeled fields, strong validation, and orderly field groups that align tightly to the grid.",
            "feedback_pattern": "Use inline messaging, notifications, and modal confirmation only when a stronger interruption is justified.",
            "data_display_pattern": "Use tables, tiles, panels, and status-rich lists with disciplined hierarchy.",
            "prompt_bias": "Use prompts such as 'Carbon enterprise console', 'IBM-style structured dashboard', '2x grid layout', and 'disciplined operational UI'.",
        },
        "styles": {
            "button": "Prefer direct, high-contrast button hierarchy with strong accessibility and limited ornament.",
            "text_field": "Use crisp text inputs with visible labels, helper text, and explicit invalid states.",
            "select": "Use structured dropdown and multiselect patterns suited to enterprise forms and filters.",
            "choice": "Use compact, high-legibility choice controls with strong state feedback.",
            "date": "Use date and time inputs that align tightly with form grids and operational scheduling tasks.",
            "search": "Use search as a structured product function, often paired with filters and result management.",
            "menu": "Use restrained menus and overflow patterns with clear grouping and accessible focus behavior.",
            "tabs": "Use tabs to segment major sibling views inside a larger enterprise shell.",
            "breadcrumb": "Use breadcrumbs for complex hierarchy, not as decorative metadata.",
            "header": "Use clear page headers and shell headers that prioritize orientation and action clarity.",
            "sidenav": "Use side nav confidently in desktop-oriented product shells.",
            "card": "Use tiles and panels for modular grouping without making the UI soft or consumer-like.",
            "table": "Use tables as a flagship component with strong structure, sorting, status, and batch action support.",
            "list": "Use structured lists when table formality is unnecessary but hierarchy still matters.",
            "badge": "Use status indicators and tags to make workflow state scannable.",
            "tooltip": "Use tooltips as clarification for dense product surfaces, not as a crutch for poor labels.",
            "dialog": "Use modals and side panels for focused tasks or confirmations that justify interruption.",
            "toast": "Use concise toast or notification patterns for background process feedback.",
            "progress": "Use progress bars, loading states, and skeletons with a calm enterprise tone.",
            "pagination": "Use pagination in longer tables and data collections where chunking improves orientation.",
        },
        "sources": [
            "https://carbondesignsystem.com/",
            "https://carbondesignsystem.com/guidelines/color/overview/",
            "https://carbondesignsystem.com/guidelines/typography/overview/",
            "https://carbondesignsystem.com/guidelines/2x-grid/overview/",
            "https://carbondesignsystem.com/components/overview/",
        ],
    },
    "Lightning Design System": {
        "slug": "lightning-design-system",
        "title": "Lightning Design System",
        "overview": "Use this specification for CRM-style, record-centric business applications. Favor structured record pages, clear utility navigation, explicit statuses, and forms or tables that support object-heavy workflows.",
        "principles": [
            "Design around records, lists, and business-object workflows.",
            "Keep page regions explicit and consistent.",
            "Use accessible business UI patterns rather than decorative surfaces.",
            "Support data-heavy tasks, filtering, and guided action flow.",
            "Make status and object metadata easy to scan.",
        ],
        "palette_note": "Representative Lightning palette for generation based on public SLDS guidance and Salesforce product styling. Use official tokens in implementation; these values are representative.",
        "colors": [
            ("Brand", "#0176D3", "Primary interactive emphasis and brand-led action color."),
            ("Brand Dark", "#032D60", "Stronger shell and enterprise emphasis."),
            ("Success", "#2E844A", "Positive completion and healthy state."),
            ("Error", "#BA0517", "Error and destructive action emphasis."),
            ("Background", "#FFFFFF", "Primary page surface."),
            ("Canvas Alt", "#F3F3F3", "Section and utility background."),
            ("Border", "#C9C9C9", "Object, field, and table separators."),
            ("Text", "#181818", "Primary readable text color."),
        ],
        "typography": [
            "Use Salesforce Sans or a close humanist enterprise sans stack.",
            "Favor practical hierarchy over expressive typography.",
            "Keep object labels, section headers, and data metadata crisp.",
            "Use compact text in forms and tables without reducing readability.",
            "Avoid over-styled headings and editorial display text.",
        ],
        "spacing": [
            "Use utility spacing and region-based composition.",
            "Use subtle radius values and straightforward enterprise surfaces.",
            "Use depth sparingly and structurally, especially for overlays and utility panels.",
            "Keep record pages aligned and compartmentalized.",
        ],
        "layout_rules": [
            "Use record-page composition with header, highlights panel, tabs, and related lists when appropriate.",
            "Use utility bars, object actions, and supporting panels for dense workflows.",
            "Support responsive desktop-first enterprise layouts rather than mobile-social composition.",
            "Keep filter, table, and form structures explicit and region-based.",
            "Use blueprint-like page segmentation whenever the workflow benefits from it.",
        ],
        "navigation_rules": [
            "Use global navigation, app launcher patterns, and object-level nav where needed.",
            "Use tabs within record pages and object areas.",
            "Use breadcrumbs lightly; object context often comes from shell and page titles.",
            "Keep utility actions near headers and record highlights.",
        ],
        "content_accessibility": [
            "Use direct labels and business-readable terminology.",
            "Preserve explicit states in forms, tables, prompts, and alerts.",
            "Use iconography to support object identification, not replace text labels.",
            "Keep validation close to the field or record action that caused it.",
            "Use accessible table and form patterns for enterprise workflows.",
        ],
        "dos": [
            "Do design around record objects, related lists, and guided business workflows.",
            "Do use page regions and object headers to structure screens.",
            "Do make status and metadata immediately visible.",
            "Do use tables, prompts, and utility actions confidently.",
            "Do keep the experience efficient and scanable for repeat work.",
        ],
        "donts": [
            "Do not make Lightning screens look like generic consumer dashboards.",
            "Do not overuse decorative cards, heavy gradients, or glassy panels.",
            "Do not hide record context or key actions behind ambiguous navigation.",
            "Do not replace business tables with card mosaics unless the use case clearly needs it.",
            "Do not soften the system into a lifestyle-brand aesthetic.",
        ],
        "screen_generation": {
            "page_structure": "Use an app shell or record-page shell with utility navigation, object header, tabs, and related content regions.",
            "density": "Use medium-to-dense density with strong business scanability.",
            "navigation_model": "Use global app navigation, object context, tabs, and contextual utility actions.",
            "form_composition": "Use sectioned enterprise forms with explicit labels, validation, and record-level actions.",
            "feedback_pattern": "Use prompts, scoped notifications, and inline field messaging for business actions.",
            "data_display_pattern": "Use data tables, record lists, related lists, and object summaries as primary patterns.",
            "prompt_bias": "Use prompts such as 'Salesforce-style record page', 'object highlights panel', 'related list table', and 'SLDS business shell'.",
        },
        "styles": {
            "button": "Prefer direct business-action button hierarchy with clear primary and utility actions.",
            "text_field": "Use explicit enterprise fields with labels, required indicators, and nearby validation.",
            "select": "Use comboboxes and picklists for structured object workflows and form completion.",
            "choice": "Use enterprise-friendly selection controls with readable spacing and explicit states.",
            "date": "Use date and time controls that work inside record-editing and scheduling flows.",
            "search": "Use global or object-level search fields with strong utility placement.",
            "menu": "Use action menus and utility menus with explicit grouping and object relevance.",
            "tabs": "Use tabs as a core local-navigation pattern inside record and object pages.",
            "breadcrumb": "Use breadcrumbs only where the shell and page context do not already provide sufficient orientation.",
            "header": "Use object or page headers that surface key metadata and immediate actions.",
            "sidenav": "Use enterprise shell navigation and object context panes instead of consumer drawers.",
            "card": "Use cards for modular business summaries, but prioritize page-region logic over card galleries.",
            "table": "Use data tables as a core pattern for records, related items, and result sets.",
            "list": "Use list views and record rows for object collections and quick scanning.",
            "badge": "Use badges and status indicators to encode record state, object type, or count.",
            "tooltip": "Use tooltips to support compact enterprise controls without replacing clear labels.",
            "dialog": "Use prompts, modals, and panels for record edits or critical confirmations.",
            "toast": "Use scoped or global notifications for action outcomes and background updates.",
            "progress": "Use spinners and progress indicators to keep long-running business actions legible.",
            "pagination": "Use pagination in data tables and list views when chunking improves enterprise throughput.",
        },
        "sources": [
            "https://v1.lightningdesignsystem.com/",
            "https://v1.lightningdesignsystem.com/design-tokens/",
            "https://v1.lightningdesignsystem.com/utilities/themes/",
            "https://v1.lightningdesignsystem.com/components/overview/",
            "https://v1.lightningdesignsystem.com/accessibility/overview/",
        ],
    },
    "Primer Product UI": {
        "slug": "primer-product-ui",
        "title": "Primer Product UI",
        "overview": "Use this specification for GitHub-like product interfaces, developer tools, settings surfaces, and workflow-oriented applications. Favor utility, clarity, and quiet but strong structure.",
        "principles": [
            "Let product utility and content hierarchy drive the screen.",
            "Use primitives and semantic variables to keep the interface systematic.",
            "Keep styling understated and developer-tool practical.",
            "Support both dense data and comfortable readability.",
            "Use component naming and layout patterns that feel familiar to serious software products.",
        ],
        "palette_note": "Representative Primer palette for generation based on current product UI primitives. Use variables in implementation; these hex values are representative.",
        "colors": [
            ("Accent", "#0969DA", "Primary interactive emphasis and link/action color."),
            ("Success", "#1F883D", "Success and positive state."),
            ("Attention", "#9A6700", "Warning and needs-attention emphasis."),
            ("Danger", "#CF222E", "Error and destructive emphasis."),
            ("Canvas Default", "#FFFFFF", "Primary page background."),
            ("Canvas Subtle", "#F6F8FA", "Muted panels and section backgrounds."),
            ("Foreground Default", "#1F2328", "Primary text and icon color."),
            ("Border Default", "#D0D7DE", "Borders, table dividers, and field boundaries."),
        ],
        "typography": [
            "Use a neutral system sans stack appropriate for developer products.",
            "Keep headings functional and direct.",
            "Use monospace only for code, data snippets, and strongly technical labels.",
            "Preserve readable density in settings pages, forms, and table-like lists.",
            "Use weight changes modestly and let layout provide most hierarchy.",
        ],
        "spacing": [
            "Use a disciplined spacing scale with practical compactness.",
            "Use small-to-moderate radii and restrained shadows.",
            "Prefer borders, muted surfaces, and layout grouping over rich card effects.",
            "Keep row height, field spacing, and action spacing highly consistent.",
        ],
        "layout_rules": [
            "Use page layouts with clear header, side navigation, and content hierarchy when the product area is complex.",
            "Support split layouts, settings pages, and repository-style information density.",
            "Use sections, subheaders, and muted containers to organize complex screens.",
            "Keep actions near the data or task they affect.",
            "Favor compact clarity over ornamental whitespace.",
        ],
        "navigation_rules": [
            "Use side nav, underline nav, and page-local patterns for clear product orientation.",
            "Use breadcrumbs only when nested hierarchy is genuinely helpful.",
            "Use tabs for sibling views and segmented content regions.",
            "Keep top-level navigation restrained and utility-first.",
        ],
        "content_accessibility": [
            "Use clear technical language and avoid ambiguous marketing copy in product screens.",
            "Maintain strong focus treatment and keyboard navigability.",
            "Use icons to support labels and status, not replace readable text.",
            "Keep error and help copy concise and task-oriented.",
            "Use code or monospace treatment only where semantics justify it.",
        ],
        "dos": [
            "Do make the UI feel practical, reliable, and developer-friendly.",
            "Do use muted surfaces, borders, and strong alignment to manage complexity.",
            "Do use components and primitives consistently across settings and workflows.",
            "Do keep navigation and metadata explicit.",
            "Do let content and action structure drive the page.",
        ],
        "donts": [
            "Do not turn Primer screens into glossy marketing pages or soft consumer dashboards.",
            "Do not overuse large shadows, loud gradients, or decorative illustrations.",
            "Do not hide important settings and actions behind ambiguous icon-only patterns.",
            "Do not over-round containers or use whimsical control styling.",
            "Do not replace practical lists and tables with over-carded layouts without reason.",
        ],
        "screen_generation": {
            "page_structure": "Use a utility-first product page with a clear title, optional side navigation, explicit section grouping, and practical action placement.",
            "density": "Use medium density with compact tendencies for settings and tool screens.",
            "navigation_model": "Use side navigation, underline nav, tabs, and page headers for strong orientation.",
            "form_composition": "Use clearly labeled fields, concise help text, and practical action groups.",
            "feedback_pattern": "Use banners, flash messages, inline validation, and dialogs only when blocking is justified.",
            "data_display_pattern": "Use lists, tables, cards, and timelines in a calm, utility-first way.",
            "prompt_bias": "Use prompts such as 'GitHub product settings page', 'Primer side nav', 'muted borders', and 'developer tool UI'.",
        },
        "styles": {
            "button": "Prefer restrained button hierarchy with clear primary emphasis and quiet secondary actions.",
            "text_field": "Use practical text inputs with visible labels, concise help, and strong keyboard/focus support.",
            "select": "Use selects and select panels that fit settings and workflow contexts rather than decorative dropdowns.",
            "choice": "Use straightforward choice controls with explicit labels and compact spacing.",
            "date": "Use date-related inputs when needed, styled to match a practical product surface.",
            "search": "Use search as a strong utility tool in headers, filters, and content lists.",
            "menu": "Use action menus and compact menus for contextual operations.",
            "tabs": "Use underline-style tabs or related navigation for sibling views.",
            "breadcrumb": "Use breadcrumbs conservatively in nested product structures.",
            "header": "Use practical page headers with clear title, metadata, and nearby actions.",
            "sidenav": "Use side nav for durable product orientation in larger tools and settings areas.",
            "card": "Use cards and muted panels to organize content without making the interface feel soft.",
            "table": "Use data tables and structured rows where developers or operators need quick scanning.",
            "list": "Use action lists and metadata-rich rows for flexible workflow presentation.",
            "badge": "Use labels, counters, and tokens to communicate state and categorization clearly.",
            "tooltip": "Use tooltips to support dense interfaces, not to compensate for vague labels.",
            "dialog": "Use dialogs and overlays for focused decisions and secondary tasks.",
            "toast": "Use flash-like transient messaging that stays practical and unobtrusive.",
            "progress": "Use spinners, skeletons, and progress bars in a quiet utility style.",
            "pagination": "Use pagination when large result sets need explicit chunking and orientation.",
        },
        "sources": [
            "https://primer.style/product",
            "https://primer.style/product/primitives/color",
            "https://primer.style/product/primitives/typography",
            "https://primer.style/product/components/page-layout",
            "https://primer.style/product/components",
        ],
    },
    "Spectrum": {
        "slug": "spectrum",
        "title": "Spectrum",
        "overview": "Use this specification for Adobe-style product experiences, creative workflows, and polished application UI. Favor semantic tokens, refined typography, clear workflow containers, and branded but disciplined visual language.",
        "principles": [
            "Support creative and professional workflows without losing clarity.",
            "Use semantic tokens and reusable language across product families.",
            "Balance polish with systematic component behavior.",
            "Let workflow structure guide page composition.",
            "Keep themes expressive but controlled.",
        ],
        "palette_note": "Representative Spectrum palette for generation. Use official Spectrum tokens in implementation; these values are representative and tuned for UI generation.",
        "colors": [
            ("Blue", "#1473E6", "Primary action and selected-state emphasis."),
            ("Purple", "#6F5CFF", "Expressive accent and branded secondary emphasis."),
            ("Green", "#008F5D", "Success and healthy completion."),
            ("Red", "#D31510", "Error and destructive emphasis."),
            ("Gray 900", "#2C2C2C", "Primary dark text and dark-mode surface anchor."),
            ("Gray 50", "#FFFFFF", "Light surface and content background."),
            ("Gray 100", "#F8F8F8", "Subtle containers and low-emphasis panels."),
            ("Border", "#D5D5D5", "Field, panel, and overlay boundaries."),
        ],
        "typography": [
            "Use Adobe Clean or a close modern neutral sans stack.",
            "Keep hierarchy polished and workflow-aware rather than purely utilitarian.",
            "Use stronger title styling than enterprise admin systems, but stay disciplined.",
            "Preserve readable body text across dense creative tools and configuration panels.",
            "Use emphasis to support tool or asset hierarchy, not marketing flourish.",
        ],
        "spacing": [
            "Use a consistent spacing scale that supports panels, toolbars, and workflow regions.",
            "Use moderate radius and refined surfaces rather than severe sharpness.",
            "Use overlays and depth with control, especially for popovers, trays, and dialogs.",
            "Keep alignment precise in tools, panels, and asset-heavy layouts.",
        ],
        "layout_rules": [
            "Use workflow-centered composition with panels, tools, and content zones.",
            "Support both focused document-like screens and denser application shells.",
            "Use side panels, headers, and trays when they strengthen creation or review flows.",
            "Keep the interface polished, but avoid decorative clutter around work content.",
            "Use thematic consistency across surfaces and control families.",
        ],
        "navigation_rules": [
            "Use shell navigation, tabs, and side panels based on the product workflow.",
            "Use breadcrumbs or path indicators only when hierarchy truly matters.",
            "Keep local tool navigation close to the content it affects.",
            "Support both app-level and object-level navigation cleanly.",
        ],
        "content_accessibility": [
            "Use direct labels and avoid hiding critical state in pure iconography.",
            "Preserve contrast and state clarity across themes.",
            "Use supporting text and contextual help around complex tools or workflows.",
            "Keep terminology consistent across panels and actions.",
            "Use empty states and onboarding copy to guide the next creative action.",
        ],
        "dos": [
            "Do make the UI feel polished and systematized.",
            "Do use semantic colors and refined typography consistently.",
            "Do organize screens around workflows, tools, and content.",
            "Do keep panels and overlays clean and purposeful.",
            "Do let Adobe-style polish emerge through consistency, not ornament overload.",
        ],
        "donts": [
            "Do not turn Spectrum screens into generic enterprise admin dashboards.",
            "Do not overuse loud gradients, glossy cards, or decorative motion.",
            "Do not crowd creative workflows with unnecessary chrome.",
            "Do not flatten all hierarchy into one neutral gray layer.",
            "Do not use rough or mismatched component styling that breaks the polished system tone.",
        ],
        "screen_generation": {
            "page_structure": "Use a workflow shell with clear content region, supporting panels, and polished but restrained app chrome.",
            "density": "Use medium density, allowing denser panels where workflow complexity requires it.",
            "navigation_model": "Use shell navigation, tabs, side panels, and contextual overlays according to the workflow.",
            "form_composition": "Use polished labeled fields with concise helper text and controlled validation.",
            "feedback_pattern": "Use toasts, dialogs, popovers, and inline status patterns with a calm but refined tone.",
            "data_display_pattern": "Use lists, asset grids, tables, and panel-based details depending on workflow fit.",
            "prompt_bias": "Use prompts such as 'Adobe Spectrum workflow UI', 'refined panels', 'creative tool shell', and 'polished semantic tokens'.",
        },
        "styles": {
            "button": "Prefer polished but restrained button hierarchy with clear primary emphasis.",
            "text_field": "Use refined text inputs with visible labels and clean helper or validation messaging.",
            "select": "Use pickers and comboboxes that fit polished workflow surfaces and complex assets or options.",
            "choice": "Use selection controls that remain explicit and accessible without feeling heavy.",
            "date": "Use date and time inputs only when the workflow requires them, styled to match Spectrum fields.",
            "search": "Use search as a strong workflow tool in headers, asset areas, or filtering contexts.",
            "menu": "Use menus and action menus with careful spacing and clear option grouping.",
            "tabs": "Use tabs to switch sibling workflows or subviews inside a larger shell.",
            "breadcrumb": "Use breadcrumbs where workflow hierarchy or path context matters, not by default.",
            "header": "Use polished headers that orient the user without overpowering the work surface.",
            "sidenav": "Use side panels or nav rails when workflow context benefits from persistent structure.",
            "card": "Use cards and panels as controlled grouping surfaces, not as casual dashboard tiles.",
            "table": "Use tables where precise asset or data scanning matters, with refined but readable density.",
            "list": "Use lists for navigational, asset, or metadata workflows with clean structure.",
            "badge": "Use badges and labels to communicate state and classification in a polished way.",
            "tooltip": "Use tooltips and coach marks for clarification in tool-dense areas.",
            "dialog": "Use dialogs, trays, and overlays for focused tasks and workflow interruptions.",
            "toast": "Use polished transient messaging that supports workflow continuity.",
            "progress": "Use progress indicators and skeletons that stay calm within content-heavy workflows.",
            "pagination": "Use pagination when dense result sets require explicit chunking; otherwise prefer filtering and navigation.",
        },
        "sources": [
            "https://spectrum.adobe.com/",
            "https://spectrum.adobe.com/page/design-language/",
            "https://spectrum.adobe.com/page/color/",
            "https://spectrum.adobe.com/page/typography/",
            "https://spectrum.adobe.com/page/components/",
        ],
    },
    "SmartHR Design System": {
        "slug": "smarthr-design-system",
        "title": "SmartHR Design System",
        "overview": "Use this specification for Japanese business SaaS, HR workflows, and back-office tools. Favor trust, clarity, and straightforward operational layouts with accessible defaults and minimal visual excess.",
        "principles": [
            "Design for trust, clarity, and dependable business operation.",
            "Use concise labels and explicit guidance for form-heavy screens.",
            "Keep visual language approachable but not casual.",
            "Prefer practical layout and component choices over expressive experimentation.",
            "Support accessibility and Japanese business-product readability by default.",
        ],
        "palette_note": "Representative SmartHR palette for generation based on public design-token guidance and product styling. Use official tokens in implementation; these values are representative.",
        "colors": [
            ("Primary", "#00C4CC", "Main action and brand-led emphasis."),
            ("Primary Tint", "#E5FAFB", "Soft highlight and selected-state background."),
            ("Text", "#23221F", "Primary text color."),
            ("Background", "#FFFFFF", "Base application surface."),
            ("Subtle Surface", "#F8F7F6", "Panels, grouped sections, and low-emphasis containers."),
            ("Border", "#D6D3D1", "Table, field, and section borders."),
            ("Warning", "#FF9900", "Caution and pending attention."),
            ("Danger", "#E5484D", "Error and destructive emphasis."),
        ],
        "typography": [
            "Use SmartHR Sans when available or a close readable sans stack that supports Japanese well.",
            "Keep hierarchy practical and approachable.",
            "Favor body readability and field clarity over large expressive headings.",
            "Use compact metadata styles but do not collapse readability in dense administrative screens.",
            "Preserve consistent rhythm between Japanese and Latin content.",
        ],
        "spacing": [
            "Use a practical spacing cadence that keeps forms and lists easy to scan.",
            "Use moderate rounding and calm surface hierarchy.",
            "Use shadows lightly and prefer whitespace plus borders for structure.",
            "Keep field spacing, labels, and section grouping highly consistent.",
        ],
        "layout_rules": [
            "Use straightforward page composition with clear title, navigation, and content blocks.",
            "Support form-heavy operational flows and list/detail patterns.",
            "Use cards, tables, and grouped sections to keep business content readable.",
            "Avoid ornamental asymmetry and aggressive visual flourishes.",
            "Favor trust-building clarity over trend-driven density extremes.",
        ],
        "navigation_rules": [
            "Use simple, readable navigation with strong labels and modest hierarchy depth.",
            "Use tabs, side navigation, or local navigation only where task grouping benefits from it.",
            "Use breadcrumbs when the information architecture becomes deep enough to justify them.",
            "Keep navigation text explicit and low-ambiguity.",
        ],
        "content_accessibility": [
            "Use plain, direct interface language suited to business and HR operations.",
            "Make validation and required fields explicit.",
            "Preserve accessible contrast and focus treatment across all controls.",
            "Use icons and illustrations as support, not as the main communication layer.",
            "Keep forms calm, readable, and easy to complete in sequence.",
        ],
        "dos": [
            "Do make the interface feel dependable and business-ready.",
            "Do prioritize form clarity, list readability, and explicit feedback.",
            "Do use subtle brand color accents rather than over-branding the full shell.",
            "Do support Japanese text comfortably in labels, tables, and help text.",
            "Do keep the experience calm and operational.",
        ],
        "donts": [
            "Do not turn SmartHR screens into flashy startup landing pages.",
            "Do not use overly dark or dramatic visual treatment by default.",
            "Do not hide validation or rely on placeholder-only labeling.",
            "Do not over-pack screens with dense micro-panels if simple sections will do.",
            "Do not use playful novelty components that weaken trust.",
        ],
        "screen_generation": {
            "page_structure": "Use a calm business shell with a readable header, practical navigation, and content grouped into forms, lists, and sections.",
            "density": "Use medium density with readable spacing.",
            "navigation_model": "Use straightforward navigation, tabs, and side navigation only where task organization benefits.",
            "form_composition": "Use stacked or well-aligned labeled fields with explicit validation and helper text.",
            "feedback_pattern": "Use inline validation, notices, toasts, and dialogs with clear business wording.",
            "data_display_pattern": "Use tables, cards, and lists for employee data, settings, and administrative workflows.",
            "prompt_bias": "Use prompts such as 'SmartHR business app', 'Japanese HR workflow', 'calm teal accents', and 'clear back-office form layout'.",
        },
        "styles": {
            "button": "Prefer clear primary and secondary buttons with calm brand color emphasis.",
            "text_field": "Use practical fields with explicit labels, helper text, and readable validation.",
            "select": "Use straightforward selects and comboboxes for business configuration and data entry.",
            "choice": "Use readable choice controls with enough spacing for Japanese labels and explanatory text.",
            "date": "Use date inputs that feel businesslike and integrate cleanly with operational forms.",
            "search": "Use search as a direct utility for finding records, people, or settings.",
            "menu": "Use menus with explicit labels and restrained visual treatment.",
            "tabs": "Use tabs when sibling business views need fast switching without adding confusion.",
            "breadcrumb": "Use breadcrumbs when deeper administrative IA needs orientation support.",
            "header": "Use practical page headers with title, summary, and a small action set.",
            "sidenav": "Use side navigation for larger business products, but keep structure simple and readable.",
            "card": "Use cards and sections to keep back-office information grouped and approachable.",
            "table": "Use tables confidently for records, settings, and administrative data.",
            "list": "Use lists where the content is lighter-weight or more narrative than a full table.",
            "badge": "Use badges and labels for status, state, and lightweight categorization.",
            "tooltip": "Use tooltips sparingly to clarify controls without hiding essential guidance.",
            "dialog": "Use dialogs for confirmations and focused secondary tasks, not for routine validation.",
            "toast": "Use toast or notice patterns for non-blocking business feedback.",
            "progress": "Use loading and progress indicators calmly and clearly.",
            "pagination": "Use pagination in longer administrative lists and records where chunking helps orientation.",
        },
        "sources": [
            "https://smarthr.design/",
            "https://smarthr.design/products/design-tokens/color-palette/",
            "https://smarthr.design/products/design-tokens/typography/",
            "https://smarthr.design/products/design-tokens/media-query/",
            "https://smarthr.design/products/components/",
        ],
    },
    "Sparkle Design": {
        "slug": "sparkle-design",
        "title": "Sparkle Design",
        "overview": "Use this specification for digital products that need a deliberate visual system with stronger brand character than a pure utility system, while still staying reusable and scalable. Favor coherent branding, practical product structure, and controlled expressiveness.",
        "principles": [
            "Use a reusable visual language that still preserves product personality.",
            "Favor scalable patterns over one-off visual flourishes.",
            "Let brand expression support product clarity, not overpower it.",
            "Keep layout and navigation practical for digital products.",
            "Use design-system thinking to make quality repeatable.",
        ],
        "palette_note": "Representative Sparkle palette inferred from public Sparkle Design examples and Goodpatch branding context. Treat these values as generation guidance, not as an official token export.",
        "colors": [
            ("Primary", "#111111", "Strong base text and key contrast anchor."),
            ("Accent", "#FF6B3D", "Expressive action and branded highlight color."),
            ("Support", "#FFC857", "Warm secondary accent for highlights and emphasis."),
            ("Background", "#FFFFFF", "Base canvas and clean surface."),
            ("Subtle Surface", "#F7F5F2", "Section grouping and quiet panel surface."),
            ("Border", "#DDD6CE", "Light structure and field boundaries."),
            ("Muted Text", "#5E5A55", "Secondary metadata and supporting labels."),
            ("Info Accent", "#4A90E2", "Supplementary interactive or informational emphasis."),
        ],
        "typography": [
            "Use a clean modern sans stack with enough personality to support brand expression.",
            "Allow slightly more expressive heading contrast than a pure enterprise system.",
            "Keep body and interface text highly readable and product-oriented.",
            "Use brand expression through hierarchy and spacing before resorting to heavy decoration.",
            "Avoid overly quirky or fashion-editorial typography in product screens.",
        ],
        "spacing": [
            "Use consistent spacing that keeps the product feeling polished and intentionally composed.",
            "Use moderate-to-soft radii when the brand direction supports it, but keep controls practical.",
            "Use depth selectively; avoid stacking gratuitous shadows everywhere.",
            "Let whitespace and composition express polish more than special effects.",
        ],
        "layout_rules": [
            "Use clear page structure and a recognizable product shell.",
            "Allow stronger brand moments in headers, hero sections, or section transitions when the workflow supports them.",
            "Keep product areas practical and navigable even when visual identity is more pronounced.",
            "Use cards, sections, and modular panels to scale the system cleanly.",
            "Prefer deliberate composition over generic dashboard repetition.",
        ],
        "navigation_rules": [
            "Use clear top-level navigation and local navigation patterns that feel product-specific but still familiar.",
            "Use tabs and side navigation when they simplify content grouping rather than for decoration.",
            "Keep labels literal even when visual styling is more expressive.",
            "Avoid hiding structure behind oversized visual branding elements.",
        ],
        "content_accessibility": [
            "Use readable contrast and explicit interaction states despite the stronger brand layer.",
            "Keep copy direct and useful; do not let tone undermine comprehension.",
            "Preserve accessible spacing and target sizes in branded components.",
            "Use imagery and iconography to support hierarchy, not to replace it.",
            "Keep form and validation guidance clear even in visually expressive screens.",
        ],
        "dos": [
            "Do let the product feel intentionally branded and well composed.",
            "Do keep reusable patterns stronger than one-off art direction.",
            "Do use expressive accent color selectively for emphasis.",
            "Do keep product shells and forms practical and scalable.",
            "Do allow stronger visual moments only where they support product identity.",
        ],
        "donts": [
            "Do not turn Sparkle screens into generic monochrome enterprise dashboards.",
            "Do not over-decorate every section with gradients, stickers, or visual noise.",
            "Do not let branding weaken form clarity or navigation comprehension.",
            "Do not use playful consumer gimmicks if the product context is serious.",
            "Do not treat expressive accents as a substitute for hierarchy and layout discipline.",
        ],
        "screen_generation": {
            "page_structure": "Use a clear product shell with opportunities for brand expression in selected anchor areas, while keeping operational content practical.",
            "density": "Use medium density with enough breathing room to let the visual system read clearly.",
            "navigation_model": "Use familiar top-level nav, tabs, and side navigation in a product-specific but readable way.",
            "form_composition": "Use clean, well-labeled forms with branded restraint rather than decorative novelty.",
            "feedback_pattern": "Use notices, toasts, and dialogs that match the system's visual voice without becoming theatrical.",
            "data_display_pattern": "Use cards, lists, and tables with stronger composition than generic admin UI, but keep them operational.",
            "prompt_bias": "Use prompts such as 'brand-conscious product UI', 'Goodpatch-style design system', 'controlled expressive accents', and 'polished reusable layout'.",
        },
        "styles": {
            "button": "Prefer a strong primary button and a carefully branded secondary treatment without losing clarity.",
            "text_field": "Use clean, readable fields with controlled brand styling and explicit labels.",
            "select": "Use selects and comboboxes that feel integrated into the product language rather than generic browser controls.",
            "choice": "Use clear choice controls with comfortable labels and visible state changes.",
            "date": "Use date and time controls only where the product workflow needs them, styled consistently with the broader product language.",
            "search": "Use search as a practical tool, not as a decorative centerpiece.",
            "menu": "Use menus that feel polished and branded but remain easy to scan.",
            "tabs": "Use tabs where sibling content needs clear grouping with a stronger visual identity than bare utility tabs.",
            "breadcrumb": "Use breadcrumbs only when hierarchy needs explicit support.",
            "header": "Use headers that can carry some brand expression while staying functional.",
            "sidenav": "Use side navigation when it helps complex products, but keep it structured and readable.",
            "card": "Use cards and panels as a key part of polished modular composition.",
            "table": "Use tables when the workflow is data-heavy, but maintain stronger visual discipline than generic enterprise UI.",
            "list": "Use lists for flexible presentation when cards or tables would be too rigid.",
            "badge": "Use badges and tags to reinforce state and categorization with measured brand emphasis.",
            "tooltip": "Use tooltips as supporting clarification, not as a stylish flourish.",
            "dialog": "Use dialogs for focused interruption and secondary tasks with polished but controlled styling.",
            "toast": "Use toast or notice patterns that align with the brand system without becoming noisy.",
            "progress": "Use progress and loading states with calm clarity and subtle branded support.",
            "pagination": "Use pagination when longer data or content sets need structure; avoid overusing it in narrative flows.",
        },
        "sources": [
            "https://sparkle-design.goodpatch.com/sparkle-design",
            "https://goodpatch.com/blog/2025-07-sparkle-design-3",
            "https://goodpatch.com/blog/2025-06-sparkle-design-1",
        ],
    },
    "デジタル庁デザインシステムβ版": {
        "slug": "digital-agency-design-system",
        "title": "Digital Agency Design System (Beta)",
        "overview": "Use this specification for Japanese public-service websites, form-heavy government flows, and trust-critical transactional screens. Favor plain language, conservative styling, explicit structure, and accessibility-first decisions.",
        "principles": [
            "Design for trust, clarity, and public comprehension.",
            "Make accessibility and legal/service readability the default.",
            "Use conservative visual treatment and explicit interaction patterns.",
            "Prefer standardization over product-specific flourish.",
            "Keep forms and service flows obvious and low-ambiguity.",
        ],
        "palette_note": "Representative Digital Agency palette for generation based on public component examples and government web guidance. Use official values when implementing; the values below are representative for generation.",
        "colors": [
            ("Primary Blue", "#005AC2", "Primary action, links, and core interactive emphasis."),
            ("Blue Hover", "#00408A", "Hover and active emphasis for primary controls."),
            ("Light Blue", "#E8F1FF", "Low-emphasis hover and outlined-button background."),
            ("Text", "#1A1A1A", "Primary readable text color."),
            ("Background", "#FFFFFF", "Primary document and service surface."),
            ("Subtle Surface", "#F5F5F5", "Section grouping and low-emphasis backgrounds."),
            ("Border", "#C8C8C8", "Field and section boundaries."),
            ("Danger", "#B00020", "Error and destructive emphasis."),
        ],
        "typography": [
            "Use highly readable Japanese-capable sans-serif typography.",
            "Keep hierarchy simple, direct, and service-oriented.",
            "Avoid decorative display styling and compressed text treatment.",
            "Favor readability in long guidance text, labels, and form instructions.",
            "Use emphasis sparingly and only where comprehension improves.",
        ],
        "spacing": [
            "Use consistent spacing that supports long-form reading and form completion.",
            "Use conservative radius values and straightforward component geometry.",
            "Use minimal shadow; structure should come from order, not depth effects.",
            "Keep forms, notices, and templates aligned and explicit.",
        ],
        "layout_rules": [
            "Use simple page templates with clear header, content flow, and service structure.",
            "Support long-form guidance, forms, notices, and result pages without visual complexity.",
            "Use sections, headings, and notices to guide the user through the task.",
            "Keep primary actions explicit and easy to locate.",
            "Prefer stable, conventional layouts over experimental composition.",
        ],
        "navigation_rules": [
            "Use straightforward global navigation, breadcrumbs, and side navigation where service scale requires them.",
            "Use local navigation only when it materially improves orientation.",
            "Keep navigation labels plain and official rather than branded.",
            "Avoid deep or playful navigation experiments.",
        ],
        "content_accessibility": [
            "Use plain language and explicit procedural wording.",
            "Preserve strong contrast, visible focus, and accessible target sizes.",
            "Use helper text, error text, and notices close to the point of action.",
            "Do not rely on iconography alone to communicate state or instruction.",
            "Keep forms predictable and cognitively light.",
        ],
        "dos": [
            "Do make the interface feel trustworthy, official, and easy to understand.",
            "Do use plain language and visible procedural guidance.",
            "Do use clear buttons, notices, and form structures.",
            "Do prioritize accessibility and predictable service flow.",
            "Do keep customization limited and purposeful.",
        ],
        "donts": [
            "Do not over-customize the visual language or invent product-specific flourishes.",
            "Do not use glassmorphism, gradient-heavy surfaces, or trendy startup styling.",
            "Do not turn service screens into dashboard-like card mosaics without need.",
            "Do not hide critical instructions inside tooltips or tertiary UI.",
            "Do not use playful illustrations or novelty interactions in transactional service flows.",
        ],
        "screen_generation": {
            "page_structure": "Use a conventional service page or form page with strong heading hierarchy, notices, and a clear primary action path.",
            "density": "Use medium density with generous readability for text and forms.",
            "navigation_model": "Use straightforward header navigation, breadcrumbs, side navigation, and in-page section structure when needed.",
            "form_composition": "Use strongly labeled fields, clear required markers, helper text, and explicit error messaging.",
            "feedback_pattern": "Use notices, inline errors, confirmation pages, and dialogs only for essential interruption.",
            "data_display_pattern": "Use simple tables, lists, summaries, and result pages with conservative styling.",
            "prompt_bias": "Use prompts such as 'Japanese public service form', 'official government service page', 'plain-language transaction flow', and 'accessible conservative UI'.",
        },
        "styles": {
            "button": "Prefer clear filled, outlined, and text button hierarchy with conservative styling and obvious labels.",
            "text_field": "Use explicit form fields with visible labels, helper text, and close-by validation.",
            "select": "Use plain, accessible selects and comboboxes with low-ambiguity labeling.",
            "choice": "Use straightforward checkboxes, radios, and switches with enough space for clear Japanese labels.",
            "date": "Use practical date inputs and calendars that favor comprehension over clever interaction.",
            "search": "Use search as a service utility, not as a central visual motif.",
            "menu": "Use menus only when they genuinely improve navigation or action grouping; keep them plain and direct.",
            "tabs": "Use tabs sparingly and only when sibling content views are clearly understood by users.",
            "breadcrumb": "Use breadcrumbs to maintain orientation in multi-level public-service information architecture.",
            "header": "Use a straightforward header with service title, utility navigation, and minimal visual flourish.",
            "sidenav": "Use side navigation only for larger multi-section services, keeping labels explicit and official.",
            "card": "Use cards and panels conservatively for summaries or grouped content, not as decorative layout tiles.",
            "table": "Use plain, readable tables for summaries, result sets, and reference information.",
            "list": "Use lists for steps, requirements, summaries, and straightforward content grouping.",
            "badge": "Use badges and labels only when they improve comprehension of status or category.",
            "tooltip": "Use tooltips sparingly; essential guidance should remain visible.",
            "dialog": "Use dialogs for clear confirmation or interruption points, not for routine guidance.",
            "toast": "Use toast-like transient feedback rarely; prefer visible notices and confirmation content.",
            "progress": "Use clear loading and progress states with explicit wording when the system is working.",
            "pagination": "Use pagination only where list length requires it and keep controls extremely explicit.",
        },
        "sources": [
            "https://design.digital.go.jp/",
            "https://design.digital.go.jp/dads/components/button/",
            "https://design.digital.go.jp/components/",
            "https://design.digital.go.jp/templates/",
            "https://design.digital.go.jp/guidelines/accessibility/",
        ],
    },
}


def read_csv():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    systems = [k for k in rows[0].keys() if k not in {"Section", "Item"}]
    data = {system: {} for system in systems}
    for row in rows:
        for system in systems:
            data[system][row["Item"]] = row[system].strip()
    return systems, data


def bullet_lines(items):
    return "\n".join(f"- {item}" for item in items)


def color_lines(colors):
    return "\n".join(
        f"- **{name} `{hex_value}`:** {usage}" for name, hex_value, usage in colors
    )


def component_block(title, alias, style, use_when, states, avoid):
    return (
        f"### {title}\n"
        f"- **Official naming / aliases:** {alias}\n"
        f"- **Preferred style:** {style}\n"
        f"- **Use when:** {use_when}\n"
        f"- **Important states:** {states}\n"
        f"- **Avoid:** {avoid}\n"
    )


def render_components(values, cfg):
    name_map = {
        "Button": "Use for the single most important page action and nearby secondary actions.",
        "Text field": "Use for short structured text entry with explicit labels and helper text.",
        "Select/combobox": "Use when the choice set is constrained, filterable, or too structured for free text.",
        "Checkbox": "Use for non-exclusive multi-select or independent boolean options.",
        "Radio": "Use for small exclusive option sets that should remain visible.",
        "Switch": "Use for immediate on/off states with direct effect or obvious persistence.",
        "Date/time picker": "Use for scheduling, filtering, or structured temporal input.",
        "Search": "Use for finding records, screens, or content, often paired with filters.",
        "Menu": "Use for contextual actions, option grouping, and compact command lists.",
        "Tabs": "Use for sibling views inside one destination or object context.",
        "Breadcrumb": "Use only when hierarchy depth needs visible orientation support.",
        "App bar/header": "Use to anchor the page title, context, and the most important actions.",
        "Side navigation/drawer": "Use for persistent destination structure or deeper information architecture.",
        "Card": "Use to group related content, metrics, or actions into a coherent module.",
        "Table/Data grid": "Use when users need to compare rows, scan columns, sort, or act on collections.",
        "List": "Use for lighter-weight collections or rows that need more flexible content than a table.",
        "Badge": "Use for status, counts, metadata, or lightweight categorization.",
        "Tooltip": "Use for supporting clarification that should not interrupt the task flow.",
        "Dialog/Modal": "Use for blocking decisions, focused secondary tasks, or high-risk confirmation.",
        "Toast/Snackbar": "Use for transient action feedback that should not block progress.",
        "Progress/Loading": "Use when background work, loading, or long-running actions need clear status.",
        "Pagination": "Use when chunking long result sets improves orientation, performance, or control.",
    }
    state_map = {
        "Button": "Rest, hover, focus, pressed, disabled, and loading if the action can take time.",
        "Text field": "Rest, focus, filled, invalid, disabled, and helper/error text visibility.",
        "Select/combobox": "Closed, focused, expanded, selected, filtered, invalid, and disabled states.",
        "Checkbox": "Unchecked, checked, indeterminate when relevant, focus, and disabled.",
        "Radio": "Unchecked, checked, focus, disabled, and clear group labeling.",
        "Switch": "Off, on, focus, disabled, and any paired status text.",
        "Date/time picker": "Empty, selected, invalid, focused, expanded, and disabled states.",
        "Search": "Idle, focused, active query, loading, empty results, and clear/reset states.",
        "Menu": "Closed, open, focused item, selected item, disabled item, and submenu when needed.",
        "Tabs": "Inactive, active, focus-visible, overflow if needed, and disabled when applicable.",
        "Breadcrumb": "Normal, current page, truncated if space is tight, and focus-visible links.",
        "App bar/header": "Default, scrolled where applicable, focus on actions, and overflow handling.",
        "Side navigation/drawer": "Collapsed or hidden, expanded, selected destination, hover, and keyboard focus.",
        "Card": "Default, hover only if interactive, selected when applicable, and loading/skeleton states.",
        "Table/Data grid": "Default, hover, selected row, sorted column, loading, empty, and error states.",
        "List": "Default, hover if interactive, selected when needed, loading, and empty states.",
        "Badge": "Neutral, positive, warning, danger, and selected/filter-active where relevant.",
        "Tooltip": "Hidden, visible, delayed appearance, and accessible trigger focus.",
        "Dialog/Modal": "Closed, open, focus trapped, destructive confirmation, and loading/submit state.",
        "Toast/Snackbar": "Appearing, visible, dismissing, action available, and stacked if multiple are possible.",
        "Progress/Loading": "Idle, indeterminate, determinate, skeleton, and completion state.",
        "Pagination": "Default, current page, hover/focus, disabled edge controls, and compact variants.",
    }
    avoid_map = {
        "Button": "Avoid using a secondary style for the main call to action or adding decorative button variants outside the system hierarchy.",
        "Text field": "Avoid placeholder-only labeling, hidden validation, or custom field chrome that breaks the system.",
        "Select/combobox": "Avoid replacing structured choice controls with free text when the choices are known.",
        "Checkbox": "Avoid using checkboxes for mutually exclusive choices.",
        "Radio": "Avoid using radios for long or dynamic option sets better served by a select.",
        "Switch": "Avoid using switches for actions that require confirmation or a final submit button.",
        "Date/time picker": "Avoid ad hoc date text entry without clear format help when the system supports a picker.",
        "Search": "Avoid styling search like a decorative hero input detached from the workflow.",
        "Menu": "Avoid burying primary actions inside menus when they should stay visible.",
        "Tabs": "Avoid using tabs for process steps or unrelated destinations.",
        "Breadcrumb": "Avoid long breadcrumb chains when side navigation or stronger page titles would orient the user better.",
        "App bar/header": "Avoid crowding the header with too many equal-weight actions.",
        "Side navigation/drawer": "Avoid introducing side navigation on small scopes that do not need persistent structure.",
        "Card": "Avoid turning every section into a decorative floating card when simpler grouping would be clearer.",
        "Table/Data grid": "Avoid using a table when the user does not need row or column comparison.",
        "List": "Avoid lists when the task needs stable columns, sorting, or bulk data operations.",
        "Badge": "Avoid using badges as the only way to communicate critical status.",
        "Tooltip": "Avoid hiding required instructions or validation inside tooltips.",
        "Dialog/Modal": "Avoid using dialogs for routine inline edits that fit naturally in the page.",
        "Toast/Snackbar": "Avoid using transient feedback for critical errors that must remain visible.",
        "Progress/Loading": "Avoid spinner-only loading when skeletons or explicit progress would reduce uncertainty.",
        "Pagination": "Avoid pagination when search, filtering, or progressive loading would better fit the workflow.",
    }

    style_map = {
        "Button": cfg["styles"]["button"],
        "Text field": cfg["styles"]["text_field"],
        "Select/combobox": cfg["styles"]["select"],
        "Checkbox": cfg["styles"]["choice"],
        "Radio": cfg["styles"]["choice"],
        "Switch": cfg["styles"]["choice"],
        "Date/time picker": cfg["styles"]["date"],
        "Search": cfg["styles"]["search"],
        "Menu": cfg["styles"]["menu"],
        "Tabs": cfg["styles"]["tabs"],
        "Breadcrumb": cfg["styles"]["breadcrumb"],
        "App bar/header": cfg["styles"]["header"],
        "Side navigation/drawer": cfg["styles"]["sidenav"],
        "Card": cfg["styles"]["card"],
        "Table/Data grid": cfg["styles"]["table"],
        "List": cfg["styles"]["list"],
        "Badge": cfg["styles"]["badge"],
        "Tooltip": cfg["styles"]["tooltip"],
        "Dialog/Modal": cfg["styles"]["dialog"],
        "Toast/Snackbar": cfg["styles"]["toast"],
        "Progress/Loading": cfg["styles"]["progress"],
        "Pagination": cfg["styles"]["pagination"],
    }

    blocks = []
    for item in COMPONENT_ORDER:
        alias = values[item]
        blocks.append(
            component_block(
                item,
                alias,
                style_map[item],
                name_map[item],
                state_map[item],
                avoid_map[item],
            )
        )
    return "\n".join(blocks)


def render(system, values):
    cfg = SYSTEM_CONFIG[system]
    sg = cfg["screen_generation"]
    return f"""# {cfg['title']} DESIGN.md

## Overview
{cfg['overview']}

- **Provider:** {values['Provider']}
- **Primary reference:** {values['Primary URL']}
- **Primary product focus:** {values['Primary product focus']}
- **Platforms:** Web: {values['Web']} | iOS: {values['iOS']} | Android: {values['Android']} | Desktop: {values['Desktop']}
- **Status:** {values['Status/maintenance']}
- **Implementation note:** This file is a standalone generation spec. Follow it directly when producing UI in this design system.

## Design Principles
{bullet_lines(cfg['principles'])}

## Color System
{cfg['palette_note']}

{color_lines(cfg['colors'])}

- **Dark mode guidance:** {values['Dark mode']}
- **Theming guidance:** {values['Theming/customization']}
- **Semantic token guidance:** {values['Design tokens']}

## Typography
{bullet_lines(cfg['typography'])}

- **Official typography note:** {values['Typography']}
- **Iconography:** {values['Iconography']}
- **Motion direction:** {values['Motion']}

## Spacing, Radius, Elevation
{bullet_lines(cfg['spacing'])}

- **Spacing system note:** {values['Spacing']}
- **Radius / shape note:** {values['Shape/radius']}
- **Elevation / shadow note:** {values['Elevation/shadow']}

## Layout Rules
{bullet_lines(cfg['layout_rules'])}

- **Official layout note:** {values['Layout/grid']}
- **Responsive behavior:** {values['Responsive/adaptive behavior']}
- **App structure:** {values['App structure']}
- **Data display guidance:** {values['Data visualization guidance']}

## Navigation Rules
{bullet_lines(cfg['navigation_rules'])}

- **Official navigation note:** {values['Navigation guidance']}
- **Pattern note:** {values['Navigation patterns']}

## Component Rules
{render_components(values, cfg)}

## Content & Accessibility
{bullet_lines(cfg['content_accessibility'])}

- **Accessibility note:** {values['Accessibility']}
- **Content note:** {values['Content design']}
- **Internationalization note:** {values['Internationalization']}
- **Localization / RTL note:** {values['Localization/RTL']}
- **Validation note:** {values['Validation/error handling']}
- **State model note:** {values['State model']}
- **Privacy / trust note:** {values['Privacy/trust']}

## Do / Don't
### Do
{bullet_lines(cfg['dos'])}

### Don't
{bullet_lines(cfg['donts'])}

## Screen Generation Heuristics
- **Default page structure:** {sg['page_structure']}
- **Default density:** {sg['density']}
- **Default navigation model:** {sg['navigation_model']}
- **Preferred form composition:** {sg['form_composition']}
- **Preferred feedback pattern:** {sg['feedback_pattern']}
- **Preferred data-display pattern:** {sg['data_display_pattern']}
- **Prompt bias:** {sg['prompt_bias']}
- **Component naming consistency:** {values['Component naming consistency']}
- **Layout rule explicitness:** {values['Layout rule explicitness']}
- **Theme describability:** {values['Theme describability']}
- **Prompt-to-UI suitability:** {values['Prompt-to-UI suitability']}

## Official Sources
{bullet_lines(cfg['sources'])}
"""


def main():
    systems, data = read_csv()
    OUT_DIR.mkdir(exist_ok=True)
    for system in systems:
        cfg = SYSTEM_CONFIG[system]
        target_dir = OUT_DIR / cfg["slug"]
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "DESIGN.md").write_text(render(system, data[system]), encoding="utf-8")


if __name__ == "__main__":
    main()
