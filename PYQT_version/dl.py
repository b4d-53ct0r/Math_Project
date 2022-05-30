from PyQt5 import QtCore, QtGui, QtWidgets
from sympy import *
from math import *
from pandas.io import clipboard

class Ui_dl(object):
    def copy(self):
            clipboard.copy(self.label.text())
    def action(self):
        x = symbols('x')
        f = self.lineEdit_3.text()
        N = int(self.spinBox.text())
        A = int(self.lineEdit_2.text())
        e = exp
        ln = log
        def der(f,n):
            df = str(diff(f.replace("e","exp"),x,n)).replace("exp","e")
            return df
        def fact(x):
            s=1
            for i in range(1,x+1):
                s=s*i
            return s
        l=[]
        for i in range(0,N+1):
            c=eval(str(der(f,i)).replace("x",str(A)))
            l=l+[c/fact(i)]
        lf=""
        for i in range(0,N+1):
            lf = lf + "+"+str(((x-A)**i)*l[i])
        lhal = "f(x) = "+str(eval(lf))
        self.label.setText(lhal)
        return lhal

    
    
    def setupUi(self, dl):
        dl.setObjectName("dl")
        dl.resize(672, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dl.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dl.setWindowIcon(icon)
        dl.setStyleSheet("*{\n"
"    background-color: rgb(231, 236, 252);\n"
"    color:rgb(20, 30, 39);\n"
"    text-align:center;\n"
"    font-size: 22px;\n"
"    \n"
"}\n"
"\n"
"")
        self.pushButton = QtWidgets.QPushButton(dl, clicked = lambda:self.action())
        self.pushButton.setGeometry(QtCore.QRect(400, 145, 141, 91))
        self.pushButton.setStyleSheet(".QPushButton{\n"
"    border-radius: 12px;\n"

"    background-color:rgb(102, 193, 167);\n"

"}\n"
"\n"
".QPushButton:Hover{\n"
"    background-color:rgb(42, 88, 127);\n"
"    border-radius: 12px;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(dl)
        self.spinBox.setGeometry(QtCore.QRect(250, 115, 101, 71))
        self.spinBox.setStyleSheet(".QSpinBox{\n"
"    border-radius: 6px;\n"
"    border: 2px solid rgb(231, 236, 252);\n"
"    text-align:center;\n"
"    padding: 0px 18px;\n"
"    background-color:rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(dl)
        self.label_4.setGeometry(QtCore.QRect(110, 136, 110, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("QLabel{\n"
        "    font-size: 27px;\n"
        "\n"
"}")
        self.label = QtWidgets.QLabel(dl)
        self.label.setGeometry(QtCore.QRect(30, 300, 621, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    background-color: rgb(102, 193, 167);\n"
"    text-align:center;\n"
"    font-size: 20px;\n"
"    padding: 0px 16px;\n"
"    border-radius: 12px;\n"
"    color:rgb(0, 0, 0);\n"
"\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(dl)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 195, 101, 71))
        self.lineEdit_2.setStyleSheet(".QLineEdit{\n"
"    border-radius: 12px;\n"
"    border: 2px solid rgb(231, 236, 252);\n"
"    padding:10px;\n"
"    background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border:2px solid rgb(102, 193, 167);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(dl)
        self.label_2.setGeometry(QtCore.QRect(110, 215, 115, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{\n"
        "    font-size: 27px;\n"
        "\n"
"}")
        self.lineEdit_3 = QtWidgets.QLineEdit(dl)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 35, 371, 71))
        self.lineEdit_3.setStyleSheet(".QLineEdit{\n"
"    border-radius: 12px;\n"
"    border: 2px solid rgb(231, 236, 252);\n"
"    padding: 0px 20px;\n"
"    background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border:2px solid rgb(102, 193, 167);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(dl)
        self.label_3.setGeometry(QtCore.QRect(110, 48, 44, 41))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{\n"
        "    font-size: 27px;\n"
        "\n"
"}")
        self.toolButton = QtWidgets.QToolButton(dl,clicked = lambda:self.copy())
        self.toolButton.setGeometry(QtCore.QRect(595, 325, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(1)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("QToolButton{\n"
"    \n"
"    background-color: none;\n"
"    border:none;\n"
"    font-size:30px\n"
"}")
        self.toolButton.setObjectName("toolButton")


        self.retranslateUi(dl)
        QtCore.QMetaObject.connectSlotsByName(dl)

    

    def retranslateUi(self, dl):
        _translate = QtCore.QCoreApplication.translate
        dl.setWindowTitle(_translate("dl", "Développement Limité "))
        self.pushButton.setText(_translate("dl", "CALCULER"))
        self.label_4.setText(_translate("dl", "D'ordre :"))
        self.lineEdit_2.setText(_translate("dl", "0"))
        self.label_2.setText(_translate("dl", "Au point :"))
        self.label_3.setText(_translate("dl", "f(X) = "))
        self.toolButton.setText(_translate("dl", "📋"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dl = QtWidgets.QDialog()
    ui = Ui_dl()
    ui.setupUi(dl)
    dl.show()
    sys.exit(app.exec_())
