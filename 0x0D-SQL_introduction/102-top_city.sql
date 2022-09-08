-- to select the city with the top 3 average temp between july and aug
SELECT AVG(value) as avg_temp, city FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY max_temp DESC LIMIT 3;
