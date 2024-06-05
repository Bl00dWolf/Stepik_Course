SELECT *,
       FIRST_VALUE(month) over (ORDER BY quantity DESC) as highest_sales_month
FROM Sales
ORDER BY month;