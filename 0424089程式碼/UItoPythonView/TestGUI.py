from PyQt5.QtWidgets import QLabel,QApplication,QDesktopWidget,QPushButton\
    ,QHBoxLayout,QWidget,QToolTip,QMainWindow,QVBoxLayout
from PyQt5.QtGui import QFont,QPalette,QIcon,QPixmap
from PyQt5.QtCore import Qt
import sys
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.center()
        self.initUI()
        self.components()
    def components(self):

        labelPic = QLabel(self)
        labelPic.setAlignment(Qt.AlignCenter)
        labelPic.setToolTip("NKFUST")
        labelPic.setPixmap(QPixmap("../image/nkfust.jpg"))

        labelExt = QLabel(self)
        labelExt.setText("<a href='https://github.com/WeiJiaZheng'>Jia Github")
        labelExt.setAlignment(Qt.AlignRight)
        labelExt.setOpenExternalLinks(True)
        labelExt.setToolTip("Github")

        closeButton=QPushButton("Close Main window")
        closeButton.clicked.connect(self.closeButtonEvent)

        vbox=QVBoxLayout()
        vbox.addWidget(labelPic)
        vbox.addStretch()
        vbox.addWidget(labelExt)
        vbox.addStretch()
        vbox.addWidget(closeButton)
        vbox.addStretch()
        self.setLayout(vbox)
    """置中函數"""
    def center(self):
        screen=QDesktopWidget().geometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def initUI(self):
        #app title
        self.setWindowTitle("Qt_-Test")
        #app Icon
        self.setWindowIcon(QIcon(""))
    #close window
    def closeButtonEvent(self):
        Qapp=QApplication.instance()
        Qapp.quit()
if __name__=="__main__":
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())