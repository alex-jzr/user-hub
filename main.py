from tools import root_code
from tools import user_code
from tools import tour_code
import sqlite3
import os
from colorama import init, Fore, Style
import msvcrt  # 用于 Windows 系统的输入处理

# 初始化 colorama，确保在 Windows 上支持颜色
init(autoreset=True)

# 用于命令行显示的颜色定义
success_color = Fore.GREEN  # 绿色
error_color = Fore.RED      # 红色
info_color = Fore.YELLOW    # 黄色
reset_color = Style.RESET_ALL

# 数据库文件路径
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'user_database.db')

# 初始化数据库
def init_db():
    """初始化数据库，创建用户表"""
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    user_type TEXT NOT NULL
                )
            ''')
            conn.commit()
            print("Database initialized successfully.")  # 打印初始化成功信息
    except Exception as e:
        print(f"Error initializing database: {e}")

# 显示消息的函数
def display_message(message, color=info_color):
    """Displays message with specified color"""
    print(f"{color}{message}{reset_color}")

# 获取密码输入并显示为 *
def get_password(prompt):
    """获取密码输入并显示为 *"""
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r':  # 回车键结束输入
            print()
            break
        elif char == '\b':  # 处理退格键
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end="", flush=True)  # 删除一个 *
        else:
            password += char
            print('*', end="", flush=True)  # 显示 *
    return password

# 全局变量
user = 'tour'
user_con = 0
rootpass = '%A%888wSR5ZnwgzBnQtNIM0ggWsTFRyvi1jFE7E7IYb01gGHDH5S1fcByMwm7DoqxZNmbYyq8SeeYWOx9LZ9N3CsA2TXgceJeWQMDpwgx1r!Sg!VcxAJpHZi**4dDYqCcte@9kcWy#AbX5dX9DrP7b41Ljs!g7gM@64Wcy3@918o4HKT9gWMCdjNaG$hH1KX3IyOlfVF#VQC26VFzc4S4zeGM0QodEba&So@kw6hJUWSU$q%Wf4w^py#AKY5^$pkGm7yKVCRhxpS7Tiq1O5HXTn7bh9T$P&4bpNqSTtDfoSNSsjKrRKnC$PB$qtq3E3rehvRB#Pt4jTByRv^vizGCzwAvE&xB0k8%GDumK!61ez5#uyFDDYcsLaM^LETt0dIWW0pmm&BjhCzt7k20MpYKVgWX7uH0h&mKTiXhTPr%8XzP@AP0cid2kMMe%EROML&@#L5mDvxC^2LOPKOLYXL4uoX$42nFdc#AgHck!&y@oWtNhW%GIGdIIBvcUk6XDG2LtNXzv8xGPRgj%!uzAcv9BUQqjIvYRWXR2qzD$z@XRTggwFigtEDU6yn@S2@HxKbnXP6$sQIkXxbK5T6QuL!X6vrKNEp4wvam#&BlYvT4Mo9BMUOuBw#rHMjAewmk%$xo#k%RorZxafEvB&J0AtuDQ$snfIk#gWSvBH%Zo77t6IJ573Vi^fO5LgLoL%BJFOv9tjbnFvjB6TZxj0DqkuiwumKq!WQ4Udbnu47@GAC5fbhsZlwFjbMf@DFUYIJ2rm@8anH0hPNW1nDlUGhiGom5POL14TRVw$c^MFWCpcthKwS5ht!1Q#K&30i3VzALrT%vkKa1ldFCSeApHMZRaSNKR5tlA^jsddA74lb0e&4arwjqSkxQ3iE^Ot#y1tz3WNRtbE9Np7uediUVz95&H9W3MLMJ^iUY7Z99gFtYtVpFw!RRPhTlXSRfA#pr*#GHr9xoXO1%Eqkb8$E7#2zooWXzaSqr!t!PJ2d9yA0gguPM1wA1^7#*v'

# 主程序
if __name__ == "__main__":
    # 初始化数据库
    init_db()

    print(f"""
    欢迎来到UserHub，一个简单的用户管理系统。
    在这里，您可以注册新用户，登录，更改用户信息，以及管理用户。
    这是一个作者的练习项目，希望您能喜欢。
    如果可以，请在https://github.com/alex-jzr/user-hub 给作者一个 star。
    作者：Alex

    键入 'help' 获取帮助。{reset_color}
    """)
    input("按 Enter 键继续...")
    os.system('cls')

    # 旅游模式循环
    while user_con == 0:
        user_input = input(f"{info_color}{user}> {reset_color}")

        if user_input == "login":
            os.system('cls')
            display_message("----- Log In -----")
            user_log_name = input(f"{info_color}{user}> Please enter your name: {reset_color}")
            user_log_password = get_password(f"{info_color}{user}> Please enter your password: {reset_color}")

            # 登录功能
            user_con, user = tour_code.Login(user_log_name, user_log_password)
            if user_con == 1:
                display_message(f"Login successful! Welcome, {user}!", success_color)
                input()
            elif user_con == 2:
                display_message(f"Login successful! Welcome, root user {user}!", success_color)
                input()
            else:
                display_message("Login failed. Please check your credentials and try again.", error_color)
                input()

        elif user_input == "register":
            os.system('cls')
            display_message("---- Create New User ----")
            user_reg_name = input(f"{info_color}{user}> Please enter your name: {reset_color}")
            user_reg_password = get_password(f"{info_color}{user}> Please enter your password: {reset_color}")
            user_reg_email = input(f"{info_color}{user}> Please enter your email: {reset_color}")
            user_reg_type = input(f"{info_color}{user}> Please enter your type (user/root): {reset_color}")

            # 用户类型为 root 时需要 root 密码验证
            if user_reg_type == 'root':
                root_pass = get_password(f"{info_color}root password: {reset_color}")
                os.system('cls')
                if root_pass == rootpass:
                    tour_code.Register(user_reg_name, user_reg_password, user_reg_email, user_reg_type)
                    display_message("Root user created successfully!", success_color)
                    input()
                else:
                    display_message("Incorrect root password. User creation failed.", error_color)
                    input()
                    break
            else:
                tour_code.Register(user_reg_name, user_reg_password, user_reg_email, user_reg_type)
                os.system('cls')
                display_message(f"User {user_reg_name} created successfully!", success_color)

                input()

        elif user_input == "help":
            os.system('cls')
            display_message("---- Help ----")
            print(tour_code.tour_help_txt)
            input(".........")

        elif user_input == "exit":
            os.system('cls')
            display_message("Goodbye! Exiting...", info_color)
            input()
            break

        else:
            display_message(f"{user_input} command not found. Try entering 'help'.", error_color)

    # 普通用户循环
    while user_con == 1:
        os.system('cls')
        user_input = input(f"{info_color}{user}> {reset_color}")

        if user_input == "help":
            os.system('cls')
            display_message("---- Help ----")
            print(user_code.help_txt)
            input(".........")

        elif user_input == "exit":
            os.system('cls')
            display_message("Goodbye! Exiting...", info_color)
            user_con = 0

        elif user_input == "name_change":
            os.system('cls')
            # 用户调用名字更改
            user_code.name_change(user_con, user)
            display_message("Username updated successfully!", success_color)
            input()

        elif user_input == "password_change":
            # 用户调用密码更改
            os.system('cls')
            user_code.password_change(user_con, user)
            display_message("Password updated successfully!", success_color)
            input()

        elif user_input == "email_change":
            os.system('cls')
            # 用户调用邮箱更改
            user_code.email_change(user_con, user)
            display_message("Email updated successfully!", success_color)
            input()

        elif user_input == "permission_upgrade":
            os.system('cls')
            # 用户调用权限升级
            user_code.permission_upgrade(user_con, user, rootpass)
            display_message("Permission upgraded successfully!", success_color)
            input()

        else:
            display_message(f"{user_input} command not found. Try entering 'help'.", error_color)

    # Root 用户循环
    while user_con == 2:
        os.system('cls')
        user_input = input(f"{info_color}{user}> {reset_color}")

        if user_input == "help":
            display_message("---- Root Help ----")
            print(root_code.help_txt)
            input(".........")

        elif user_input == "exit":
            os.system('cls')
            display_message("Goodbye! Exiting...", info_color)
            input()
            user_con = 0

        elif user_input == "user_add":
            os.system('cls')
            # Root 用户调用添加用户
            root_code.user_add(rootpass, user_con)
            display_message("User added successfully!", success_color)
            input()

        elif user_input == "user_delete":
            os.system('cls')
            # Root 用户调用删除用户
            root_code.user_delete(rootpass)
            display_message("User deleted successfully!", success_color)
            input()

        elif user_input == "user_info_update":
            os.system('cls')
            # Root 用户调用更新用户信息
            root_code.user_info_update(rootpass)
            display_message("User info updated successfully!", success_color)
            input()

        elif user_input == "users_printer":
            os.system('cls')
            # Root 用户调用打印用户信息
            
            root_code.users_printer(user_con, rootpass)
            display_message("User information printed successfully!", success_color)
            input()

        else:
            display_message(f"{user_input} command not found. Try entering 'help'.", error_color)
            input()