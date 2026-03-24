from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tests" / "sample1"


SYSTEMS = [
    {
        "slug": "ant-design",
        "title": "Ant Design",
        "layout": "sidebar",
        "font": "ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "page_bg": "#f5f5f5",
        "shell_bg": "#001529",
        "surface": "#ffffff",
        "surface_alt": "#fafafa",
        "text": "#1f1f1f",
        "muted": "#595959",
        "primary": "#1677ff",
        "primary_soft": "#e6f4ff",
        "secondary_shell": "#0b2647",
        "border": "#d9d9d9",
        "success": "#52c41a",
        "warning": "#faad14",
        "danger": "#ff4d4f",
        "radius": "8px",
        "button_radius": "8px",
        "shadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
        "header_tag": "Enterprise workspace",
        "nav_label": "Data Admin",
    },
    {
        "slug": "atlassian-design-system",
        "title": "Atlassian Design System",
        "layout": "atlassian",
        "font": "'Atlassian Sans', ui-sans-serif, system-ui, sans-serif",
        "page_bg": "#f7f8f9",
        "shell_bg": "#1d2125",
        "surface": "#ffffff",
        "surface_alt": "#f1f2f4",
        "text": "#172b4d",
        "muted": "#44546f",
        "primary": "#0c66e4",
        "primary_soft": "#e9f2ff",
        "secondary_shell": "#ffffff",
        "border": "#dcdfe4",
        "success": "#1f845a",
        "warning": "#b65c02",
        "danger": "#c9372c",
        "radius": "10px",
        "button_radius": "8px",
        "shadow": "0 1px 1px rgba(9, 30, 66, 0.06)",
        "header_tag": "Workspace",
        "nav_label": "Operations",
    },
    {
        "slug": "carbon-design-system",
        "title": "Carbon Design System",
        "layout": "carbon",
        "font": "'IBM Plex Sans', ui-sans-serif, system-ui, sans-serif",
        "page_bg": "#f4f4f4",
        "shell_bg": "#161616",
        "surface": "#ffffff",
        "surface_alt": "#f4f4f4",
        "text": "#161616",
        "muted": "#525252",
        "primary": "#0f62fe",
        "primary_soft": "#edf5ff",
        "secondary_shell": "#262626",
        "border": "#c6c6c6",
        "success": "#198038",
        "warning": "#f1c21b",
        "danger": "#da1e28",
        "radius": "0px",
        "button_radius": "0px",
        "shadow": "none",
        "header_tag": "UI shell",
        "nav_label": "Master data",
    },
    {
        "slug": "digital-agency-design-system",
        "title": "Digital Agency Design System",
        "layout": "public-service",
        "font": "'Noto Sans JP', 'Hiragino Sans', 'Yu Gothic', sans-serif",
        "page_bg": "#ffffff",
        "shell_bg": "#ffffff",
        "surface": "#ffffff",
        "surface_alt": "#f7f7f7",
        "text": "#1a1a1a",
        "muted": "#4d4d4d",
        "primary": "#005ac2",
        "primary_soft": "#e8f0fb",
        "secondary_shell": "#f5f6f8",
        "border": "#d0d0d0",
        "success": "#2f7d32",
        "warning": "#b7791f",
        "danger": "#c62828",
        "radius": "6px",
        "button_radius": "6px",
        "shadow": "none",
        "header_tag": "行政サービス",
        "nav_label": "手続きメニュー",
    },
    {
        "slug": "fluent-2",
        "title": "Fluent 2",
        "layout": "workspace-light",
        "font": "'Segoe UI', ui-sans-serif, system-ui, sans-serif",
        "page_bg": "#f3f2f1",
        "shell_bg": "#ffffff",
        "surface": "#ffffff",
        "surface_alt": "#faf9f8",
        "text": "#242424",
        "muted": "#616161",
        "primary": "#0f6cbd",
        "primary_soft": "#e8f3fc",
        "secondary_shell": "#f8f8f8",
        "border": "#e1dfdd",
        "success": "#107c10",
        "warning": "#986f0b",
        "danger": "#d13438",
        "radius": "8px",
        "button_radius": "6px",
        "shadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
        "header_tag": "Productivity",
        "nav_label": "Master data",
    },
    {
        "slug": "human-interface-guidelines",
        "title": "Human Interface Guidelines",
        "layout": "apple",
        "font": "'SF Pro Display', 'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif",
        "page_bg": "#f5f5f7",
        "shell_bg": "rgba(255,255,255,0.82)",
        "surface": "rgba(255,255,255,0.88)",
        "surface_alt": "#f2f2f7",
        "text": "#1c1c1e",
        "muted": "#636366",
        "primary": "#007aff",
        "primary_soft": "#eaf3ff",
        "secondary_shell": "rgba(255,255,255,0.7)",
        "border": "rgba(60,60,67,0.18)",
        "success": "#34c759",
        "warning": "#ff9f0a",
        "danger": "#ff3b30",
        "radius": "18px",
        "button_radius": "12px",
        "shadow": "0 10px 30px rgba(15, 23, 42, 0.08)",
        "header_tag": "Sidebar + toolbar",
        "nav_label": "Master data",
    },
    {
        "slug": "lightning-design-system",
        "title": "Lightning Design System",
        "layout": "lightning",
        "font": "'Salesforce Sans', 'Arial', sans-serif",
        "page_bg": "#f3f3f3",
        "shell_bg": "#032d60",
        "surface": "#ffffff",
        "surface_alt": "#f8f9fb",
        "text": "#181818",
        "muted": "#444444",
        "primary": "#0176d3",
        "primary_soft": "#eef4ff",
        "secondary_shell": "#16325c",
        "border": "#dddbda",
        "success": "#2e844a",
        "warning": "#8a6d3b",
        "danger": "#ba0517",
        "radius": "6px",
        "button_radius": "4px",
        "shadow": "0 1px 2px rgba(0, 0, 0, 0.08)",
        "header_tag": "Record page",
        "nav_label": "Sales ops",
    },
    {
        "slug": "material-design",
        "title": "Material Design",
        "layout": "material",
        "font": "Roboto, ui-sans-serif, system-ui, sans-serif",
        "page_bg": "#f6f0ff",
        "shell_bg": "#fffbfe",
        "surface": "#fffbfe",
        "surface_alt": "#f3edf7",
        "text": "#1c1b1f",
        "muted": "#49454f",
        "primary": "#6750a4",
        "primary_soft": "#ede7f6",
        "secondary_shell": "#e8def8",
        "border": "#cac4d0",
        "success": "#386a20",
        "warning": "#7a5d00",
        "danger": "#b3261e",
        "radius": "16px",
        "button_radius": "20px",
        "shadow": "0 1px 3px rgba(0, 0, 0, 0.12)",
        "header_tag": "Adaptive shell",
        "nav_label": "Destinations",
    },
    {
        "slug": "primer-product-ui",
        "title": "Primer Product UI",
        "layout": "primer",
        "font": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif",
        "page_bg": "#f6f8fa",
        "shell_bg": "#ffffff",
        "surface": "#ffffff",
        "surface_alt": "#f6f8fa",
        "text": "#1f2328",
        "muted": "#57606a",
        "primary": "#0969da",
        "primary_soft": "#ddf4ff",
        "secondary_shell": "#f6f8fa",
        "border": "#d0d7de",
        "success": "#1a7f37",
        "warning": "#9a6700",
        "danger": "#cf222e",
        "radius": "8px",
        "button_radius": "6px",
        "shadow": "0 1px 0 rgba(27,31,36,0.04)",
        "header_tag": "PageLayout",
        "nav_label": "Repository-style nav",
    },
    {
        "slug": "smarthr-design-system",
        "title": "SmartHR Design System",
        "layout": "business-light",
        "font": "'Hiragino Sans', 'Yu Gothic', 'Noto Sans JP', sans-serif",
        "page_bg": "#f8fbfd",
        "shell_bg": "#ffffff",
        "surface": "#ffffff",
        "surface_alt": "#f4f8fb",
        "text": "#23221f",
        "muted": "#5c5b57",
        "primary": "#0077c7",
        "primary_soft": "#e8f2fb",
        "secondary_shell": "#eef7fd",
        "border": "#d7e6e8",
        "success": "#008060",
        "warning": "#a66300",
        "danger": "#d63638",
        "radius": "10px",
        "button_radius": "8px",
        "shadow": "0 1px 2px rgba(0, 0, 0, 0.04)",
        "header_tag": "業務ダッシュボード",
        "nav_label": "運用メニュー",
    },
    {
        "slug": "sparkle-design",
        "title": "Sparkle Design",
        "layout": "sparkle",
        "font": "'Avenir Next', 'Helvetica Neue', Helvetica, Arial, sans-serif",
        "page_bg": "#fbfaf7",
        "shell_bg": "#ffffff",
        "surface": "#ffffff",
        "surface_alt": "#f4efe5",
        "text": "#111111",
        "muted": "#58544d",
        "primary": "#ff6b3d",
        "primary_soft": "#ffe7de",
        "secondary_shell": "#111111",
        "border": "#ded6c7",
        "success": "#29643a",
        "warning": "#8d5f18",
        "danger": "#b42318",
        "radius": "18px",
        "button_radius": "999px",
        "shadow": "0 14px 36px rgba(17, 17, 17, 0.08)",
        "header_tag": "Branded product shell",
        "nav_label": "Sparkle workspace",
    },
    {
        "slug": "spectrum",
        "title": "Spectrum",
        "layout": "spectrum",
        "font": "'Adobe Clean', ui-sans-serif, system-ui, sans-serif",
        "page_bg": "#f5f5f5",
        "shell_bg": "#ffffff",
        "surface": "#ffffff",
        "surface_alt": "#f8f8f8",
        "text": "#2c2c2c",
        "muted": "#5c5c5c",
        "primary": "#1473e6",
        "primary_soft": "#e8f1fb",
        "secondary_shell": "#2c2c2c",
        "border": "#d5d5d5",
        "success": "#008f5d",
        "warning": "#b25f00",
        "danger": "#d31510",
        "radius": "12px",
        "button_radius": "18px",
        "shadow": "0 6px 20px rgba(44, 44, 44, 0.08)",
        "header_tag": "Creative workflow",
        "nav_label": "Adobe app shell",
    },
]

