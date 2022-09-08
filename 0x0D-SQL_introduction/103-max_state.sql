SELECT max(value) as max_temp, state FROM temperatures GROUP BY state ORDER BY max_temp DESC LIMIT 3;
