"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can
"""
import math

def paint_calc(height, width, coverage):
    number_of_cans = (height * width)/coverage
    rounded_cans = round(number_of_cans)
    return rounded_cans

height = int(input("What is the height of your wall in meters? "))
width = int(input("What is the width of your wall in meters?"))
coverage = 5

number_of_cans = paint_calc(height, width, coverage)

print(f"You will need {number_of_cans} can(s) to paint your wall.")
