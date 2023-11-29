import random

guesses_taken = 0
player_name = input("What is your name? ")
print("Welcome " + player_name + "." + " Can you guess the number I have in mind which is between 20 and 100?")


number = random.randint(20, 100)

try:
    for guesses_taken in range(10): # You can also decide to neglect using the 'guesses_taken' variable here but
        #you would have to make sure you change some things in the code beneath this.
        guess = int(input("Take a guess: "))
        #guesses_taken += 1
        if guess < number:
            print("Your guess is too low.")

        if guess > number:
            print("Your guess is too high.")

        if guess == number:
            break

    if guess == number:
        guesses_taken = str(guesses_taken + 1)
        #The above line of code can actually be used but I would prefer my things my way.
        print("Well done " + player_name + ", that was actually smart of you." + " You guessed my number right in " +
        guesses_taken + " guesses.") #The 'str' in 'str(guesses_taken) can be omitted if the line of code commented
        #out above was used.

    if guess != number:
        print("Oh no! You were unable to guess my number correctly." + " The number I was thinking of was " + str(number) + ".")
except SyntaxError as err:
    print(err)

except ValueError as error:
    print("Invalid Input!")
