import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(0, 700)
    w.setWindowTitle('Hello World')
    w.show()

    sys.exit(app.exec())