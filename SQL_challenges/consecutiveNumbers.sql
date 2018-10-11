-- tested on MySQL

/* consecutiveNumbers
Write a SQL query to find all numbers that appear at least three times 
consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

For example, given the above Logs table, 1 is the only number that appears 
consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

*/


SELECT DISTINCT lo.Num AS ConsecutiveNums
FROM Logs lo
JOIN Logs lo2 
ON lo.Id +1 = lo2.Id
JOIN Logs lo3 
ON lo.Id +2 = lo3.Id
WHERE lo.Num = lo2.Num
AND lo.Num = lo3.Num;


/*
input: {"headers": {"Logs": ["Id", "Num"]}, "rows": {"Logs": [[1, 1], [2, 1]
, [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}

output: {"headers":["ConsecutiveNums"],"values":[[1]]}
*/