CARDS = [
    ("管理中マスタ", "128", "+6 this week"),
    ("本日の更新", "42", "14 pending approval"),
    ("承認待ち", "7", "3 over SLA"),
    ("不整合 / エラー", "5", "2 critical"),
]

ALERTS = [
    ("商品マスタ", "参照不整合", "Critical", "10:24"),
    ("取引先マスタ", "必須項目欠損", "Warning", "09:18"),
    ("拠点マスタ", "公開期限切れ", "Notice", "08:52"),
]

APPROVALS = [
    ("山田 花子", "商品分類マスタ", "更新申請", "09:42", "SLA 2h"),
    ("佐藤 健", "店舗マスタ", "削除申請", "08:30", "SLA 5h"),
    ("鈴木 一郎", "権限グループ", "新規申請", "昨日 18:12", "SLA over"),
]

ROWS = [
    ("商品マスタ", "MST-001", "営業本部", "2026-03-25 09:55", "山田", "正常", "3,240", "0"),
    ("取引先マスタ", "MST-004", "購買部", "2026-03-25 09:10", "佐藤", "注意", "1,148", "2"),
    ("店舗マスタ", "MST-021", "店舗運営部", "2026-03-25 08:55", "高橋", "承認待ち", "244", "0"),
    ("権限グループ", "MST-031", "情報システム部", "2026-03-24 18:12", "鈴木", "エラー", "58", "3"),
]

TIMELINE = [
    ("09:55", "商品マスタが更新されました", "Update"),
    ("09:42", "商品分類マスタの承認依頼があります", "Approval"),
    ("09:18", "取引先マスタで必須項目欠損を検知", "Alert"),
    ("08:30", "店舗マスタの削除申請が提出されました", "Approval"),
]

NAV = ["ダッシュボード", "マスタ一覧", "承認待ち", "更新履歴", "監査ログ", "ユーザー/権限", "設定"]


def status_color(system, label):
    return {
        "正常": system["success"],
        "注意": system["warning"],
        "承認待ち": system["primary"],
        "エラー": system["danger"],
        "Critical": system["danger"],
        "Warning": system["warning"],
        "Notice": system["primary"],
        "Update": system["primary"],
        "Approval": system["warning"],
        "Alert": system["danger"],
    }[label]


