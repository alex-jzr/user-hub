# UserHub

## root密码！！！

%A%888wSR5ZnwgzBnQtNIM0ggWsTFRyvi1jFE7E7IYb01gGHDH5S1fcByMwm7DoqxZNmbYyq8SeeYWOx9LZ9N3CsA2TXgceJeWQMDpwgx1r!Sg!VcxAJpHZi**4dDYqCcte@9kcWy#AbX5dX9DrP7b41Ljs!g7gM@64Wcy3@918o4HKT9gWMCdjNaG$hH1KX3IyOlfVF#VQC26VFzc4S4zeGM0QodEba&So@kw6hJUWSU$q%Wf4w^py#AKY5^$pkGm7yKVCRhxpS7Tiq1O5HXTn7bh9T$P&4bpNqSTtDfoSNSsjKrRKnC$PB$qtq3E3rehvRB#Pt4jTByRv^vizGCzwAvE&xB0k8%GDumK!61ez5#uyFDDYcsLaM^LETt0dIWW0pmm&BjhCzt7k20MpYKVgWX7uH0h&mKTiXhTPr%8XzP@AP0cid2kMMe%EROML&@#L5mDvxC^2LOPKOLYXL4uoX$42nFdc#AgHck!&y@oWtNhW%GIGdIIBvcUk6XDG2LtNXzv8xGPRgj%!uzAcv9BUQqjIvYRWXR2qzD$z@XRTggwFigtEDU6yn@S2@HxKbnXP6$sQIkXxbK5T6QuL!X6vrKNEp4wvam#&BlYvT4Mo9BMUOuBw#rHMjAewmk%$xo#k%RorZxafEvB&J0AtuDQ$snfIk#gWSvBH%Zo77t6IJ573Vi^fO5LgLoL%BJFOv9tjbnFvjB6TZxj0DqkuiwumKq!WQ4Udbnu47@GAC5fbhsZlwFjbMf@DFUYIJ2rm@8anH0hPNW1nDlUGhiGom5POL14TRVw$c^MFWCpcthKwS5ht!1Q#K&30i3VzALrT%vkKa1ldFCSeApHMZRaSNKR5tlA^jsddA74lb0e&4arwjqSkxQ3iE^Ot#y1tz3WNRtbE9Np7uediUVz95&H9W3MLMJ^iUY7Z99gFtYtVpFw!RRPhTlXSRfA#pr*#GHr9xoXO1%Eqkb8$E7#2zooWXzaSqr!t!PJ2d9yA0gguPM1wA1^7#*v'


## 项目介绍

呃…这个东西其实是 **Alex** 在无聊的时候写的一个命令行用户管理系统。如果你认为它看起来很简单，那当然是的！我也没打算做什么复杂的东西，毕竟只是我打发时间的一点小尝试。

不过，虽然看起来有点像“玩具”，它还是完成了用户注册、登录、权限管理这些基本功能。毕竟，程序员的意义就是为了那些看起来“无用”的功能而不断创造和尝试，不是吗？ 😎

## 功能概述

1. **用户注册与登录**  
   用户可以创建账号，并通过提供用户名、密码和邮箱进行注册。登录时需要输入用户名和密码来验证身份。 🎶

2. **权限管理**  
   用户角色有两种：普通用户和管理员。管理员（root）可以进行更高级的操作，比如权限升级、删除用户等。普通用户只能进行一些基本的操作，比如修改自己的用户名和密码。 😏

3. **用户信息管理**  
   你可以修改自己的用户名、密码和邮箱，这些信息都保存在一个简单的 `usermessage.txt` 文件中。你甚至可以用记事本打开它看一下…是不是很原始？ 🤘

4. **管理员（root）操作**  
   管理员可以将普通用户的权限提升为 root 权限，从而获得更多的操作权限。没有管理员权限的用户只能乖乖地待在自己的小圈子里，无法改变其他用户的信息。 😈

5. **用户组管理**  
   至于用户组嘛…如果你真心想为这个系统加点什么，自己动手，写一个吧。反正这项目已经有点够了，剩下的就看你自己想不想弄。 💀

---

## 使用流程

1. 登录：
   ```
   > login
   Please enter your name: <用户名>
   Please enter your password: <密码>
   ```

2. 注册：
   ```
   > register
   Please enter your name: <用户名>
   Please enter your password: <密码>
   Please enter your email: <邮箱>
   Please enter your type (user/root): <用户类型>
   ```

3. 修改个人信息：
   - 修改用户名：
     ```
     > name_change
     Enter your new username (current: <当前用户名>): <新用户名>
     Username updated successfully.
     ```

   - 修改密码：
     ```
     > password_change
     Enter your new password: <新密码>
     Password updated successfully.
     ```

   - 修改邮箱：
     ```
     > email_change
     Enter your new email (current: <当前邮箱>): <新邮箱>
     Email updated successfully.
     ```

   - 权限升级（管理员专用）：
     ```
     > permission_upgrade
     Enter the root password to upgrade your permissions: <root密码>
     User upgraded to root successfully.
     ```

4. 获取帮助：
   ```
   > help
   Available commands:
   - name_change: Change your username.
   - password_change: Change your password.
   - email_change: Change your email.
   - permission_upgrade: Upgrade your permissions to root (requires root password).
   - exit: Exit the program.
   ```

5. 退出：
   ```
   > exit
   Goodbye! Exiting...
   ```

---

## 未来目标与计划

虽然这玩意儿现在看起来就像个纯粹的命令行工具，但未来嘛，我也许会考虑加个图形化界面…但可能性很小。毕竟，我就这样写着玩，不会做太多的优化或者添加功能，简单好用就行。 🤡

再说了，这系统并不复杂。未来的目标是让它能满足基本需求，不管是做什么都要用最简单的方式。至于是否能扩展到更大的应用场景？嗯…也许吧，但先让它在这里完成当前目标再说。 🤘

---

## 注意事项

1. 代码挺简陋的，写得有点马虎，但如果你能接受这点“粗糙”，那就好。 🦹‍♂️  
2. 这个系统可能不适用于正式生产环境，除非你真想用它来玩玩。 🎸  
3. 如果你觉得它还不错，可以随便修改，但别指望它会有任何“高级”的功能。 😏

---

**Alex，签名** ✌️

---
