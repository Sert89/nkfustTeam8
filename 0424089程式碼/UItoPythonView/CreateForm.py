from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_CreateAccount(object):
    def setupUi(self,CreateAccount):
        CreateAccount.setObjectName("CreateAccount")
        CreateAccount.resize(434, 312)
        CreateAccount.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 254, 219, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(250, 255, 237, 255), stop:1 rgba(230, 255, 216, 255));\n"
"}")
        self.username_label = QtWidgets.QLabel(CreateAccount)
        self.username_label.setGeometry(QtCore.QRect(70, 100, 80, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(CreateAccount)
        self.password_label.setGeometry(QtCore.QRect(70, 140, 80, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.email_label = QtWidgets.QLabel(CreateAccount)
        self.email_label.setGeometry(QtCore.QRect(70, 180, 80, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.lineusername = QtWidgets.QLineEdit(CreateAccount)
        self.lineusername.setGeometry(QtCore.QRect(170, 100, 113, 22))
        self.lineusername.setObjectName("lineusername")
        self.linepassword = QtWidgets.QLineEdit(CreateAccount)
        self.linepassword.setGeometry(QtCore.QRect(170, 140, 113, 22))
        self.linepassword.setObjectName("linepassword")
        self.lineemail = QtWidgets.QLineEdit(CreateAccount)
        self.lineemail.setGeometry(QtCore.QRect(170, 180, 113, 22))
        self.lineemail.setObjectName("lineemail")
        self.buttonSign = QtWidgets.QPushButton(CreateAccount)
        self.buttonSign.setGeometry(QtCore.QRect(160, 230, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonSign.setFont(font)
        self.buttonSign.setObjectName("buttonSign")
        self.creat__label = QtWidgets.QLabel(CreateAccount)
        self.creat__label.setGeometry(QtCore.QRect(140, 40, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.creat__label.setFont(font)
        self.creat__label.setObjectName("creat__label")
        self.retranslateUi(CreateAccount)
        QtCore.QMetaObject.connectSlotsByName(CreateAccount)
        """connect Event
                """
        self.linepassword.setEchoMode(QLineEdit.Password)
        self.buttonSign.clicked.connect(self.insertUserData)
    def retranslateUi(self, CreateAccount):
        _translate = QtCore.QCoreApplication.translate
        CreateAccount.setWindowTitle(_translate("CreateAccount", "創建新帳戶"))
        self.username_label.setText(_translate("CreateAccount", "使用者名稱"))
        self.password_label.setText(_translate("CreateAccount", "密碼"))
        self.email_label.setText(_translate("CreateAccount", "Email"))
        self.buttonSign.setText(_translate("CreateAccount", "註冊"))
        self.creat__label.setText(_translate("CreateAccount", "創建新帳戶"))
    def insertUserData(self):
        username=self.lineusername.text()
        email=self.lineemail.text()
        password=self.linepassword.text()
        connection = sqlite3.connect('../DB/login.db')
        result = connection.execute("SELECT *FROM USERS WHERE USERNAME = ?OR EMAIL=?", (username,email))
        if (len(result.fetchall()) > 0):
            self.showMessageBox("警告", "使用者存在")
        else:
            if username=="" or email=="" or password=="":
                self.showMessageBox("警告", "空白存在")
            else:
                connection.execute("INSERT INTO USERS VALUES(?,?,?)", (username, email, password))
                connection.commit()
        connection.close()
    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
if __name__ == "__main__":
    import sys
    app =QApplication(sys.argv)
    Dialog =QDialog()
    ui = Ui_CreateAccount()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