def badge(system, label):
    color = status_color(system, label)
    if system["slug"] == "atlassian-design-system":
        tone = {"Critical": "Removed", "Warning": "In progress", "Approval": "Moved", "Update": "New", "Notice": "Default"}.get(label, label)
        return f'<span class="inline-flex items-center rounded px-2 py-1 text-[11px] font-semibold uppercase tracking-[0.06em]" style="background:{system["primary_soft"]}; color:{color};">{tone}</span>'
    if system["slug"] == "carbon-design-system":
        return f'<span class="inline-flex items-center px-2 py-1 text-[11px] font-semibold uppercase tracking-[0.06em]" style="background:{system["surface_alt"]}; color:{color}; border-left:3px solid {color};">{label}</span>'
    if system["slug"] == "material-design":
        return f'<span class="inline-flex items-center rounded-full px-2.5 py-1 text-[11px] font-medium" style="background:{system["primary_soft"]}; color:{color};">{label}</span>'
    if system["slug"] == "primer-product-ui":
        return f'<span class="inline-flex items-center rounded-md border px-2 py-0.5 text-[11px] font-medium" style="border-color:{system["border"]}; color:{color}; background:{system["surface"]};">{label}</span>'
    if system["slug"] == "digital-agency-design-system":
        return f'<span class="inline-flex items-center border px-2 py-1 text-[11px] font-semibold" style="background:{system["surface"]}; color:{color}; border-color:{color};">{label}</span>'
    if system["slug"] == "fluent-2":
        phrase = {"Update": "Updated", "Approval": "Needs review", "Critical": "Critical", "Warning": "Warning", "Notice": "Info"}.get(label, label)
        return f'<span class="inline-flex items-center rounded-md px-2.5 py-1 text-[11px] font-semibold" style="background:{system["primary_soft"]}; color:{color};">{phrase}</span>'
    if system["slug"] == "lightning-design-system":
        return f'<span class="inline-flex items-center rounded px-2 py-1 text-[11px] font-semibold" style="background:{system["primary_soft"]}; color:{color}; border:1px solid {system["border"]};">{label}</span>'
    return f'<span class="inline-flex items-center rounded-full border px-2.5 py-1 text-[11px] font-semibold" style="background:{system["surface"]}; color:{color}; border-color:{color};">{label}</span>'


def control_button(system, label, kind="secondary"):
    if system["slug"] == "carbon-design-system":
        if kind == "primary":
            return f'<button class="px-4 py-2 text-sm font-semibold" style="background:{system["primary"]}; color:white; border-radius:0;">{label} →</button>'
        if kind == "ghost":
            return f'<button class="px-3 py-2 text-sm font-medium" style="background:transparent; color:{system["primary"]}; border-radius:0;">{label}</button>'
        return f'<button class="px-3 py-2 text-sm font-medium" style="background:transparent; color:{system["text"]}; border:1px solid {system["border"]}; border-radius:0;">{label}</button>'
    if system["slug"] == "fluent-2":
        if kind == "primary":
            return f'<button class="px-4 py-2 text-sm font-semibold" style="background:{system["primary"]}; color:white; border-radius:{system["button_radius"]};">{label}</button>'
        if kind == "ghost":
            return f'<button class="px-3 py-2 text-sm font-medium" style="background:transparent; color:{system["primary"]}; border-radius:{system["button_radius"]};">{label}</button>'
        return f'<button class="px-3 py-2 text-sm font-medium" style="background:{system["surface_alt"]}; color:{system["text"]}; border:1px solid {system["border"]}; border-radius:{system["button_radius"]};">{label}</button>'
    if system["slug"] == "digital-agency-design-system" and kind == "ghost":
        return f'<button class="px-3 py-2 text-sm font-medium underline underline-offset-4" style="background:transparent; color:{system["primary"]}; border-radius:{system["button_radius"]};">{label}</button>'
    if kind == "primary":
        return f'<button class="px-4 py-2 text-sm font-semibold" style="background:{system["primary"]}; color:white; border-radius:{system["button_radius"]};">{label}</button>'
    if kind == "ghost":
        return f'<button class="px-3 py-2 text-sm font-medium" style="background:transparent; color:{system["primary"]}; border-radius:{system["button_radius"]};">{label}</button>'
    return f'<button class="px-3 py-2 text-sm font-medium" style="background:{system["surface"]}; color:{system["text"]}; border:1px solid {system["border"]}; border-radius:{system["button_radius"]};">{label}</button>'


def summary_cards(system):
    blocks = []
    for label, value, meta in CARDS:
        tone = "Update"
        if "承認" in label:
            tone = "Approval"
        if "エラー" in label:
            tone = "Critical"
        bg = system["surface_alt"] if system["slug"] in {"material-design", "sparkle-design", "fluent-2"} else system["surface"]
        shadow = "none" if system["slug"] in {"primer-product-ui", "digital-agency-design-system"} else system["shadow"]
        blocks.append(
            f"""
            <section class="border p-4" style="background:{bg}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{shadow};">
              <div class="flex items-start justify-between gap-3">
                <div>
                  <p class="text-sm font-semibold" style="color:{system['muted']};">{label}</p>
                  <p class="mt-3 text-3xl font-semibold tracking-tight" style="color:{system['text']};">{value}</p>
                </div>
                {badge(system, tone)}
              </div>
              <p class="mt-3 text-sm" style="color:{system['muted']};">{meta}</p>
            </section>
            """
        )
    return "\n".join(blocks)


def alert_list(system):
    items = []
    for master, message, severity, time in ALERTS:
        items.append(
            f"""
            <li class="border p-4" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:{system['radius']};">
              <div class="flex items-start justify-between gap-3">
                <div>
                  <p class="text-sm font-semibold" style="color:{system['text']};">{master}</p>
                  <p class="mt-1 text-sm" style="color:{system['muted']};">{message}</p>
                </div>
                {badge(system, severity)}
              </div>
              <div class="mt-3 flex items-center justify-between text-xs" style="color:{system['muted']};">
                <span>{time}</span>
                <div class="flex gap-2">
                  {control_button(system, "詳細", "ghost")}
                  {control_button(system, "対象へ移動")}
                </div>
              </div>
            </li>
            """
        )
    return "\n".join(items)


def approval_list(system):
    items = []
    for user, master, kind, time, sla in APPROVALS:
        primary_kind = "primary"
        primary_label = "承認"
        if system["slug"] in {"fluent-2", "carbon-design-system"}:
            primary_kind = "secondary"
            primary_label = "レビュー"
        if system["slug"] == "primer-product-ui":
            primary_kind = "secondary"
            primary_label = "Open"
        items.append(
            f"""
            <li class="border p-4" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:{system['radius']};">
              <div class="flex items-start justify-between gap-3">
                <div>
                  <p class="text-sm font-semibold" style="color:{system['text']};">{master}</p>
                  <p class="mt-1 text-sm" style="color:{system['muted']};">{user} / {kind}</p>
                </div>
                {badge(system, 'Warning' if 'over' in sla else 'Approval')}
              </div>
              <div class="mt-3 flex items-center justify-between text-xs" style="color:{system['muted']};">
                <span>{time} / {sla}</span>
                <div class="flex gap-2">
                  {control_button(system, "詳細")}
                  {control_button(system, primary_label, primary_kind)}
                </div>
              </div>
            </li>
            """
        )
    return "\n".join(items)


