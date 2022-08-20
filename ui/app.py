import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import ui.widgets.mainwindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = ui.widgets.mainwindow.SDMainWindow()

    main_window.show()
    sys.exit(app.exec())
