to_do_list = []

def remove_item():
            item = input("Please choose an item to remove: ")
            if item in to_do_list:
                to_do_list.remove(item)
                print("It has been removed")
            else:
                print("Try again")

print("Welcome to your to do list")

while True:

    choice = input(
        "\nWhat would you like to do?\n" 
        "1) Add\n" 
        "2) Remove\n"
        "3) View list\n" 
        "4) Quit\n"
        "Enter your choice: "
    )
    if choice == "1" or "Add".lower():

        n = int(input("Please enter the number of items you want to add to the list: "))

        for i in range(n):
            item = str(input("Now please enter the item you wish to add to the list: ")).lower()
            to_do_list.append(item)
        print("Items added.")

    elif choice == "2" or "Remove".lower():
        remove_item()
        
    elif choice == "3" or "View list".lower():
         print(to_do_list)

    elif choice == "4" or "Quit".lower():
         break
    
    
    again = input("Enter to restart or type quit to exit")
    if again == "quit":
         
        break