def table_region(system):
    if system["slug"] == "carbon-design-system":
        toolbar = f"""
        <div class="flex flex-wrap items-center justify-between gap-3 border-b px-5 py-3" style="border-color:{system['border']}; background:{system['surface_alt']};">
          <div class="flex items-center gap-3">
            <span class="text-sm font-semibold" style="color:{system['text']};">Data table</span>
            <span class="text-xs" style="color:{system['muted']};">4 selected-ready rows</span>
          </div>
          <div class="flex gap-2">
            {control_button(system, 'Filter')}
            {control_button(system, 'Batch action')}
          </div>
        </div>
        """
    else:
        toolbar = f"""
        <div class="flex flex-wrap items-center justify-between gap-3 border-b px-5 py-4" style="border-color:{system['border']}; background:{system['surface_alt']};">
          <div>
            <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Master registry</p>
            <h3 class="mt-2 text-xl font-semibold" style="color:{system['text']};">マスタ一覧</h3>
          </div>
          <div class="flex flex-wrap gap-2">
            {control_button(system, '状態: すべて')}
            {control_button(system, '部署: 全体')}
            {control_button(system, '更新順', 'ghost')}
          </div>
        </div>
        """
    rows = []
    for name, code, dept, updated, editor, status, count, errors in ROWS:
        row_actions = control_button(system, "詳細")
        if system["slug"] not in {"carbon-design-system", "fluent-2"}:
            row_actions += control_button(system, "編集", "ghost")
        rows.append(
            f"""
            <tr class="border-t" style="border-color:{system['border']};">
              <td class="px-4 py-3 font-semibold" style="color:{system['text']};">{name}</td>
              <td class="px-4 py-3">{code}</td>
              <td class="px-4 py-3">{dept}</td>
              <td class="px-4 py-3">{updated}</td>
              <td class="px-4 py-3">{editor}</td>
              <td class="px-4 py-3">{badge(system, status)}</td>
              <td class="px-4 py-3 text-right">{count}</td>
              <td class="px-4 py-3 text-right">{errors}</td>
              <td class="px-4 py-3"><div class="flex justify-end gap-2">{row_actions}</div></td>
            </tr>
            """
        )
    article_shadow = "none" if system["slug"] in {"primer-product-ui", "digital-agency-design-system"} else system["shadow"]
    return f"""
    <article class="border overflow-hidden" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{article_shadow};">
      {toolbar}
      <div class="overflow-x-auto">
        <table class="min-w-full text-sm" style="color:{system['muted']};">
          <thead style="background:{system['surface_alt']}; color:{system['muted']};">
            <tr>
              <th class="px-4 py-3 text-left font-semibold">マスタ名</th>
              <th class="px-4 py-3 text-left font-semibold">コード</th>
              <th class="px-4 py-3 text-left font-semibold">管理部署</th>
              <th class="px-4 py-3 text-left font-semibold">最終更新</th>
              <th class="px-4 py-3 text-left font-semibold">更新者</th>
              <th class="px-4 py-3 text-left font-semibold">ステータス</th>
              <th class="px-4 py-3 text-right font-semibold">件数</th>
              <th class="px-4 py-3 text-right font-semibold">エラー</th>
              <th class="px-4 py-3 text-right font-semibold">操作</th>
            </tr>
          </thead>
          <tbody>
            {''.join(rows)}
          </tbody>
        </table>
      </div>
    </article>
    """


def timeline_region(system):
    items = []
    for time, message, kind in TIMELINE:
        items.append(
            f"""
            <li class="flex items-start gap-3">
              <span class="mt-1 h-2.5 w-2.5 rounded-full" style="background:{status_color(system, kind)};"></span>
              <div>
                <p class="text-sm font-medium" style="color:{system['text']};">{message}</p>
                <p class="mt-1 text-xs" style="color:{system['muted']};">{time} / {kind}</p>
              </div>
            </li>
            """
        )
    article_shadow = "none" if system["slug"] in {"primer-product-ui", "digital-agency-design-system"} else system["shadow"]
    return f"""
    <article class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{article_shadow};">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Activity</p>
          <h3 class="mt-2 text-xl font-semibold" style="color:{system['text']};">更新履歴 / 通知</h3>
        </div>
        {badge(system, 'Update')}
      </div>
      <div class="mt-4 flex flex-wrap gap-2">
        {control_button(system, '全体', 'ghost')}
        {control_button(system, '自分関連')}
        {control_button(system, 'エラーのみ')}
      </div>
      <ul class="mt-5 space-y-4">{''.join(items)}</ul>
    </article>
    """


def side_nav(system, active_index=0):
    icon_map = ["◉", "▣", "◌", "⋯", "⌘", "⚙", "≡"]
    items = []
    for idx, label in enumerate(NAV):
        bg = system["primary_soft"] if idx == active_index else "transparent"
        color = system["primary"] if idx == active_index else system["muted"]
        text = f"{icon_map[idx]} {label}" if system["slug"] in {"fluent-2"} else label
        trailing = f"{idx + 1:02d}"
        if system["slug"] == "atlassian-design-system":
            text = ["Overview", "Masters", "Approvals", "Activity", "Audit", "People", "Settings"][idx]
            trailing = ""
        if system["slug"] == "human-interface-guidelines":
            text = ["Overview", "Masters", "Approvals", "Recents", "Logs", "People", "Settings"][idx]
            trailing = ""
        items.append(
            f'<a href="#" class="flex items-center justify-between px-3 py-2 text-sm font-medium" style="background:{bg}; color:{color}; border-radius:{system["button_radius"]};"><span>{text}</span><span class="text-[11px] opacity-70">{trailing}</span></a>'
        )
    return "\n".join(items)


def header_block(system):
    eyebrow = system["header_tag"]
    body = "更新・承認・異常検知を1画面で確認できる運用ダッシュボード"
    create_label = "新規登録"
    notice_label = "通知 3"
    if system["slug"] == "smarthr-design-system":
        eyebrow = "マスタ管理システム"
        body = "更新・承認・異常検知を、落ち着いた業務UIで確認する画面"
    if system["slug"] == "fluent-2":
        body = "作業導線を優先した、落ち着いた生産性UIのダッシュボード"
        create_label = "新規作成"
        notice_label = "アクティビティ"
    if system["slug"] == "primer-product-ui":
        body = "Focused product page for operational review, approval, and audit activity."
        create_label = "New master"
        notice_label = "Notifications"
    if system["slug"] == "digital-agency-design-system":
        body = "手続きの状況、承認、更新を分かりやすく確認するための画面"
        create_label = "登録"
        notice_label = "お知らせ"
    if system["slug"] == "human-interface-guidelines":
        body = "Content-first operational overview using sidebar, toolbar, and grouped content."
        create_label = "Add"
        notice_label = "Updates"
    search = f'<label class="flex min-w-[220px] items-center gap-3 border px-3 py-2" style="background:{system["surface"]}; border-color:{system["border"]}; border-radius:{system["button_radius"]}; color:{system["muted"]};"><span class="text-xs">Search</span><input class="w-full bg-transparent text-sm outline-none" value="商品 / コード / 管理部署" /></label>'
    return f"""
    <div class="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
      <div>
        <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">{eyebrow}</p>
        <h1 class="mt-2 text-3xl font-semibold" style="color:{system['text']};">マスタ管理ダッシュボード</h1>
        <p class="mt-2 text-sm" style="color:{system['muted']};">{body}</p>
      </div>
      <div class="flex flex-wrap items-center gap-2">
        {search}
        {control_button(system, create_label, 'primary')}
        {control_button(system, notice_label)}
      </div>
    </div>
    """


