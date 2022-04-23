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


health = 100


def entry():
    global health
    print(f"\nHealth: {health}")
    fprint("You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out.", 2)
    print("Ahead, you can see a cavern. Will you continue?")
    while True:
        action = input("\n> ")
        if action == "yes":
            cavern()
        elif action == "no":
            fprint("A bat flies over your head and you hear screetches in the distance.")
        else:
            fprint("You sit in total darkness wondering if there's a way out.")


def cavern():
    global health
    print(f"\nHealth: {health}")
    bat_attack = random.choice([True,False])
    if bat_attack == True:
        fprint("You were attacked by a bat!",2)
        health -= random.randint(1,100)
        if health == 0:
            fprint("You are dead!")
            sys.exit()

    fprint("You stumble into a dimly lit cavern", 2)
    print("You cannot go right or left but the cave continues ahead. Will you go on")
    while True:
        action = input("\n> ")
        if action == "yes":
            hallway()
        elif action == "no":
            fprint("You sit down and eat some food you brought with you.")
        else:
            fprint("You shiver from the cold.")


def hallway():
    global health
    print(f"\nHealth: {health}")
    fprint("You are in a wide hallway. It continues on indefinitely", 2)
    print("There's no turning back. Will you go on?")
    while True:
        action = input("\n> ")
        if action == "yes":
            pit()
        elif action == "no":
            fprint("You try to call your help but no one is there.")
        else:
            fprint("You wonder what time it is.")


def pit():
    global health
    print(f"\nHealth: {health}")
    fprint("You fall head first into an ominous and languid pit.", 2)
    sprint("Luckly, you only landed on your back.", 2)
    print("You can try to climb out. Will you try?")
    while True:
        action = input("\n> ")
        if action == "yes":
            fprint("You try to climb out but you slide off of the rocky wall and fall down again.", 2)
            print("GAME OVER.")
        elif action == "no":
            fprint("You sit in utter darkness.")
        else:
            fprint("You feel hopeless.")

            
