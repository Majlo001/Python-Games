from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QComboBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import sys

import sudoku_main
import sudoku_solver

UI_PATH = 'ui_files\\'
IMAGES_PATH = 'images\\'



class MainWindow(QMainWindow):
    def __init__(self):
            super().__init__()
            
            # Load the ui file
            self.ui = loadUi(UI_PATH+"main_window.ui", self)
            self.setWindowTitle("Sudoku Game")

            # Define widgets
            self.sudokuPlayButton = self.findChild(QPushButton, "playButton")
            self.sudkouTryButton = self.findChild(QPushButton, "tryButton")
            self.difficultyComboBox = self.findChild(QComboBox, "difficultyComboBox")
            self.boardComboBox = self.findChild(QComboBox, "boardComboBox")
            self.image1 = self.findChild(QLabel, "image1")
            self.image2 = self.findChild(QLabel, "image2")
            self.errorsCheckBox = self.findChild(QCheckBox, "errorsCheckBox")


            # Set images
            self.sudokuImage = QPixmap(IMAGES_PATH + "sudoku-game-2.png")
            self.solverImage = QPixmap(IMAGES_PATH + "sudoku-solver-1.png")
            self.image1.setPixmap(self.sudokuImage)
            self.image2.setPixmap(self.solverImage)
            self.image1.resize(self.sudokuImage.width(), self.sudokuImage.height())
            self.image2.resize(self.solverImage.width(), self.solverImage.height())
            self.image1.show()
            self.image2.show()


            # Click buttons
            self.sudokuPlayButton.clicked.connect(self.playSudoku)
            self.sudkouTryButton.clicked.connect(self.solveSudoku)

            # Show The App
            self.show()

    def playSudoku(self):
        '''
        Opening new window with Sudoku Game with given settings.
        '''
        difficulty = self.difficultyComboBox.currentText()
        board = self.boardComboBox.currentText()
        showErrors = self.errorsCheckBox.isChecked()
        
        gMode = 1
        if board == "Load from file":
            gMode = 2
        
        sudoku_main.SudokuMainWindow(gMode, difficulty.lower(), showErrors)

    def solveSudoku(self):
        '''
        Opening new window with Sudoku Solver
        '''
        sudoku_solver.SudokuSolver()




app = QtWidgets.QApplication(sys.argv)
ui = MainWindow()
sys.exit(app.exec_())