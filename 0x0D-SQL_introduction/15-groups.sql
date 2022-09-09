-- A query that groups rows with the same score and count them
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY number DESC;