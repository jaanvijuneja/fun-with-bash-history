CREATE TABLE user_history (
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   command VARCHAR(500),
   unix_timestamp VARCHAR(50),
   system_timestamp VARCHAR(200),
   user VARCHAR(100)
);

