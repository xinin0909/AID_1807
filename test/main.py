import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import ui_regist
import ui_login


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 实例登录窗口
    login_widget = ui_login.Ui_Form()

    # 实例注册窗口
    reg_widget = ui_regist.Ui_Form()

    # 按钮绑定事件
    btn_reg = login_widget.pushButton_regist
    btn_reg.clicked.connect(reg_widget.show)

    # 显示登录窗口
    login_widget.show()

    sys.exit(app.exec_())
