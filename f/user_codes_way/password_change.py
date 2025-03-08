def password_change(user_con, user):
    if user_con == 1:

        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'r') as file:
            new_line = []
            lines = file.readlines()

            for line in lines:
                user_info = line.strip().split()

                if user == user_info[0]:

                    password_update = input(f"{user}, enter your new password: ")
                    user_info[1] = password_update
                    new_line.append(" ".join(user_info) + "\n")
                else:

                    new_line.append(line)


        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'w') as file:
            file.writelines(new_line)

    else:
        print("Please login first.")
