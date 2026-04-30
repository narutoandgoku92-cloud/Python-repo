prompt = input("Give me a word or a sentence:")

new_prompt = prompt.lower()

def vowel_counter():
    count = 0
    
    for i in range(len(new_prompt)):
        if new_prompt[i] == "a" or new_prompt[i] == "e" or new_prompt[i] == "i" or new_prompt[i] == "o" or new_prompt[i] == "u":
            count += 1
    print(count)
    
    
    
def consonant_counter(): 
    count = 0
    
    for i in range(len(new_prompt)):
        if new_prompt[i] == "a" or new_prompt[i] == "e" or new_prompt[i] == "i" or new_prompt[i] == "o" or new_prompt[i] == "u":
            count += 10
    score = len(new_prompt.replace(" ","")) - count
    print(score)
    
def palindrome():
    old_prompt = new_prompt.replace(" ","")
    palin = old_prompt[::-1]
    if palin == old_prompt:
        return True
    else:
        return False
    
def largest_word():
    large = 0 
    word_bank = prompt.split()
    
    output = max(word_bank, key=len)     
    print(output)  
    
largest_word()


def main():
    print(
"""
****************************************************
CHOOSE YOUR OPTION:
1.LARGEST WORD
2.PALINDROME
3.CONSONANT COUNTER
4.VOWEL COUNTER
"""
    )
    
    try:
        ans = int(input("Input: "))
        
        if ans == 1:
            largest_word()
        elif ans == 2:
            palindrome()
        elif ans == 3:
            vowel_counter()
        elif ans == 4:
            consonant_counter()
        else:
            print("Invalid input")
    except ValueError:
        print("Incorrect Input")    
        

            