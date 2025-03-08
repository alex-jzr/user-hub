def Login(user_log_name, user_log_password):
    global user_con, user
    user_con = 0
    user = "tour"

    with open('E:\\code\\python_code\\UserHub\\usermessage.txt', "r") as file:
        for line in file:
            user_log_info = line.strip().split()
            user_name, user_password, types = user_log_info[0], user_log_info[1], user_log_info[3]

            if user_log_name == user_name:
                if user_log_password == user_password:
                    user = user_name
                    user_con = 2 if types == 'root' else 1
                    print(f"-----pass-----\nWelcome {types} {user_name}!")
                    return user_con, user

                else:
                    print(f"{types} {user_name} password error")
                    return user_con, user

    print(f"user {user_log_name} cannot find")
    return user_con, user
