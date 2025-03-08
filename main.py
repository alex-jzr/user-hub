import tour_code
import user_code
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

# 旅游模式循环
while user_con == 0:
    user_input = input(f"{info_color}{user}> {reset_color}")

    if user_input == "login":
        print(f"\n{info_color}----- Log In -----{reset_color}")
        user_log_name = input(f"{info_color}{user}> Please enter your name: {reset_color}")
        user_log_password = input(f"{info_color}{user}> Please enter your password: {reset_color}")

        # 登录功能
        user_con, user = tour_code.Login(user_log_name, user_log_password)
        if user_con == 1:
            print(f"{success_color}Login successful! Welcome, {user}!{reset_color}")
        else:
            print(f"{error_color}Login failed. Please check your credentials and try again.{reset_color}")

    elif user_input == "register":
        print(f"\n{info_color}---- Create New User ----{reset_color}")
        user_reg_name = input(f"{info_color}{user}> Please enter your name: {reset_color}")
        user_reg_password = input(f"{info_color}{user}> Please enter your password: {reset_color}")
        user_reg_email = input(f"{info_color}{user}> Please enter your email: {reset_color}")
        user_reg_type = input(f"{info_color}{user}> Please enter your type (user/root): {reset_color}")

        # 用户类型为root时需要root密码验证
        if user_reg_type == 'root':
            root_pass = input(f"{info_color}root password: {reset_color}")
            if root_pass == rootpass:
                tour_code.Register(user_reg_name, user_reg_password, user_reg_email, user_reg_type)
                print(f"{success_color}Root user created successfully!{reset_color}")
            else:
                print(f"{error_color}Incorrect root password. User creation failed.{reset_color}")
                break
        else:
            tour_code.Register(user_reg_name, user_reg_password, user_reg_email, user_reg_type)
            print(f"{success_color}User {user_reg_name} created successfully!{reset_color}")

    elif user_input == "help":
        print(f"\n{info_color}---- Help ----{reset_color}")
        print(tour_code.tour_help_txt)

    elif user_input == "exit":
        print(f"\n{info_color}Goodbye! Exiting...{reset_color}")
        break

    else:
        print(f"{error_color}{user_input} command not found. Try entering 'help'.{reset_color}")

# 普通用户循环
while user_con == 1:
    user_input = input(f"{info_color}{user}> {reset_color}")

    if user_input == "help":
        print(f"\n{info_color}---- Help ----{reset_color}")
        print(user_code.help_txt)

    elif user_input == "exit":
        print(f"\n{info_color}Goodbye! Exiting...{reset_color}")
        break

    elif user_input == "name_change":
        # 用户调用名字更改
        user_code.name_change(user_con, user)
        print(f"{success_color}Username updated successfully!{reset_color}")

    elif user_input == "password_change":
        # 用户调用密码更改
        user_code.password_change(user_con, user)
        print(f"{success_color}Password updated successfully!{reset_color}")

    elif user_input == "email_change":
        # 用户调用邮箱更改
        user_code.email_change(user_con, user)
        print(f"{success_color}Email updated successfully!{reset_color}")

    elif user_input == "permission_upgrade":
        # 用户调用权限升级
        user_code.permission_upgrade(user_con, user, rootpass)
        print(f"{success_color}Permission upgraded successfully!{reset_color}")

    else:
        print(f"{error_color}{user_input} command not found. Try entering 'help'.{reset_color}")
