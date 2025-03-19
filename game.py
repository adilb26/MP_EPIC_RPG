import time
from user import load_user_data, save_user_data, register, login, delete_user
from combat import rpg_hunt, rpg_adventure, rpg_chop, reward
from inventory import view_inventory
from profile import view_profile
from store import store
from utils import get_level, item_emojis

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

    last_hunt_time = 0
    last_adventure_time = 0
    last_chop_time = 0
    last_reward_time = 0

    while True:
        print("\nMenu:")
        print(f"1. {item_emojis['Hunt']} Hunt")
        print(f"2. {item_emojis['Adventure']} Adventure")
        print(f"3. {item_emojis['Heal using Life Potion']} Heal using Life Potion")
        print(f"4. {item_emojis['View Inventory']} View Inventory")
        print(f"5. {item_emojis['View Profile']} View Profile")
        print(f"6. {item_emojis['Store']} Store")
        print(f"7. {item_emojis['Chop_woods']} Chop Wood")
        print(f"8. {item_emojis['Reward']} Reward")
        print(f"9. {item_emojis['Delete User']} Delete User")
        print(f"10. {item_emojis['Exit']} Exit")
        choice = input("Enter your choice: ")

        current_time = time.time()

        if choice == '1':
            if current_time - last_hunt_time >= 10:
                level = get_level(current_user['xp'])
                if current_user['health'] > 0:
                    rpg_hunt(level, current_user)
                    if current_user['health'] <= 0:
                        print("You have no health left. Game over.")
                        break
                    save_user_data(users)
                    last_hunt_time = current_time
            else:
                print("Hunt is on cooldown. Please wait a few seconds.")
        elif choice == '2':
            if current_time - last_adventure_time >= 30:
                level = get_level(current_user['xp'])
                if current_user['health'] > 0:
                    rpg_adventure(level, current_user)
                    save_user_data(users)
                    last_adventure_time = current_time
                else:
                    print("You don't have enough health for an adventure.")
            else:
                print("Adventure is on cooldown. Please wait a few seconds.")
        elif choice == '3':
            if current_user['health'] == current_user['total_health']:
                print("You already have full health. You cannot use the Life Potion.")
            elif 'Life Potion' in current_user['inventory'] and current_user['inventory']['Life Potion'] > 0:
                current_user['health'] = current_user['total_health']
                current_user['inventory']['Life Potion'] -= 1
                print("You have been healed to full health.")
                save_user_data(users)
            else:
                print("You don't have any Life Potions.")
        elif choice == '4':
            view_inventory(current_user)
        elif choice == '5':
            view_profile(current_user)
        elif choice == '6':
            store(current_user)
            save_user_data(users)
        elif choice == '7':
            if current_time - last_chop_time >= 20:
                rpg_chop(current_user)
                save_user_data(users)
                last_chop_time = current_time
            else:
                print("Chop Wood is on cooldown. Please wait a few seconds.")
        elif choice == '8':
            if current_time - last_reward_time >= 20:
                reward(current_user)
                save_user_data(users)
                last_reward_time = current_time
            else:
                print("Reward is on cooldown. Please wait a few seconds.")
        elif choice == '9':
            delete_user(user)
            break
        elif choice == '10':
            print("Exiting the game.")
            save_user_data(users)
            break
        else:
            print("Invalid choice. Please enter a valid option.")