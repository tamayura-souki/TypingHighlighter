from PySide2.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QStyle
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import QUrl

HOME_URL = "https://github.com/tamayura-souki/TypingHighlighter"
VERSION = 1.0

class TrayWidget(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)

        menu = QMenu(parent)
        info_action = menu.addAction(f"Typing Highlighter v{VERSION}")
        info_action.triggered.connect(self.open_page)
        menu.addSeparator()
        quit_action = menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)

        self.setContextMenu(menu)

        icon = QApplication.style().standardIcon(QStyle.SP_DialogApplyButton)
        self.setIcon(icon)

    def open_page(self):
        url = QUrl(HOME_URL)
        QDesktopServices.openUrl(url)

    def quit(self):
        QApplication.quit()
