CREATE VIEW ord_year_prd AS
SELECT YEAR(purchase_date) AS date, product_id, COUNT(*) AS quant
FROM Orders
GROUP BY date, product_id
HAVING quant >= 3
ORDER BY date DESC, product_id;

SELECT DISTINCT O1.product_id
FROM ord_year_prd AS O1
         JOIN ord_year_prd AS O2 ON O1.product_id = O2.product_id
WHERE O1.date = O2.date - 1;

# Еще вариант:
CREATE VIEW ProductInfo AS
SELECT product_id, YEAR(purchase_date) AS purchase_year
FROM Orders
GROUP BY product_id, purchase_year
HAVING COUNT(*) >= 3;


SELECT DISTINCT P1.product_id
FROM ProductInfo AS P1,
     ProductInfo AS P2
WHERE P1.product_id = P2.product_id
  AND P1.purchase_year = P2.purchase_year + 1
