-- https://dev.mysql.com/doc/refman/8.0/en/regexp.html#function_regexp-like
-- https://stackoverflow.com/a/54922417
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  REGEXP_LIKE(CITY, '^[aeiou]', 'i')
