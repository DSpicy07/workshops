import random
user_total = 0
comp_total = 0
user_average = 0
comp_average = 0
total_throws = []
highest_throw = 0
lowest_throw = 0
def creator():
    print("Romeo Skoog Fiou")

def dice():
    global user_total, comp_total, user_average, comp_average, user_throws, comp_throws, highest_throw, lowest_throw
    turns = int(input("How many turns do you want to play?\n"))
    print("------------------------------")
    for i in range(turns):
        if i < turns:
            i =+ 1
            user_throw1 = random.randint(1, 6)
            total_throws.append(user_throw1)
            user_throw2 = random.randint(1, 6)
            total_throws.append(user_throw2)
            user_dice = user_throw1 + user_throw2
            user_total += user_dice
            print(f"You got {user_dice}")
            computer_throw1 = random.randint(1, 6)
            total_throws.append(computer_throw1)
            computer_throw2 = random.randint(1, 6)
            total_throws.append(computer_throw2)
            computer_dice = computer_throw1 + computer_throw2
            comp_total += computer_dice
            print(f"Computer got {computer_dice}")
            if user_dice > computer_dice:
                print("User won!")
                print("------------------------------")
                continue
            elif user_dice < computer_dice:
                print("Computer won!")
                print("------------------------------")
                continue
            else:
                print("Tie!")
                print("------------------------------")
                continue
        else:
            break
    user_average = round(user_total / turns, 1)
    comp_average = round(comp_total / turns, 1)
    for i in total_throws:
        if i > highest_throw:
            highest_throw = i
        elif i < lowest_throw:
            lowest_throw = i
    if user_total > comp_total:
        print(f"User won with a total of {user_total} points!\nAverage throw value {user_average}")
        print(f"Computer only got {comp_total} points!\nAverage throw value {comp_average}")
        print(f"Highest throw was {highest_throw}\nLowest throw was {lowest_throw}")

        
    elif user_total < comp_total:
        print(f"Computer won with a total of {comp_total} points!\nAverage throw value {comp_average}")
        print(f"User only got {user_total} points!\nAverage throw value {user_average}")
        print(f"Highest throw was {highest_throw}\nLowest throw was {lowest_throw}")
    else: 
        print(f"Tie between user {user_total} and computer {comp_total}\nUser average throw value {user_average}\nComputer average throw value {comp_average}")
        print(f"Highest throw was {highest_throw}\nLowest throw was {lowest_throw}")


dice()


