def login():
    valid_users = {
        "admin": "password",
    }
    attempts = 1
    while attempts >= 0:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username in valid_users and valid_users[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")
            attempts -= 1
    print("Too many failed attempts. Access denied.")
   



    if __name__ == "__main__":
        login()


        