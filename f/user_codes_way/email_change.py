def email_change(user_con, user):
    if user_con == 1:
        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'r') as file:
            new_line = []
            lines = file.readlines()

            for line in lines:
                user_info = line.strip().split()
                
                if user == user_info[0]:
                    new_email = input(f"Enter your new email (current: {user_info[2]}): ")
                    user_info[2] = new_email
                    new_line.append(" ".join(user_info) + "\n")
                else:
                    new_line.append(line)

        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'w') as file:
            file.writelines(new_line)

    else:
        print("Please login first.")
