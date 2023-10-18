-- User grant script
-- User permissions
-- if the user already exists, the code
-- doesn't fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;
