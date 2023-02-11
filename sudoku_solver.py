from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QThread
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont
from PyQt5.uic import loadUi
import sys

import numpy as np

from Sudoku.SudokuGame import *
from Sudoku.Timer import *
from Sudoku.SudokuResultDialog import *

UI_PATH = 'ui_files\\'
ICON_PATH = 'Sudoku\\media\\icons\\'


class SudokuSolver(QMainWindow):
    def __init__(self):
            super().__init__()
            self.__isSolved = False
            
            # Load the ui file
            self.ui = loadUi(UI_PATH+"sudoku_solver.ui", self)
            self.setWindowTitle("Sudoku Solver")

            # Define widgets
            self.clearButton = self.findChild(QPushButton, "clearButton")
            self.solveButton = self.findChild(QPushButton, "solveButton")
            self.sudokuTable = self.findChild(QTableWidget, "SudokuTable")

            # Click buttons
            self.clearButton.clicked.connect(self.clearSudokuTable)
            self.solveButton.clicked.connect(self.solveSudokuTable)
            
            # Suoku Matrix
            self.sudokuObject = Sudoku(0, 0)
            self.sudokuArray = self.sudokuObject.getSudokuArray()
            self.createSudokuTable()

            # Change cell
            self.sudokuTable.itemChanged.connect(self.sudokuCellChanged)

            # Show The App
            self.show()
      
    def createSudokuTable(self):
            '''
            Creating Sudoku table form Matrix and puting numbers to cells
            '''
            for row in range(len(self.sudokuArray)):
                for col in range(len(self.sudokuArray[row])):
                    self.sudokuArray[row][col] = 0
                    self.sudokuTable.setItem(row, col, QTableWidgetItem(""))
                    self.sudokuTable.item(row, col).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)

    def clearSudokuTable(self):
            '''
            Clearing sudoku Table after clicking a button
            '''
            if self.__isSolved == True:
                self.solveButton.setText("Solve")
                self.__isSolved = False
            
            self.sudokuObject.restartSudokuTable()
            self.sudokuArray = self.sudokuObject.getSudokuArray()
            self.createSudokuTable()

    def solveSudokuTable(self):
            '''
            Solving sudoku Table after clicking a button and write solve into table
            '''
            if self.__isSolved == True:
                self.saveToFile()

            else:
                if self.sudokuObject.validateSudokuSolver() != True:
                    errors = self.sudokuObject.getValidateErrors()

                    for i in range(len(errors)):
                        row, col = errors[i]
                        self.sudokuTable.item(row, col).setBackground(QtGui.QColor(255, 0, 0))
                    
                    self.showInformationDialog("Given Array have errors!")


                else:
                    self.sudokuObject.solveMainTable()
                    self.sudokuArray = self.sudokuObject.getSudokuArray()
                    self.__isSolved = True
                    self.solveButton.setText("Save to file")

                    for row in range(len(self.sudokuArray)):
                        for col in range(len(self.sudokuArray[row])):
                            self.sudokuTable.setItem(row, col, QTableWidgetItem(str(self.sudokuArray[row][col])))
                            self.sudokuTable.item(row, col).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                            self.sudokuTable.item(row, col).setBackground(QtGui.QColor(255, 255, 255))
    
    def sudokuCellChanged(self, item):
            '''
            Validating is it possible to change cell, if yes, then change.
            '''
            if item.text() == "":
                self.sudokuObject.updateSudokuArray(item.row(), item.column(), 0)
                return

            if item.text().isdigit():
                if int(item.text()) > 9 or int(item.text()) < 1:
                    self.sudokuTable.item(item.row(), item.column()).setText("")
                    self.sudokuObject.updateSudokuArray(item.row(), item.column(), 0)
                    self.showInformationDialog("You can only enter numbers in a range 1-9")
                else:
                    self.sudokuTable.item(item.row(), item.column()).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.sudokuObject.updateSudokuArray(item.row(), item.column(), int(item.text()))
            else:
                self.sudokuTable.item(item.row(), item.column()).setText("")
                self.sudokuObject.updateSudokuArray(item.row(), item.column(), 0)
                self.showInformationDialog("You can only enter numbers in a range 1-9")

    def showInformationDialog(self, message):
            '''
            Showing Informational Dialog with given message
            '''
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(message)
            msgBox.setWindowTitle("Sudoku Information")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                pass
    
    def saveToFile(self):
        '''
        Open dialog and save Solved Sudoku to the specified file
        '''
        name = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Text Files (*.txt)")
        fileName = name[0]
        if fileName != "":
            file = open(fileName, 'w+', encoding='utf8')
            text = str(self.sudokuArray)
            file.write(text)
            file.close()