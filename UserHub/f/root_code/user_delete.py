def user_delete(root_password):
    password_in = input("Enter root password: ")

    if password_in == root_password:
        delete_user_name = input("Enter the name of the user to delete: ")

        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'r') as file:
            lines = file.readlines()
        
        new_lines = []
        user_found = False

        for line in lines:
            user_info = line.strip().split()
            
            if user_info[0] != delete_user_name:
                new_lines.append(line)
            else:
                user_found = True

        if user_found:
            with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'w') as file:
                file.writelines(new_lines)
            print(f"User {delete_user_name} deleted successfully.")
        else:
            print(f"User {delete_user_name} not found.")
    else:
        print("Incorrect root password. User deletion failed.")


user_delete('12141327Alex')