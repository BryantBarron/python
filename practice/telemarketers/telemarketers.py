num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# telemarketer numbers: first digit 8 or 9, fourth digit 8 or 9, second digit 
# and third digit are the same (8119 = telemarketer, 8129 is not)

if((num1 == 8 or num1 == 9) and
    (num4 == 8 or num4 == 9) and
    (num2 == num3)):
    print('ignore')
else:
    print('answer')

# input redirection (call file with data to run this program off of )
# python telemarketers.py < telemarketers_input.txt 