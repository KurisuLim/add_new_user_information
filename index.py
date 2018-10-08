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
    print()# Adds space between choices

    # Exits the program
    if option == "0":
        print("Thank you for using the program. Good bye for now!")

    # Shows User List
    elif option == "1":
        if userInfos == []:
            print("\nSorry No User Found!")
        else:
            print("\nUser List")
            for addNewUser in userInfos:
                name, email, password = addNewUser
                print()
                print("Name: ", name)
                print("Email: ", email)
                print("Password: ", password)
    # Add New User
    elif option == "2":
        name = str(input("What is your name?: "))
        email = str(input("What is your email?: "))
        password = str(input("What is your password?: "))
        addNewUser = (name,email,password)
        userInfos.append(addNewUser)

    # Removes a User
    elif option == "3":
        userList = str(input("Who user you want to remove?: "))
        if userList in userInfos:
            userInfos.remove(userList)
            print()
            print(userList, " has been removed.")
        else:
            print()
            print(userList, " isn't in the user list.")

    # Message for wrong info
    else:
        print("Option ", option , " is not a valid choice. Please try again.")

input("\n\nPress the enter key to exit.")