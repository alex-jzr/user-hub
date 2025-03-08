
## Login
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



## Register
def Register(user_name, user_password,email,types):
    with open ('E:\\code\\python_code\\UserHub\\usermessage.txt',"r") as file:

        for line in file :

           users_info = line.strip().split()

           if user_name == users_info[0] or email == users_info[2]:
               print( f"user {user_name} has been used" )
               return None
               

    with open ('E:\\code\\python_code\\UserHub\\usermessage.txt',"a") as file:
        file.write(f"{user_name} {user_password} {email} {types}\n")

        print( f"-----{user_name} has been creat successfully!-----" )
        return None



# helpdoc
tour_help_txt = """
----------------- Help -----------------

1. login:
- To log in, enter your username and password.
- If successful, you will be welcomed based on your user type.
- If the username or password is incorrect, an error message will be shown.

2. register:
- To register, provide a unique username, password, email, and user type (either 'admin' or 'user').
- If the username or email already exists, a message will inform you that it has already been used.
- If registration is successful, you will be notified.

3. exit:
- To exit out type 'exit'

-----------------------------------------
"""
