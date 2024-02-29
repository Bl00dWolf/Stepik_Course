INSERT INTO Songs (id, trackname, artist)
SELECT (SELECT MAX(id) FROM Songs) + 1,
       'Let Me Kiss You',
       'Morrissey';