def content_grid(system):
    cards = summary_cards(system)
    alerts = alert_list(system)
    approvals = approval_list(system)
    table = table_region(system)
    activity = timeline_region(system)
    section_shadow = "none" if system["slug"] in {"primer-product-ui", "digital-agency-design-system"} else system["shadow"]
    return f"""
    <section class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">{cards}</section>
    <section class="mt-6 grid gap-4 xl:grid-cols-[1.2fr_1fr]">
      <article class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{section_shadow};">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Alerts</p>
            <h3 class="mt-2 text-xl font-semibold" style="color:{system['text']};">要対応アラート</h3>
          </div>
          {badge(system, 'Critical')}
        </div>
        <ul class="mt-4 space-y-3">{alerts}</ul>
      </article>
      <article class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{section_shadow};">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Approvals</p>
            <h3 class="mt-2 text-xl font-semibold" style="color:{system['text']};">承認待ち</h3>
          </div>
          {badge(system, 'Approval')}
        </div>
        <ul class="mt-4 space-y-3">{approvals}</ul>
      </article>
    </section>
    <section class="mt-6 grid gap-4 2xl:grid-cols-[1.45fr_0.75fr]">
      {table}
      {activity}
    </section>
    """


def layout_sidebar(system):
    return f"""
    <div class="min-h-screen lg:grid lg:grid-cols-[248px_minmax(0,1fr)]">
      <aside class="border-r px-4 py-5" style="background:{system['shell_bg']}; border-color:{system['border']};">
        <div class="rounded border p-4" style="background:{system['secondary_shell']}; border-color:rgba(255,255,255,0.12);">
          <p class="text-xs uppercase tracking-[0.18em]" style="color:#cbd5e1;">{system['nav_label']}</p>
          <h2 class="mt-2 text-lg font-semibold text-white">{system['title']}</h2>
        </div>
        <nav class="mt-6 space-y-1">{side_nav(system)}</nav>
      </aside>
      <main class="px-4 py-4 lg:px-8 lg:py-6">
        <header class="border px-5 py-4" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{system['shadow']};">{header_block(system)}</header>
        <div class="mt-6">{content_grid(system)}</div>
      </main>
    </div>
    """


def layout_atlassian(system):
    banner = f'<div class="mb-4 rounded px-4 py-3 text-sm" style="background:{system["primary_soft"]}; color:{system["text"]}; border:1px solid {system["border"]};">Workflow notice: 3 records are waiting on approval and 1 record needs an owner update.</div>'
    return f"""
    <div class="min-h-screen">
      <header class="border-b px-5 py-3" style="background:{system['shell_bg']}; border-color:#3d4552; color:white;">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="rounded px-2 py-1 text-xs font-semibold" style="background:#0c66e4;">OPS</span>
            <span class="text-sm font-semibold">Master data workspace</span>
          </div>
          <div class="text-sm text-slate-300">Projects / Governance / Settings</div>
        </div>
      </header>
      <div class="lg:grid lg:grid-cols-[260px_minmax(0,1fr)]">
        <aside class="border-r px-4 py-5" style="background:{system['secondary_shell']}; border-color:{system['border']};">
          <div class="text-xs font-semibold uppercase tracking-[0.16em]" style="color:{system['muted']};">Workspace navigation</div>
          <nav class="mt-4 space-y-1">{side_nav(system)}</nav>
        </aside>
        <main class="px-4 py-5 lg:px-8">
          {banner}
          <header class="px-1 py-1">{header_block(system)}</header>
          <div class="mt-6">{content_grid(system)}</div>
        </main>
      </div>
    </div>
    """


def layout_carbon(system):
    return f"""
    <div class="min-h-screen">
      <header class="border-b px-5 py-3" style="background:{system['shell_bg']}; border-color:#393939; color:white;">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4">
            <span class="text-sm font-semibold">IBM Data Admin</span>
            <span class="text-sm text-slate-300">Products</span>
            <span class="text-sm text-slate-300">Governance</span>
            <span class="text-sm text-slate-300">Audit</span>
          </div>
          <div class="text-sm text-slate-300">Profile</div>
        </div>
      </header>
      <div class="lg:grid lg:grid-cols-[220px_minmax(0,1fr)]">
        <aside class="border-r px-4 py-5" style="background:{system['secondary_shell']}; border-color:#393939;">
          <div class="text-xs uppercase tracking-[0.18em] text-slate-400">Productive nav</div>
          <nav class="mt-4 space-y-1">{side_nav(system)}</nav>
        </aside>
        <main class="px-4 py-4 lg:px-8 lg:py-6">
          <header class="pb-6">{header_block(system)}</header>
          {content_grid(system)}
        </main>
      </div>
    </div>
    """


def layout_public_service(system):
    top_links = "ホーム / データ整備 / マスタ管理"
    return f"""
    <div class="min-h-screen">
      <header class="border-b" style="background:{system['shell_bg']}; border-color:{system['border']};">
        <div class="mx-auto max-w-7xl px-4 py-3 lg:px-8">
          <div class="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
            <div>
              <p class="text-xs" style="color:{system['muted']};">{top_links}</p>
              <h1 class="mt-2 text-2xl font-semibold" style="color:{system['text']};">{system['header_tag']}</h1>
            </div>
            <div class="flex gap-2">
              {control_button(system, '検索')}
              {control_button(system, 'メニュー')}
            </div>
          </div>
        </div>
      </header>
      <main class="mx-auto max-w-7xl px-4 py-6 lg:px-8">
        <section class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']};">
          {header_block(system)}
        </section>
        <div class="mt-6">{content_grid(system)}</div>
      </main>
    </div>
    """


def layout_workspace_light(system):
    return f"""
    <div class="min-h-screen lg:grid lg:grid-cols-[220px_minmax(0,1fr)]">
      <aside class="border-r px-4 py-5" style="background:{system['secondary_shell']}; border-color:{system['border']};">
        <div class="text-sm font-semibold" style="color:{system['text']};">{system['nav_label']}</div>
        <nav class="mt-4 space-y-1">{side_nav(system)}</nav>
      </aside>
      <main class="px-4 py-4 lg:px-8 lg:py-6">
        <header class="border px-5 py-4" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']};">{header_block(system)}</header>
        <div class="mt-6">{content_grid(system)}</div>
      </main>
    </div>
    """


