# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))
# # remember indentation in python is very important
# if height > 120: 
#     print("You can ride the rollercoaster")
# else:
#     print("Can't ride")

#Write a program that works out whether if a given number is an odd or even number.
# num = int(input("Please enter a number: "))
# if (num % 2) == 0:
#     print("You number is even")
# else:
#     print("Your number is odd")

#nested if/else
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))
# #remember indentation in python is very important
# if height > 120: 
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Can't ride")

# print("Another BMI Calculator")
# weight = int(input("Please enter your weight in kgs: "))
# height = int(input("Please enter your height in meters: "))

# bmi = float(weight) / float(float(height) ** 2)
# bmi = round(bmi, 2)

# print(f"Your bmi is: {bmi}.")

# if bmi < 18.5:
#     print("You are underweight")
# elif ((bmi >= 18.5) and (bmi < 25)):
#     print("You have normal weight")
# elif ((bmi >= 25 ) and (bmi < 30)):
#     print("You are slightly overweight")
# elif ((bmi >= 30) and (bmi < 35)):
#     print("You are obese")
# else: 
#     print("You are obese")        

# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra
# day in February.

# year = int(input("Please pick a year and write the full year: " ))
# if ((year % 4) == 0):
#     print("You picked a leap year")
#     if ((year % 100) == 0):
#         if((year % 400) == 0):
#             print("Not a leap year")
#         else:
#             print("You picked a leap year")
# else: 
#     print(f"{year} is not a leap year.")

#Automatic Pizza Program
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# #Small = 15, med = 20, lg = 25, pepperoni=2 on small, 3 on large/med, cheese= 1
# total = 0.0
# size.upper()
# add_pepperoni.upper()
# extra_cheese.upper()
# if((size == "L") or (size == "M") or (size == "S")):
#     if(extra_cheese == "Y"):
#         total += 1
#     if((size == "L") or (size == "M")):
#         if(add_pepperoni == "Y"):
#             total += 3
#     elif(size == "S"):
#         if(add_pepperoni == "Y"):
#             total += 2
# if(size == "L"):
#     total += 25
#     print(f"Your pizza will cost: {total}")
# elif(size == "M"):
#     total += 20
#     print(f"Your pizza will cost: {total}")
# elif(size == "S"):
#     total += 15
#     print(f"Your pizza will cost: {total}")
# else:
#     print("Wrong pizza size")

python uses and not &&, or not ||, not instead of !
love calculator
calculator takes both peoples names and check fore the number of times the 
letters in the word TRUE occur. The check the number of times the letters 
in the world LOVE occur. Then combine these numbers to make a 2 digit 
number. Then give a rating off that number.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# name1.upper() DOESNT WORK
# REMEMBER .upper doesnt work just on the variable you must do it this way
name1 = name1.upper()
name2 = name2.upper()

count_name1 = 0
count_name2 = 0
count = 0

for element in name1:
    # project doesnt tell us if we have to count the "E" twice or not so I am
    if((element == "T") or (element == "R") or (element == "U") or (element == "E")):
        count_name1 += 1
    if((element == "L") or (element == "O") or (element == "V") or (element == "E")):
        count_name1 += 1

for element in name2:
    # project doesnt tell us if we have to count the "E" twice or not so I am
    if((element == "T") or (element == "R") or (element == "U") or (element == "E")):
        count_name2 += 1
    if((element == "L") or (element == "O") or (element == "V") or (element == "E")):
        count_name2 += 1
# did this because you have to combine count 1 and 2s digits, figured it was 
# easier then converting to a character combining to a str then converting back 
# to a number, both of those wouldn't take into account what happens if you 
# an instance where some how someone has > 10 of these hits in their names

count_name1 = count_name1 * 10
count = count_name1 + count_name2

if ((count < 10) and (count > 90)):
    print(f"Your score is {count}, you go together like coke and mentos")
elif((count >= 40) and (count <= 50)):
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}, we don't care about you.")
