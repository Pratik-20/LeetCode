/*

1667. Fix Names in a Table

Easy

SQL Schema
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The query result format is in the following example.

 

Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |

*/


-- Solution

/*
We are going to just take name as substring 2 times and making first characters uppercase and from 2nd characters making lowercase then concatenating both substrings...
 */

SELECT user_id, CONCAT(UCASE(SUBSTRING(name,1,1)), LOWER(SUBSTRING(name,2))) AS name FROM Users               -- except "UCASE" we can use "UPPER" also....
ORDER BY user_id asc;         -- don't forget to order in ascending order