import random


#randomization intergers and floats

random_seed=(123)
random_number=random.randint(1,40)
print(random_number)
random_float=random.random()*40
print(random_float)
love_score= random.randint(1,100)
print(f"Your love score is {love_score}")

##Heads and Tails

test_seed =int(input("Create a seed number:"))
random.seed(test_seed)
random_side = random.randint(0,1)
if random_side==1:
    print("Heads")
else:
    print("Tails")

#Lists operations

siblings =["grace","lona","linda","jane","pauline","catherine","hilda","prudence"]
print(siblings)
siblings[2]="amy"
print(siblings)
# # adding a list to an existing list
siblings.extend(["mary","janet","wahura"])
print(siblings)
print(len(siblings))
number=len(siblings)
print(siblings[number-1])#otherwise an index out of range error

#nested lists

row1=["a","@","c"]
row2=["d","$","f"]
row3=["g","*","i"]
map=[row1,row2,row3]
position =(input("Place your value"))
horizontal=int(position[0])
vertical=int(position[1])
map[vertical-1][horizontal-1]="LONA"
print(f"{row1} {row2} {row3}")

##random lottery guess game

test_seed =int(input("Create a seed number:"))
random.seed(test_seed)
lottery_winner=input("Guess name paying our bill today.")
names=lottery_winner.split(",")
print(len(lottery_winner))
print(names)
name_list =len(lottery_winner)
print(name_list)
random_choice=random.randint(0,name_list-1)
print(random_choice)
lucky_one=names[random_choice]
print(lucky_one + "is our winner today!!")


