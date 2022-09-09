-- query to get the top three states maximum temperture
SELECT state, max(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3;
