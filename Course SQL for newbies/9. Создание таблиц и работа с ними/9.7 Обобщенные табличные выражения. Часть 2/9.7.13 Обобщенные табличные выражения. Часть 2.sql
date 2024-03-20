WITH RECURSIVE chrcv AS (SELECT 65  as num,
                                'A' as letter
                         UNION
                         DISTINCT
                         SELECT num + 1, CONVERT(CHAR(num + 1), CHAR)
                         FROM chrcv
                         WHERE num < 90)

SELECT letter
FROM chrcv;

# Варик лучше
WITH RECURSIVE AsciiUpperCase AS (SELECT 'A' AS letter
                                  UNION
                                  SELECT CHAR(ORD(letter) + 1)
                                  FROM AsciiUpperCase
                                  LIMIT 26)

SELECT *
FROM AsciiUpperCase;