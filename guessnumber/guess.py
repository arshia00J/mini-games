from random import *
num_range = int(input("Enter the range of numbers (0 - ?]: "))
number = randint(0, num_range)  # Generate a random number within the given range.
i = 0
while(True):
    given_num = int(input("Guess the number: "))
    i += 1
    if given_num > number:
        print("Try  a smaller number.")
        
    elif given_num < number:
        print("Try a larger number.")
    else:
        print(f"TADA! you  guessed it right.({i} try)")
        break