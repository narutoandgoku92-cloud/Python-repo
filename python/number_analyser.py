
while True:
    prompt =input("Input a number: ")
    
    try:
        if prompt.isdigit():
            prompt = int(prompt)
            break
            
        else:
            print("Incorrect input")
    except:
        print("Incorrect value")
        
def prime():
    if prompt % 2 == 0:
        print("Even")
    else:
        print("Odd")

def sum():
    new_prompt = str(prompt)
    count = 0 
    for i in range(len(new_prompt)):
        count += int(new_prompt[i])
    print(count)
    
def reverse():
    new_num= str(prompt)
    reversed_string = new_num[::-1]
    newer_num= int(reversed_string)
    print(newer_num)
    
def main():
    print(
"""
****************************************
Choose your options 
 1. Prime
 2.Sum
 3.Reverse
 ***************************************
""")
    try:
        ans = int(input("Input: "))
        
        if ans == 1:
            prime()
        elif ans == 2:
            sum()
        elif ans == 3:
            reverse()
        else:
            print("Invalid input")
    except ValueError:
        print("Incorrect Input")    
        

        
        
        
        