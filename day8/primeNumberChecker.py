from math import sqrt

def isPrime(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("Its a prime number")
    else:
        print("Its not a prime")

num = int(input("What number do you think is prime? "))

isPrime(num)