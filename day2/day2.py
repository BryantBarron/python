# print(len("Hello"))

# #basic data types
# #string 
# print("hello"[2]) #this is subscripting
# #integer, don't have to write int in front of it
# #float
# #boolean
# #mystery =  734_529.678
# mystery = 734529.678
# print(mystery)
# #python will strip the underscore
# #type check function
# # num = 25
# # print(type(num))
# # #type casting
# # num_char = len(input("What is your name?"))
# # new_num_char = str(num_char)
# # #cant put num_char here because it throws a data type error
# # print("Your name is" + new_num_char + " characters")
# a = 123
# print(type(a))
# a = str(123)
# print(type(a))
# a = float(123)
# print(type(a))
# print(70+ float("100.5"))
# print(str(70)+str(100)) #prints the string 70100
# #Write a program that adds the digits in a 2 digit number. e.g.
# #if the input was 35, then the output should be 3 + 5 = 8
# num = input("Give me a two digit number: ")
# a = num[0]
# b = num[1]

# num1 = int(a)
# num2 = int(b)
# print("The sum of the two digits of your number is:")
# print(num1 + num2)
# # +,-,*,/ but remember power is ** IE 2 ** 2, python follows pemdas

# #Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# #The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# #The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# #https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

# #Warning you should convert the result to a whole number.
# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = float(weight) / float(int(height)**2)

# print("Your BMI is: ")
# print(bmi)

# #rounding numbers
# print(round(8/3))
# #precise rounding 
# print(round(8/3, 2)) #2 decimal places
# #floor division
# print(8//3) #forces to become an int

# score = 0
# height = 1.8
# isWinning = True #use cap for boolean
# #f-string
# print(f"your score is: {score}, your height is: {height}, you are winning is {isWinning}")

# age = input("What is your current age?")
# age = int(age)
# months99 = 99 * 12
# weeks99 = 99 * 52
# days99 = 99 * 365

# monthsUser = age * 12 
# weeksUser = age * 52
# daysUser = age * 365

# monthsLeft = months99 - monthsUser
# weeksLeft = weeks99 - weeksUser
# daysLeft = days99 - daysUser35

# print(f"You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left." )

print("Welcome to the tip calculator")
bill = input("What is the total bill?")
percentTip = input("What percent tip would you like to leave? 10, 12, 15 or 20?") 
numPeople = input("How many people are splitting the bill?")
bill =float(bill)
percentTip = int(percentTip)
numPeople = int(numPeople)
billPercent = float(bill) * float(percentTip/100)
tip = float(billPercent / numPeople)
final_tip =round(tip, 2)

print(f"Each person should pay: {final_tip}")