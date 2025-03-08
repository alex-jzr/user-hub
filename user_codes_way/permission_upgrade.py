def permission_upgrade(user_con, user, root_password):
    if user_con == 1:
        entered_password = input("Enter the root password to upgrade your permissions: ")

        if entered_password == root_password:
            with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'r') as file:
                new_line = []
                lines = file.readlines()

                for line in lines:
                    user_info = line.strip().split()
                    
                    if user == user_info[0]:
                        user_info[3] = "root"
                        new_line.append(" ".join(user_info) + "\n")
                    else:
                        new_line.append(line)

            with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'w') as file:
                file.writelines(new_line)

            print(f"User {user} has been upgraded to root.")
        else:
            print("Incorrect root password. Permission upgrade failed.")
    else:
        print("You must be logged in as user to upgrade your permissions.")
