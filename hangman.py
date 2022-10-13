import random
from practise import words
import string

def hang(words):
    computer_input=random.choice(words)  # selecting a word from the give list(words) randomly.
    while '-' in computer_input or ' ' in computer_input:
        computer_input=random.choice(words)
    return computer_input.upper()
def hangman():
    word = hang(words)
    word_letters = set(word)  # set is a command that help to make unique word in the sentence
    alphabet=set(string.ascii_uppercase) #doesnot repeat the alphabet twice
    used_letters= set()
    lives=6
    while len(word_letters)>0 and lives>0:
        print('you have',lives,'You have used these letters',' '.join(used_letters)) #join will join the string words
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('current word',' '.join(word_list))
        user_letters=input("guess a letter").upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives=lives-1
                print('letter is not in word.')

        elif user_letters in used_letters:
            print("you have already used that character,pleases try again!!")
        else:
            print('invalid character')
    if lives==0:
        print("your died,sorry",word)
    else:
        print("your guess word",word)

hangman()

