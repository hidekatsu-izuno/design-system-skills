# 組織マスタ検索画面 設計書

## 1. 画面概要

組織マスタ (`organization_master`) を検索し、一覧表示する画面。
組織コード、組織名、利用状態を条件に検索する。

## 2. 対象テーブル

- `ddl/organization_master.sql`

## メニュー情報

- メニュー構成と画面全体のページマップは `tests/sample3/AGENTS.md` を参照する

## 3. 検索条件

| 項目名 | 物理名 | 型 / 桁数 | 入力形式 | 説明 |
| --- | --- | --- | --- | --- |
| 組織コード | `organization_code` | `VARCHAR(20)` | テキストボックス | 前方一致または部分一致検索 |
| 組織名 | `organization_name` | `VARCHAR(100)` | テキストボックス | 部分一致検索 |
| 有効フラグ | `is_active` | `BOOLEAN` | ラジオボタン / セレクト | `全て / 有効 / 無効` |
| 親組織ID | `parent_organization_id` | `BIGINT` | プルダウン / 組織検索ダイアログ | 親組織で絞り込み |

## 4. 一覧表示項目

| 項目名 | 物理名 | 説明 |
| --- | --- | --- |
| 組織ID | `organization_id` | DB採番ID |
| 組織コード | `organization_code` | 一意キー |
| 組織名 | `organization_name` | 組織名称 |
| 親組織ID | `parent_organization_id` | 上位組織ID |
| 有効フラグ | `is_active` | 利用状態 |
| 作成日時 | `created_at` | 登録日時 |
| 更新日時 | `updated_at` | 更新日時 |

## 5. 操作

- `検索` ボタン
  入力条件に一致する組織を一覧表示する
- `クリア` ボタン
  検索条件を初期化する
- `新規登録` ボタン
  組織マスタ登録画面へ遷移する
- 一覧行クリック
  将来的に詳細 / 編集画面へ遷移可能とする

## 6. 検索仕様

- `organization_code` は前方一致または部分一致で検索する
- `organization_name` は部分一致で検索する
- `is_active` が `全て` の場合は条件に含めない
- `parent_organization_id` 指定時は完全一致で検索する
- 初期表示は未検索、または有効データのみ表示のいずれかを採用する

## 7. ソート順

- 初期ソートは `organization_code ASC`
- 任意で `updated_at DESC` への切替を許可する

## 8. メッセージ

- 検索結果なし: `該当する組織はありません。`
- 検索失敗: `検索処理でエラーが発生しました。`