def layout_apple(system):
    return f"""
    <div class="min-h-screen p-4 lg:p-6">
      <div class="overflow-hidden lg:grid lg:grid-cols-[250px_minmax(0,1fr)]" style="border:1px solid {system['border']}; border-radius:{system['radius']}; box-shadow:{system['shadow']}; background:{system['surface']};">
        <aside class="border-r px-4 py-5" style="background:{system['secondary_shell']}; border-color:{system['border']};">
          <div class="text-sm font-semibold" style="color:{system['text']};">Sidebar</div>
          <nav class="mt-4 space-y-1">{side_nav(system)}</nav>
        </aside>
        <main class="px-4 py-4 lg:px-6">
          <div class="mb-5 flex items-center justify-between">
            <div>
              <p class="text-sm" style="color:{system['muted']};">{system['header_tag']}</p>
              <h1 class="mt-1 text-3xl font-semibold" style="color:{system['text']};">マスタ管理ダッシュボード</h1>
            </div>
            <div class="flex items-center gap-2">
              <label class="flex items-center gap-2 border px-3 py-2 text-sm" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:{system['button_radius']}; color:{system['muted']};"><span>Search</span><input class="bg-transparent outline-none" value="商品 / コード" /></label>
              {control_button(system, '新規登録', 'primary')}
            </div>
          </div>
          {content_grid(system)}
        </main>
      </div>
    </div>
    """


def layout_lightning(system):
    tabs = "".join(
        f'<a href="#" class="px-4 py-3 text-sm font-semibold" style="color:{system["primary"] if i == 0 else system["muted"]}; border-bottom:2px solid {system["primary"] if i == 0 else "transparent"};">{label}</a>'
        for i, label in enumerate(["概要", "関連リスト", "承認", "履歴"])
    )
    return f"""
    <div class="min-h-screen">
      <header class="px-5 py-3" style="background:{system['shell_bg']}; color:white;">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4">
            <span class="rounded px-2 py-1 text-xs font-semibold" style="background:#0176d3;">App Launcher</span>
            <span class="text-sm font-semibold">Sales Ops Console</span>
            <span class="text-sm text-slate-300">Accounts</span>
            <span class="text-sm text-slate-300">Masters</span>
          </div>
          <div class="text-sm text-slate-300">Utility Bar</div>
        </div>
      </header>
      <main class="px-4 py-4 lg:px-8 lg:py-6">
        <section class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{system['shadow']};">
          <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Master Data</p>
          <div class="mt-3 flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
            <div>
              <h1 class="text-3xl font-semibold" style="color:{system['text']};">マスタ管理ダッシュボード</h1>
              <p class="mt-2 text-sm" style="color:{system['muted']};">Record-page inspired dashboard with approvals, alerts, and related data lists.</p>
            </div>
            <div class="flex flex-wrap gap-2">
              {control_button(system, '編集')}
              {control_button(system, '承認', 'primary')}
            </div>
          </div>
          <div class="mt-4 grid gap-3 lg:grid-cols-3">
            <div class="border p-4" style="border-color:{system['border']}; border-radius:{system['radius']}; background:{system['surface_alt']};"><p class="text-xs" style="color:{system['muted']};">Owner</p><p class="mt-1 font-semibold">営業本部</p></div>
            <div class="border p-4" style="border-color:{system['border']}; border-radius:{system['radius']}; background:{system['surface_alt']};"><p class="text-xs" style="color:{system['muted']};">Stage</p><p class="mt-1 font-semibold">Operational</p></div>
            <div class="border p-4" style="border-color:{system['border']}; border-radius:{system['radius']}; background:{system['surface_alt']};"><p class="text-xs" style="color:{system['muted']};">Last sync</p><p class="mt-1 font-semibold">2026-03-25 09:55</p></div>
          </div>
        </section>
        <nav class="mt-4 flex flex-wrap gap-1 border-b" style="border-color:{system['border']};">{tabs}</nav>
        <div class="mt-6">{content_grid(system)}</div>
      </main>
    </div>
    """


def layout_material(system):
    rail = "".join(
        f'<a href="#" class="flex flex-col items-center gap-1 px-2 py-3 text-xs font-medium" style="color:{system["primary"] if i == 0 else system["muted"]};"><span class="rounded-full px-3 py-2" style="background:{system["primary_soft"] if i == 0 else "transparent"};">●</span><span>{label[:4]}</span></a>'
        for i, label in enumerate(NAV[:5])
    )
    cards = summary_cards(system)
    alerts = alert_list(system)
    approvals = approval_list(system)
    table = table_region(system)
    activity = timeline_region(system)
    return f"""
    <div class="min-h-screen">
      <div class="px-4 py-2 text-xs lg:px-8" style="background:{system['primary_soft']}; color:{system['primary']};">Adaptive shell preview: top app bar, navigation rail, and supporting pane shift with viewport width.</div>
      <header class="border-b px-4 py-3 lg:px-8" style="background:{system['surface']}; border-color:{system['border']};">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Adaptive shell</p>
            <h1 class="mt-1 text-2xl font-semibold" style="color:{system['text']};">マスタ管理ダッシュボード</h1>
          </div>
          <div class="flex gap-2">
            {control_button(system, 'フィルタ')}
            {control_button(system, '新規登録', 'primary')}
          </div>
        </div>
      </header>
      <div class="lg:grid lg:grid-cols-[96px_minmax(0,1fr)]">
      <aside class="border-r px-3 py-5" style="background:{system['secondary_shell']}; border-color:{system['border']};">
        <div class="space-y-2">{rail}</div>
      </aside>
      <main class="px-4 py-4 lg:px-8 lg:py-6">
        <section class="grid gap-4 lg:grid-cols-[minmax(0,1fr)_320px]">
          <div class="space-y-4">
            <header class="border px-5 py-4" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:12px; box-shadow:{system['shadow']};">
              <div class="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
                <div>
                  <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Role-driven containers</p>
                  <p class="mt-2 text-sm" style="color:{system['muted']};">Use tonal hierarchy, adaptive navigation, and shape variation across summary, approval, and data regions.</p>
                </div>
                <div class="flex gap-2">
                  {control_button(system, 'チップ: 全体', 'ghost')}
                  {control_button(system, '通知')}
                </div>
              </div>
            </header>
            <section class="grid gap-4 lg:grid-cols-[1.1fr_0.9fr]">
              <article class="border p-5" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:24px; box-shadow:{system['shadow']};">
                <div class="flex items-start justify-between gap-4">
                  <div>
                    <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Featured container</p>
                    <h3 class="mt-2 text-2xl font-semibold" style="color:{system['text']};">Operational status</h3>
                    <p class="mt-2 text-sm" style="color:{system['muted']};">Lead with a higher-emphasis tonal container before lower-priority metric tiles.</p>
                  </div>
                  {badge(system, 'Update')}
                </div>
                <div class="mt-5 grid gap-4 sm:grid-cols-3">
                  <div class="rounded-[20px] px-4 py-4" style="background:{system['surface']};">
                    <p class="text-sm" style="color:{system['muted']};">Pending approval</p>
                    <p class="mt-2 text-3xl font-semibold" style="color:{system['text']};">7</p>
                  </div>
                  <div class="rounded-[16px] px-4 py-4" style="background:{system['surface']};">
                    <p class="text-sm" style="color:{system['muted']};">Alerts</p>
                    <p class="mt-2 text-3xl font-semibold" style="color:{system['text']};">5</p>
                  </div>
                  <div class="rounded-[12px] px-4 py-4" style="background:{system['surface']};">
                    <p class="text-sm" style="color:{system['muted']};">Updated today</p>
                    <p class="mt-2 text-3xl font-semibold" style="color:{system['text']};">42</p>
                  </div>
                </div>
              </article>
              <section class="grid gap-4 sm:grid-cols-2">{cards}</section>
            </section>
          </div>
          <aside class="space-y-4">
            <section class="border p-4" style="background:{system['surface']}; border-color:{system['border']}; border-radius:28px 12px 28px 12px; box-shadow:{system['shadow']};">
              <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Supporting pane</p>
              <p class="mt-2 text-sm" style="color:{system['muted']};">Adaptive layout uses a rail for destinations and a separate supporting pane for low-priority operational context.</p>
            </section>
            <section class="border p-4" style="background:{system['surface']}; border-color:{system['border']}; border-radius:12px; box-shadow:{system['shadow']};">
              <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Pending work</p>
              <div class="mt-3 space-y-3">
                <div class="rounded-full px-3 py-2 text-sm" style="background:{system['primary_soft']}; color:{system['primary']};">承認待ち 7</div>
                <div class="rounded-full px-3 py-2 text-sm" style="background:{system['surface_alt']}; color:{system['warning']};">期限超過 3</div>
              </div>
            </section>
          </aside>
        </section>
        <section class="mt-6 grid gap-4 xl:grid-cols-[1.15fr_0.95fr]">
          <article class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:12px; box-shadow:{system['shadow']};">
            <div class="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
              <div>
                <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Approvals</p>
                <h3 class="mt-2 text-xl font-semibold" style="color:{system['text']};">承認待ち</h3>
              </div>
              {badge(system, 'Approval')}
            </div>
            <ul class="mt-4 space-y-3">{approvals}</ul>
          </article>
          <article class="border p-5" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:28px 12px 28px 12px; box-shadow:{system['shadow']};">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Alerts</p>
                <h3 class="mt-2 text-xl font-semibold" style="color:{system['text']};">要対応アラート</h3>
              </div>
              {badge(system, 'Critical')}
            </div>
            <ul class="mt-4 space-y-3">{alerts}</ul>
          </article>
        </section>
        <section class="mt-6 grid gap-4 2xl:grid-cols-[1.45fr_0.75fr]">
          {table}
          {activity}
        </section>
      </main>
      </div>
    </div>
    """


