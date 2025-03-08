def users_printer(user_con,root_password):
    password_in = input("enter root password:")
    if user_con == 2 and password_in == root_password:
        with open('E:\\code\\python_code\\UserHub\\usermessage.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                print (f"===========users inpormatiopn=========\n{line.strip()}")


