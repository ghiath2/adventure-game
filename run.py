# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import sys
import os
import random
import time


class Game:

    def print_slow(self, str, delay=0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")


    def reset_console(self):
        print("\n")
        os.system('cls||clear')


    def fprint(self, str, delay=0):
        print("\n" + str)
        time.sleep(delay)


    def sprint(self, str, delay=0):
        print(str)
        time.sleep(delay)


player = {"location":"", "health":100, "items":[]}


class NPC:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        game_functions.fprint(f"A {self.name} emerges from the shadows.")
        game_functions.fprint("'Hisssss! Stay away from me!'")

    def move(self):
        available_locations = ["entry", "cavern", "hallway", "pit"]
        self.location = random.choice(available_locations)


goblin = NPC("goblin", "hallway")


def entry():
    player["location" = "entry"]
    print(f"\nHealth: {health}")
    fprint("You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out.", 2)
    print("Ahead, you can see a cavern. Will you continue?")
    print("Enter 'yes' or 'no' .")
    check_medkit()
        handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            cavern()
        elif action == "no":
            fprint("A bat flies over your head and you hear screetches in the distance.")
        elif action == "m":
        use_medkit()
        else:
            fprint("You sit in total darkness wondering if there's a way out.")


def cavern():
    player["location" = "entry"]
    print(f"\nHealth: {health}")
    fprint("You stumble into a dimly lit cavern", 2)
    print("You cannot go right or left but the cave continues ahead. Will you go on")
    print("Enter 'yes' or 'no' .")
    bat_attack = random.choice([True,False])
    if bat_attack == True:
        fprint("You were attacked by a bat!",2)
        health -= random.randint(1,100)
        print(f"\nHealth: {health}")
        if health == 0:
            fprint("You are dead!")
            sys.exit()
    handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            hallway()
        elif action == "no":
            fprint("You sit down and eat some food you brought with you.")
            elif action == "m":
            use_medkit()
        else:
            fprint("You shiver from the cold.")


def hallway():
    player["location" = "entry"]
    print(f"\nHealth: {health}")
    fprint("You are in a wide hallway. It continues on indefinitely", 2)
    print("There's no turning back. Will you go on?")
    print("Enter 'yes' or 'no' .")
    handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            pit()
        elif action == "no":
            fprint("You try to call your help but no one is there.")
            elif action == "m":
            use_medkit()
        else:
            fprint("You wonder what time it is.")


def pit():
    player["location" = "entry"]
    print(f"\nHealth: {health}")
    fprint("You fall head first into an ominous and languid pit.", 2)
    sprint("Luckly, you only landed on your back.", 2)
    print("You can try to climb out. Will you try?")
    print("Enter 'yes' or 'no' .")
    handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            fprint("You try to climb out but you slide off of the rocky wall and fall down again.", 2)
            print("GAME OVER.")
        elif action == "no":
            fprint("You sit in utter darkness.")
            elif action == "m":
            use_medkit()

        else:
            fprint("You feel hopeless.")


def use_medkit(self):
        if "medkit" in hero.items:
            hero.items.remove("medkit")
            game_functions.fprint("You used your medkit")
            hero.health = 100
            print(f"\nHealth: {hero.health}")
        else:
            game_functions.fprint("You don't have a medkit.")


def handle_goblin(self):
        goblin.move()
        if hero.location == goblin.location:
            goblin.talk()



 def check_medkit(self):
        medkit_find = random.choice([True, False])
        if medkit_find is True:
            hero.items.append("medkit")
            game_functions.fprint("You found a medkit!", 2)
            print("Enter 'm' to use it.")

            
