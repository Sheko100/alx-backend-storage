-- Creates a stored procedure that calculates the average score of a student
-- Creates a stored procedure that calculates the average score of a student
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(user_id int)
BEGIN
 SELECT id, name, AVG(corrections.score) as average_score from users INNER JOIN corrections ON corrections.user_id=users.id GROUP BY users.id;
END $$
DELIMITER ; $$
