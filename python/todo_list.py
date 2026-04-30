import json 
import sys

things = {}
def add():
    id = int(input("ID:"))
    item = input("Item:")
    things[id]= item
    with open("things.json", 'w') as f:
        json.dump(things,f)
    print(f'{id}.{item}')
    
def remove():
    print(things)
    if not things:
        print("No items to remove.")
    else:
        item = input("Item:")
        if item not in things:
            print("Item not found.")
        else:
            del things[item]
            with open("things.json", 'w') as f:
                json.dump(things,f)
            print(f'{item} removed.')
        
def show():
    if not things:
        print("No items in To-Do List.")
    else:
        print("To-Do List")
        with open("things.json", 'r') as f:
            json.load(f)
        for id, item in things.items():
            print(f'{id}.{item}')



def main():
    choice = 0
    while choice != 4:
        try:
            print(""""
    1. Add Item
    2. Remove Item  
    3. Show To-Do List
    4. Exit      
                """)
            
        
            choice = int(input("Choice:"))
            if choice == 1:
                add()
            elif choice == 2:
                remove()
            elif choice == 3:
                show()
            elif choice == 4:
                print("Exiting...")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
        
        
main()