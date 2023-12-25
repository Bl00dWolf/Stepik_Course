SELECT name, surname
FROM Math
WHERE surname = ANY (SELECT surname
                     FROM Math AS Mt
                     WHERE id != Math.id)
ORDER BY surname, name