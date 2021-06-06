import random
import math
lower_b= int(input("Enter Lower bound:- "))
upper_b= int(input("Enter Upper bound:- "))
x = random.randint(lower_b, upper_b)
print("\n\tYou've only ",
       round(math.log(upper_b - lower_b + 1, 2)),
      " chances to guess the integer!\n")
count = 0
while count < math.log(upper_b - lower_b + 1, 2):
    count += 1
    guess=int(input("Guess a number:- "))
    if x==guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x>guess:
        print("You guessed too small!")
    elif x<guess:
        print("You Guessed too high!")
if count >= math.log(upper_b - lower_b + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")