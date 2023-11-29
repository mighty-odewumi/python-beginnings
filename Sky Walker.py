import time


print("SKY WALKER")
print("       \\\       ")
print(  "        \\\     ")
print( "   <<<<<<<<<<<<<<<    ")
print( "  <               >")
print("<                  >")
print("<                  >")
print("  <               >")
print( "   <<<<<<<<<<<<<<<   ")
print("Prepare to battle alien forces!")
print()

player_name = input("Enter your name: ")
if player_name == "" or player_name == " ":
    print("Please, enter a valid name.")
else:
    print("Hello " + player_name + "\n")

    print("I am Alex, the Loop's digital computer system.\n")
    time.sleep(3)
    print("Alien forces have laid siege on Earth.\n")
    time.sleep(3)

    print("A team of fighters has been assembled to battle these forces.\n")
    time.sleep(4)
    print("Are you ready to defend Earth against invaders?\n")
    time.sleep(4)

    response = input("What is your decision? (Yes or No): ")
    if response == "yes" or response == "y" or response == "Yes" or response == "Y":
        for i in range(0, 1):
            print("\nThank you " + player_name + "." " You may proceed to the arsenal.\n")
            time.sleep(4)

        arsenal = ["Grenade", "Ion Collider", "Plasma Saber", "Beretta", "Glock"]
        print(arsenal)
        #print("Please, ensure you pick the right weapons and check your inventory.\n")
        #inventory = input("Select your weapons " + player_name + ":")

        #print("\nThis is your inventory: " + inventory + "\n")
        time.sleep(6)
        print()

        print("Transport takes off in 5 minutes. Proceed to Station 2.\n")
        time.sleep(5)

        print("You've been assigned to a team led by Captain Jason.")
        time.sleep(4)
        print()

        print("Player's Thoughts:" + " Doing a short jog to the vessel, I ground to a halt as I saw the beast in\n"
              "front of me. My jaw drops looking at the devilish beauty.\n"
              "Taking a look around it,I can count 10 antimissile systems. It also has 15 rail guns. I think\n"
              "the vessel\n"
              "is going to have a large crew with automation. I must agree that it is a mammoth of a craft.\n")
        time.sleep(20)

        print("Captain Jason: Welcome everyone.")
        print()
        time.sleep(3)

        print("I personally handpicked this crew and I am looking forward to working with you all.")
        print()
        time.sleep(5)

        print("The fate of Earth rests on the shoulders of everyone here.")
        print()
        time.sleep(6)

        print("I want you all to give this mission your best and remember, Earth must not fall.")
        print()
        time.sleep(6)

        print("Think of everyone you've got. Friends and family who you cherish and cherish you.")
        print()
        time.sleep(6)

        print("We must ensure the enemies realize they have stirred the hornet's nest and must be prepared to face\n"
              "the consequences.\n")
        print()
        time.sleep(6)

        print("Player's Thoughts: Boarding the craft, I felt a feeling of uneasiness. Heading into battle against\n"
              "a race of villainous creatures is enough to send a chill down your spine.")
        print()
        time.sleep(7)
        print("Hearing Captain Jason's pep talk gave me some encouragement. I think the rest of the crew also tried\n"
              "to mask their fears and act courageous.\n")
        time.sleep(12)
        print()

        print("Captain Jason: We've received intel from our stealth drones on the location of the alien vessels.\n"
              "We are to take off in 2 minutes. Everyone, to your positions. We are launching hot and hard.\n"
              + player_name + " is going to be our Defense op.\n"
              "Matthew is our Pilot. Jane as our navigator. With old Smith coming as our technician.\n"
              "Systems Check!\n")
        time.sleep(20)

        print("Player's Thoughts: I have tried to keep my fears. A lot of what ifs swirling around me at the moment.\n"
              "Status reports from individual crew member flew in and I have to snap out of my thoughts to give my\n"
              "report. Captain Jason must have heard the fear in my voice because he turned and said, 'It\'s\n"
              "gon' be fine, but I got a feeling this ain't true. In a few seconds, we are going to blast off to\n"
              "space to battle a force Earth has never fought before.\n")
        time.sleep(25)

        print("Captain Jason: All systems are online. We are a go.\n")
        time.sleep(3)
        print("Player's Thoughts: Here comes the dreaded feeling...\n")
        time.sleep(4)

        print("Pilot: Approaching Lunar Colony. ETA to target is 10 cints. Engaging hyper drive. Hang on!\n")
        time.sleep(5)
        print("Player's thoughts: That's 20 seconds as a cint is equal to 2 seconds. Dang it! I need to adjust\n"
              "my seatbelt.\n")
        time.sleep(4)

        engage_belt = input("Enter 'activate hyper belt' or 'ahb' to engage hyper drive safety belt" + ": \n")
        if engage_belt == "activate hyper belt" or engage_belt == "ahb" or engage_belt == "AHB"\
                or engage_belt == "ACTIVATE HYPER BELT":
            print("HDS belt engaged!\n")
            time.sleep(5)
            print("Pilot: Disengaging hyper drive!\n")
            time.sleep(2)
            print("Navigator: 7 cints to target!")

        else:
            print("Spelling Error!")
            time.sleep(2)
            print()
            print("GAME OVER!")
            time.sleep(1)
            print("Sorry " + player_name + ", you hit your head against the display board.")
            print()
            time.sleep(5)
            print("Would you like to play again?")
            print()
            print("If yes, click the run button on the screen to reload the game or press 'ctrl + F5'.")
            print()
            print("If no, click the exit button.")
            print()
            print("Thanks for playing.")
            print("Watch out for newer versions of this application. You can let us know what you think about\n"
                  "this game, talking about gaming experience and ways of improving.")
    else:
        print("\nYou are not fit to defend Earth on Doomsday! Please, exit the Loop.")
