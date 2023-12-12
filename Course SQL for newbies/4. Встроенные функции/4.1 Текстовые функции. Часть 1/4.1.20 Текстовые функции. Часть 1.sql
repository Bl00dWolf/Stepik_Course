# SELECT english, russian
# FROM Palindromes
# WHERE LPAD(english, CHAR_LENGTH(english) / 2, '') =
#       RPAD(REVERSE(english), CHAR_LENGTH(english) / 2, '')
#   AND LPAD(russian, CHAR_LENGTH(russian) / 2, '') =
#       RPAD(REVERSE(russian), CHAR_LENGTH(russian) / 2, '')
# ORDER BY english;

SELECT english, russian
FROM Palindromes
WHERE english = REVERSE(english)
  AND russian = REVERSE(russian)
ORDER BY english