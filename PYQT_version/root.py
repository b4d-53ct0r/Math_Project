from PyQt5 import QtCore, QtGui, QtWidgets
from dl import Ui_dl
from tvi import Ui_tvi
from instruction import Ui_instruction
from details import Ui_details



class Ui_root(object):
    def opendl(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_dl()
        self.ui.setupUi(self.window)
        self.window.show()
    def opentvi(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_tvi()
        self.ui.setupUi(self.window)
        self.window.show()
    def openinstruction(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_instruction()
        self.ui.setupUi(self.window)
        self.window.show()
    def opendetails(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_details()
        self.ui.setupUi(self.window)
        self.window.show()
    





    
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(672, 430)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        root.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("root.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        root.setWindowIcon(icon)
        root.setStyleSheet("*{\n"
"    background-color: qlineargradient(spread:pad, x1:0.186, y1:0.193273, x2:0.995, y2:0.988636, stop:0 rgba(124, 232, 182, 255), stop:1 rgba(0, 14, 99, 255));\n"
"    color:rgb(20, 30, 39);\n"
"    text-align:center;\n"
"    font-size: 32px;\n"
"    \n"
"}\n"
"\n"
"")
        self.pushButton = QtWidgets.QPushButton(root, clicked = lambda:self.opendetails())
        self.pushButton.setGeometry(QtCore.QRect(440, 360, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(".QPushButton{\n"
"    border-radius: 12px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
".QPushButton:Hover{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius: 12px;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(root)
        self.label.setGeometry(QtCore.QRect(252, 20, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet(".QLabel{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
".QLabel:hover{\n"
"    color:rgb(20, 30, 39)\n"
"\n"
"}\n"
"")
        self.label.setObjectName("label")

        self.label_5 = QtWidgets.QLabel(root)
        self.label_5.setGeometry(QtCore.QRect(236, 90, 250, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setStyleSheet(".QLabel{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"    color:rgb(255, 255, 255);\n"
"    font-size: 50px;\n"
"\n"
"}\n"

"")
        self.label_5.setObjectName("label")


        self.pushButton_2 = QtWidgets.QPushButton(root, clicked = lambda:self.opendl())
        self.pushButton_2.setGeometry(QtCore.QRect(410, 175, 181, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(".QPushButton{\n"
"    border-radius: 12px;\n"
"    border: 2px solid rgb(102, 193, 167);\n"
"background-color: rgb(102, 193, 167);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
".QPushButton:Hover{\n"
"    background-color:rgb(240, 243, 252);\n"
"color:rgb(0, 0, 0);\n"

"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(root, clicked = lambda:self.opentvi())
        self.pushButton_3.setGeometry(QtCore.QRect(100, 175, 181, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(".QPushButton{\n"
"  border-radius: 12px;\n"
"    border: 2px solid rgb(42, 88, 127);\n"
"background-color:rgb(42, 88, 127);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
".QPushButton:Hover{\n"
"    background-color:rgb(240, 243, 252);\n"
"color:rgb(0, 0, 0);\n"

"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(root)
        self.label_2.setGeometry(QtCore.QRect(185, 360, 285, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(".QLabel{\n"
        "font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"

"")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(root, clicked = lambda:self.openinstruction())
        self.pushButton_4.setGeometry(QtCore.QRect(500, 360, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(".QPushButton{\n"
"    border-radius: 12px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
".QPushButton:Hover{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius: 12px;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "MATH PROJECT"))
        self.pushButton.setText(_translate("root", "©"))
        self.label.setText(_translate("root", "Math Project"))
        self.pushButton_2.setText(_translate("root", "DL"))
        self.pushButton_3.setText(_translate("root", "TVI"))
        self.label_2.setText(_translate("root", "MADE WITH LOVE 🤍"))
        self.pushButton_4.setText(_translate("root", "?"))
        self.label_5.setText(_translate("root", "WELCOME"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QDialog()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
