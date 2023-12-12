SELECT id,
       name,
       surname,
       LEFT(email, LOCATE('@', email) - 1) AS local_part
FROM Directors
ORDER BY id DESC;