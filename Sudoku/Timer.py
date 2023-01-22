from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject, QTimer, QTime, QThread


class Timer(QThread):
      timerSignal = pyqtSignal(str)

      def __init__(self):
            super().__init__()
            self.__isRunning = True

            self.timer = QTimer()
            self.time = QTime(0, 0, 0)
            self.timer.timeout.connect(self.timerEvent)
            self.timer.start(1000)

      def timerEvent(self):
            if self.__isRunning == True:
                  self.time = self.time.addSecs(1)
                  #print(self.time.toString("hh:mm:ss"))
                  self.timerSignal.emit(self.time.toString("hh:mm:ss"))
      
      
      def stopTimer(self):
            self.__isRunning = False