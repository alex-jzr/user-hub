def user_add(root_password,user_con):

    password_in = input("Enter root password: ")
    
    if password_in == root_password and user_con == 2:

        add_user_name = input("Enter new user's name: ")
        add_user_password = input("Enter new user's password: ")
        add_user_email = input("Enter new user's email: ")
        add_user_type = input("Enter new user's type (user/root): ")

        if add_user_type not in ['user', 'root']:
            print("Invalid user type! Please enter 'user' or 'root'.")
            return
        

        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'a') as file:

            file.write(f"{add_user_name} {add_user_password} {add_user_email} {add_user_type}\n")
        
        print(f"User {add_user_name} added successfully!")
    else:
        print("Incorrect root password. User addition failed.")

