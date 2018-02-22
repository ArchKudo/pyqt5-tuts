import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QToolTip, QPushButton, QWidget, QMessageBox
import PyQt5.Qt as Qt


class ButtonWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        font = QFont('SansSerif', 10)
        QToolTip.setFont(font)
        self.setToolTip('This is a <b>QWidget</b> widget!')

        btn = QPushButton('NewBtn', self)
        btn.setToolTip('This is a <b>QButton</b> widget!')

        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.setToolTip('This <b>QButton</b> quits!')
        qbtn.move(50, 100)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips & Buttons')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonWindow()
    sys.exit(app.exec())
