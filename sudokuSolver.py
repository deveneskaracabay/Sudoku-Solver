from PyQt5 import QtCore, QtGui, QtWidgets
from qt5_file.ui import Ui_MainWindow
from solutionClass.sudokuClass import Sudoku
from functions.GetItem import getitem_func
from functions.AddItem import additem_func
from functions.Reset import reset_func
import sys

def reset():
    reset_func(ui)

def error():    
    QtWidgets.QMessageBox.about(Qmain,"Error","Please enter valid numbers")

def getitem():
    matrix = getitem_func(ui)
    solution_func(matrix)

def additem(solution):
    additem_func(ui,solution)

def solution_func(matrix):
    solution = Sudoku(matrix)
    if solution.flag:
        return additem(solution)
    else:
        error()
        


app = QtWidgets.QApplication(sys.argv)
Qmain = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Qmain)
Qmain.show()

ui.Button.clicked.connect(getitem)
ui.Button_2.clicked.connect(reset)

sys.exit(app.exec_())




