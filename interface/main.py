from PySide6.QtWidgets import QApplication

import function.analyse
from interface.widget import Widget
from function.analyse import compare
import threading

back_thread = threading.Thread(target=function.analyse.pre_func, daemon=True)
back_thread.start()

app = QApplication()

widget = Widget()
widget.show()

app.exec()
