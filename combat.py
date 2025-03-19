import random
from user import save_user_data
from utils import item_emojis

def rpg_hunt(level, user):
    events = [
        {"creature": "Goblin", "coins": (1, 5), "xp": (5, 10), "hp_loss": (1, 2), "items": ["Rusty Dagger", "Torn Pouch", "Small Gem"]},
        {"creature": "Wolf", "coins": (3, 6), "xp": (8, 12), "hp_loss": (2, 3), "items": ["Wolf Fang", "Tattered Hide", "Cracked Fang"]},
        {"creature": "Golem", "coins": (7, 12), "xp": (18, 22), "hp_loss": (4, 5), "items": ["Cracked Stone", "Magic Core", "Heavy Rock"]},
    ]
    
    if level < 1 or level > len(events):
        print("Invalid level. Please choose a valid level.")
        return
    
    event = events[level - 1]
    coins = random.randint(*event["coins"])
    xp_gain = random.randint(*event["xp"])
    hp_loss = random.randint(*event["hp_loss"])
    item = random.choice(event["items"])

    user['coin'] += coins
    user['xp'] += xp_gain
    user['health'] -= hp_loss
    if item in user['inventory']:
        user['inventory'][item] += 1
    else:
        user['inventory'][item] = 1
    print("\n")
    print("--------------------------------------------------")
    print(f"⚔️ Encountered a {event['creature']}!")
    print(f"💔 Lost {hp_loss} health.")
    print(f"⭐ Gained {xp_gain} XP.")
    print(f"💰 Earned {coins} coins.")
    print(f"📦 Found: {item_emojis[item]} {item}")
    
    if user['health'] <= 0:
        if user['inventory'].get("Life Potion", 0) > 0:
            print("🩸 You are critically wounded! Do you want to use a Life Potion to restore your health? (yes/no)")
            choice = input("➡️ ").strip().lower()

            if choice == "yes":
                user['health'] = user['total_health']
                user['inventory']['Life Potion'] -= 1
                print("✨ You used a Life Potion and fully restored your health!")
            else:
                print("💀 You have been defeated and lost all your XP.")
                user['xp'] = 0
        else:
            print("💀 You have been defeated and lost all your XP.")
            user['xp'] = 0

    print(f"❤️ Health: {user['health']}/{user['total_health']}")
    print("--------------------------------------------------")

def rpg_adventure(level, user):
    adventure_creatures = [
        {"name": "Ancient Dragon", "hp": 250, "attack": 30, "reward": 100, "xp": 75, "emoji": "🐉"},
        {"name": "Dark Titan", "hp": 300, "attack": 35, "reward": 150, "xp": 100, "emoji": "🗿"},
        {"name": "Demonic Hydra", "hp": 400, "attack": 45, "reward": 200, "xp": 150, "emoji": "🐍"}
    ]
    
    creature = random.choice(adventure_creatures)
    print("\n")
    print("--------------------------------------------------")
    print(f"You encountered {creature['emoji']} {creature['name']}! Prepare for battle!")
    
    user_damage = random.randint(20, 40)
    user["health"] -= user_damage
    
    if user["health"] <= 0:
        print("You were defeated in the adventure! You barely escape with your life.")
        user["health"] = 10
    else:
        print(f"You survived and defeated {creature['emoji']} {creature['name']}!")
        user["coin"] += creature["reward"]
        user["xp"] += creature["xp"]
        print(f"You earned {creature['reward']} coins and {creature['xp']} XP!")
    print("--------------------------------------------------")
    
    save_user_data(user)

def rpg_chop(user):
    Wood = ["🪵 Oak Log", "🪵 Pine Log", "🪵 Birch Log", "🪵 Maple Log"]
    Wood_Choice = random.choice(Wood)
    
    if Wood_Choice in user['inventory']:
        user['inventory'][Wood_Choice] += 1
    else:
        user['inventory'][Wood_Choice] = 1
    
    print("\n")
    print("--------------------------------------------------")
    print(f"🪓 You chopped down a tree and obtained: {Wood_Choice}")
    print("--------------------------------------------------")
    
    save_user_data(user)

def reward(user):
    coins_reward = random.randint(100, 600)
    life_potion_reward = random.randint(2, 20)
        
    user['coin'] += coins_reward
    if 'Life Potion' in user['inventory']:
        user['inventory']['Life Potion'] += life_potion_reward
    else:
        user['inventory']['Life Potion'] = life_potion_reward
        
    print("\n")
    print("--------------------------------------------------")
    print(f"🎁 You received a reward!")
    print(f"💰 Coins: {coins_reward}")
    print(f"🧪 Life Potions: {life_potion_reward}")
    print("--------------------------------------------------")
        
    save_user_data(user)
