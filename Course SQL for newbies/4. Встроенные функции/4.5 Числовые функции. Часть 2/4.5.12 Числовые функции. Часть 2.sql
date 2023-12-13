SELECT num,
       CONV(num, 10, 2)  as bin,
       CONV(num, 10, 8)  as oct,
       CONV(num, 10, 16) as hex
FROM PrimeNumbers
ORDER BY num DESC;