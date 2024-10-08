database = {}


def register(username, password):
    # Check if the username already exists
    if username in database:
        return "Username already taken!"
    else:
        # Add the new user to the database
        database[username] = {"username": username, "password": password}
        return "Registration successful!"


def login(username, password):
    # Check if the username exists
    if username in database:
        # Verify password
        return database[username]["password"] == password


username = input("Enter the user_name ")
pass_word = input("Enter the password ")

if login(username, pass_word):
    print("Sucessfully Login")
else:
    print("User Does not Exist !")
    new_ragister = input("Are you want to ragister new account ? (Yes/No) ")
    if new_ragister.lower() in "yes":
        user_name = input("Enter the user_name ")
        password = input("Enter the password ")
        register(user_name, password)
        print("Sucessfully Ragisted")
    else:
        print("Thank You Visit again")
