from PySide6.QtWidgets import QWidget
from interface.ui_py.ui_category_widget import Ui_Category_Form


class CategoryWidget(QWidget, Ui_Category_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Category Detail")
