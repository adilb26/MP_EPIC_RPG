import json

user_data_file = 'user_data.json'

def load_user_data():
    try:
        with open(user_data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open(user_data_file, 'w') as file:
        json.dump(data, file, indent=4)

def register():
    users = load_user_data()
    username = input("Enter a new username: ").strip()
    if not username or username in users:
        print("Invalid or existing username. Try again.")
        return None
    password = input("Enter a new password: ").strip()
    users[username] = {
        'password': password,
        'coin': 0,
        'xp': 0,
        'health': 100,
        'total_health': 100,
        'attack': 10,
        'defense': 5,
        'inventory': {}
    }
    save_user_data(users)
    print("Registration successful!")
    return username

def login():
    users = load_user_data()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]['password'] == password:
        print(f"Login successful! Welcome, {username}!")
        return username
    else:
        print("Invalid username or password.")
        return None

def delete_user(username):
    users = load_user_data()
    if username in users:
        confirm = input(f"Are you sure you want to delete the user {username}? (yes/no): ")
        if confirm.lower() == 'yes':
            del users[username]
            save_user_data(users)
            print(f"User {username} has been deleted.")
        else:
            print("User deletion cancelled.")
    else:
        print("User not found.")
