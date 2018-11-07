"""This is a dice bet game."""

"""You will have 100 dollars to bet with the house for either bigger or smaller."""

import random

while True:
    
    print("You can enter < big >, < small >, or < quit > to resume.")

    choice = input("You want to bet your dice bigger or smaller than the house? Or you want to quit? : ...")

    if choice == "quit":

        break

    elif choice == "big" or choice == "small":

        gamer = 100.0

        print("Here is how much you have: " + str(gamer))

        bet = int(input("Please enter how much you wanna bet: "))

        print(str(bet) + " is how much you wanna bet.")

        if bet > gamer:

            print("You don't have that much.")

        else:
            print("Let's start.")

            house_dice = random.randint(1, 7)

            gamer_dice = random.randint(1, 7)

            print(str(gamer_dice) + " is yours.")

            if gamer_dice > house_dice and choice == "big":

                print("You Win!!!")

                print("House have " + str(house_dice))

                gamer += bet

                print("You have left " + str(gamer))

            elif gamer_dice > house_dice and choice == "small":

                print("You Lose!!!")

                print("House have " + str(house_dice))

                gamer -= bet

                print("You have left " + str(gamer))

            elif gamer_dice < house_dice and choice == "big":

                print("You Lose!!!")

                print("House have " + str(house_dice))

                gamer -= bet

                print("You have left " + str(gamer))

            elif gamer_dice < house_dice and choice == "small":
                
                print("You Win!!!")

                print("House have " + str(house_dice))

                gamer += bet

                print("You have left " + str(gamer))
            
            else:

                print(str(gamer_dice) + " yours" + str(house_dice) + " house's")

                print("It's even.")



                

    else:
        print("Invalid input.")



 




