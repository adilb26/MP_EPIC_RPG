from utils import item_emojis

def store(user):
    print("\n")
    print("--------------------------------------------------")
    items = {"1": ("Basic Armour", 200), "2": ("Sword", 300), "3": ("Golden Apples", 5000), "4": ("Life Potion", 20)}

    print("Store:")
    print(f"💰 Coins: {user['coin']}")
    for number, (item, cost) in items.items():
        print(f"{number}. {item_emojis[item]} {item}: {cost} coins")

    print("--------------------------------------------------")
    choice = input("Enter item number to buy: ").strip()
    if choice not in items:
        print("Invalid choice.")
        return

    item, cost = items[choice]
    if item == "Life Potion":
        quantity = int(input("Enter quantity of Life Potions to buy: ").strip())
        total_cost = cost * quantity
        if user['coin'] < total_cost:
            print("Insufficient coins.")
            return
        user['coin'] -= total_cost
        user['inventory'][item] = user['inventory'].get(item, 0) + quantity
        print(f"Bought {quantity} Life Potions.")
        
    else:
        quantity = 1
        total_cost = cost * quantity
        if user['coin'] < total_cost:
            print("Insufficient coins.")
            return
        user['coin'] -= total_cost
        user['inventory'][item] = user['inventory'].get(item, 0) + quantity
        print(f"Bought {item}.")