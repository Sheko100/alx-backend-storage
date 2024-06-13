-- Creates users table
-- Creates users table with id, email, name as columns
CREATE TABLE IF NOT EXISTS users (
        id int AUTO_INCREMENT NOT NULL,
        email varchar(255) UNIQUE NOT NULL,
        name varchar(255),
        PRIMARY KEY (id)
);
