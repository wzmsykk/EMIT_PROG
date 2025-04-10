import sys
from ui.main_qt import MainDialog
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

app = QApplication(sys.argv)

mainwindow = MainDialog()
mainwindow.show()

sys.exit(app.exec_())