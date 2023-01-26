from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QFont

class SudokuResultDialog(QDialog):
      def __init__(self, errorCount, timerText, sudokuArray):
            super().__init__()
            self.sudokuArray = sudokuArray
            self.setWindowTitle('Sudoku result')
            self.resize(200, 250)
            self.layout = QVBoxLayout()
            self.label1 = QLabel("Sudoku ukończone!")
            self.label2 = QLabel()
            self.label3 = QLabel("Czas "+timerText)
            self.button0 = QPushButton("Zapisz wynik do pliku")
            self.button1 = QPushButton("Nowa gra")
            self.button2 = QPushButton("Zakończ")

            if errorCount == 0:
                  self.label2.setText("Gratulacje brak błędów")
            else:
                  self.label2.setText("Błędy: " + str(errorCount))

            self.button0.clicked.connect(self.saveToFile)
            self.button1.clicked.connect(self.accept)
            self.button2.clicked.connect(self.reject)

            
            self.label1.setFont(QFont('Arial', 16))
            self.label2.setFont(QFont('Arial', 12))
            self.label3.setFont(QFont('Arial', 10))

            self.layout.addWidget(self.label1)
            self.layout.addWidget(self.label2)
            self.layout.addWidget(self.label3)
            self.layout.addWidget(self.button0)
            self.layout.addWidget(self.button1)
            self.layout.addWidget(self.button2)
            self.setLayout(self.layout)
      
      def saveToFile(self):
            '''
            Open dialog and save result with Sudoku to the specified file
            '''
            name = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Text Files (*.txt)")
            fileName = name[0]
            file = open(fileName, 'w+', encoding='utf8')
            text = self.label2.text() + "\n"
            text += self.label3.text() + "\n\n"
            text += str(self.sudokuArray)
            file.write(text)
            file.close()