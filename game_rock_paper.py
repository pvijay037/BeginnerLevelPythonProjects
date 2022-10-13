#playing rock paper sissor game
import random
def game():
    user_input= input("what is u r choice 'r' for rock 'p' for paper 's' for sisscor")
    computer_input=random.choice(['r','p','s'])
    #sissocor>paper,paer>rock,rock>sicssor
    if user_input==computer_input:
        return "It's a tie"
    if iswin(user_input,computer_input):
        return "You Won"
    return "you lost"
def iswin(player,opponent):
    if(player == 's' and opponent == 'p')or(player == 'p' and opponent == 'r')or(player == 'r' and opponent == 's'):
        return True
print(game())