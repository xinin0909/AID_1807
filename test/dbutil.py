from pymysql import *


class MysqlConnection(object):
    def __init__(self, password):
        self.__host = "127.0.0.1"
        self.__port = 3306
        self.__user = "root"
        self.__password = password
        self.__charset = "utf8"
        self.__database = "chatroom"

    # 连接数据库
    def __open(self):
        try:
            self.__conn = connect(host=self.__host, user=self.__user, password=self.__password, port=self.__port, database=self.__database, charset=self.__charset)
        except Exception as err:
            print("Opened Error!", err)
        self.__cur = self.__conn.cursor()

    # 关闭连接数据库
    def __close(self):
        self.__cur.close()
        self.__conn.close()

    # 执行SQL语句方法
    def exec_sql(self, sqlst):
        self.__open()
        try:
            self.__cur.execute(sqlst)
            self.__conn.commit()
            # print("Executed Success!")
            self.__close()
            return True
        except Exception as err:
            self.__conn.rollback()
            # print("Executed Failed!", err)
            self.__close()
            return False

    # 查询所有表信息的方法
    def get_all(self, sqlst):
        self.__open()
        self.__cur.execute(sqlst)
        # print("Executed Success!")
        data = self.__cur.fetchall()
        self.__close()
        return data

