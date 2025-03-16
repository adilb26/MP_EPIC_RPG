from utils import get_level

def view_profile(user):
    print("--------------------------------------------------")
    print(f"👤 {user['username']}")
    print(f"⭐ Level: {get_level(user['xp'])}")
    print(f"⚔️ Attack: {user['attack']} | 🛡️ Defense: {user['defense']}")
    print(f"❤️ {user['health']}/{user['total_health']} | 💰 Coins: {user['coin']} | 📈 XP: {user['xp']}")
    print("--------------------------------------------------")
