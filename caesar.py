

from helpers import alphabet_position, rotate_character
from sys import argv, exit


def encrypt(text, rot):
    newText = ""
    for i in text:
        newText += rotate_character(i, rot)
    return newText

def user_input_is_valid(cl_args):
    if cl_args[-1].isdigit():
        return True
    else:
        return False



if user_input_is_valid(argv) == False:
    None
    #print("usage: python3 ceasar.py n")
    #exit()
#print("I know that these are the words that the user typed on the command line:", argv)
#print(encrypt(input("Type a message:  "), argv[-1]))
