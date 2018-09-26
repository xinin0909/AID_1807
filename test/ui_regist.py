# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regist.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from dbutil import MysqlConnection
from hashlib import sha1
import sys

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(516, 402)
        self.setMinimumSize(QtCore.QSize(516, 402))
        self.setMaximumSize(QtCore.QSize(516, 402))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.setFont(font)
        self.label_username = QtWidgets.QLabel(self)
        self.label_username.setGeometry(QtCore.QRect(100, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_passwd = QtWidgets.QLabel(self)
        self.label_passwd.setGeometry(QtCore.QRect(100, 110, 91, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_passwd.setFont(font)
        self.label_passwd.setObjectName("label_passwd")
        self.label_passwd_2 = QtWidgets.QLabel(self)
        self.label_passwd_2.setGeometry(QtCore.QRect(30, 170, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_passwd_2.setFont(font)
        self.label_passwd_2.setObjectName("label_passwd_2")
        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setGeometry(QtCore.QRect(100, 230, 91, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.pushButton_regist = QtWidgets.QPushButton(self)
        self.pushButton_regist.setGeometry(QtCore.QRect(200, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.pushButton_regist.setFont(font)
        self.pushButton_regist.setObjectName("pushButton_regist")
        self.lineEdit_username = QtWidgets.QLineEdit(self)
        self.lineEdit_username.setGeometry(QtCore.QRect(200, 60, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_passwd = QtWidgets.QLineEdit(self)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(200, 120, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.lineEdit_passwd.setFont(font)
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.lineEdit_passwd_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_passwd_2.setGeometry(QtCore.QRect(200, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.lineEdit_passwd_2.setFont(font)
        self.lineEdit_passwd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd_2.setObjectName("lineEdit_passwd_2")
        self.lineEdit_email = QtWidgets.QLineEdit(self)
        self.lineEdit_email.setGeometry(QtCore.QRect(200, 240, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.retranslateUi(self)
        self.pushButton_regist.clicked.connect(self.buttonOkClicked)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "i Chat 注册"))
        self.label_username.setText(_translate("Form", "用户名："))
        self.label_passwd.setText(_translate("Form", "密  码："))
        self.label_passwd_2.setText(_translate("Form", "再次输入密码："))
        self.label_email.setText(_translate("Form", "邮  箱："))
        self.pushButton_regist.setText(_translate("Form", "确 认"))

    def buttonOkClicked(self):
        # 创建提示对话框对象
        msg_box = QtWidgets.QMessageBox()

        # 从输入框中获取文本
        username = self.lineEdit_username.text()
        password1 = self.lineEdit_passwd.text()
        password2 = self.lineEdit_passwd_2.text()
        email = self.lineEdit_email.text()

        # 输入检测
        if not (username and password1 and password2 and email):
            msg_box.warning(None, "Error", "输入信息不完整！请重新输入！",
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        else:
            if password1 != password2:
                msg_box.warning(None, "Error", "两次输入密码不一致！",
                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            else:
                # 给password加密
                s1 = sha1()
                s1.update(password2.encode("utf8"))  # 转码
                en_password = s1.hexdigest()  # 返回十六进制加密结果

                # 插入数据库
                mysql = MysqlConnection("root")
                sql = "insert into user(`username`,`password`) values('{}','{}');".format(username, en_password)
                if mysql.exec_sql(sql):
                    msg_box.warning(None, "Success", "注册成功！",
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                    # 关闭对话框
                    self.close()
                else:
                    msg_box.warning(None, "Error", "注册失败！请重试！",
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
