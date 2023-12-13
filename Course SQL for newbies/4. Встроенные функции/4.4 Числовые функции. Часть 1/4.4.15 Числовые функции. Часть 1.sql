SELECT actual_size,
       limit_deviation,
       ABS(nominal_size - actual_size) as difference
FROM Sizes
WHERE ABS(nominal_size - actual_size) <= limit_deviation
ORDER BY actual_size;