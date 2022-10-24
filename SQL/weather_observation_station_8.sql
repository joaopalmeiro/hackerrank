-- https://dev.mysql.com/doc/refman/8.0/en/regexp.html#regexp-syntax
-- https://dev.mysql.com/doc/refman/8.0/en/regexp.html#function_regexp-like
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  REGEXP_LIKE(CITY, '^[aeiou].*[aeiou]$', 'i')
