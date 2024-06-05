SELECT *,
       ABS((FIRST_VALUE(date) over (ORDER BY amount)) - date) as days_between_cheapest_order
FROM Orders
ORDER BY id;