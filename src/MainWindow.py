import sys

from LRDWindow import LRDWindow
from PySide6.QtWidgets import (
    QApplication,
)

class MainWindow(LRDWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Laser Resonator Designer")
        self.help_Button.clicked.connect(self.help_Button_clicked)
        self.reset_Button.clicked.connect(self.reset_Button_clicked)

    def help_Button_clicked(self):
        print("Help button is clicked!")
        self.textEdit.setText("Help button is clicked!")

    def reset_Button_clicked(self):
        self.textEdit.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
