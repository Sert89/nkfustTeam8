from CreateForm import Ui_CreateAccount
from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_LoginUI(object):
    def setupUi(self, LoginUI):
        LoginUI.setObjectName("LoginUI")
        LoginUI.resize(439, 310)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginUI.sizePolicy().hasHeightForWidth())
        LoginUI.setSizePolicy(sizePolicy)
        LoginUI.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 222, 255, 255), stop:0.55 rgba(59, 144, 235, 255), stop:0.98 rgba(25, 78, 255, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")
        self.username_label = QtWidgets.QLabel(LoginUI)
        self.username_label.setGeometry(QtCore.QRect(70, 120, 100, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setMidLineWidth(1)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(LoginUI)
        self.password_label.setGeometry(QtCore.QRect(80, 180, 70, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.username_Edit = QtWidgets.QLineEdit(LoginUI)
        self.username_Edit.setGeometry(QtCore.QRect(180, 110, 113, 22))
        self.username_Edit.setObjectName("username_Edit")
        self.password_Edit = QtWidgets.QLineEdit(LoginUI)
        self.password_Edit.setGeometry(QtCore.QRect(180, 170, 113, 22))
        self.password_Edit.setObjectName("password_Edit")
        self.LoginButton = QtWidgets.QPushButton(LoginUI)
        self.LoginButton.setGeometry(QtCore.QRect(100, 230, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setObjectName("LoginButton")
        self.SignButton = QtWidgets.QPushButton(LoginUI)
        self.SignButton.setGeometry(QtCore.QRect(220, 230, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SignButton.setFont(font)
        self.SignButton.setObjectName("SignButton")
        self.login_label = QtWidgets.QLabel(LoginUI)
        self.login_label.setGeometry(QtCore.QRect(130, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.retranslateUi(LoginUI)
        QtCore.QMetaObject.connectSlotsByName(LoginUI)
        """
                connect Event
                components edit
                """
        self.password_Edit.setEchoMode(QLineEdit.NoEcho)
        self.SignButton.clicked.connect(self.sign_clicked)
        self.LoginButton.clicked.connect(self.login_clicked)
    def retranslateUi(self, LoginUI):
        _translate = QtCore.QCoreApplication.translate
        LoginUI.setWindowTitle(_translate("LoginUI", "CVSystem"))
        self.username_label.setText(_translate("LoginUI", "使用者名稱"))
        self.password_label.setText(_translate("LoginUI", "密碼"))
        self.LoginButton.setText(_translate("LoginUI", "登入"))
        self.SignButton.setText(_translate("LoginUI", "註冊"))
        self.login_label.setText(_translate("LoginUI", "登入畫面"))

    """
            Extra Method
        """
    def sign_clicked(self):
        self.createAccountForm=QDialog()
        self.ui=Ui_CreateAccount()
        self.ui.setupUi(self.createAccountForm)
        self.createAccountForm.show()
    def login_clicked(self):
        username=self.username_Edit.text()
        password=self.password_Edit.text()
        connection = sqlite3.connect('../DB/login.db')
        result=connection.execute("SELECT *FROM USERS WHERE USERNAME = ?AND PASSWORD=?",(username,password))
        if (len(result.fetchall())>0):
            self.password_Edit.setText("")
            self.username_Edit.setText("")
            self.showMessageBox("通過","進入系統")
        else:
            self.password_Edit.setText("")
            self.showMessageBox("警告","使用者或密碼錯誤")
    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
if __name__ == "__main__":
    import sys
    app =QApplication(sys.argv)
    Dialog =QDialog()
    ui = Ui_LoginUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())