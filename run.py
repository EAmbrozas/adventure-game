name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")


answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You came to a river, you can walk around it or swim accross? Type walk to walk or swim to swim accross: ")

    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross? (cross/back): ")

    if answer == "cross":
        answer = input("You crosse the bridge and meet a stranger. Do you talk to them? (yes/no): ")

        if answer == "yes":
            print("You talk to stranger and they give you gold. You WIN!")
        
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")

        else:
            print("Not a valid option. You lose!")

    elif answer == "back":
        answer = input("You go back and loose.")

    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")

print(f"Thank you for trying {name}")