def layout_primer(system):
    tabs = "".join(
        f'<a href="#" class="px-3 py-3 text-sm font-medium" style="color:{system["primary"] if i == 0 else system["muted"]}; border-bottom:2px solid {system["primary"] if i == 0 else "transparent"};">{label}</a>'
        for i, label in enumerate(["Overview", "Approvals", "History", "Audit"])
    )
    cards = summary_cards(system)
    alerts = alert_list(system)
    approvals = approval_list(system)
    table = table_region(system)
    activity = timeline_region(system)
    return f"""
    <div class="min-h-screen px-4 py-5 lg:px-8">
      <header class="border-b pb-4" style="border-color:{system['border']};">
        <div class="mb-3 text-sm" style="color:{system['muted']};">Settings / Data governance / Masters</div>
        <div class="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
          <div>
            <p class="text-sm" style="color:{system['muted']};">{system['header_tag']}</p>
            <h1 class="mt-1 text-3xl font-semibold" style="color:{system['text']};">Master Data Dashboard</h1>
          </div>
          <div class="flex gap-2">
            {control_button(system, 'New rule')}
            {control_button(system, 'New master', 'primary')}
          </div>
        </div>
        <nav class="mt-4 flex flex-wrap gap-1">{tabs}</nav>
      </header>
      <div class="mt-6 grid gap-6 xl:grid-cols-[220px_minmax(0,1fr)_320px]">
        <aside>
          <nav class="border rounded-md p-2" style="background:{system['surface']}; border-color:{system['border']};">
            {side_nav(system)}
          </nav>
        </aside>
        <div class="space-y-6">
          <section class="grid gap-3 md:grid-cols-2">
            <article class="border rounded-md px-4 py-3" style="background:{system['surface']}; border-color:{system['border']};">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-sm font-semibold" style="color:{system['text']};">Overview</p>
                  <p class="mt-1 text-sm" style="color:{system['muted']};">Low-noise summary blocks with direct counts and restrained framing.</p>
                </div>
                {badge(system, 'Update')}
              </div>
            </article>
            <article class="border rounded-md px-4 py-3" style="background:{system['surface_alt']}; border-color:{system['border']};">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-sm font-semibold" style="color:{system['text']};">Checks</p>
                  <p class="mt-1 text-sm" style="color:{system['muted']};">Alerts, approvals, and metadata stay near the records they affect.</p>
                </div>
                <span class="text-xs" style="color:{system['muted']};">3 open</span>
              </div>
            </article>
          </section>
          <section class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">{cards}</section>
          <section class="grid gap-4 xl:grid-cols-[1.2fr_1fr]">
            {table}
            <section class="space-y-4">
              {activity}
              <article class="border p-4" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']};">
                <p class="text-sm font-semibold" style="color:{system['text']};">Review queue</p>
                <ul class="mt-3 space-y-3">{approvals}</ul>
              </article>
            </section>
          </section>
        </div>
        <aside class="space-y-4">
          <section class="border p-4" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:{system['radius']};">
            <p class="text-sm font-semibold" style="color:{system['text']};">Repository-style context</p>
            <p class="mt-2 text-sm" style="color:{system['muted']};">Focused side pane for metadata, checks, and related context.</p>
          </section>
          <section class="border p-4" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']};">
            <p class="text-sm font-semibold" style="color:{system['text']};">Notes</p>
            <p class="mt-2 text-sm" style="color:{system['muted']};">Focused PageLayout with restrained panels, muted chrome, and product-oriented hierarchy.</p>
          </section>
          <article class="border p-4" style="background:{system['surface_alt']}; border-color:{system['border']}; border-radius:{system['radius']};">
            <p class="text-sm font-semibold" style="color:{system['text']};">Alert summary</p>
            <ul class="mt-3 space-y-3">{alerts}</ul>
          </article>
        </aside>
      </div>
    </div>
    """


