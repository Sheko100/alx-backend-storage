-- Ranks country origins of bands ordered by the number of fans
-- Selects origin, sum of the origin fans as origin and nb_fans columns
SELECT DISTINCT origin, SUM(fans) AS nb_fans FROM metal_bands GROUp BY origin ORDER BY SUM(fans) DESC;
