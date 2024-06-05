WITH ntile_month AS (SELECT *,
                            NTILE(4) over (ORDER BY month) as quartal
                     FROM Sales)

SELECT month,
       quantity,
       FIRST_VALUE(month) over (PARTITION BY quartal ORDER BY quantity DESC)    as highest_sales_month_within_quarter,
       FIRST_VALUE(quantity) over (PARTITION BY quartal ORDER BY quantity DESC) as highest_sales_quantity_within_quarter
FROM ntile_month
ORDER BY month;