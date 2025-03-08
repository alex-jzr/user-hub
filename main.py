from tools import root_code
from tools import user_code
from tools import tour_code


from colorama import init, Fore, Style  # 导入用于彩色显示的库

# 初始化 colorama，确保在 Windows 上支持颜色
init(autoreset=True)

# 用于命令行显示的颜色定义
success_color = Fore.GREEN  # 绿色
error_color = Fore.RED      # 红色
info_color = Fore.YELLOW    # 黄色
reset_color = Style.RESET_ALL

user = 'tour'
user_con = 0
rootpass = '12141327Alex'

def display_message(message, color=info_color):
    """Displays message with specified color"""
    print(f"{color}{message}{reset_color}")

# 旅游模式循环
while user_con == 0:
    user_input = input(f"{info_color}{user}> {reset_color}")

    if user_input == "login":
        display_message("----- Log In -----")
        user_log_name = input(f"{info_color}{user}> Please enter your name: {reset_color}")
        user_log_password = input(f"{info_color}{user}> Please enter your password: {reset_color}")

        # 登录功能
        user_con, user = tour_code.Login(user_log_name, user_log_password)
        if user_con == 1:
            display_message(f"Login successful! Welcome, {user}!", success_color)
        elif user_con == 2:
            display_message(f"Login successful! Welcome, root user {user}!", success_color)
        else:
            display_message("Login failed. Please check your credentials and try again.", error_color)

    elif user_input == "register":
        display_message("---- Create New User ----")
        user_reg_name = input(f"{info_color}{user}> Please enter your name: {reset_color}")
        user_reg_password = input(f"{info_color}{user}> Please enter your password: {reset_color}")
        user_reg_email = input(f"{info_color}{user}> Please enter your email: {reset_color}")
        user_reg_type = input(f"{info_color}{user}> Please enter your type (user/root): {reset_color}")

        # 用户类型为 root 时需要 root 密码验证
        if user_reg_type == 'root':
            root_pass = input(f"{info_color}root password: {reset_color}")
            if root_pass == rootpass:
                tour_code.Register(user_reg_name, user_reg_password, user_reg_email, user_reg_type)
                display_message("Root user created successfully!", success_color)
            else:
                display_message("Incorrect root password. User creation failed.", error_color)
                break
        else:
            tour_code.Register(user_reg_name, user_reg_password, user_reg_email, user_reg_type)
            display_message(f"User {user_reg_name} created successfully!", success_color)

    elif user_input == "help":
        display_message("---- Help ----")
        print(tour_code.tour_help_txt)

    elif user_input == "exit":
        display_message("Goodbye! Exiting...", info_color)
        input()

    else:
        display_message(f"{user_input} command not found. Try entering 'help'.", error_color)

# 普通用户循环
while user_con == 1:
    user_input = input(f"{info_color}{user}> {reset_color}")

    if user_input == "help":
        display_message("---- Help ----")
        print(user_code.help_txt)

    elif user_input == "exit":
        display_message("Goodbye! Exiting...", info_color)
        user_con = 0

    elif user_input == "name_change":
        # 用户调用名字更改
        user_code.name_change(user_con, user)
        display_message("Username updated successfully!", success_color)

    elif user_input == "password_change":
        # 用户调用密码更改
        user_code.password_change(user_con, user)
        display_message("Password updated successfully!", success_color)

    elif user_input == "email_change":
        # 用户调用邮箱更改
        user_code.email_change(user_con, user)
        display_message("Email updated successfully!", success_color)

    elif user_input == "permission_upgrade":
        # 用户调用权限升级
        user_code.permission_upgrade(user_con, user, rootpass)
        display_message("Permission upgraded successfully!", success_color)

    else:
        display_message(f"{user_input} command not found. Try entering 'help'.", error_color)

# Root 用户循环
while user_con == 2:
    user_input = input(f"{info_color}{user}> {reset_color}")

    if user_input == "help":
        display_message("---- Root Help ----")
        print(root_code.help_txt)

    elif user_input == "exit":
        display_message("Goodbye! Exiting...", info_color)
        user_con = 0

    elif user_input == "user_add":
        # Root 用户调用添加用户
        root_code.user_add(rootpass, user_con)
        display_message("User added successfully!", success_color)

    elif user_input == "user_delete":
        # Root 用户调用删除用户
        root_code.user_delete(rootpass)
        display_message("User deleted successfully!", success_color)

    elif user_input == "user_info_update":
        # Root 用户调用更新用户信息
        root_code.user_info_update(rootpass)
        display_message("User info updated successfully!", success_color)

    elif user_input == "users_printer":
        # Root 用户调用打印用户信息
        root_code.users_printer(user_con, rootpass)
        display_message("User information printed successfully!", success_color)

    else:
        display_message(f"{user_input} command not found. Try entering 'help'.", error_color)