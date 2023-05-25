from PyQt5 import QtCore, QtGui, QtWidgets
from RSA_windowLogic import MainWindow
import sys
from QCandyUi import CandyWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())