import random
from utils import item_emojis

def rpg_hunt(level, user):
    total_health = user['health']
    
    events = [
        {"creature": "Goblin", "coins": (1, 5), "xp": (5, 10), "hp_loss": (1, 2), "items": ["Rusty Dagger", "Torn Pouch", "Small Gem"]},
        {"creature": "Wolf", "coins": (3, 6), "xp": (8, 12), "hp_loss": (2, 3), "items": ["Wolf Fang", "Tattered Hide", "Cracked Fang"]},
        {"creature": "Golem", "coins": (7, 12), "xp": (18, 22), "hp_loss": (4, 5), "items": ["Cracked Stone", "Magic Core", "Heavy Rock"]},
    ]
    
    event = events[level - 1]
    coins = random.randint(*event["coins"])
    xp_gain = random.randint(*event["xp"])
    hp_loss = random.randint(*event["hp_loss"])
    item = random.choice(event["items"])

    user['coin'] += coins
    user['xp'] += xp_gain
    user['health'] -= hp_loss  # ✅ Decrease only current health
    if item in user['inventory']:
        user['inventory'][item] += 1
    else:
        user['inventory'][item] = 1

    print(f"⚔️ Encountered a {event['creature']}!")
    print(f"💔 Lost {hp_loss} health.")
    print(f"⭐ Gained {xp_gain} XP.")
    print(f"💰 Earned {coins} coins.")
    print(f"📦 Found: {item_emojis[item]} {item}")
    
    # Check if health is 0 and allow using Life Potion
    if user['health'] <= 0:
        if user['inventory'].get("Life Potion", 0) > 0:
            print("🩸 You are critically wounded! Do you want to use a Life Potion to restore your health? (yes/no)")
            choice = input("➡️ ").strip().lower()

            if choice == "yes":
                user['health'] = user['total_health']  # Restore to max health
                user['inventory']['Life Potion'] -= 1  # Reduce potion count
                print("✨ You used a Life Potion and fully restored your health!")
            else:
                print("💀 You have been defeated and lost all your XP.")
                user['xp'] = 0  # Reset XP on defeat
        else:
            print("💀 You have been defeated and lost all your XP.")
            user['xp'] = 0  # Reset XP on defeat

    print(f"❤️ Health: {user['health']}/{user['total_health']}")
    print("-----------------")
