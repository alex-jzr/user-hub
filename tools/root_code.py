import sqlite3
import os
import re

# 数据库文件路径
DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'user_database.db')

def validate_email(email):
    """验证电子邮件格式"""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def user_add(root_password, user_con):
    """添加新用户"""
    password_in = input("Enter root password: ")
    
    if password_in == root_password and user_con == 2:
        add_user_name = input("Enter new user's name: ")
        add_user_password = input("Enter new user's password: ")
        add_user_email = input("Enter new user's email: ")

        # 检查用户类型
        add_user_type = input("Enter new user's type (user/root): ")
        if add_user_type not in ['user', 'root']:
            print("Invalid user type! Please enter 'user' or 'root'.")
            return

        # 验证邮箱格式
        if not validate_email(add_user_email):
            print("Invalid email format!")
            return
        
        try:
            with sqlite3.connect(DATABASE_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password, email, user_type) VALUES (?, ?, ?, ?)",
                               (add_user_name, add_user_password, add_user_email, add_user_type))
                conn.commit()
                print(f"User {add_user_name} added successfully!")
        except Exception as e:
            print(f"An error occurred while adding the user: {e}")
    else:
        print("Incorrect root password or insufficient permissions. User addition failed.")

def user_delete(root_password):
    """删除用户"""
    password_in = input("Enter root password: ")

    if password_in == root_password:
        delete_user_name = input("Enter the name of the user to delete: ")

        try:
            with sqlite3.connect(DATABASE_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM users WHERE username = ?", (delete_user_name,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"User {delete_user_name} deleted successfully.")
                else:
                    print(f"User {delete_user_name} not found.")
        except Exception as e:
            print(f"An error occurred while deleting the user: {e}")
    else:
        print("Incorrect root password. User deletion failed.")

def user_info_update(root_password):
    """更新用户信息"""
    password_in = input("Enter root password: ")

    if password_in == root_password:
        update_user_name = input("Enter the name of the user to update: ")

        try:
            with sqlite3.connect(DATABASE_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username = ?", (update_user_name,))
                user_info = cursor.fetchone()

                if user_info:
                    print(f"Current info of {update_user_name}:")
                    print(f"Username: {user_info[1]}, Password: {user_info[2]}, Email: {user_info[3]}, Type: {user_info[4]}")

                    new_username = input(f"Enter new username (current: {user_info[1]}): ")
                    new_password = input(f"Enter new password (current: {user_info[2]}): ")
                    new_email = input(f"Enter new email (current: {user_info[3]}): ")
                    new_user_type = input(f"Enter new user type (current: {user_info[4]}): ")

                    # 更新用户信息
                    cursor.execute("""
                        UPDATE users
                        SET username = ?, password = ?, email = ?, user_type = ?
                        WHERE username = ?
                    """, (new_username, new_password, new_email, new_user_type, update_user_name))
                    conn.commit()
                    print(f"User {update_user_name} info updated successfully.")
                else:
                    print(f"User {update_user_name} not found.")
        except Exception as e:
            print(f"An error occurred while updating the user info: {e}")
    else:
        print("Incorrect root password. User info update failed.")

def users_printer(user_con, root_password):
    """打印用户信息"""
    password_in = input("Enter root password: ")
    
    if password_in == root_password and user_con == 2:
        try:
            with sqlite3.connect(DATABASE_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()

                for user in users:
                    print(f"=========== User Information =========")
                    print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[3]}, Type: {user[4]}")
        except Exception as e:
            print(f"An error occurred while reading the user data: {e}")
    else:
        print("Incorrect root password or insufficient permissions.")

# help_txt 保持不变
help_txt = """
Root User Management Functions Help Document:

1. user_add(root_password, user_con):
   - This function allows a root user to add a new user.
   - Parameters:
     - root_password: The root password used to verify the root user's access.
     - user_con: The user's connection level. Only a root user (user_con == 2) can add users.
   - Steps:
     1. The function asks for the root password.
     2. If the password is correct and the user has root privileges (user_con == 2), it proceeds to add a new user.
     3. The function prompts the root user to input the new user's name, password, email, and type (either 'user' or 'root').
     4. If the type is valid, the user is added to the database.
     5. If successful, a confirmation message is displayed.

2. user_delete(root_password):
   - This function allows a root user to delete an existing user.
   - Parameters:
     - root_password: The root password used to verify the root user's access.
   - Steps:
     1. The function asks for the root password.
     2. If the password is correct, it prompts for the name of the user to delete.
     3. The function searches through the database and removes the specified user if found.
     4. If the user exists and is successfully deleted, a confirmation message is shown.
     5. If the user does not exist, an error message is displayed.

3. user_info_update(root_password):
   - This function allows a root user to update an existing user's information.
   - Parameters:
     - root_password: The root password used to verify the root user's access.
   - Steps:
     1. The function asks for the root password.
     2. If the password is correct, it prompts for the name of the user whose information needs to be updated.
     3. The function searches through the database and displays the current information of the user.
     4. The root user can then modify the username, password, email, and user type.
     5. If the update is successful, the information is saved in the database.

4. users_printer(user_con, root_password):
   - This function allows a root user to print out all users' information.
   - Parameters:
     - user_con: The user's connection level. Only a root user (user_con == 2) can access this feature.
     - root_password: The root password used to verify the root user's access.
   - Steps:
     1. The function asks for the root password.
     2. If the password is correct and the user has root privileges (user_con == 2), it reads and prints all users' information from the database.
     3. It displays the user information in a clear format.
"""