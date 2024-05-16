WITH rtn AS (SELECT DENSE_RANK() over (ORDER BY rating DESC) as num,
                    full_name,
                    rating
             FROM Directors)

SELECT full_name, rating
FROM rtn
WHERE num = 2
ORDER BY full_name;