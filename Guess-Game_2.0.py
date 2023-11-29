import time, pyfiglet

secret_word = "Mighty"
user_guess = ""
guess_count = 0
guess_limit = 10
out_of_guesses = False
hint = "The name of the game dev."

logo = pyfiglet.figlet_format('Brain Matters 1.0', font = 'digital')
print(logo)
"""
print("\n'GUESS ME' \nBrain matters.\n")
print("  *  *   *  *  ")
print("  *         * ")
print("   *       * ")
print("    *     * ")
print("      *** ")
"""
# I was initially trying to make sure I create a logo for the Guess Me game. This is all I can think of for now.
# I was trying to illustrate a bulb that lights up when you have an idea about something.

print("This is a fun and addictive game designed to test your reasoning capability.\n ")
print("This is just a beginner level so expect easy words like...(kidding). Don't say I never warned you though!\nEnough talk,"
      "let's go on fellas.\n")
print("Level One\n")

while user_guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        user_guess = input("Enter a guess word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if user_guess != secret_word:
    print(hint)

if user_guess == secret_word:
    print("EUREKA! YOU GUESSED THE SECRET WORD.\nThat was so smart of you.\n")
    print("Let's progress to the next level.")

else:
    print("Game Over")
    #print(hint)

"""
You can also use the lines of code below. I just wanna deviate a bit from the lesson. 
if out_of_guesses:
    print("You lose!")
    print(hint)
else:
    print("You win!")
"""
time.sleep(3)

print()
print()
if user_guess == secret_word:
    secret_word = "cattle"
    user_guess = ""
    guess_count = 0
    guess_limit = 6
    out_of_guesses = False
    hint = "It is a work animal."

'''
print("GUESS ME \nBrain matters.\n")
print("  *  *   *  *  ")
print("  *         * ")
print("   *       * ")
print("    *     * ")
print("      *** ")
'''
# I was initially trying to make sure I create a logo for the Guess Me game. This is all I can think of for now.
# I was trying to illustrate a bulb that lights up when you have an idea about something.

#print("This is a fun and addictive game designed to test your reasoning capability.\n ")
print("Level Two\n")
#print("This is just a beginner level so expect easy words like... Don't say I never warned you enough!\nEnough talk, let's go on fellas.\n")
while user_guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        user_guess = input("Enter a guess word: ")
        guess_count += 1
    else:
        out_of_guesses = True


if user_guess != secret_word:

    print(hint)


if user_guess == secret_word:
    print("EUREKA! YOU GUESSED THE SECRET WORD.\nThat was so smart of you.\n")
    print("Thanks for playing.")
else:
    print("You lose!")
    #print(hint)


"""
You can also use the lines of code below. I just wanna deviate a bit from the lesson. 
if out_of_guesses:
    print("You lose!")
    print(hint)
else:
    print("You win!")
"""
time.sleep(2)
