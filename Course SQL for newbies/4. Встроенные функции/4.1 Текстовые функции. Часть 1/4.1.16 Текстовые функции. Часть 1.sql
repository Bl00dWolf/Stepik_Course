SELECT name, surname
FROM Directors
WHERE BINARY name = LOWER(name)
   OR BINARY surname = LOWER(surname)
ORDER BY name;