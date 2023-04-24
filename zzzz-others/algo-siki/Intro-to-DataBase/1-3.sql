-- テーブルから条件付きで検索するクエリ
-- ここでは人口が1000000未満のもののみ抽出

SELECT * FROM prefectures WHERE  population < 1000000;
