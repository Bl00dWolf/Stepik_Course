SELECT DISTINCT movie,
                NTH_VALUE(amount, 1) over (PARTITION BY movie) as first_month_box_office
FROM BoxOffice;

# еще вариант
WITH FirstMonth AS (
    SELECT DISTINCT movie,
           FIRST_VALUE(amount) OVER (PARTITION BY movie ORDER BY month) AS first_month_box_office
    FROM BoxOffice
)
SELECT movie, first_month_box_office
FROM FirstMonth;