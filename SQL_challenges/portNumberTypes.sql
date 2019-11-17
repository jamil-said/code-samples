
/* portNumberTypes -- MySQL
Given a table "portgroups" as following:

    CREATE TABLE portgroups (
        port_number integer not null,
        group_type integer not null,
        value float not null,
        time timestamp not null
    );

create a SQL query that returns all port numbers (port_number) with the 
number of different group types (group_type) registered on each port, 
ordered by port_number.

For example, given the following table:

     port_number | group_type | value  |        time         
    -------------+------------+--------+---------------------
               4 |          3 |   9.31 | 2017-09-14 11:32:00
               4 |          5 | -24.42 | 2017-09-14 11:17:03
               4 |          3 |  834.5 | 2017-09-14 10:34:37
               7 |          2 | -31.27 | 2017-09-14 14:45:06
               4 |          8 |   8.64 | 2017-09-14 18:31:31

your query should return the following result:

     port_number | types 
    -------------+-------
               4 |     3
               7 |     1
*/

/* Create database
mysql -u root -p
CREATE DATABASE portypes;
use portypes;
*/

/* Create example table and populate it
CREATE TABLE portgroups (
    port_number integer not null,
    group_type integer not null,
    value float not null,
    time timestamp not null
);


INSERT INTO portgroups (port_number, group_type, value, time) VALUES
    (4, 3, 9.31, '2017-09-14 11:32:00'),
    (4, 5, -24.42, '2017-09-14 11:17:03'),
    (4, 3, 834.5, '2017-09-14 10:34:37'),
    (7, 2, -31.27, '2017-09-14 14:45:06'),
    (4, 8, 8.64, '2017-09-14 18:31:31');
*/


SELECT port_number, COUNT(DISTINCT group_type) AS types
    FROM portgroups
    GROUP BY port_number
    ORDER BY port_number;


/*

 port_number | types 
-------------+-------
           4 |     3
           7 |     1

*/

