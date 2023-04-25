--最高気温のうち最大のものと、最低気温のうち最小のものを取得
--カラム名も変更する
SELECT
    MAX(highest) AS '最高気温',
    MIN(lowest) AS '最低気温'
FROM
    temperature_august;
