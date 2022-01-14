# Day 4 Randomisation and Python Lists
import random
import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.pi)

# random_float = random.random()
# #generates a random number from 0 - 9.99999 so just doesnt include 10
# random_float = random_float * 10
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is: {love_score}")

#code challenge heads or tails with
# coin = random.randint(0,1)
# if coin == 0:
#     print("Tails")
# elif coin == 1:
#     print("Heads")
# else:
#     print("Broken")

# state1 = "Delaware"
# state2 = "Pennsylvania"
# states_of_america = [ "Delaware", "Pennsylvania", "California", "Arizona", "Texas"]

# print(states_of_america) #prints array of states
# print(states_of_america[0]) #prints the first item in the array
# print(states_of_america[-1]) #prints the last item in the array, negatives move from the end of the array in
# print(states_of_america[-2])

# states_of_america.append("Hawaii") # adds a single item to the end of the array
# print(states_of_america)

#code challenge Banker Roullete
# names_string = input("Give me everybody's names, seperated by a comma. ")

# names = names_string.split(", ")

# #number of people
# num = len(names)
# #unlucky person is
# unlucky = random.randint(1, num)
# print(f"Person paying the bill is: {names[unlucky]}.")


#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#nested list
# fruits = [ "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears" ]
# vegatables = [ "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes",]
# dirty_dozen = [fruits, vegatables]
# print(dirty_dozen)

# #treasure map challenge
# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
# row3 = [" ", " ", " "]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?")

# horizontal = int(position[0])
# vertical = int(position[1])

# #selected_row = map[vertical - 1]
# #selected_row[horizontal - 1] = "X"
# map[vertical -1][horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

#rock paper scissors challenge
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock, Paper, Scissors vs RNG (Random Number Generator)")
print("Input 1 for Rock, 2 for Papper, 3 for Scissors and see if you beat RNG.")

def print_user_choice(user_choice):
    if user_choice == "1":
        print(rock)
        print("You chose Rock.")
    elif user_choice == "2":
        print(paper)
        print("You chose Paper.")
    elif user_choice == "3":
        print(scissors)
        print("You chose Scissors.")
    else:
        print("Incorrect Choice.")

def print_computer(computer_choice):
    if computer_choice == "1":
        print(rock)
        print("The computer chose Rock.")
    elif computer_choice == "2":
        print(paper)
        print("The computer chose Paper.")
    elif computer_choice == "3":
        print(scissors)
        print("The computer chose Scissors.")
        
user_choice = ""
while (user_choice != "1") and (user_choice != "2") and (user_choice != "3"):
    user_choice = input("Please chose 1, 2, or 3: ")
    print_user_choice(user_choice) 

computer_choice = random.randint(1, 3)
computer_choice = str(computer_choice)
print_computer(computer_choice)

#rock beats scissors, paper beats rock, scissors beat paper
#draw
if(user_choice == computer_choice):
    print("Its A Draw!")
elif((user_choice == "1") and (computer_choice == "2")):
    print("You Lost to Paper.")
elif((user_choice == "1") and (computer_choice == "3")):
    print("You Beat Scissors.")
elif((user_choice == "2") and (computer_choice == "1")):
    print("You Beat Roc.k")
elif((user_choice == "2") and (computer_choice == "3")):
    print("You Lost to Scissors.")
elif((user_choice == "3") and (computer_choice == "1")):
    print("You Lost to Rock.")
elif((user_choice == "3") and (computer_choice == "2")):
    print("You Beat Paper.")
else:
    print("Something Broke.")


