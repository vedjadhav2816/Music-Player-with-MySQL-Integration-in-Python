# python code

import pymysql
import pygame
import os


pygame.mixer.init()


def play_all_music():
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', database='spacedb')
        cursor = conn.cursor()

        cursor.execute("SELECT filepath FROM music_files")
        result = cursor.fetchall()

        if result:
            for row in result:
                filepath = row[0]

        
                if os.path.exists(filepath):
                    print(f"Playing: {filepath}")
                    
                 
                    pygame.mixer.music.load(filepath)
                    pygame.mixer.music.play()

           
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                else:
                    print(f"File not found: {filepath}")
        else:
            print("No music found in the database.")
    
    except pymysql.MySQLError as e:
        print(f"MySQL error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


def add_music():
    """Add a new music entry to the database"""
    music_name = input("Enter music name: ") 
    filepath = input("Enter music file path: ") 
    
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', database='spacedb')
        cursor = conn.cursor()

  
        cursor.execute("INSERT INTO music_files (music_name, filepath) VALUES (%s, %s)", (music_name, filepath))
        conn.commit()
        print("Music added successfully!")

    except pymysql.MySQLError as e:
        print(f"MySQL Error: {e}")
    finally:
        cursor.close()
        conn.close()


def show_music_list():
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', database='spacedb')
        cursor = conn.cursor()


        cursor.execute("SELECT musicid, music_name, filepath FROM music_files")
        result = cursor.fetchall()

        if result:
            print("Music List:")
            for row in result:
                print(f"ID: {row[0]} | Name: {row[1]} | Filepath: {row[2]}")
        else:
            print("No music found in the database.")

    except pymysql.MySQLError as e:
        print(f"MySQL Error: {e}")
    finally:
        cursor.close()
        conn.close()


def main():
    while True:
        print("\n--- Music Database ---")
        print("1. Add Music")
        print("2. Show Music List")
        print("3. Play All Music")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_music()
        elif choice == '2':
            show_music_list()
        elif choice == '3':
            play_all_music()  
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
# SQL CODE 
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



