import random
import time

def displayIntro():
    print("""You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly
and will share his treasures with you. The other dragon is greedy and hungry and will eat you up on sight. """)
print()

def ChooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into (1 or 2)?")
        cave = input()
        return cave
def CheckCave(ChosenCave):
    print("You approach the cave...\n")
    time.sleep(1)
    print("It is cold, dark and spooky...\n")
    time.sleep(2)
    print("Skulls of animals litter the crevice of the cave. Taking two steps into the cave...\n")
    time.sleep(4)
    print("A large dragon jumps out in front of you! He opens his jaws and...\n")
    print()
    time.sleep(4)

    FriendlyCave = random.randint(1, 2)

    if ChosenCave == str(FriendlyCave):
        print("Gives you his treasures!Wow!That's awesome.\n")
    else:
        print("Gobbles you down in one bite! Buuuurp! He belges.\n"
              "This is a delicious meal.\n")

PlayAgain = "yes"
while PlayAgain == "yes" or PlayAgain == "y":
    displayIntro()
    CaveNumber = ChooseCave()
    CheckCave(CaveNumber)

    print("Do you want to play again? (yes or no)")
    PlayAgain = input()

