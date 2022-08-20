from PyQt5 import QtWidgets, QtGui, QtCore


class SDMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent: QtWidgets.QWidget = None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.setWindowTitle("Stable Diffusion UI")

        # Initialise the UI
        self.create_menu()
        self.setup_layout()

        self.resize(1000, 600)

    ###################################################

    def create_menu(self):
        # Create the Menu Bar
        self.menu_bar = QtWidgets.QMenuBar()
        self.setMenuBar(self.menu_bar)

        # File menu
        self.menu_file = QtWidgets.QMenu()
        self.menu_bar.addMenu(self.menu_file)
        self.menu_file.setTitle("File")

        # File->quit
        self.quit_action = QtWidgets.QAction()
        self.menu_file.addAction(self.quit_action)
        self.quit_action.setText("Exit")
        self.quit_action.triggered.connect(self.quit)

    def setup_layout(self):
        pass

    ###################################################
    # File Menu Callbacks

    def quit(self):
        self.close()
