database = {}


def add_student():
    while True:
        try:
            prompt = input("Name:")
            if prompt.strip() in database:
                print("Student already exists.")
                ans = input("Would you like to update student score:")
                if ans.lower() == "y":
                    update()
                elif ans.lower() == "n":
                    print("Thank you for your time")
                    break
            else:
                score = int(input("Score:"))
                database[prompt.strip()] = score
        except ValueError:
            print("Invalid Input")    
    
def update():
    while True:
        try:
            prompt = input("Name:")
            
            if prompt.strip() not in database:
                print("student does not exist.")
                ans = input("Would you like to add the student(y/n)")
                if ans.lower() == "y":
                    add_student()
                elif ans.lower() == "n":
                    break
            else:
                score = int(input("Score:"))
                database[prompt.strip()] = score
        except ValueError:
            print("Invalid input")
            
            
            
def display_all():
    for student,score in database.items():
        print(student, ":", score)
            
            
def highest_score():
    data = max(database, key= database.get)
    value = database[data]
    print(value, data)
        
         
def average_score():
    total = 0 
    for score in database.values:
        total += score
    average = float(total/len(database.values))
    
    print(average)
    
        
             