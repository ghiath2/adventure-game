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

def entry():
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
    pass


def hallway():
    pass


def pit():
    pass
