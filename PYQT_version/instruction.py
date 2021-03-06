

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_instruction(object):
    def setupUi(self, instruction):
        instruction.setObjectName("instruction")
        instruction.resize(500, 550)
        instruction.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("instructions.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        instruction.setWindowIcon(icon)
        instruction.setStyleSheet("*{\n"
"    background-color: rgb(238, 237, 222);\n"
"}")
        self.label = QtWidgets.QLabel(instruction)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 551))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(1)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("*{\n"
"    background-color: rgb(231, 236, 252);\n"
"    color:rgb(20, 30, 39);\n"
"    text-align:center;\n"
"    font-size: 20px;\n"
"    padding:30%;\n"
"    \n"
"}")
        self.label.setObjectName("label")

        self.retranslateUi(instruction)
        QtCore.QMetaObject.connectSlotsByName(instruction)

    def retranslateUi(self, instruction):
        _translate = QtCore.QCoreApplication.translate
        instruction.setWindowTitle(_translate("instruction", "instruction"))
        self.label.setText(_translate("instruction", "•    abs: absolute value\n"
"•    acos: arc cosine\n"
"•    asin: arc sine\n"
"•    atan: arc tangent\n"
"•    cbrt: cubic root\n"
"•    ceil: nearest upper integer\n"
"•    cos: cosine\n"
"•    cosh: hyperbolic cosine\n"
"•    e: euler\'s number raised to the power (e^x)\n"
"•    floor: nearest lower integer\n"
"•    ln: logarithmus naturalis (base e)\n"
"•    log10: logarithm (base 10)\n"
"•    log2: logarithme naturel (base 2)\n"
"•    sin: sine\n"
"•    sinh: hyperbolic sine\n"
"•    sqrt: square root\n"
"•    tan: tangent\n"
"•    tanh: hyperbolic tangent\n"
"•    signum: signum function\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    instruction = QtWidgets.QDialog()
    ui = Ui_instruction()
    ui.setupUi(instruction)
    instruction.show()
    sys.exit(app.exec_())
