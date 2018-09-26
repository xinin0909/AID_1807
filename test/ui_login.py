# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
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
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(464, 254)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(464, 254))
        self.setMaximumSize(QtCore.QSize(464, 254))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/login.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 91, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_login = QtWidgets.QPushButton(self)
        self.pushButton_login.setGeometry(QtCore.QRect(100, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_regist = QtWidgets.QPushButton(self)
        self.pushButton_regist.setGeometry(QtCore.QRect(260, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton_regist.setFont(font)
        self.pushButton_regist.setObjectName("pushButton_regist")
        self.lineEdit_username = QtWidgets.QLineEdit(self)
        self.lineEdit_username.setGeometry(QtCore.QRect(140, 40, 281, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_passwd = QtWidgets.QLineEdit(self)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(140, 100, 281, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.lineEdit_passwd.setFont(font)
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")

        self.retranslateUi(self)
        self.pushButton_login.clicked.connect(self.btnLoginClicked)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "i Chat"))
        self.label.setText(_translate("Form", "账 号："))
        self.label_2.setText(_translate("Form", "密 码："))
        self.pushButton_login.setText(_translate("Form", "登 陆"))
        self.pushButton_regist.setText(_translate("Form", "注 册"))

    def btnLoginClicked(self):
        # 创建提示对话框对象
        msg_box = QtWidgets.QMessageBox()

        # 从输入框中获取文本
        username = self.lineEdit_username.text()
        password = self.lineEdit_passwd.text()

        # 给password加密
        s1 = sha1()
        s1.update(password.encode("utf8"))  # 转码
        en_password = s1.hexdigest()  # 返回十六进制加密结果

        # 和数据库进行匹配
        mysql = MysqlConnection("root")
        sql = "select user_id from user where username='{}' and password='{}';".format(username, en_password)
        result = mysql.get_all(sql)
        if result:
            msg_box.warning(None, "Success", "登陆成功",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        else:
            msg_box.warning(None, "Error", "用户名密码错误！",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
