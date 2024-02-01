SELECT name, surname
FROM (SELECT name, surname, 1 AS sortvalue
      FROM Mathematicians

      UNION

      SELECT name, surname, 2
      FROM Physicists
      UNION

      SELECT name, surname, 3
      FROM Programmers) AS UN1
ORDER BY sortvalue, name DESC, surname DESC;

# Еще вариант
SELECT name, surname
FROM ((SELECT name, surname, 1 AS sort_value
       FROM Mathematicians)

      UNION

      (SELECT name, surname, 2
       FROM Physicists)

      UNION

      (SELECT name, surname, 3
       FROM Programmers)
      ORDER BY sort_value, name DESC, surname DESC) AS tmp;