import random

print("This is a dice-bet program.")
print("Please enjoy.")
print("===========================")

# set the player starts at $500
gamer = 500

# while player still have money
while gamer > 0:
    print("you have " + str(gamer) + " dollars.")

    # ask about how player want to bet
    print("You can enter < big >, < small >, or < quit > to continue.")
    player_input = input("< big >, < small >, < even > or < quit >: ")

    if player_input == "quit":

        break

    elif player_input == "big":

        # ask about bet
        print("how much you want to bet?")

        # make sure player only enter interger
        try:
            bet = int(input("..."))
        except ValueError:
            print("you can only enter round numbers")
            continue
        else:
            # if player bet more than he has
            if bet > gamer:
                print("you don't have that much, you can't bet that much.")

            # when given a valid bet
            elif bet > 0:

                # throw the dice
                house_dice = random.randint(1, 7)
                player_dice = random.randint(1, 7)

                if player_dice > house_dice:

                    print(f"player: {player_dice}")
                    print(f"house: {house_dice}")
                    print("player > house")
                    print(f"you bet {player_input}")
                    print("you win")
                    gamer += bet

                else:

                    print(f"player: {player_dice}")
                    print(f"house: {house_dice}")
                    print(f"you bet {player_input}")
                    print("you lose")
                    gamer -= bet

            else:

                print("invalid input")

    elif player_input == "small":

        print("how much you want to bet?: ")

        try:
            bet = int(input("..."))
        except ValueError:
            print("you can only input round numbers")
            continue
        else:
            if bet > gamer:

                print("you don't have that much, you can't bet that much.")

            elif bet > 0:
                house_dice = random.randint(1, 7)
                player_dice = random.randint(1, 7)

                if player_dice < house_dice:

                    print(f"player: {player_dice}")
                    print(f"house: {house_dice}")
                    print("player < house")
                    print(f"you bet {player_input}")
                    print("you win")
                    gamer += bet

                else:

                    print(f"player: {player_dice}")
                    print(f"house: {house_dice}")
                    print(f"you bet {player_input}")
                    print("you lose")
                    gamer -= bet

            else:

                print("invalid input")


    elif player_input == "even":

        print("how much you want to bet?: ")

        try:
            bet = int(input("..."))
        except ValueError:
            print("you can only input round numbers")
            continue
        else:
            if bet > gamer:
                print("you don't have that much, you can't bet that much.")

            elif bet > 0:
                house_dice = random.randint(1, 7)
                player_dice = random.randint(1, 7)

                if player_dice == house_dice:

                    print(f"player: {player_dice}")
                    print(f"house: {house_dice}")
                    print("player = house")
                    print(f"you bet {player_input}")
                    print("you win")
                    gamer += bet

                else:

                    print(f"player: {player_dice}")
                    print(f"house: {house_dice}")
                    print(f"you bet {player_input}")
                    print("you lose")
                    gamer -= bet

            else:

                print("invalid input")

    else:

        print("Invalid input")

if (gamer == 0):
    print("GAME OVER")
    print("You lost all your money.")
