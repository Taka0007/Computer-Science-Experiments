-- prefectures テーブルの id カラム (列) と name カラム (列) の情報を取得し表示
-- name カラムのカラム名は「都道府県名」に変更

SELECT id,name  AS '都道府県名' From prefectures;



--別解
SELECT
    id,
    name AS "都道府県名"
FROM
    prefectures;
