# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

#average student height
# student_heights = input("Input a list of student heights ").split()
# total_heights = 0
# count = 0
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     total_heights = total_heights + int(student_heights[n])
#     count = count + 1

# average_height = total_heights / count
# average_height = round(average_height, 2)

# print(f"The Average Height is: {average_height}")

#student scores
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# lowest_score = 100
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#     if score < lowest_score:
#         lowest_score = score
        
# print(f"The highest score is: {highest_score}")
# print(f"The lowest score is: {lowest_score}")

#for loop practice
# total = 0
# for i in range(0,101):
#     #total = total + i
#     total += i
# print(total)

# even = 0
# even_array = []
# for i in range(0,101):
#     if((i%2) == 0):
#         even += i
#         even_array.append(i)
# print(even)
# print(even_array)

#fizzbuzz
# for i in range(1, 101):
#     if(((i%3) == 0) and ((i%5) == 0)):
#         print("FizzBuzz")
#     elif((i%3)== 0):
#         print("Fizz")
#     elif((i%5) == 0):
#         print("Buzz")
#     else:
#         print(i)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for i in range(1, len(nr_letters)):
    

