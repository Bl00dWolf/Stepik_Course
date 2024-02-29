INSERT INTO Songs (id, trackname, artist)
VALUES (6, 'Running up That Hill', 'Kate Bush'),
       (7, 'Thrill', 'The Sounds'),
       (8, 'Keep Yourself Alive', 'Queen');

#еще вариант
INSERT INTO Songs (id, trackname, artist)
VALUES ((SELECT MAX(id) FROM Songs AS S1) + 1, 'Running up That Hill', 'Kate Bush'),
       ((SELECT MAX(id) FROM Songs AS S2) + 1, 'Thrill', 'The Sounds'),
       ((SELECT MAX(id) FROM Songs AS S3) + 1, 'Keep Yourself Alive', 'Queen')