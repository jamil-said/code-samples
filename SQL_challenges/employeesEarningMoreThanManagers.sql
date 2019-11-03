-- Tested on MySQL

/* employeesEarningMoreThanManagers

The Employee table holds all employees including their managers. Every 
employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who 
earn more than their managers. For the above table, Joe is the only employee 
who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

*/


SELECT em1.Name as Employee FROM Employee em1
JOIN Employee em2
ON em1.ManagerId = em2.Id
AND em1.Salary > em2.Salary;


/*
input: {"headers": {"Employee": ["Id", "Name", "Salary", "ManagerId"]}
, "rows": {"Employee": [[1, "Joe", 70000, 3], [2, "Henry", 80000, 4]
, [3, "Sam", 60000, null], [4, "Max", 90000, null]]}}

output: {"headers":["Employee"],"values":[["Joe"]]}
*/
