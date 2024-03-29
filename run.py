"""
Imported libraries supporting the application
"""
import sys  # To provide the user with an exit from the ordering system
import os
import random  # To create sequential order references
import time  # To add a pause between certain functions executing


class Game:
    # define function to slow down
    def print_slow(self, str, delay=0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")

    # define function to reset the console
    def reset_console(self):
        print("\n")
        os.system('cls||clear')

    # define function to print in a different way
    def fprint(self, str, delay=0):
        print("\n" + str)
        time.sleep(delay)

    # define function to print in a different way
    def sprint(self, str, delay=0):
        print(str)
        time.sleep(delay)


game_functions = Game()


class player:
    def __init__(self, location, health, items):
        self.location = location
        self.health = health
        self.items = items


hero = player("entry", 100, [])


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


class World:

    def entry(self):
        """
        Function will show the situation and give
        multiple choices and ask the player if they wish
        to continue or not
        """
        hero.location = "entry"
        #  Shows the health
        print(f"\nHealth: {hero.health}")
        game_functions.fprint(
            "You are in a dark cave." +
            "The entry has been sealed by fallen rocks." +
            "There is no way out.", 2)
        print("Ahead, you can see a cavern. Will you continue?")
        print("Enter 'yes' or 'no'.")
        self.check_medkit()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.cavern()
            elif action == "no":
                #  Appears when no is chosen
                game_functions.fprint(
                    "A bat flies over your head and" +
                    "you hear screetches in the distance.")
            elif action == "m":
                #  Gives a choice to use med kit
                self.use_medkit()
            else:
                game_functions.fprint(
                    "You sit in total darkness" +
                    "wondering if there's a way out.")

    def cavern(self):
        """
        Function will show the next level and give
        multiple choices and ask the player if they wish
        to continue or not
        """
        hero.location = "cavern"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You stumble into a dimly lit cavern.", 2)
        print(
            "You cannot go right or left but" +
            " the cave continues ahead. Will you go on?")
        print("Enter 'yes' or 'no'.")
        #  Shows when ansewr is no
        self.check_bat_attack()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.hallway()
            elif action == "no":
                game_functions.fprint(
                    "You sit down and eat some" +
                    "food you brought with you.")
            elif action == "m":
                #  Asks to use midkit
                self.use_medkit()
            else:
                game_functions.fprint("You shiver from the cold.")

    def hallway(self):
        """
        Function will show the next level and give
        multiple choices and ask the player if they wish
        to continue or not
        """
        hero.location = "hallway"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint(
            "You are in a wide hallway." +
            " It continues on indefinitely.", 2)
        print("There's no turning back. Will you go on?")
        print("Enter 'yes' or 'no'.")
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.pit()
            elif action == "no":
                # when answer is no
                game_functions.fprint(
                    "You try to call your help" +
                    "but no one is there.")
            elif action == "m":
                #  Asks to use midkit
                self.use_medkit()
            else:
                game_functions.fprint("You wonder what time it is.")

    def pit(self):
        """
        Function will show the next level and give
        multiple choices and ask the player if they wish
        to continue or not
        """
        hero.location = "pit"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint(
            "You fall head first into" +
            "an ominous and languid pit.", 2)
        game_functions.sprint("Luckly, you only landed on your back.", 2)
        print("You can try to climb out. Will you try?")
        print("Enter 'yes' or 'no'.")
        self.handle_goblin()
        while True:
            action = input("\n> ")
            #  if yes print game over
            if action == "yes":
                game_functions.fprint(
                    "You try to climb out but you slide off of" +
                    "the rocky wall and fall down again.", 2)
                print("GAME OVER.")
                sys.exit()
            elif action == "no":
                game_functions.fprint("You sit in utter darkness.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You feel hopeless.")

    def use_medkit(self):
        """
        Function will show the midkit choice randomly
        when use it will refresh the health
        """
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

    #  shows the midkit messege randomly
    def check_medkit(self):
        medkit_find = random.choice([True, False])
        if medkit_find is True:
            hero.items.append("medkit")
            game_functions.fprint("You found a medkit!", 2)
            print("Enter 'm' to use it.")

    def check_bat_attack(self):
        bat_attack = random.choice([True, False])
        if bat_attack is True:
            game_functions.fprint("You were attacked by a bat!", 2)
            hero.health -= random.randint(1, 100)
            print(f"\nHealth: {hero.health}")
            if hero.health == 0:
                game_functions.fprint("You are dead!")
                sys.exit()


new_world = World()


new_world.entry()
