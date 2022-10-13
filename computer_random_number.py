# to guess a correct number using random computer inputs
'''
computer is guessing input
advantages:
take input
assign low
assign high
tell the user to guess weather the guess nubmer is to high or low or correct
disadvantages:
what if the input below to low number
what if the user feedback given wrong ther we have to give exception
that user confuesd there gueedd number
'''
import random
def computer_guess(x):
    low = 1
    high = x
    user_feedback = ''
    while(user_feedback != 'c'):
        if low != high:
            guess=random.randint(low,high)
        else:
            guess = low
        user_feedback=input(f'is the input number {guess} weather high (H) or low(l) or correct(c)')
        if user_feedback == 'h':
            high = guess-1
        elif user_feedback=='l':
            low = guess + 1
    print('yeah computer u gueesed the correct number')

computer_guess(1000)