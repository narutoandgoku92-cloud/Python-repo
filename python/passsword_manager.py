import sys
import json
import string
import random


def password_generator(length = 8):
    alpha = string.ascii_letters
    num = string.digits
    char  = alpha + num
    formed  = []
    try:

        length = int("Length:") 
        if length < 8:
            print("Too short")
        else:
            for i in range(length):
               formed.append(random.choice(char))
        
        finished = "".join(formed)
        
        with open("formed.json", "w") as file:
            json.dump(finished,file)
            

    except TypeError:
        print("Wrong Input")