SET @num_of_id := 1;
SELECT @num_of_id := (SELECT MAX(id) DIV 3 FROM Directors);

WITH ntile_group AS (SELECT *,
                            NTILE(@num_of_id) over (ORDER BY id) AS grp
                     FROM Directors)

SELECT grp as group_number, AVG(rating) as avg_rating
FROM ntile_group
GROUP BY grp
ORDER BY grp DESC;

# Еще вариант
SELECT COUNT(*) DIV 3
INTO @count_of_groups
FROM Directors;

WITH GroupRating AS (SELECT NTILE(@count_of_groups) OVER (ORDER BY id) AS group_number, rating
                     FROM Directors)

SELECT group_number, AVG(rating) AS avg_rating
FROM GroupRating
GROUP BY group_number
ORDER BY group_number DESC;