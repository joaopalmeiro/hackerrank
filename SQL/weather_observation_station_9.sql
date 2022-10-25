-- https://dev.mysql.com/doc/refman/8.0/en/regexp.html#operator_not-regexp
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  NOT REGEXP_LIKE(CITY, '^[aeiou]', 'i')
