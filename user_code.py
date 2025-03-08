def name_change(user_con, user):
    if user_con == 1:
        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'r') as file:
            new_line = []
            lines = file.readlines()

            for line in lines:
                user_info = line.strip().split()
                
                if user == user_info[0]:
                    new_username = input(f"Enter your new username (current: {user}): ")
                    user_info[0] = new_username
                    new_line.append(" ".join(user_info) + "\n")
                else:
                    new_line.append(line)

        with open('E:\\code\\python_code\\UserHub\\usermessage.txt', 'w') as file:
            file.writelines(new_line)

    else:
        print("Please login first.")



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




help_txt = """"
==============help==============

Here's the help documentation for regular users (`user`) in English, detailing the commands they can execute and their functionality:

### Regular User Help Documentation

#### 1. **Change Username (`name_change`)**

- **Function**: Allows the user to change their username.
- **How to Use**:
  - Enter the command `name_change`.
  - The system will prompt the user to enter a new username, and it will update the username in the `usermessage.txt` file.

- **Example**:
  ```bash
  user> name_change
  Enter your new username (current: old_username): new_username
  Username updated successfully.
  ```

#### 2. **Change Password (`password_change`)**

- **Function**: Allows the user to change their password.
- **How to Use**:
  - Enter the command `password_change`.
  - The system will prompt the user to enter a new password, and it will update the password in the `usermessage.txt` file.

- **Example**:
  ```bash
  user> password_change
  Enter your new password: new_password
  Password updated successfully.
  ```

#### 3. **Change Email (`email_change`)**

- **Function**: Allows the user to change their email address.
- **How to Use**:
  - Enter the command `email_change`.
  - The system will prompt the user to enter a new email, and it will update the email in the `usermessage.txt` file.

- **Example**:
  ```bash
  user> email_change
  Enter your new email (current: old_email@example.com): new_email@example.com
  Email updated successfully.
  ```

#### 4. **Permission Upgrade (`permission_upgrade`)**

- **Function**: If the user has the right to upgrade permissions, they can input the correct root password to upgrade their permissions from a regular user to root.
- **How to Use**:
  - Enter the command `permission_upgrade`.
  - The system will prompt the user to input the root password. If correct, the user's permissions will be upgraded.

- **Example**:
  ```bash
  user> permission_upgrade
  Enter the root password to upgrade your permissions: root_password
  User upgraded to root successfully.
  ```

#### 5. **Exit the System (`exit`)**

- **Function**: Exit the current user session and return to the guest mode or directly quit the program.
- **How to Use**:
  - Enter the command `exit`.

- **Example**:
  ```bash
  user> exit
  Goodbye! Exiting...
  ```

#### 6. **Help Command (`help`)**

- **Function**: Display a list of available commands with brief descriptions.
- **How to Use**:
  - Enter the command `help`.

- **Example**:
  ```bash
  user> help
  Available commands: 
  - name_change: Change your username.
  - password_change: Change your password.
  - email_change: Change your email.
  - permission_upgrade: Upgrade your permissions to root (requires root password).
  - exit: Exit the program.
  ```

---

### Notes:
- **Permission Management**:
  - The `permission_upgrade` command is used to upgrade the current user's permissions from a regular user (`user`) to an administrator (`root`). The upgrade will only succeed if the correct root password is entered.
  - Regular users without upgraded permissions cannot perform high-level operations such as modifying other users' information.

- **Command Input**:
  - When executing commands, make sure the input is correct. If the command is invalid, the system will display a message like "Command not found."

- **File Updates**:
  - Every time the username, password, or email is changed, the corresponding information is directly updated in the `usermessage.txt` file.

---

### FAQ:

- **Q: How do I recover a lost password?**
  - The current system does not support password recovery. If you forget your password, you need to register a new account.

- **Q: How can I downgrade my user permissions from root to user?**
  - The current system does not provide a feature to downgrade permissions. Users can only be upgraded to root but cannot downgrade back to a regular user.

---

This is the help documentation for regular users, detailing the available commands and basic operations they can perform in the system. If you have more questions, feel free to use the `help` command to get assistance at any time.
"""
