import sys

from LRDWindow import LRDWindow
from PySide6.QtWidgets import QApplication


class MainWindow(LRDWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Laser Resonator Designer")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
