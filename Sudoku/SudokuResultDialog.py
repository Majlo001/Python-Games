from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont

class SudokuResultDialog(QDialog):
    def __init__(self, errorCount, timerText):
            super().__init__()
            self.setWindowTitle('Sudoku result')
            self.resize(200, 250)
            self.layout = QVBoxLayout()
            self.label1 = QLabel("Sudoku ukończone!")
            self.label2 = QLabel()
            self.label3 = QLabel("Czas "+timerText)
            self.button1 = QPushButton("Nowa gra")
            self.button2 = QPushButton("Zakończ")

            if errorCount == 0:
                  self.label2.setText("Gratulacje brak błędów")
            else:
                  self.label2.setText("Błędy: " + str(errorCount))

            self.button1.clicked.connect(self.accept)
            self.button2.clicked.connect(self.reject)

            
            self.label1.setFont(QFont('Arial', 16))
            self.label2.setFont(QFont('Arial', 12))
            self.label3.setFont(QFont('Arial', 10))

            self.layout.addWidget(self.label1)
            self.layout.addWidget(self.label2)
            self.layout.addWidget(self.label3)
            self.layout.addWidget(self.button1)
            self.layout.addWidget(self.button2)
            self.setLayout(self.layout)