SELECT director,
       (SELECT title
        FROM Films
        WHERE F.director = director
          AND release_year = (SELECT MIN(release_year)
                              FROM Films
                              WHERE F.director = director)) as title
FROM Films as F
GROUP BY director;

# НОРМАЛЬНОЕ решение
WITH NumberedTitle AS (
    SELECT director, title,
           ROW_NUMBER() OVER (PARTITION BY director ORDER BY release_year) AS num
    FROM Films
)

SELECT director, title
FROM NumberedTitle
WHERE num = 1;