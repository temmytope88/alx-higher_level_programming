-- select from a table name and id
SELECT id, name
FROM cities
WHERE state_id IN
    (SELECT id
    FROM state
    WHERE name = california)
ORDER BY id ASC;