-- a query to select city and determine their average temperatures
SELECT city, AVG(value) AS "avg_temp" FROM temperature GROUP BY city avg_temp DESC;