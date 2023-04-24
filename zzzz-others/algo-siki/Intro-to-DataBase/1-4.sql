-- 面積が大きい順に並び替えたときの上位10件を出力

SELECT * FROM prefectures 
ORDER BY area DESC
LIMIT 10
;


--別解
SELECT
    *
FROM
    prefectures
ORDER BY
    area
LIMIT 10;
