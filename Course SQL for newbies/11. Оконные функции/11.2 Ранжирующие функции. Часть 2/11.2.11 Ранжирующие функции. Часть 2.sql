SELECT *
FROM Directors
ORDER BY NTILE(2) over (ORDER BY id DESC), rating DESC, id;