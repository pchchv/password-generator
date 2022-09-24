import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_slider_to_spinbox()
    
    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_length.valueChanged.connect(self.ui.spinbox_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.ui.slider_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.set_password)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
