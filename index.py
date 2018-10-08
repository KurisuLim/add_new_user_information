# Add User Information
# We will be using nested sequences

userInfos = []

option = None
while option != "0":

    print("""
    User Information

    1 - Show User List
    2 - Add New User
    3 - Remove User
    0 - Exit
    """
    )

    option = input("Option: ")
    print()#Adds space between choices

    # Exits the program
    if option == "0":
        print("Thank you for using the program. Good bye for now!")
    # Message for wrong info
    
    else:
        print("Option ", option , " is not a valid choice. Please try again.")

input("\n\nPress the enter key to exit.")