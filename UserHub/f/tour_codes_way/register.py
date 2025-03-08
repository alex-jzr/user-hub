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

#Register("Alex_ji","12141327","3388134545@qq.com","user")