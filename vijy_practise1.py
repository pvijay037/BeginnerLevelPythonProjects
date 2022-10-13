import random
from practise import words
import string
def hang(words):
    com_input=random.choice(words)
    while "-" in com_input or ' ' in com_input:
        com_input=random.choice(words)
    return com_input.upper()
def hangman():
    word=hang(words)
    words_letter=set(word)
    alphabet=set(string.ascii_uppercase)
    saved_words=set()
    lives=6
    while len(words_letter)>0 or lives>0:
        print(f"{lives} input left","".join(saved_words))
        user_input=input("enter an alphabet").upper()
    =[i if i in saved_words else "-" for i in word]
