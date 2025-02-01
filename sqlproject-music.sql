create database project;
use spacedb;
SHOW VARIABLES LIKE 'secure_file_priv';
show variables like 'sec%';
CREATE TABLE IF NOT EXISTS music_files (
    musicid INT AUTO_INCREMENT PRIMARY KEY,
    music_name VARCHAR(255) NOT NULL,
    filepath VARCHAR(255) NOT NULL
);
SHOW VARIABLES LIKE 'secure_file_priv';
SHOW VARIABLES LIKE 'sec%';

INSERT INTO music_files (music_name, filepath) 
VALUES 
('Shadows of Destiny', 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Shadows of Destiny.mp3'),
('Marco Tony Mayhem BGM', 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/marco_tony_mayhem_bgm.mp3'),
('Raja Ala', 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/raja_ala.mp3');

SELECT musicid, music_name, HEX(filepath) FROM music_files;
SELECT music_name, filepath FROM music_files WHERE musicid = 1;
DELIMITER $$

CREATE PROCEDURE callmusic(IN music_id INT)
BEGIN
    SELECT music_name, filepath 
    FROM music_files 
    WHERE musicid = music_id;
END $$

DELIMITER ;

CALL callmusic(1);  
CALL callmusic(2); 
CALL callmusic(3);  


DESC music_files;
SELECT * FROM music_files;
