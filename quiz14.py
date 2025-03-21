#make a program that writes jokes into database
#the user will supply the jokes 
import sqlite3

# db conn
def setup_database():
    conn = sqlite3.connect("jokes.db")
    cursor = conn.cursor()
    
    # Create jokes table if 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jokes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        joke_text TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    return conn, cursor

# Add a joke to the database
def add_joke(cursor, conn):
    print("\n--- Add a New Joke ---")
    joke_text = input("Type your joke: ")
    
    if joke_text.strip() == "":
        print("Joke cannot be empty!")
        return
    
    cursor.execute("INSERT INTO jokes (joke_text) VALUES (?)", (joke_text,))
    conn.commit()
    print("Joke saved successfully!")

# View all jokes
def view_jokes(cursor):
    print("\n--- All Jokes ---")
    cursor.execute("SELECT id, joke_text FROM jokes")
    jokes = cursor.fetchall()
    
    if not jokes:
        print("No jokes found. Try adding some!")
        return
    
    for joke in jokes:
        print(f"Joke #{joke[0]}: {joke[1]}")
        print("-" * 30)

# Main program
def main():
    conn, cursor = setup_database()
    
    while True:
        print("\n=== JOKE DATABASE ===")
        print("1. Add a joke")
        print("2. View all jokes")
        print("3. Exit")
        
        choice = input("\n Ano ba ang gusto mong sabihin?  (1/2/3): ")
        #if ung napili ng user is 1, 2, or 3 then proceed sa next steps else ang user will require to enter 1,2, or 3
        if choice == "1":
            add_joke(cursor, conn)
        elif choice == "2":
            view_jokes(cursor)
        elif choice == "3":
            print("Thanks for using the Joke Database!")
            break
        else:
            print("Please enter 1, 2, or 3.")
    
    conn.close()

# Start the program
if __name__ == "__main__":
    main()