SELECT x,
       y,
       ROUND(SQRT(POW(x, 2) + POW(y, 2)), 2) as distance
FROM Points
WHERE SQRT(POW(x, 2) + POW(y, 2)) > 20
ORDER BY distance DESC;