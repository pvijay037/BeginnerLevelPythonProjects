# to guess the number between 1 to 10

import random
def ran(x):
    random_num = random.randint(1,x)
    guess=0
    while(guess!=random_num):
        guess = int(input(f"enter a number betweem 1 to {x} "))
        if guess < random_num:
            print(f"enter the number above {guess}")
        elif guess > random_num:
            print(f"enter the number below {guess}")
    print("yooo! hooo you guess the correct number")
ran(10)


