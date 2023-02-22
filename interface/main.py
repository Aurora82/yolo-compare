from PySide6.QtWidgets import QApplication
from interface.widget import Widget

app = QApplication()

widget = Widget()
widget.show()

app.exec()
