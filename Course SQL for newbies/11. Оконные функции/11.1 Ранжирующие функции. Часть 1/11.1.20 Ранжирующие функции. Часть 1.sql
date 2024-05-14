WITH formated_films AS (SELECT title,
                               director,
                               ROW_NUMBER() over (PARTITION BY director, title) as num2,
                               release_year
                        FROM Films
                        ORDER BY release_year),

     formated_films2 AS (SELECT title,
                                director,
                                num2,
                                release_year,
                                ROW_NUMBER() over (ORDER BY release_year) as num
                         FROM formated_films
                         WHERE num2 = 1)

SELECT num,
       title,
       director,
       release_year
FROM formated_films2
ORDER BY num DESC;

# Верное решение
WITH UniqueFilms AS (
    SELECT DISTINCT title, director, release_year
    FROM Films
)
SELECT ROW_NUMBER() OVER (ORDER BY release_year) AS num,
       UniqueFilms.*
FROM UniqueFilms
ORDER BY num DESC;