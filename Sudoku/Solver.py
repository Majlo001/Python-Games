import numpy as np
import random

class SudokuSolver():
      def __init__(self):
            pass

      
      def findSpaces(self):
            '''
            Finds the first empty space on the board - 0
            '''
            for row in range(len(self.board)):
                  for col in range(len(self.board[0])):
                        if self.board[row][col] == 0:
                              return (row, col)

            return False