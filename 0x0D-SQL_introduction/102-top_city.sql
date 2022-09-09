-- to select the city with the top 3 average temp between july and aug
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
