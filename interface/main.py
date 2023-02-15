from PySide6.QtWidgets import QApplication, QMainWindow
from widget import Widget

if __name__ == '__main__':
    app = QApplication()

    widget = Widget()
    widget.show()

    app.exec()
