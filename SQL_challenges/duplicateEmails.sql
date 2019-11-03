-- tested on MySQL

/* duplicateEmails

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+

Note: All emails are in lowercase.

*/

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1;

/*
input: {"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[1, "a@b.com"]
, [2, "c@d.com"], [3, "a@b.com"]]}} 

output: {"headers":["Email"],"values":[["a@b.com"]]}
*/
