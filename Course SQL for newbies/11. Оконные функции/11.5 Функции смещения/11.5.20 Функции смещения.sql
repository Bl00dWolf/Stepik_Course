SELECT *,
       LAG(quantity, 1, 0) over (ORDER BY month) as prev_month_sales,
       LAG(quantity, 2, 0) over (ORDER BY month) as second_prev_month_sales
FROM Sales;