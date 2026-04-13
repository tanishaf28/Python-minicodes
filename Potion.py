import random

# Player setup
name = input("Enter your name, adventurer: ")
player_hp = 40
inventory = {"potions": 2}
level = 1

print(f"\nWelcome, {name}! Your adventure begins...\n")

# Function to fight enemies
def battle(enemy_name, enemy_hp, enemy_min, enemy_max):
    global player_hp

    print(f"\n⚔️ You encountered a {enemy_name}!")

    while player_hp > 0 and enemy_hp > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Run")

        choice = input("Choose (1/2/3): ")

        if choice == "1":
            damage = random.randint(6, 12)
            enemy_hp -= damage
            print(f"You dealt {damage} damage to the {enemy_name}!")

        elif choice == "2":
            if inventory["potions"] > 0:
                heal = random.randint(8, 15)
                player_hp += heal
                inventory["potions"] -= 1
                print(f"You used a potion and healed {heal} HP!")
                print(f"Potions left: {inventory['potions']}")
            else:
                print("No potions left!")
                continue

        elif choice == "3":
            print("You escaped!")
            return False

        else:
            print("Invalid choice.")
            continue

        if enemy_hp <= 0:
            print(f"\n🎉 You defeated the {enemy_name}!")
            return True

        # Enemy turn
        enemy_damage = random.randint(enemy_min, enemy_max)
        player_hp -= enemy_damage
        print(f"The {enemy_name} hit you for {enemy_damage} damage!")

        print(f"\nYour HP: {player_hp}")
        print(f"{enemy_name} HP: {enemy_hp}")

    return player_hp > 0


# --- STORY START ---
print("You stand at a crossroad...")
print("1. Go LEFT into a dark forest 🌲")
print("2. Go RIGHT toward the mountains ⛰️")

path = input("Choose your path (1/2): ")

# --- LEFT PATH ---
if path == "1":
    print("\nYou walk into the forest... it's quiet... too quiet.")

    won = battle("Goblin 🧌", 25, 3, 8)

    if not won:
        print("\nGame Over!")
    else:
        level += 1
        print(f"\n✨ You leveled up! Level: {level}")
        inventory["potions"] += 1
        print("You found a potion!")

        print("\nA huge shadow appears... it's a DRAGON 🐉!")

        won = battle("Dragon 🐉", 40, 6, 12)

        if won:
            print("\n🏆 You defeated the Dragon and became a legend!")
        else:
            print("\n💀 The Dragon defeated you...")

# --- RIGHT PATH ---
elif path == "2":
    print("\nYou climb the mountains and find a treasure chest!")

    inventory["potions"] += 2
    print("🎒 You found 2 potions!")

    print("\nA Goblin ambushes you!")

    won = battle("Goblin 🧌", 20, 2, 6)

    if not won:
        print("\nGame Over!")
    else:
        level += 1
        print(f"\n✨ You leveled up! Level: {level}")

        print("\nAt the peak... a DRAGON awaits you 🐉!")

        won = battle("Dragon 🐉", 45, 7, 13)

        if won:
            print("\n🏆 You conquered the mountain and defeated the Dragon!")
        else:
            print("\n💀 The Dragon was too powerful...")

else:
    print("You got lost... Game Over!")

print("\nThanks for playing!")
