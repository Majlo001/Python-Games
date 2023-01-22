from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QThread
from PyQt5.QtWidgets import QMainWindow, QDialog, QPushButton, QComboBox, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont
from PyQt5.uic import loadUi
import sys

import numpy as np
import sudoku_main

UI_PATH = 'ui_files\\'
ICON_PATH = 'Sudoku\\media\\icons\\'
#TODO:Wszystkie globalne do PythonSettings


class MainWindow(QMainWindow):
    def __init__(self):
            super().__init__()
            
            # Load the ui file
            self.ui = loadUi(UI_PATH+"main_window.ui", self)
            self.setWindowTitle("Sudoku Game")

            # Define widgets
            self.sudokuPlayButton = self.findChild(QPushButton, "playButton")
            self.sudkouTryButton = self.findChild(QPushButton, "tryButton")
            #self.conncet4PlayButton = self.findChild(QPushButton, "conncet4PlayButton")
            self.difficultyComboBox = self.findChild(QComboBox, "difficultyComboBox")
            self.boardComboBox = self.findChild(QComboBox, "boardComboBox")


            # Click buttons
            self.sudokuPlayButton.clicked.connect(self.playSudoku)
            # self.checkButton.clicked.connect(self.checkSudokuTable)

            # Show The App
            self.show()

    def playSudoku(self):
        difficulty = self.difficultyComboBox.currentText()
        board = self.boardComboBox.currentText()
        
        isGenerate = 1
        if board == "Load from file":
            isGenerate = 2
        
        sudoku_main.SudokuMainWindow(isGenerate, difficulty.lower())




app = QtWidgets.QApplication(sys.argv)
ui = MainWindow()
sys.exit(app.exec_())