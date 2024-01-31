SELECT 'Mathematician' AS profession, COUNT(*) AS total
FROM Mathematicians
GROUP BY profession

UNION ALL

SELECT 'Physicist' AS profession, COUNT(*) AS total
FROM Physicists
GROUP BY profession

UNION ALL

SELECT 'Programmer' AS profession, COUNT(*) AS total
FROM Programmers
GROUP BY profession;