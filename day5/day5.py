# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

#average student height
student_heights = input("Input a list of student heights ").split()
total_heights = 0
count = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_heights = total_heights + int(student_heights[n])
    count = count + 1

average_height = total_heights / count
average_height = round(average_height, 2)

print(f"The Average Height is: {average_height}")

