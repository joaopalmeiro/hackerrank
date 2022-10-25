-- https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_right
SELECT
  Name
FROM
  STUDENTS
WHERE
  Marks > 75
ORDER BY
  RIGHT(Name, 3),
  ID ASC
