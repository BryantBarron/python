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
names_string = input("Give me everybody's names, seperated by a comma. ")

names = names_string.split(", ")

#number of people
num = len(names)
#unlucky person is
unlucky = random.randint(1, num)
print(f"Person paying the bill is: {names[unlucky]}.")
