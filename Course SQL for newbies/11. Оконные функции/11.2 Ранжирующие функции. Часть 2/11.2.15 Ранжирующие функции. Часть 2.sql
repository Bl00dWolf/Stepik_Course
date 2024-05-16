SELECT MAX(id) DIV 2
FROM Directors
INTO @group_id_count;

WITH grp AS (SELECT *,
                    NTILE(@group_id_count) over (ORDER BY id) as num_group
             FROM Directors),

     grp2 AS (SELECT D1.full_name                             as D1Fullname,
                     D1.num_group,
                     D2.full_name                             AS D2Fullname,
                     IF(D1.country = D2.country, 'yes', 'no') as from_same_country
              FROM grp AS D1
                       JOIN grp AS D2 ON D1.num_group = D2.num_group AND D1.full_name != D2.full_name),
     grp3 AS (SELECT num_group,
                     GROUP_CONCAT(D1Fullname SEPARATOR ', ') as pair,
                     MIN(from_same_country)                  AS from_same_country
              FROM grp2
              GROUP BY num_group)

SELECT pair, from_same_country
FROM grp3;

# Еще вариант
# SELECT COUNT(*) DIV 2 INTO @count_of_groups
# FROM Directors;
#
# WITH GroupDirectors AS (
#     SELECT Directors.*,
#            NTILE(@count_of_groups) OVER (ORDER BY id) AS group_director
#     FROM Directors
# )
#
# SELECT GROUP_CONCAT(full_name SEPARATOR ', ') AS pair,
#        IF(COUNT(DISTINCT country) = 1, 'yes', 'no') AS from_same_country
# FROM GroupDirectors
# GROUP BY group_director;