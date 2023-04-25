-- データの都道府県名を更新するクエリ
-- 最後に表を表示するのを忘れずに

UPDATE
    prefectures
SET
    name = '茨城県'
WHERE
    name = '茨木県';

UPDATE
    prefectures
SET
    name = '鳥取県'
WHERE
    name = '取鳥県';


SELECT
    *
FROM
    prefectures;
