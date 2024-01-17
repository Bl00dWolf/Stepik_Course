#TODO решить задачу
SELECT id, name
FROM Books
WHERE (SELECT SUM(quantity)
       FROM Orders
       WHERE book_id = Books.id
       GROUP BY book_id) < 10
  AND (SELECT (TO_DAYS('2023-09-20') - TO_DAYS(dispatch_date))
       FROM Orders
       WHERE book_id = Books.id) <= 365;

SELECT book_id, (TO_DAYS('2023-09-20') - TO_DAYS(dispatch_date))
FROM Orders
GROUP BY book_id