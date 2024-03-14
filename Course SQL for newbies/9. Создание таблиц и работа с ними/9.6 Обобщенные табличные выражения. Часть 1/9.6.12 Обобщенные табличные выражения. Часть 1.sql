WITH AvgSum_Orders AS (SELECT store,
                              ROUND(AVG(amount), 1) AS avg_for_store
                       FROM Orders
                       GROUP BY store)

SELECT Orders.id, Orders.store, Orders.amount, AvgSum_Orders.avg_for_store
FROM Orders
         JOIN AvgSum_Orders ON Orders.store = AvgSum_Orders.store;