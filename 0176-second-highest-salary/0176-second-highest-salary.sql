# Write your MySQL query statement below
SELECT 
    IF(
        (SELECT COUNT(DISTINCT salary) FROM Employee) > 1, 
        (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1), 
        null
    ) 
AS SecondHighestSalary;