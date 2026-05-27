/*
LeetCode #0175: Combine Two Tables
Difficulty: Easy
Date: 2026-05-26

[Query explanation]
- Scan Type: Index Scan -> The query utilizes the clustered index on 'PersonId' rather than a full table scan.
- Bottleneck Risk(if exist): High memory overhead if the Address table grows exponentially due to the LEFT JOIN materialization.

[AI Mentor Feedback]
- Utilizing an outer join is correct here to prevent losing Person records that lack corresponding Address data.
- Ensure 'PersonId' is designated as a Foreign Key to maintain referential integrity and optimize the query planner.

[Useful Technical English]
- "This query optimizes execution time by performing an index lookup on the join predicate."
*/

SELECT 
    p.FirstName, 
    p.LastName, 
    a.City, 
    a.State
FROM 
    Person p
LEFT JOIN 
    Address a 
ON 
    p.PersonId = a.PersonId;
