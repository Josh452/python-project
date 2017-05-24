import sys
import os
from core import icore

def end():
        exit = input("Do you want to exit? y or n \n")
        no = "n" or "N"
        yes = "y" or "N"
        if exit==no:
            print("-Info- Restarting")
            ibot()

        if exit==yes:
            print ("-Info- Exiting")
            sys.exit
        else:
            print("-Info- Not valid input")
            end()

def ibot():
    icore.start()
    icore.yn("are you haveing a good day?", "Thats good to hear", "Damn thats not too good. I am sure u will have a better one temmrow.")
    icore.yn("Are you cool?", "Yep!!", "Nah your cool")
    icore.type("What is your job.", "Thats cool, I have always wanted to a", "!")
    icore.type("Who is your best friend?", "Wow! they sound cool! I like the name", " :)")
    icore.type("When is your birthday?", "Lit! Always wanted my birthday to be in", "!")
    icore.yn("Do you like memes?", "You are a lit person", "You sould try them!")
    icore.type("What school do you do to?", "Woah! ", ", What a lit school")
    icore.type("are you a pc or xbox gamer?", "Meh.. I guess the are all ok.. but", " you can do better")
    icore.yn("Are you in our class", "Woah you are cooooool", "Next time ;)")

ibot()
end()
