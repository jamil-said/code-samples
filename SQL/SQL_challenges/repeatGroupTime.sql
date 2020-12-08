/* repeatGroupTime -- MySQL
Given a table "grouptimes" as following:

    CREATE TABLE grouptimes (
        group_number integer not null,
        value integer not null,
        time timestamp not null,
        unique(group_number, time)
    );

create a SQL query that, for each group_number that appears more than once, 
returns the difference between the latest value (most recent in terms 
of time) and the second latest value. The table should be ordered by 
group_number (ascending order). 

For example, given the following data:

     group_number | value |        time         
    --------------+-------+---------------------
                4 |     8 | 2017-08-12 11:32:00
                5 |    -2 | 2017-08-12 11:39:58
                4 |     2 | 2017-08-12 13:37:35
                4 |    12 | 2017-08-12 09:50:23
                6 |    11 | 2017-08-12 08:12:51
                6 |    -3 | 2017-08-12 09:11:00


your query should return the following result:

     group_number | value 
    --------------+-------
                4 |    -6
                6 |   -14

For the group_number 4, the latest value is 2 and the second latest value 
is 8, so the difference between them is -6. 
*/

/* Create database
mysql -u root -p
CREATE DATABASE repeatgroup;
USE repeatgroup;
*/

/* Create example table and populate it
CREATE TABLE grouptimes (
    group_number integer not null,
    value integer not null,
    time timestamp not null,
    unique(group_number, time)
);

INSERT INTO grouptimes (group_number, value, time) VALUES
    (4, 8, '2017-08-12 11:32:00'),
    (5, -2, '2017-08-12 11:39:58'),
    (4, 2, '2017-08-12 13:37:35'),
    (4, 12, '2017-08-12 9:50:23'),
    (6, 11, '2017-08-12 8:12:51'),
    (6, -3, '2017-08-12 9:11:00');
*/


SELECT gr1.group_number, (gr1.value - gr2.value) AS value 
FROM grouptimes gr1
JOIN grouptimes gr2 
ON gr1.group_number = gr2.group_number
AND gr1.time = (SELECT tmp1.time 
    FROM grouptimes tmp1 
    WHERE tmp1.group_number=gr1.group_number 
    ORDER BY time DESC 
    LIMIT 1)
AND gr2.time = (SELECT tmp2.time 
    FROM grouptimes tmp2
    WHERE tmp2.group_number=gr2.group_number 
    ORDER BY time DESC 
    LIMIT 1 
    OFFSET 1)
ORDER BY group_number;


/* expected result

 group_number | value 
--------------+-------
            4 |    -6
            6 |   -14

*/
