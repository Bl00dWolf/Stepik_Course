SELECT CONCAT(angle, '°')            as x,
       ROUND(SIN(RADIANS(angle)), 1) as 'sin(x)',
       ROUND(COS(RADIANS(angle)), 1) as 'cos(x)'
FROM Angles
ORDER BY angle;