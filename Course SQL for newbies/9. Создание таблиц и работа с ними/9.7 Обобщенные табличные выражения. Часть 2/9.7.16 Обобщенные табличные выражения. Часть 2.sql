WITH RECURSIVE num AS (SELECT 1 as num, FLOOR(RAND() * (50 - 10 + 1)) + 10 as cht
                       UNION
                       DISTINCT
                       SELECT num + 1, FLOOR(RAND() * (50 - 10 + 1)) + 10 as cht
                       FROM num
                       WHERE num < 20)

SELECT cht AS number
FROM num;

# Еще вариант
with recursive numbers(num) as (select 10
                                UNION ALL
                                select num + 1
                                from numbers
                                where num < 50)
select num as number
from numbers
order by RAND()
limit 20;