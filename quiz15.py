#make a program that reads random jokes from database
import sqlite3
import random

def get_random_joke():
    try:
        # Connect to the database
        conn = sqlite3.connect("jokes.db")
        cursor = conn.cursor()
        
        # Count total jokes
        cursor.execute("SELECT COUNT(*) FROM jokes")
        total_jokes = cursor.fetchone()[0]
        
        if total_jokes == 0:
            return "No jokes found in the database. Add some jokes first!"
        
        # Get a random joke
        cursor.execute("SELECT id, joke_text FROM jokes ORDER BY RANDOM() LIMIT 1")
        joke = cursor.fetchone()
        
        conn.close()
        
        return f"Joke #{joke[0]}: {joke[1]}"
    
    except sqlite3.Error as e:
        return f"Database error: {e}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=== RANDOM JOKE GENERATOR ===")
    
    while True:
        print("\nOptions:")
        print("1. Get a random joke")
        print("2. Exit")
        
        choice = input("\nWhat would you like to do? (1/2): ")
        
        if choice == "1":
            joke = get_random_joke()
            print("\n" + joke)
        elif choice == "2":
            print("Thanks for using the Random Joke Generator!")
            break
        else:
            print("Please enter 1 or 2.")

if __name__ == "__main__":
    main()