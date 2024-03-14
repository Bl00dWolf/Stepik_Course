WITH Max_In_June AS (SELECT store, SUM(amount)
                     FROM Orders
                     WHERE MONTHNAME(order_date) = 'June'
                     GROUP BY store
                     ORDER BY 2 DESC
                     LIMIT 1),
     Max_In_July AS (SELECT store, SUM(amount)
                     FROM Orders
                     WHERE MONTHNAME(order_date) = 'July'
                     GROUP BY store
                     ORDER BY 2 DESC
                     LIMIT 1)

SELECT Max_In_June.store AS best_in_june, Max_In_July.store AS best_in_july
FROM Max_In_June,
     Max_In_July;