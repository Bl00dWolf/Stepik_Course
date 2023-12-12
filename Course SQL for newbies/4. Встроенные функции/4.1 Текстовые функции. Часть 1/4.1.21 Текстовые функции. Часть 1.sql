SELECT REPEAT(english, CHAR_LENGTH(english)) as english
FROM Palindromes
WHERE english = REVERSE(english)
  AND russian != REVERSE(russian)