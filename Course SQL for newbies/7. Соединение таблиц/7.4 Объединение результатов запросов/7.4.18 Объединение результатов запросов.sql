SELECT 'bee' AS word, COUNT(*) AS count
FROM Files
WHERE UPPER(content) LIKE UPPER('% bee %')
   OR UPPER(content) LIKE UPPER('bee %')
   OR UPPER(content) LIKE UPPER('% bee')
   OR UPPER(content) LIKE UPPER('bee')

UNION

SELECT 'geek' AS word, COUNT(*)
FROM Files
WHERE UPPER(content) LIKE UPPER('% geek %')
   OR UPPER(content) LIKE UPPER('geek %')
   OR UPPER(content) LIKE UPPER('% geek')
   OR UPPER(content) LIKE UPPER('geek');

# Еще вариант
select 'bee' as word, count(*) as count
from Files
where content REGEXP '\\bbee\\b'
union
select 'geek', count(*)
from Files
where content REGEXP '\\bgeek\\b';