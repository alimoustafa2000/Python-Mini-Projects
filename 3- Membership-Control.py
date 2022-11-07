admins = ["Ahmed", "Osama", "Ali", "Manal", "Rahma", "Mahmoud", "Enas"]

passwords = ['user@12345']

tries = 5

# login
name = input("What's your name? ").strip().capitalize()

# check name in admins
if name in admins:
    print(f"Hello {name}, Welcome back!")

    option = input("Do you want to delete or update your name? ").strip().lower()

# update option
    if option == "update":
        new_name = input("Enter your new name, please. ").strip().capitalize()

        admins[admins.index(name)] = new_name
        print("Your name is updated.")
        print(admins)

# delete option
    elif option == "delete":
        make_sure = input("Are you sure? Yes or No ").strip().lower()
        if make_sure == "yes":
            admins.remove(name)
            print("Your name is deleted.")
            print(admins)

        else:
            print("please don't play.")

# Wrong Option
    else:
        print("Wrong option.")

      
# if not an admin
else:
    ques = input("You are not an admin.\nDo you want to be an admin? Yes or No ").strip().lower()

    if ques == "yes":
        user_password = input("Please enter your password. ").strip().lower()
        if user_password in passwords:
            admins.append(name)
            print("Your name is added.")
            print(admins)
            
        else:
            while user_password not in passwords:
                tries -= 1
                
                if tries == 0:
                    print('Wrong password, Last chance left')
                elif tries == 1:
                    print('Wrong password, 1 chance left')
                else:
                    print(f'Wrong password, {tries} chances left')
            
                user_password = input("Enter your password. ")
            
                if tries == 0 and user_password not in passwords: 
                    print('All chances are finished!')
                    break
            
            else:
                admins.append(name)
                print("Your name is added.")
                print(admins)

    else:
        print("You Are Not Added.")
    
