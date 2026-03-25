# 組織マスタ登録画面 設計書

## 1. 画面概要

組織マスタ (`organization_master`) を新規登録する画面。
組織コード、組織名、親組織、利用状態を入力して登録する。

## 2. 対象テーブル

- `ddl/organization_master.sql`

## 3. 入力項目

| 項目名 | 物理名 | 必須 | 型 / 桁数 | 入力形式 | 説明 |
| --- | --- | --- | --- | --- | --- |
| 組織コード | `organization_code` | 必須 | `VARCHAR(20)` | テキストボックス | 組織を一意に識別するコード |
| 組織名 | `organization_name` | 必須 | `VARCHAR(100)` | テキストボックス | 組織名称 |
| 親組織ID | `parent_organization_id` | 任意 | `BIGINT` | プルダウン / 組織検索ダイアログ | 上位組織。未指定可 |
| 有効フラグ | `is_active` | 必須 | `BOOLEAN` | チェックボックス | 初期値は有効 (`true`) |

## 4. 表示項目

| 項目名 | 内容 |
| --- | --- |
| 組織ID | 新規登録時は表示のみ。保存後に採番結果を表示 |
| 作成日時 | 保存後に表示 |
| 更新日時 | 保存後に表示 |

## 5. バリデーション

- `organization_code` は必須、20文字以内、重複不可
- `organization_name` は必須、100文字以内
- `parent_organization_id` を指定した場合、存在する組織IDであること
- `parent_organization_id` に自組織自身は指定不可
- `is_active` は未指定不可

## 6. 操作

- `登録` ボタン
  入力内容を検証後、`organization_master` に新規登録する
- `クリア` ボタン
  入力項目を初期値へ戻す
- `一覧へ戻る` ボタン
  組織マスタ検索画面へ遷移する

## 7. 登録処理

1. 入力チェックを実施する
2. `organization_code` の重複チェックを実施する
3. `organization_master` に以下を登録する
   - `organization_code`
   - `organization_name`
   - `parent_organization_id`
   - `is_active`
4. `organization_id` はDBのIDENTITYで採番する
5. `created_at` と `updated_at` はDBの `CURRENT_TIMESTAMP` を使用する

## 8. メッセージ

- 登録成功: `組織を登録しました。`
- 重複エラー: `指定した組織コードは既に使用されています。`
- 入力エラー: `入力内容を確認してください。`

