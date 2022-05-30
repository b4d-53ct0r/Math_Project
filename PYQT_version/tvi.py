from PyQt5 import QtCore, QtGui, QtWidgets
from math import *
ln = log
e = exp
class Ui_tvi(object):
    def action(self):
        def check(f , a, b):
            x = a
            y_a = eval(f)
            x = b
            y_b = eval(f)
            if y_a*y_b > 0 :
                self.label.setText("your interval or your function is not valid")
                return 0
            else:
                return 1
        def find_interval(f,a,b,p):
            mid = (b+a)/2
            x = a
            y_a = eval(f)
            x = b
            y_b = eval(f)
            x = mid
            y_mid = eval(f)
                
            if y_mid * y_a < 0:
                return find_interval(f,a,mid,1)
            if y_mid * y_b  < 0:
                return find_interval(f,mid,b,0)
            if y_mid * y_a > 0 and y_mid * y_b > 0:
                if p == 1:
                    a = mid*2-b
                if p == 0:
                    b=2*(mid)-a
            return [a,b]
            
        def main():
            
            f = self.lineEdit_3.text()
            a = float(self.lineEdit_2.text())
            b = float(self.lineEdit_4.text())
            #validity check
            if check(f,a,b) == 0:
                return 0
            else:
                
                self.label.setText(str(find_interval(f,a,b,2)))
                
        if "__main__"== __name__:
            main()
            
    def setupUi(self, tvi):
        tvi.setObjectName("tvi")
        tvi.resize(672, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dl.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tvi.setWindowIcon(icon)
        tvi.setStyleSheet("*{\n"
"    background-color: rgb(231, 236, 252);\n"
"    color:rgb(20, 30, 39);\n"
"    text-align:center;\n"
"    font-size: 22px;\n"
"    \n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(tvi)
        self.label.setGeometry(QtCore.QRect(30, 300, 621, 111))
        self.label.setStyleSheet("QLabel{\n"
"    background-color: rgb(42, 88, 127);\n"
"    text-align:center;\n"
"    font-size: 18px;\n"
"    padding: 0px 16px;\n"
"    border-radius: 12px;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(tvi)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 115, 101, 71))
        self.lineEdit_2.setStyleSheet(".QLineEdit{\n"
"    border-radius: 12px;\n"
"    border: 2px solid rgb(231, 236, 252);\n"
"    padding: 0px 20px;\n"
"    background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border:2px solid rgb(42, 88, 127);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(tvi)
        self.label_2.setGeometry(QtCore.QRect(110, 136, 110, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{\n"
        "    font-size: 27px;\n"
        "\n"
"}")
        self.lineEdit_3 = QtWidgets.QLineEdit(tvi)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 35, 371, 71))
        self.lineEdit_3.setStyleSheet(".QLineEdit{\n"
"    border-radius: 12px;\n"
"    border: 2px solid rgb(231, 236, 252);\n"
"    padding: 0px 20px;\n"
"    background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border:2px solid rgb(42, 88, 127);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(tvi)
        self.label_3.setGeometry(QtCore.QRect(110, 48, 44, 41))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{\n"
        "    font-size: 27px;\n"
        "\n"
"}")
        self.lineEdit_4 = QtWidgets.QLineEdit(tvi)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 195, 101, 71))
        self.lineEdit_4.setStyleSheet(".QLineEdit{\n"
"    border-radius: 12px;\n"
"    border: 2px solid rgb(231, 236, 252);\n"
"    padding: 0px 20px;\n"
"    background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border:2px solid rgb(42, 88, 127);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(tvi)
        self.label_4.setGeometry(QtCore.QRect(110, 215, 115, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("QLabel{\n"
        "    font-size: 27px;\n"
        "\n"
"}")
        self.pushButton = QtWidgets.QPushButton(tvi, clicked = lambda:self.action())
        self.pushButton.setGeometry(QtCore.QRect(400, 145, 141, 91))
        self.pushButton.setStyleSheet(".QPushButton{\n"
"    border-radius: 12px;\n"
"    background-color:rgb(42, 88, 127);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
".QPushButton:Hover{\n"
"    background-color:rgb(102, 193, 167);\n"
"    border-radius: 12px;\n"
"color:rgb(0, 0, 0);\n"
"}")
       
        self.retranslateUi(tvi)
        QtCore.QMetaObject.connectSlotsByName(tvi)

    def retranslateUi(self, tvi):
        _translate = QtCore.QCoreApplication.translate
        tvi.setWindowTitle(_translate("tvi", "Tvi"))
        self.label_2.setText(_translate("tvi", "a :"))
        self.label_3.setText(_translate("tvi", "f(X) = "))
        self.label_4.setText(_translate("tvi", "b :"))
        self.pushButton.setText(_translate("tvi", "TROUVER"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tvi = QtWidgets.QDialog()
    ui = Ui_tvi()
    ui.setupUi(tvi)
    tvi.show()
    sys.exit(app.exec_())
