SELECT CONCAT_WS(', ', Meals.name, Drinks.name) AS combo,
       CONCAT(Meals.price + Drinks.price, '€')  AS price
FROM Meals,
     Drinks
ORDER BY Meals.price + Drinks.price, Meals.price, Drinks.name;