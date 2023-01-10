from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QPushButton, QMessageBox, QLabel, QLineEdit, QDialogButtonBox, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
import sys

import numpy as np
import json
import random


def getSudokuFromFile(x):
      f = open('sudoku.json')
      data = json.load(f)
      difficulty = 'easy'
      retSudoku = np.zeros([0,0], dtype = int)

      if x == 1: difficulty = 'easy'
      elif x == 2: difficulty = 'normal'
      elif x == 3: difficulty = 'hard'

      sudokuVariant = random.randint(0, len(data['easy'])-1)

      for arr in data[difficulty][sudokuVariant]:
            for row in arr:
                  retSudoku = np.append(retSudoku, row)

      retSudoku = np.resize(retSudoku, (9,9))
      return retSudoku


class Sudoku():
      def __init__(self, x):
            x = 1
            self.gameLoaded = False

            if x == 0:
                  self.basicSudokuArray = self.generateSudoku()
            else:
                  self.basicSudokuArray = self.getSudokuFromFile(x)
            
            self.sudokuArray = np.copy(self.basicSudokuArray)

      def getSudokuFromFile(x):
            f = open('sudoku.json')
            data = json.load(f)
            difficulty = 'easy'
            retSudoku = np.zeros([0,0], dtype = int)

            if x == 1: difficulty = 'easy'
            elif x == 2: difficulty = 'normal'
            elif x == 3: difficulty = 'hard'

            sudokuVariant = random.randint(0, len(data['easy'])-1)

            for arr in data[difficulty][sudokuVariant]:
                  for row in arr:
                        retSudoku = np.append(retSudoku, row)

            retSudoku = np.resize(retSudoku, (9,9))
            return retSudoku
      
      def generateSudoku():
            pass



UI_PATH = 'ui_files\\'

class Ui_MainWindow(QMainWindow):
      def __init__(self):
            super().__init__()
            self.editItemWindow = None
            self.isEditItemOpen = False
            self.tempItems = []
            
            # Load the ui file
            self.ui = loadUi(UI_PATH+"sudoku_game.ui", self)
            self.setWindowTitle("Sudoku Game")

            # Define widgets
            # self.lineEdit = self.findChild(QLineEdit, "lineEdit")

            self.clearButton = self.findChild(QPushButton, "clearButton")
            self.checkButton = self.findChild(QPushButton, "checkButton")
            self.timerLabel = self.findChild(QLabel, "timerLabel")
            self.difficultyLabel = self.findChild(QLabel, "difficultyLabel")
            self.sudokuTable = self.findChild(QTableWidget, "SudokuTable")

            # Click the buttons
            #   self.addItem.clicked.connect(self.add_it)
            #   self.editItem.clicked.connect(self.edit_it)
            #   self.removeItem.clicked.connect(self.remove_it)
            #   self.clearList.clicked.connect(self.clear_list)


            # Create Sudoku Table
            self.basicSudokuArray = getSudokuFromFile(1)
            self.sudokuArray = np.copy(self.basicSudokuArray)
            row = 0
            col = 0
            for arr in self.sudokuArray:
                  print(arr)
                  for i in arr:
                        self.sudokuTable.setItem(row, col, QTableWidgetItem(""))
                        self.sudokuTable.item(row, col).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        if i != 0:
                              self.sudokuTable.setItem(row, col, QTableWidgetItem(str(i)))
                              self.sudokuTable.item(row, col).setBackground(QtGui.QColor(220,220,220))
                              self.sudokuTable.item(row, col).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        col = col+1
                  row = row+1
                  col = 0

            # Change cell
            self.sudokuTable.itemChanged.connect(self.sudoku_cell_changed)

            # Show The App
            self.show()
      
      def sudoku_cell_changed(self, item):
            if int(self.basicSudokuArray[item.row(), item.column()]) == 0:
                  if item.text().isdigit() or item.text() == "":
                        print(item.row(), item.column(), item.text())
                        # if int(item.text()) > 9 or int(item.text()) < 0:
                        #
                        # else:
                        self.sudokuTable.item(item.row(), item.column()).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                  else:
                        self.sudokuTable.setItem(item.row(), item.column(), QTableWidgetItem(""))
                        # self.sudokuTable.item(item.row(), item.column()).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            else:
                  #if self.sudokuTable[item.row(), item.column()] != str(self.basicSudokuArray[item.row(), item.column()]):
                  print("Help here")
                  print(item.row(), item.column(), item.text())
                  #print(int(self.sudokuTable[item.row(), item.column()]))
                  #
                  # print(int(self.basicSudokuArray[item.row(), item.column()]))
                  self.sudokuTable.setItem(item.row(), item.column(), QTableWidgetItem(str(self.basicSudokuArray[item.row(), item.column()])))
                        # self.sudokuTable.item(item.row(), item.column()).setBackground(QtGui.QColor(220,220,220))
                        # self.sudokuTable.item(item.row(), item.column()).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)





app = QtWidgets.QApplication(sys.argv)
ui = Ui_MainWindow()
sys.exit(app.exec_())