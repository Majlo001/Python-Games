import numpy as np
import json
import random

from .SudokuSettings import *

class Sudoku():
      def __init__(self, x, difficulty):
            self.gameLoaded = False
            self.sudokuArray = np.zeros([9,9], dtype = int)

            if x == 1:
                  self.basicSudokuArray = self.__generateDiagonalSudoku()
                  self.sudokuArray = np.copy(self.basicSudokuArray)
                  self.__generateRest()
                  self.__generateEmptySpaces(difficulty)
            elif x == 2:
                  self.basicSudokuArray = self.__getSudokuFromFile(difficulty)
                  self.sudokuArray = np.copy(self.basicSudokuArray)
            else:
                  #TODO: Solve and enter
                  print("solve here")
            

            #print("Last print: ")
            #print(self.sudokuArray)
            #self.validateSudoku()
      
      def getSudokuArray(self):
            '''
            Return main Sudoku Matrix.
            '''
            return self.sudokuArray

      def __getSudokuFromFile(difficulty):
            '''
            Opens JSON file and return Sudoku Matrix depend on difficulty
            '''

            f = open('sudoku.json') #TODO: To settings
            data = json.load(f)
            retSudoku = np.zeros([0,0], dtype = int)

            sudokuVariant = random.randint(0, len(data[difficulty])-1)

            for arr in data[difficulty][sudokuVariant]:
                  for row in arr:
                        retSudoku = np.append(retSudoku, row)

            retSudoku = np.resize(retSudoku, (9,9))
            return retSudoku
      

      def __generateDiagonalSudoku(self):
            '''
            Generates numbers in Matrix diagonally
            '''
            retSudoku = np.zeros([9,9], dtype = int)

            for i in range(0, 3):
                  freeNumbers = list(range(1, 10))
                  for row in range(0 + 3*i, 3 + 3*i):
                        for col in range(0 + 3*i, 3 + 3*i):
                              number = random.choice(freeNumbers)
                              freeNumbers.remove(number)
                              retSudoku[row][col] = number

            return retSudoku
      
      def __generateEmptySpaces(self, difficulty):
            '''
            Sets empty spaces in the matrix.
            Count depend on difficulty.
            '''

            r1, r2 = SudokuSettings.DIFFICULTY_DICT[difficulty]
            spaces = random.randint(r1, r2)

            while(spaces != 0):
                  randRow = random.randint(0, len(self.sudokuArray)-1)
                  randCol = random.randint(0, len(self.sudokuArray)-1)
                  if self.sudokuArray[randRow][randCol] != 0:
                        self.sudokuArray[randRow][randCol] = 0
                        spaces -= 1

            return

      def findEmptySpaces(self):
            '''
            Finds the first empty space in the matrix - 0
            '''
            
            for row in range(len(self.sudokuArray)):
                  for col in range(len(self.sudokuArray[row])):
                        if self.sudokuArray[row][col] == 0:
                              return (row, col)

            return False

      def solve(self): 
            '''
            Solves the matrix (use recursion)
            '''
            spacesAvailable = self.findEmptySpaces()
            if spacesAvailable == False:
                  return True
            
            row, col = spacesAvailable

            for n in range(1, 10):
                  if self.checkSpace(n, row, col):
                        self.sudokuArray[row][col] = n
                        
                        if self.solve():
                              return True
                        
                        self.sudokuArray[row][col] = 0

            return False

      def checkSpace(self, num, row, col):
            '''
            Checks if we can enter a number in a given position in the matrix.
            '''
            if self.sudokuArray[row][col] != 0: # check to see if space is a number already
                  return False

            for tempcol in self.sudokuArray[row]: # check to see if number is already in row
                  if tempcol == num:
                        return False

            for temprow in range(len(self.sudokuArray)): # check to see if number is already in column
                  if self.sudokuArray[temprow][col] == num:
                        return False

            modRow = row // 3
            modCol = col // 3

            for i in range(0, 3): # check to see if internal box already has number
                  for j in range(0, 3):
                        if self.sudokuArray[i + (modRow * 3)][j + (modCol * 3)] == num:
                              return False
            
            return True
      
      def __generateRest(self):
            '''
            Generate rest of the matrix
            '''
            for row in range(len(self.sudokuArray)):
                  for col in range(len(self.sudokuArray[row])):
                        if self.sudokuArray[row][col] == 0:
                              randNum = random.randint(1, 9)

                              if self.checkSpace(randNum, row, col):
                                    self.sudokuArray[row][col] = randNum
                                    
                                    if self.solve():
                                          return self.sudokuArray

                                    self.sudokuArray[row][col] = 0

            return False
      
      def checkSudokuPosition(self, num, row, col):
            '''
            Checks if we can enter a number in a given position in the matrix.
            Checks by row and column.
            '''
            for tempcol in range(len(self.sudokuArray)):
                  if self.sudokuArray[row][tempcol] == num and tempcol != col:
                        return False

            for temprow in range(len(self.sudokuArray)):
                  if self.sudokuArray[temprow][col] == num and temprow != row:
                        return False
            
            return True

      def validateSudoku(self):
            '''
            Validate the correctness of Sudoku matrix row by row, column by column.
            '''
            if self.findEmptySpaces() != False:
                  return
            
            for row in range(len(self.sudokuArray)):
                  for col in range(len(self.sudokuArray[row])):
                        if self.quickCheck(self.sudokuArray[row][col], row, col) != True:
                              print("blad: ", row, col)
                              return False
            
            return True



