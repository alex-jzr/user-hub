import sqlite3
import os

# 数据库文件路径
DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'user_database.db')

def read_user_data():
    """从数据库中读取用户数据"""
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username, password, email, user_type FROM users")
            return cursor.fetchall()
    except Exception as e:
        print(f"Error reading user data: {e}")
        return []

def Login(user_log_name, user_log_password):
    global user_con, user
    user_con = 0  # 默认未登录
    user = "tour"  # 默认用户

    # 从数据库中读取用户数据
    user_data = read_user_data()

    for user_info in user_data:
        username, password, email, user_type = user_info

        # 检查用户名和密码
        if user_log_name == username:
            if user_log_password == password:
                user = username
                user_con = 2 if user_type == 'root' else 1
                print(f"-----pass-----\nWelcome {user_type} {username}!")
                return user_con, user
            else:
                print(f"{user_type} {username} password error")
                return user_con, user

    print(f"user {user_log_name} cannot be found")
    return user_con, user

def Register(username, password, email, user_type):
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            # 检查用户名或邮箱是否已存在
            cursor.execute("SELECT username, email FROM users WHERE username = ? OR email = ?", (username, email))
            if cursor.fetchone():
                print(f"user {username} or email {email} has already been used")
                return None

            # 插入新用户
            cursor.execute("INSERT INTO users (username, password, email, user_type) VALUES (?, ?, ?, ?)",
                            (username, password, email, user_type))
            conn.commit()
            print(f"-----{username} has been created successfully!-----")
    except Exception as e:
        print(f"An error occurred while creating the user: {e}")

# helpdoc 保持不变
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