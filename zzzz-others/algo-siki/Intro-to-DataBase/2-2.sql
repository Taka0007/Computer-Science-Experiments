-- 地方ごとに集計(グループ分け)し、地方ごとの総面積を大きい順に表示

SELECT
    region AS '地方名' , 
    COUNT(*) AS '都道府県数', 
    SUM(area) AS '総面積' 

FROM
    prefectures  GROUP BY region

ORDER BY
    SUM(area)
    DESC;


-- SUM(area)の部分を「総面積」で置き換える際には`総面積`としなければならない
