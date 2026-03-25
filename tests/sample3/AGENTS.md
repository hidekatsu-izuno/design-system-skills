# sample3 ページマップ

## 1. 画面一覧

| 機能 | 画面名 | パス | 参照設計書 |
| --- | --- | --- | --- |
| 組織管理 | 組織マスタ検索画面 | `organization/list/index.html` | `organization/list/AGENTS.md` |
| 組織管理 | 組織マスタ登録画面 | `organization/new/index.html` | `organization/new/AGENTS.md` |
| ユーザー管理 | ユーザーマスタ検索画面 | `user/list/index.html` | `user/list/AGENTS.md` |
| ユーザー管理 | ユーザーマスタ登録画面 | `user/new/index.html` | `user/new/AGENTS.md` |

## 2. メニュー情報

- 第1階層メニュー: `組織管理`
  遷移先: `organization/list/index.html`
- 第1階層メニュー: `ユーザー管理`
  遷移先: `user/list/index.html`

## 3. ページ遷移

- `組織管理` メニューから `組織マスタ検索画面` へ遷移する
- `組織マスタ検索画面` の `新規登録` から `組織マスタ登録画面` へ遷移する
- `組織マスタ登録画面` の `一覧へ戻る` から `組織マスタ検索画面` へ遷移する
- `ユーザー管理` メニューから `ユーザーマスタ検索画面` へ遷移する
- `ユーザーマスタ検索画面` の `新規登録` から `ユーザーマスタ登録画面` へ遷移する
- `ユーザーマスタ登録画面` の `一覧へ戻る` から `ユーザーマスタ検索画面` へ遷移する
