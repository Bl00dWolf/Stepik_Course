INSERT INTO NewSongs (id, trackname, artist)
SELECT (SELECT MAX(id) FROM NewSongs AS NS1) + id, trackname, artist
FROM Songs;