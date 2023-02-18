from PySide6.QtWidgets import QWidget
from interface.ui_py.ui_box_widget import Ui_Box_Form


class BoxWidget(QWidget, Ui_Box_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Box Detail")
