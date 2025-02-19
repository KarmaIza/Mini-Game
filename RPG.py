from colorama import init, Fore, Back, Style
init()
import random

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Enemy Class
class Enemy:
    def __init__(self, name, hp, attack, level):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.level = level
        self.max_hp = hp

    def is_alive(self):
        return self.hp > 0

    def attack_player(self):
        return random.randint(self.attack-1, self.attack+1)

    def reset_hp(self):
        self.hp = self.max_hp

    def show_status(self):
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")

# Enemies
WOLF = Enemy("Wolf", 20, 5, 1)
ORC = Enemy("Orc", 30, 10, 2)
TROLL = Enemy("Troll", 50, 20, 3)

random_enemy = random.choice([WOLF, ORC, TROLL])

# Player Statistics
name = "Karma"
level = 1 
hp = 100
attack = 10
gold = 0
exp = 0
max_hp = hp

# Actions
actions = [
    "stats",
    "rest",
    "fight",
]

def show_status():
    print(f"Name: {YELLOW}{name}{RESET}")
    print(f"Level: {BLUE}{level}{RESET}")
    print(f"HP: {GREEN}{hp}/{max_hp}{RESET}")
    print(f"Attack: {RED}{attack}{RESET}")
    print(f"Gold: {YELLOW}{gold}{RESET}")
    print(f"Experience: {BLUE}{exp}{RESET}")

def fight(enemy):
    global hp, gold, level
    enemy.reset_hp()
    print(f"{RED}A {enemy.name} appears!{RESET}")
    
    while enemy.is_alive() and hp > 0:
        print(f"\n{GREEN}Your HP: {hp}{RESET}")
        print(f"{RED}Enemy HP: {enemy.hp}{RESET}")
        
        # Player attacks
        damage = random.randint(attack-3, attack+3)
        enemy.hp -= damage
        print(f"{YELLOW}You deal {damage} damage!{RESET}")
        
        if not enemy.is_alive():
            gold_reward = enemy.level * 10
            exp_reward = enemy.level * 20
            gold += gold_reward
            gain_experience(exp_reward)
            print(f"{GREEN}You won! Got {gold_reward} gold!{RESET}")
            return True
            
        # Enemy attacks
        damage = enemy.attack_player()
        hp -= damage
        print(f"{RED}Enemy deals {damage} damage!{RESET}")

# Actions Functions
def train():
    global attack
    attack += 2
    print(f"{RED}You trained and increased your attack to {attack}{RESET}")

def rest():
    global hp
    if hp == max_hp:
        print(f"{RED}You are already at full health!{RESET}")
        return
    hp = max_hp
    print(f"{GREEN}You rested and increased your hp to {hp}{RESET}")

def gain_experience(amount):
    global level, hp, max_hp, attack, exp
    exp_needed = level * 100

# Experience needed to level up
    exp += amount
    print(f"{YELLOW}You gained {amount} experience!{RESET}")

    if exp >= exp_needed:
        level += 1
        exp -= exp_needed
        max_hp += 10
        hp = max_hp
        attack += 2
        print(f"{BLUE}You leveled up! You reached Level {level}{RESET}")
        print(f"{GREEN}HP: {hp}{RESET}")
        print(f"{RED}Attack: {attack}{RESET}")
        exp_needed = level * 100
        print(f"{YELLOW}Experience needed to level up: {exp_needed}{RESET}")

# Main Program
def main():
    while True:
        if hp <= 0:
            print(f"{RED}You died!{RESET}")
            break
        print("\nWhat do you want to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")

        try: 
            choice = int(input(f"{BLUE}Choose a number{RESET}"))
            if choice == 1:
                show_status()
            elif choice == 2:
                rest()
            elif choice == 3:
                fight(random_enemy)
            else:
                print(f"{RED}Invalid input!{RESET}")
        except ValueError:
            print("Please enter a number!")

if __name__ == "__main__":
    import random
    main()
