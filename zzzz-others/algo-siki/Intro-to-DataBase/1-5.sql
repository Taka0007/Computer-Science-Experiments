-- 「島」が含まれる県を抽出

SELECT * 
FROM 
    prefectures 
WHERE 
    name LIKE '%島%' ;
