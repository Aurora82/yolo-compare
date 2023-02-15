from PySide6.QtWidgets import QWidget
from ui_img_inf_widget import Ui_Img_Inf_Form


class ImgInfWidget(QWidget, Ui_Img_Inf_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("IMG INF")

