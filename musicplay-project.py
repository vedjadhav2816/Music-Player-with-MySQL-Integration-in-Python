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

   


