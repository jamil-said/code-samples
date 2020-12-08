-- Tested on MySQL

/* customersWhoNeverOrder

Suppose that a website contains two tables, the Customers table and the 
Orders table. Write a SQL query to find all customers who never order 
anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

*/


SELECT c.Name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL


/* Alternative, slower

SELECT c.Name AS Customers 
FROM Customers c
WHERE c.Id NOT IN (SELECT CustomerId FROM Orders);

*/


/*
input:  {"headers": {"Customers": ["Id", "Name"], "Orders": ["Id", "CustomerId"]}
, "rows": {"Customers": [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]]
, "Orders": [[1, 3], [2, 1]]}}

output: {"headers":["Customers"],"values":[["Henry"],["Max"]]}
*/
