from user import load_user_data, save_user_data, register, login, delete_user
from combat import rpg_hunt
from inventory import view_inventory
from profile import view_profile
from store import store
from utils import get_level

def start_game():
    user = None
    while user is None:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        choice = input("Enter your choice: ")

        if choice == '1':
            user = register()
        elif choice == '2':
            user = login()
        else:
            print("Invalid choice. Please enter 1 or 2.")

    users = load_user_data()
    current_user = users[user]
    current_user['username'] = user

    while True:
        print("\nMenu:")
        print("1. Hunt")
        print("2. View Inventory")
        print("3. View Profile")
        print("4. Store")
        print("5. Delete User")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            level = get_level(current_user['xp'])
            if current_user['health'] > 0:
                rpg_hunt(level, current_user)
                if current_user['health'] <= 0:
                    print("You have no health left. Game over.")
                    break
                save_user_data(users)
        elif choice == '2':
            view_inventory(current_user)
        elif choice == '3':
            view_profile(current_user)
        elif choice == '4':
            store(current_user)
            save_user_data(users)
        elif choice == '5':
            delete_user(user)
            break
        elif choice == '6':
            print("Exiting the game.")
            save_user_data(users)
            break
        else:
            print("Invalid choice. Please enter a valid option.")
