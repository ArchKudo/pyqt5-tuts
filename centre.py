import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class CentreWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Window at centre')
        self.show()

    def center(self):

        centre_loc = QDesktopWidget().availableGeometry().center()
        geom = self.frameGeometry()
        geom.moveCenter(centre_loc)
        self.move(geom.topLeft())


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    centre = CentreWindow()
    sys.exit(app.exec())
