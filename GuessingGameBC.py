import random

def main():
    guessesTaken1 = 0
    guessesTaken2 = 0
    roundswon1 = 0
    roundswon2 = 0

    print("\nHello there Players! Welcome to the Guessing Game!")
    print("Would you like to play an easy, medium, or hard game, and do you want 1-player or 2-players?")
    print("1. Easy 1 player!\n2. Medium 1 player!\n3. Hard 1 player!\n4. Easy 2 player!\n5. Medium 2 player!\n6. Hard 2 player!")
    difficulty = int(input("Enter difficulty and number of players:"))

    if difficulty == 1:
        randNum = random.randrange(1, 11)
        choice = int(input("Player, enter a number:"))
        while choice < randNum:
            print("The number you entered is too low.")
            choice = int(input("Player, enter another number:"))
        while choice > randNum:
            print("The number you entered is too high.")
            choice = int(input("Player, enter another number:"))
        if choice == randNum:
            print("Congratulations, you got it! You win the game! Would you like to play again?")
            replay = int(input("1.Yes\n2.No"))
            if replay == 1:
                main()

    elif difficulty == 2:
        randNum = random.randrange(1, 21)
        choice = int(input("Player, enter a number:"))
        while choice < randNum:
            print("The number you entered is too low.")
            choice = int(input("Player, enter another number:"))
        while choice > randNum:
            print("The number you entered is too high.")
            choice = int(input("Player, enter another number:"))
        if choice == randNum:
            print("Congratulations, you got it! You win the game! Would you like to play again?")
            replay = int(input("1.Yes\n2.No"))
            if replay == 1:
                main()

    elif difficulty == 3:
        randNum = random.randrange(1, 101)
        choice = int(input("Player, enter a number:"))
        while choice < randNum:
            print("The number you entered is too low.")
            choice = int(input("Player, enter another number:"))
        while choice > randNum:
            print("The number you entered is too high.")
            choice = int(input("Player, enter another number:"))
        if choice == randNum:
            print("Congratulations, you got it! You win the game. Would you like to play again?")
            replay = int(input("1.Yes\n2.No"))
            if replay == 1:
                main()

    elif difficulty == 4:
        while roundswon1 != 3 or roundswon2 != 3:
            randNum = random.randrange(1, 11)
            choice1 = int(input("Player 1, enter a number:"))
            guessesTaken1 = guessesTaken1 + 1
            while choice1 < randNum:
                print("The number you entered is too low.")
                choice1 = int(input("Player 1, enter another number:"))
                guessesTaken1 = guessesTaken1 + 1
            while choice1 > randNum:
                print("The number you entered is too high.")
                choice1 = int(input("Player 1, enter another number:"))
                guessesTaken1 = guessesTaken1 + 1
            if choice1 == randNum:
                print("Congratulations, you got it!")
            randNum = random.randrange(1, 11)
            choice2 = int(input("Player 2, enter a number:"))
            guessesTaken2 = guessesTaken2 + 1
            while choice2 < randNum:
                print("The number you entered is too low.")
                choice2 = int(input("Player 2, enter another number:"))
                guessesTaken2 = guessesTaken2 + 1
            while choice2 > randNum:
                print("The number you entered is too high.")
                choice2 = int(input("Player 2, enter another number:"))
                guessesTaken2 = guessesTaken2 + 1
            if choice2 == randNum:
                print("Congratulations, you got it!")
                if guessesTaken1 > 10 or guessesTaken1 > guessesTaken2:
                    print("Player 2, you win this round!")
                    roundswon2 = roundswon2 + 1
                if guessesTaken2 > 10 or guessesTaken2 > guessesTaken1:
                    print("Player 1, you win this round!")
                    roundswon1 = roundswon1 + 1
                if guessesTaken1 == guessesTaken2:
                    print("It's a tied match!")
            if roundswon1 == 3:
                print("Player 1, you win the game! Would you like to play again?")
                replay = int(input("1. Yes\n2. No"))
                if replay == 1:
                    main()
            if roundswon2 == 3:
                print("Player 2, you win the game! Would you like to play again?")
                replay = int(input("1. Yes\n2. No"))
                if replay == 1:
                    main()


    elif difficulty == 5:
        while roundswon1 != 3 or roundswon2 != 3:
            randNum = random.randrange(1, 21)
            choice1 = int(input("Player 1, enter a number:"))
            guessesTaken1 = guessesTaken1 + 1
            while choice1 < randNum:
                print("The number you entered is too low.")
                choice1 = int(input("Player 1, enter another number:"))
                guessesTaken1 = guessesTaken1 + 1
            while choice1 > randNum:
                print("The number you entered is too high.")
                choice1 = int(input("Player 1, enter another number:"))
                guessesTaken1 = guessesTaken1 + 1
            if choice1 == randNum:
                print("Congratulations, you got it!")
            randNum = random.randrange(1, 21)
            choice2 = int(input("Player 2, enter a number:"))
            guessesTaken2 = guessesTaken2 + 1
            while choice2 < randNum:
                print("The number you entered is too low.")
                choice1 = int(input("Player 2, enter another number:"))
                guessesTaken2 = guessesTaken2 + 1
            while choice2 > randNum:
                print("The number you entered is too high.")
                choice2 = int(input("Player 2, enter another number:"))
                guessesTaken2 = guessesTaken2 + 1
            if choice2 == randNum:
                print("Congratulations, you got it!")
                if guessesTaken1 > 15 or guessesTaken1 > guessesTaken2:
                    print("Player 2, you win this round!")
                    roundswon2 = roundswon2 + 1
                if guessesTaken2 > 15 or guessesTaken2 > guessesTaken1:
                    print("Player 1, you win this round!")
                    roundswon1 = roundswon1 + 1
                if guessesTaken1 == guessesTaken2:
                    print("It's a tied match!")
            if roundswon1 == 3:
                print("Player 1, you win the game! Would you like to play again?")
                replay = int(input("1. Yes\n2. No"))
                if replay == 1:
                    main()
            if roundswon2 == 3:
                print("Player 2, you win the game! Would you like to play again?")
                replay = int(input("1. Yes\n2. No"))
                if replay == 1:
                    main()

    else:
        while roundswon1 != 3 or roundswon2 != 3:
            randNum = random.randrange(1, 101)
            choice1 = int(input("Player 1, enter a number:"))
            guessesTaken1 = guessesTaken1 + 1
            while choice1 < randNum:
                print("The number you entered is too low.")
                choice1 = int(input("Player 1, enter another number:"))
                guessesTaken1 = guessesTaken1 + 1
            while choice1 > randNum:
                print("The number you entered is too high.")
                choice1 = int(input("Player 1, enter another number:"))
                guessesTaken1 = guessesTaken1 + 1
            if choice1 == randNum:
                print("Congratulations, you got it!")
            randNum = random.randrange(1, 101)
            choice2 = int(input("Player 2, enter a number:"))
            guessesTaken2 = guessesTaken2 + 1
            while choice2 < randNum:
                print("The number you entered is too low.")
                choice2 = int(input("Player 2, enter another number:"))
                guessesTaken2 = guessesTaken2 + 1
            while choice2 > randNum:
                print("The number you entered is too high.")
                choice2 = int(input("Player 2, enter another number:"))
                guessesTaken2 = guessesTaken2 + 1
            if choice2 == randNum:
                print("Congratulations, you got it!")
                if guessesTaken1 > 30 or guessesTaken1 > guessesTaken2:
                    print("Player 2, you win this round!")
                    roundswon2 = roundswon2 + 1
                if guessesTaken2 > 30 or guessesTaken2 > guessesTaken1:
                    print("Player 1, you win this round!")
                    roundswon1 = roundswon1 + 1
                if guessesTaken1 == guessesTaken2:
                    print("It's a tied match!")
            if roundswon1 == 3:
                print("Player 1, you win the game! Would you like to play again?")
                replay = int(input("1. Yes\n2. No"))
                if replay == 1:
                    main()
            if roundswon2 == 3:
                print("Player 2, you win the game! Would you like to play again?")
                replay = int(input("1. Yes\n2. No"))
                if replay == 1:
                    main()

main()