def layout_business_light(system):
    return f"""
    <div class="min-h-screen lg:grid lg:grid-cols-[220px_minmax(0,1fr)]">
      <aside class="border-r px-4 py-5" style="background:{system['secondary_shell']}; border-color:{system['border']};">
        <p class="text-sm font-semibold" style="color:{system['text']};">{system['nav_label']}</p>
        <nav class="mt-4 space-y-1">{side_nav(system)}</nav>
      </aside>
      <main class="px-4 py-4 lg:px-8 lg:py-6">
        <header class="border px-5 py-4" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']};">{header_block(system)}</header>
        <div class="mt-6">{content_grid(system)}</div>
      </main>
    </div>
    """


def layout_sparkle(system):
    return f"""
    <div class="min-h-screen px-4 py-4 lg:px-8 lg:py-6" style="background:radial-gradient(circle at top left, {system['primary_soft']}, {system['page_bg']} 46%);">
      <header class="border p-6" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{system['shadow']};">
        <div class="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
          <div>
            <p class="text-xs uppercase tracking-[0.18em]" style="color:{system['muted']};">{system['header_tag']}</p>
            <h1 class="mt-3 text-4xl font-semibold" style="color:{system['text']};">マスタ管理ダッシュボード</h1>
            <p class="mt-3 max-w-2xl text-sm" style="color:{system['muted']};">Reusable operations UI with stronger product personality, controlled accent color, and deliberate section composition.</p>
          </div>
          <div class="flex flex-wrap gap-2">
            {control_button(system, 'Preview')}
            {control_button(system, 'Publish', 'primary')}
          </div>
        </div>
      </header>
      <div class="mt-6 grid gap-6 xl:grid-cols-[260px_minmax(0,1fr)]">
        <aside class="border p-4" style="background:{system['secondary_shell']}; border-color:{system['secondary_shell']}; border-radius:{system['radius']}; color:white;">
          <p class="text-xs uppercase tracking-[0.18em] text-slate-300">{system['nav_label']}</p>
          <nav class="mt-4 space-y-1">{side_nav(system)}</nav>
        </aside>
        <main>{content_grid(system)}</main>
      </div>
    </div>
    """


def layout_spectrum(system):
    cards = summary_cards(system)
    alerts = alert_list(system)
    approvals = approval_list(system)
    table = table_region(system)
    activity = timeline_region(system)
    return f"""
    <div class="min-h-screen">
      <header class="border-b px-4 py-3 lg:px-8" style="background:{system['surface']}; border-color:{system['border']};">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Spectrum workflow</p>
            <h1 class="mt-1 text-2xl font-semibold" style="color:{system['text']};">マスタ管理ダッシュボード</h1>
          </div>
          <div class="flex gap-2">
            {control_button(system, 'Share')}
            {control_button(system, 'Publish', 'primary')}
          </div>
        </div>
      </header>
      <div class="lg:grid lg:grid-cols-[120px_minmax(0,1fr)]">
        <aside class="px-4 py-5" style="background:{system['surface_alt']}; color:{system['muted']}; border-right:1px solid {system['border']};">
          <div class="space-y-4 text-center text-xs">
            <div class="rounded-xl py-2" style="background:{system['surface']}; color:{system['text']}; box-shadow:{system['shadow']};">Home</div>
            <div>Assets</div>
            <div>Review</div>
            <div>Publish</div>
          </div>
        </aside>
        <main class="px-4 py-4 lg:px-8 lg:py-6">
          <header class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{system['shadow']};">
            <div class="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
              <div>
                <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Creative workflow</p>
                <h2 class="mt-2 text-3xl font-semibold" style="color:{system['text']};">Master data review workspace</h2>
                <p class="mt-2 text-sm" style="color:{system['muted']};">Refined workflow chrome, lighter navigation framing, and friendlier hierarchy for approvals, alerts, and publishing.</p>
              </div>
              <div class="flex gap-2">
                {control_button(system, 'Search')}
                {control_button(system, 'Review', 'primary')}
              </div>
            </div>
          </header>
          <div class="mt-4 flex flex-wrap gap-2">
            <span class="rounded-full px-3 py-1.5 text-xs font-semibold" style="background:{system['surface']}; color:{system['text']}; border:1px solid {system['border']};">Review board</span>
            <span class="rounded-full px-3 py-1.5 text-xs font-semibold" style="background:{system['surface_alt']}; color:{system['muted']};">Publishing</span>
            <span class="rounded-full px-3 py-1.5 text-xs font-semibold" style="background:{system['surface_alt']}; color:{system['muted']};">Audit</span>
          </div>
          <section class="mt-6 grid gap-4 xl:grid-cols-[1.05fr_0.95fr]">
            <div class="space-y-4">
              <section class="grid gap-4 md:grid-cols-2">
                <article class="border p-4 md:col-span-2" style="background:{system['surface']}; border-color:{system['border']}; border-radius:16px; box-shadow:{system['shadow']};">
                  <div class="flex items-center justify-between gap-3">
                    <div>
                      <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Workspace status</p>
                      <p class="mt-2 text-sm" style="color:{system['muted']};">Friendlier workflow framing with clearer review context, quieter shell chrome, and more polished panel hierarchy.</p>
                    </div>
                    {badge(system, 'Update')}
                  </div>
                </article>
                {cards}
              </section>
              {table}
            </div>
            <div class="space-y-4">
              <article class="border p-5" style="background:{system['surface']}; border-color:{system['border']}; border-radius:{system['radius']}; box-shadow:{system['shadow']};">
                <div class="flex items-center justify-between">
                  <div>
                    <p class="text-xs uppercase tracking-[0.16em]" style="color:{system['muted']};">Review</p>
                    <h3 class="mt-2 text-xl font-semibold" style="color:{system['text']};">Approvals and alerts</h3>
                  </div>
                  {badge(system, 'Approval')}
                </div>
                <ul class="mt-4 space-y-3">{approvals}</ul>
                <div class="mt-4 border-t pt-4" style="border-color:{system['border']};">
                  <ul class="space-y-3">{alerts}</ul>
                </div>
              </article>
              {activity}
            </div>
          </section>
        </main>
      </div>
    </div>
    """


def render(system):
    body = {
        "sidebar": layout_sidebar,
        "atlassian": layout_atlassian,
        "carbon": layout_carbon,
        "public-service": layout_public_service,
        "workspace-light": layout_workspace_light,
        "apple": layout_apple,
        "lightning": layout_lightning,
        "material": layout_material,
        "primer": layout_primer,
        "business-light": layout_business_light,
        "sparkle": layout_sparkle,
        "spectrum": layout_spectrum,
    }[system["layout"]](system)
    return f"""<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{system['title']} Dashboard Mock</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      body {{
        font-family: {system['font']};
        background: {system['page_bg']};
        color: {system['text']};
      }}
    </style>
  </head>
  <body>{body}</body>
</html>
"""


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for system in SYSTEMS:
        (OUT_DIR / f"{system['slug']}.html").write_text(render(system), encoding="utf-8")


if __name__ == "__main__":
    main()
