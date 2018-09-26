from dbutil import MysqlConnection
from hashlib import sha1


username = input("请输入用户名：")
password = input("请输入密码：")

# 给password加密
s1 = sha1()
s1.update(password.encode("utf8"))    # 转码
en_password = s1.hexdigest()    # 返回十六进制加密结果
# print(en_password)

# 和数据库进行匹配
mysql = MysqlConnection("root")
sql = "select user_id from user where username='{}' and password='{}';".format(username, en_password)
result = mysql.get_all(sql)
if result:
    print("登陆成功！")
else:
    print("用户名密码错误！")
