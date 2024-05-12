SELECT CONVERT(CHAR(ROW_NUMBER() over (ORDER BY num) + 64), char) as letter,
       num
FROM PrimeNumbers
ORDER BY letter DESC;
