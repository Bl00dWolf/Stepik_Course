SELECT name,
       surname,
       REPLACE(email, 'outlook.com', 'pygen.ru') as email
FROM Directors
WHERE SUBSTRING_INDEX(email, '@', -1) = 'outlook.com'
ORDER BY email