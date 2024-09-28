import random
import os

#Families define where you will be born
families = ['Noble','Mage','Merchant',]
print("---------------------------")
print("Teacher: Welcome, dear adventurer... To the wonderful world of Elaria!")
print("Teacher: I am your teacher and its time for you to choose your class.")
print("---------------------------")

Player_class = int(input("type out the number:\n1)Warrior\n2)Mage\n3)Rogue\n4)Ranger\n"))
try:
    if Player_class == 1:
        print("Teacher: A great choice I must say.")
        print("---------------------------")
        print("Received = Old Sword")
        cw = "Old Sword"
        with open('weapon.txt','w') as current_weapon:
            current_weapon.write("Old Sword")

    if Player_class == 2:
        print("Teacher: Arcane arts gives rise to a lot of possibilities!")
        print("---------------------------")
        print("Received = Old Wand")
        cw = "Old Wand"
        with open('weapon.txt','w') as current_weapon:
            current_weapon.write("Old Wand")

    if Player_class == 3:
        print("Teacher: Stealthy, like an assassin... Good.")
        print("---------------------------")
        print("Received = Old Dagger")
        cw = "Old Dagger"
        with open('weapon.txt','w') as current_weapon:
            current_weapon.write("Old Dagger")

    if Player_class == 4:
        print("Teacher: A Ranger. I must say its a fine choice, young lad.\nHere a wooden bow to get you started.")
        print("---------------------------")
        print("Received = Wooden Bow")
        cw = "Wooden Bow"
        with open('weapon.txt','w') as current_weapon:
            current_weapon.write("Wooden Bow")

except ValueError as value_error:
    print(value_error)

print("---------------------------")
print(f"Teacher: Since you got your weapon now, let's test out the {cw}")
fight = str(input("Do you wish to test your weapon?: (Y or N)"))
if fight.lower() == "y":
    print("---------------------------")
    attack = input("Alright, type a to attack me: ")
    dice_roll = random.randint(1,6)
    if dice_roll > random.randint(1,6):
        print("HIT!")
    else:
        print("MISS!")
if fight.lower() == "n":
    print("Teacher: All right young lad, I wont force you.")
    
