-- https://dev.mysql.com/doc/refman/8.0/en/case.html
-- https://www.w3schools.com/sql/func_mysql_case.asp
SELECT
  CASE
    WHEN A + B <= C OR
    A + C <= B OR
    B + C <= A THEN "Not A Triangle"
    WHEN A = B AND
    B = C THEN "Equilateral"
    WHEN A = B OR
    A = C OR
    B = C THEN "Isosceles"
    ELSE "Scalene"
  END
FROM
  TRIANGLES
