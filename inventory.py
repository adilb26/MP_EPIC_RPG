from utils import item_emojis

def view_inventory(user):
    if not user['inventory']:
        print("Your inventory is empty.")
    else:
        print("\n")
        print("--------------------------------------------------")
        print("Inventory:")
        for item, qty in user['inventory'].items():
            print(f"{item_emojis.get(item, '')} {item}: {qty}")
        print("--------------------------------------------------")
        print("\n")