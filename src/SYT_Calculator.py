import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("/home/addinedu/dev_ws/PyQt/src/SYT_Calculator.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SYT_Calculator!")

        self.setStyleSheet("background-color: darkgray;")
        self.equation.setStyleSheet("background-color: darkgray")         


        self.equation.setText('')
        self.result = self.equation.text()
        self.equation_list = []
        self.solve_list = []
        self.paren_flag = 0
        self.idx = 0
        self.sign_idx = 0
        self.sign_flag = 0


        self.button_add.clicked.connect(lambda state, operation = '+': self.button_operation_clicked(operation))
        self.button_sub.clicked.connect(lambda state, operation = '-': self.button_operation_clicked(operation))
        self.button_mul.clicked.connect(lambda state, operation = '*': self.button_operation_clicked(operation))
        self.button_div.clicked.connect(lambda state, operation = '/': self.button_operation_clicked(operation))
    

        self.button_1.clicked.connect(lambda state, num = '1': self.button_num_clicked(num))
        self.button_2.clicked.connect(lambda state, num = '2': self.button_num_clicked(num))
        self.button_3.clicked.connect(lambda state, num = '3': self.button_num_clicked(num))
        self.button_4.clicked.connect(lambda state, num = '4': self.button_num_clicked(num))
        self.button_5.clicked.connect(lambda state, num = '5': self.button_num_clicked(num))
        self.button_6.clicked.connect(lambda state, num = '6': self.button_num_clicked(num))
        self.button_7.clicked.connect(lambda state, num = '7': self.button_num_clicked(num))
        self.button_8.clicked.connect(lambda state, num = '8': self.button_num_clicked(num))
        self.button_9.clicked.connect(lambda state, num = '9': self.button_num_clicked(num))
        self.button_0.clicked.connect(lambda state, num = '0': self.button_num_clicked(num))
        
        
        self.button_open.clicked.connect(self.button_open_clicked)
        self.button_close.clicked.connect(self.button_close_clicked)
        self.button_float.clicked.connect(self.button_float_clicked)
        self.button_sol.clicked.connect(self.button_equal_clicked)
        self.button_del.clicked.connect(self.button_backspace_clicked)
        self.button_clear.clicked.connect(self.button_clear_clicked)
        self.button_reset.clicked.connect(self.button_reset_clicked)
        self.button_record.clicked.connect(self.button_record_clicked)
        self.button_percent.clicked.connect(self.button_percent_clicked)
        self.button_change.clicked.connect(self.button_change_clicked)


    # 연산자 입력
    def button_operation_clicked(self, operation):
        if (self.result and self.result[-1] in ('+', '-', '*', '/')):
            self.result = self.result[:-1] + operation
            self.equation.setText(self.result)
            self.result = self.equation.text()
            self.sign_idx = self.idx

        elif (self.result == ''):
            self.equation.setText('')

        else:
            self.result += operation
            self.equation.setText(self.result)
            self.result = self.equation.text()
            self.idx += 1
            self.sign_idx = self.idx 


    def button_num_clicked(self, num):
        self.result = self.equation.text()
        self.result = self.result + num 
        self.equation.setText(self.result)
        self.idx += 1


    def button_backspace_clicked(self):
        self.result = self.equation.text()
        if (self.result == ''):
            self.idx = 0
            self.sign_idx = 0
            self.sign_flag = 0
        else:
            self.result = self.result[:-1]
            self.equation.setText(self.result)
            self.idx -= 1


    def button_clear_clicked(self):
        self.result = ''
        self.idx = 0
        self.sign_idx = 0
        self.sign_flag = 0
        self.equation.setText("")
        self.solve.setText("")

    
    def button_float_clicked(self):
        self.result = self.equation.text()
        self.result += '.'
        self.idx += 1
        self.equation.setText(self.result)
    

    def button_equal_clicked(self):
        try:  
            self.result = self.equation.text()
            solution = eval(self.result)
            self.solve.setText(str(solution))
            self.equation_list.append(self.result)
            self.solve_list.append(solution)    

        except:
            pass

    def button_backspace_clicked(self):
        self.result = self.equation.text()
        self.result = self.result[:-1]
        self.idx -=1
        self.equation.setText(self.result)


    def button_clear_clicked(self):
        self.result = ''
        self.idx = 0
        self.sign_idx = 0
        self.equation.setText("")
        self.solve.setText("")
        

    def button_float_clicked(self):
        self.result = self.equation.text()
        self.result += '.'
        self.idx += 1
        self.equation.setText(self.result)

    
    def button_open_clicked(self):
        self.result = self.equation.text()
        self.result = self.result + '('
        self.idx += 1
        self.equation.setText(self.result)


    def button_close_clicked(self):
        self.result = self.equation.text()
        self.result = self.result + ')'
        self.idx += 1
        self.equation.setText(self.result)
        self.sign_flag = 0
    
    
    def button_reset_clicked(self):
        self.equation_list = []
        self.solve_list = []
        self.record.setText('')


    def button_record_clicked(self):
        self.record.setText('')
        for (a, b) in zip(self.equation_list, self.solve_list):
            self.record.append(str(a))
            self.record.append(str(b))
            self.record.append('')


    def button_percent_clicked(self):
        self.result = self.equation.text()
        self.result = self.result + '/100'
        self.idx += 4
        self.equation.setText(self.result)


    def button_change_clicked(self):
        self.result = self.equation.text()
        if (self.sign_flag == 0):
            self.tmp = self.result[:self.sign_idx] + '(-'
            self.result = self.tmp + self.result[(self.sign_idx):]
            self.idx += 2
            self.sign_flag = 1
        else:
            self.result = self.result.replace("(-", "")
            self.sign_flag = 0
            self.idx -= 2
        self.equation.setText(self.result)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())