import os

USER_FILE_PATH = os.path.join(os.path.dirname(__file__), 'usermessage.txt')

def read_user_data():
    """读取用户数据"""
    try:
        with open(USER_FILE_PATH, 'r') as file:
            return [line.strip().split() for line in file]
    except Exception as e:
        print(f"Error reading user data: {e}")
        return []


## Login
def Login(user_log_name, user_log_password): 
    global user_con, user
    user_con = 0  # Default is not logged in
    user = "tour"  # Default user

    # Read user data
    user_data = read_user_data()

    for user_log_info in user_data:
        user_name, user_password, email, types = user_log_info[0], user_log_info[1], user_log_info[2], user_log_info[3]

        # Check if the username matches
        if user_log_name == user_name:
            if user_log_password == user_password:
                user = user_name
                # Set user_con based on user type
                user_con = 2 if types == 'root' else 1
                print(f"-----pass-----\nWelcome {types} {user_name}!")
                return user_con, user
            else:
                print(f"{types} {user_name} password error")
                return user_con, user

    print(f"user {user_log_name} cannot be found")
    return user_con, user



## Register
def Register(user_name, user_password, email, types):
    user_data = read_user_data()

    for users_info in user_data:
        if user_name == users_info[0] or email == users_info[2]:
            print(f"user {user_name} or email {email} has already been used")
            return None

    try:
        with open(USER_FILE_PATH, 'a') as file:
            file.write(f"{user_name} {user_password} {email} {types}\n")
        print(f"-----{user_name} has been created successfully!-----")
    except Exception as e:
        print(f"An error occurred while creating the user: {e}")
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
