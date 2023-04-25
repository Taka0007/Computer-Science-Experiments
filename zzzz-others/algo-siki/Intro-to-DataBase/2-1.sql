-- 副問い合わせ
-- 別のテーブルにあるものだけを抽出して表示

SELECT
    *
FROM
    prefectures

WHERE
    name in (SELECT * FROM kanto_regions);
