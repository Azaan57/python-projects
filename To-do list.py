to_do_list = []

def remove_item():
            item = input("Please choose an item to remove: ")
            if item in to_do_list:
                to_do_list.remove(item)
                print("It has been removed")
            else:
                print("Try again")

def add_item():
    n = int(input("Please enter the number of items you want to add to the list: "))

    for i in range(n):
        item = str(input("Now please enter the item you wish to add to the list: ")).lower()
        to_do_list.append(item)
    print("Items added.")

def list_choice():
     return input(
            "\nWhat would you like to do?\n" 
            "1) Add\n" 
            "2) Remove\n"
            "3) View list\n" 
            "4) Quit\n"
            "Enter your choice: "
        ).strip().lower()

def main():
    print("Welcome to your to do list")

    while True:

        choice = list_choice()
        
        if choice in {"1", "add"}:
            add_item()

        elif choice in {"2", "remove"}:
            remove_item()
        
        elif choice in {"3", "view", "view list"}:
            print(to_do_list)

        elif choice in {"4", "quit"}:
            break
    
    
        again = input("Enter to restart or type quit to exit. ")
        if again == "quit":
            break

if __name__ == "__main__":
     main()