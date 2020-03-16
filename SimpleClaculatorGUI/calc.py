from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    op1 = op2 = op = ""
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('calc.ui', self)
        self.show()
        self.B1.clicked.connect(self.print1)
        self.B2.clicked.connect(self.print2)
        self.B3.clicked.connect(self.print3)
        self.B4.clicked.connect(self.print4)
        self.B5.clicked.connect(self.print5)
        self.B6.clicked.connect(self.print6)
        self.B7.clicked.connect(self.print7)
        self.B8.clicked.connect(self.print8)
        self.B9.clicked.connect(self.print9)
        self.B0.clicked.connect(self.print0)
        self.add.clicked.connect(self.addition)
        self.sub.clicked.connect(self.subtraction)
        self.mul.clicked.connect(self.multiplication)
        self.div.clicked.connect(self.division)
        self.calculate.clicked.connect(self.calculator)
        self.cls.clicked.connect(self.clear_screen)
    def print1(self):
        dis = self.display.text()
        self.display.setText(dis + "1")
    def print2(self):
        dis = self.display.text()
        self.display.setText(dis + "2")
    def print3(self):
        dis = self.display.text()
        self.display.setText(dis + "3")
    def print4(self):
        dis = self.display.text()
        self.display.setText(dis + "4")
    def print5(self):
        dis = self.display.text()
        self.display.setText(dis + "5")
    def print6(self):
        dis = self.display.text()
        self.display.setText(dis + "6")
    def print7(self):
        dis = self.display.text()
        self.display.setText(dis + "7")
    def print8(self):
        dis = self.display.text()
        self.display.setText(dis + "8")
    def print9(self):
        dis = self.display.text()
        self.display.setText(dis + "9")
    def print0(self):
        dis = self.display.text()
        self.display.setText(dis + "0") 
    def addition(self):
        self.op1 = self.display.text()
        self.display.setText("")
        self.sub_display.setText(self.op1 + " + ")
        self.op = "+"
    def subtraction(self):
        self.op1 = self.display.text()
        self.display.setText("")
        self.sub_display.setText(self.op1 + " - ")
        self.op = "-"
    def multiplication(self):
        self.op1 = self.display.text()
        self.display.setText("")
        self.sub_display.setText(self.op1 + " * ")
        self.op = "*"
    def division(self):
        self.op1 = self.display.text()
        self.display.setText("")
        self.sub_display.setText(self.op1 + " / ")
        self.op = "/"            
    def clear_screen(self):
        self.display.setText("")
        self.sub_display.setText("")
    def calculator(self):
        self.op2 = self.display.text()
        if self.op == "+":
            self.sub_display.setText(self.sub_display.text() + self.op2)
            sum = float(self.op1) + float(self.op2)
            self.display.setText(str('%g'%(sum)))
        elif self.op == "-":
            self.sub_display.setText(self.sub_display.text() + self.op2)
            sub = float(self.op1) - float(self.op2)
            self.display.setText(str('%g'%(sub)))
        elif self.op == "*":
            self.sub_display.setText(self.sub_display.text() + self.op2)
            mul = float(self.op1) * float(self.op2)
            self.display.setText(str('%g'%(mul)))
        else:
            self.sub_display.setText(self.sub_display.text() + self.op2)
            div = float(self.op1) / float(self.op2)
            self.display.setText(str('%g'%(div)))

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()s
