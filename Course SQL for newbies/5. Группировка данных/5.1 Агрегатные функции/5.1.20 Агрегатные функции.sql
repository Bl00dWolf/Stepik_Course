SELECT GROUP_CONCAT(DISTINCT country ORDER BY country SEPARATOR ', ') AS countries
FROM Directors;