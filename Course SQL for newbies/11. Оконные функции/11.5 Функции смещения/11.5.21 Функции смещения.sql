SELECT *,
       LAG(quantity, 3, 0) over (ORDER BY month) as prev_quarter_month_sales
FROM Sales;