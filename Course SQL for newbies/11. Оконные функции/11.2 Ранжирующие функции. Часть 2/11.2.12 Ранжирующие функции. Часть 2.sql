WITH rtn AS (SELECT *,
                    DENSE_RANK() over (PARTITION BY country ORDER BY rating DESC) as rating_dense
             FROM Directors)

SELECT full_name, country, rating
FROM rtn
WHERE rating_dense = 1
ORDER BY country, full_name;