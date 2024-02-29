INSERT INTO MorrisseySongs (id, trackname, artist)
SELECT id, trackname, artist
FROM Songs
WHERE artist = 'Morrissey';

DELETE
FROM Songs
WHERE artist = 'Morrissey';