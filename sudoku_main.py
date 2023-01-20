from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QTimer, QTime, QThread
from PyQt5.QtWidgets import QMainWindow, QDialog, QPushButton, QMessageBox, QLabel, QDialogButtonBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
import sys

import numpy as np

from Sudoku.SudokuGame import *
from Sudoku.Timer import *

UI_PATH = 'ui_files\\'
ICON_PATH = 'Sudoku\\media\\icons\\'
#TODO:Wszystkie globalne do PythonSettings


class Ui_MainWindow(QMainWindow):
      def __init__(self):
            super().__init__()
            self.editItemWindow = None
            self.isEditItemOpen = False
            self.difficulty = "normal"
            
            # Load the ui file
            self.ui = loadUi(UI_PATH+"sudoku_game.ui", self)
            self.setWindowTitle("Sudoku Game")

            # Define widgets
            self.clearButton = self.findChild(QPushButton, "clearButton")
            self.checkButton = self.findChild(QPushButton, "checkButton")
            self.pauseButton = self.findChild(QPushButton, "pauseButton")
            self.timerLabel = self.findChild(QLabel, "timerLabel")
            self.difficultyLabel = self.findChild(QLabel, "difficultyLabel")
            self.sudokuTable = self.findChild(QTableWidget, "SudokuTable")

            # Timer Thread
            self.thread = QThread()
            self.timer = Timer()
            self.timer.moveToThread(self.thread)
            self.timer.timerSignal.connect(self.updateTimerLabel)
            self.thread.start()

            # Set labels, text, images
            self.difficultyLabel.setText(self.difficulty.upper())
            self.timerLabel.setText("00:00:00")
            self.pauseButton.setText("")
            self.pauseButton.setIcon(QIcon(ICON_PATH + "circled-play-60.png"))

            # Click buttons
            self.clearButton.clicked.connect(self.clearSudokuTable)
            self.checkButton.clicked.connect(self.checkSudokuTable)


            # Create Sudoku Table
            self.sudokuObject = Sudoku(1, self.difficulty)
            self.basicSudokuArray = self.sudokuObject.getSudokuArray()
            self.sudokuArray = np.copy(self.basicSudokuArray)
            self.createSudokuTable()
            

            # Change cell
            self.sudokuTable.itemChanged.connect(self.sudoku_cell_changed)
            

            # Show The App
            self.show()
      

      def createSudokuTable(self):
            row = 0
            col = 0
            for arr in self.sudokuArray:
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

      def clearSudokuTable(self):
            self.sudokuArray = np.copy(self.basicSudokuArray)
            self.createSudokuTable()

      def checkSudokuTable(self):
            print("check")
            self.timer.stopTimer()
            #TODO: Check table valid
      
      def updateTimerLabel(self, value):
            self.timerLabel.setText(value)

      def sudoku_cell_changed(self, item):
            if int(self.basicSudokuArray[item.row(), item.column()]) == 0:
                  if item.text() == "":
                        return
                  if item.text().isdigit():
                        #print(item.row(), item.column(), item.text())
                        if int(item.text()) > 9 or int(item.text()) < 1:
                              self.sudokuTable.item(item.row(), item.column()).setText("")
                              # TODO: Modal tutaj - liczby z zakresu 1-9
                        else:
                              self.sudokuTable.item(item.row(), item.column()).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                  else:
                        self.sudokuTable.item(item.row(), item.column()).setText("")
            else:
                  if item.text() == str(self.basicSudokuArray[item.row(), item.column()]):
                        return
                  # TODO: Modal tutaj - Tylko liczby z zakresu 1-9
                  #print(item.row(), item.column(), item.text())
                  self.sudokuTable.item(item.row(), item.column()).setText(str(self.basicSudokuArray[item.row(), item.column()]))





app = QtWidgets.QApplication(sys.argv)
ui = Ui_MainWindow()
sys.exit(app.exec_())