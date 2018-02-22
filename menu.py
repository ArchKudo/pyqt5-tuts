import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._status_bar = None
        self.init_ui()

    def init_ui(self):

        # Setup status-bar
        self._status_bar = self.statusBar()
        self.statusBar().showMessage('Ready')

        # Create menu bar
        menu_bar = self.menuBar()

        # Add menus
        file_menu = menu_bar.addMenu('&File')
        view_menu = menu_bar.addMenu('&View')

        # Add a submenu
        import_menu = QMenu('Import', self)
        import_action = QAction('Import mail', self)
        import_menu.addAction(import_action)

        # Add a new action
        new_action = QAction('New', self)

        # Exit app
        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit App')
        exit_action.triggered.connect(qApp.quit)

        # Checkbox to show/hide status-bar
        view_stat_bar_action = QAction('Statusbar', self, checkable=True)
        view_stat_bar_action.setStatusTip('Toggle viewing statusbar')
        view_stat_bar_action.setChecked(True)
        view_stat_bar_action.triggered.connect(self.toggle_status_bar)

        # Add all the actions to file_menu
        file_menu.addAction(new_action)
        file_menu.addMenu(import_menu)
        file_menu.addAction(exit_action)

        # Add status bar toggle to view menu
        view_menu.addAction(view_stat_bar_action)

        self.setGeometry(500, 500, 350, 250)
        self.setWindowTitle('Menu and Status-bar')
        self.show()


    def toggle_status_bar(self,state):
        self.statusBar.show() if state else self.statusBar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MenuWindow()
    sys.exit(app.exec())
