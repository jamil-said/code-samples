-- Tested on MySQL

/* nthHighestSalary

Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the nth highest salary where 
n = 2 is 200. If there is no nth highest salary, then the query should 
return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

*/

-- put "select" in subquery to generate NULL instead of empty, use "distinct"
-- because problem wants a "distinct" second highest (can't be equal to highest)

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
    BEGIN
        DECLARE J INT;
        SET J = N - 1;
        RETURN (
            SELECT (SELECT DISTINCT Salary from Employee
            ORDER BY Salary DESC LIMIT 1 OFFSET J) AS getNthHighestSalary
        );
    END

/*

input: {"headers": {"Employee": ["Id", "Salary"]}, "argument": 2, "rows"
: {"Employee": [[1, 100], [2, 200], [3, 300]]}}

output: {"headers":["getNthHighestSalary(2)"],"values":[[200]]}

*/

