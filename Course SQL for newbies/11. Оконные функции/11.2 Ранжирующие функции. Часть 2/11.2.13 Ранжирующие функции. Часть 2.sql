WITH rtn AS (SELECT DENSE_RANK() over (ORDER BY COUNT(*) DESC) as place,
                    director,
                    COUNT(*)                                   as number_of_films
             FROM Films
             GROUP BY director)

SELECT *
FROM rtn
ORDER BY place, director;