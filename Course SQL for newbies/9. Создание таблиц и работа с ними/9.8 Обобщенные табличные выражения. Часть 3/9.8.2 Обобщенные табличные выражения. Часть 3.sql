WITH RECURSIVE FolderMap AS (SELECT id, name, CONVERT(name, CHAR(100)) AS path
                             FROM Files
                             WHERE parent_directory_id is NULL

                             UNION ALL

                             SELECT Files.id, Files.name, CONCAT_WS('/', FolderMap.path, Files.name) AS path
                             FROM FolderMap
                                      INNER JOIN Files ON FolderMap.id = Files.parent_directory_id)

SELECT id, path
FROM FolderMap;