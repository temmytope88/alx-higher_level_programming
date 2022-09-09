--query to get the top three states maximum temperture
SELECT max(value) as 'max_temp', state FROM 'temperatures' GROUP BY 'state' ORDER BY 'state' ASC LIMIT 3;
