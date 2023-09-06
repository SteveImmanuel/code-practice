CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE B INT;
  SET B = N-1;
  RETURN (
    SELECT IF(
        (SELECT COUNT(DISTINCT salary) FROM Employee) > B, 
        (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET B), 
        null
    ) 
  );
END