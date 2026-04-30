import string
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
special_character = string.punctuation
def validation():
    while True:
    
        prompt = input("Password: ")
        if prompt.isdigit():
            continue
        else:
            print("No Digits")
            break 
        if prompt in uppercase:
            continue
        else:
            print("No uppercase")
            break
        if prompt in lowercase:
            continue
        else:
            print("No lowercase")
            break
        if prompt in special_character:
            continue
        else:
            print("No Special Characters")
            break
          