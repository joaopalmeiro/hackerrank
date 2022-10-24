-- https://dev.mysql.com/doc/refman/8.0/en/union.html#union-order-by-limit
(
  SELECT
    CITY,
    LENGTH(CITY)
  FROM
    STATION
  ORDER BY
    LENGTH(CITY) ASC,
    CITY
  LIMIT
    1
)
UNION
(
  SELECT
    CITY,
    LENGTH(CITY)
  FROM
    STATION
  ORDER BY
    LENGTH(CITY) DESC,
    CITY
  LIMIT
    1
)
