from PyQt5 import QtWidgets
import sys
from form import Ui_PlayingField

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_PlayingField()
    window = QtWidgets.QMainWindow()
    ui.setupUi(window)

    window.setWindowTitle("D&D Helper")
    window.show()
    app.exec()