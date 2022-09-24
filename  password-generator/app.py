import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
