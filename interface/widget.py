import os

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QListWidgetItem
from ui_widget import Ui_Form
from function.analyse import compare
from function.res import Result, CategoryView, BoxView, ImageInf
from PIL import Image
from box_widget import BoxWidget
from category_widget import CategoryWidget
from img_inf_widget import ImgInfWidget


class Widget(QWidget, Ui_Form):
    res_dict: dict

    def __init__(self):
        super().__init__()
        self.box_widget = None
        self.category_widget = None
        self.img_inf_widget = None
        self.setupUi(self)
        self.setWindowTitle("YOLO Result Analyse Tool")
        # self.setFixedSize(self.width(), self.height())

        self.compare_start.clicked.connect(self.ui_compare)

    def ui_compare(self):
        # dir1 = self.a_path_line_edit.text()
        # dir2 = self.b_path_line_edit.text()
        # dir3 = self.standard_path_line_edit.text()
        # img_dir =
        # print(dir1, '/n', dir2, '/n', dir3)
        dir1 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/YOLOv5改进结果/_predictions.json'
        dir2 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/YOLOv5/_predictions.json'
        dir3 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/coco数据集/val2017/'
        img_dir = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/val2017'
        res_dict = compare(dir1, dir2, dir3, img_dir)
        self.res_dict = res_dict
        self.res_table_fill(res_dict)

    def res_table_fill(self, res_dict: dict):
        row = self.res_table.rowCount()
        for _key in res_dict.keys():
            self.res_table_one_row_fill(res_dict[_key], self.res_table.rowCount())

    def res_table_one_row_fill(self, res: Result, row: int):
        img_button = QPushButton("SHOW IMG")
        img_button.clicked.connect(self.img_button_clicked)

        img_inf_button = QPushButton("SHOW INF")
        img_inf_button.clicked.connect(self.ui_img_inf_widget_show)

        category_button = QPushButton("DETAIL")
        category_button.clicked.connect(self.ui_category_widget_show)

        box_button = QPushButton("DETAIL")
        box_button.clicked.connect(self.ui_box_widget_show)

        self.res_table.insertRow(row)
        self.res_table.setItem(row, 0, QTableWidgetItem(str(res.image_id)))
        self.res_table.setCellWidget(row, 1, img_button)
        self.res_table.setCellWidget(row, 2, img_inf_button)
        self.res_table.setCellWidget(row, 3, category_button)
        self.res_table.setItem(row, 4, QTableWidgetItem(str(res.a_category_coverage_rate)))
        self.res_table.setItem(row, 5, QTableWidgetItem(str(res.b_category_coverage_rate)))
        self.res_table.setCellWidget(row, 6, box_button)
        self.res_table.setItem(row, 7, QTableWidgetItem(str(res.a_box_amount)))
        self.res_table.setItem(row, 8, QTableWidgetItem(str(res.b_box_amount)))
        self.res_table.setItem(row, 9, QTableWidgetItem(str(res.a_box_coverage_rate)))
        self.res_table.setItem(row, 10, QTableWidgetItem(str(res.b_box_coverage_rate)))
        self.res_table.setItem(row, 11, QTableWidgetItem(str(res.a_comprehensive_evaluation)))
        self.res_table.setItem(row, 12, QTableWidgetItem(str(res.b_comprehensive_evaluation)))

    def img_button_clicked(self):
        button = self.sender()
        if button:
            row = self.res_table.indexAt(button.pos()).row()
            image_id_item = self.res_table.item(row, 0)
            image_id = image_id_item.text()
            res = self.res_dict[int(image_id)]
            img = Image.open(res.img_inf.path)
            img.show(res.img_inf.name)

    def ui_img_inf_widget_show(self):
        button = self.sender()
        if button:
            row = self.res_table.indexAt(button.pos()).row()
            image_id_item = self.res_table.item(row, 0)
            image_id = image_id_item.text()
            res = self.res_dict[int(image_id)]
            self.img_inf_widget = ImgInfWidget()
            self.img_inf_widget.tableWidget.setItem(0, 0, QTableWidgetItem(str(res.img_inf.name)))
            self.img_inf_widget.tableWidget.setItem(1, 0, QTableWidgetItem(str(res.img_inf.path)))
            self.img_inf_widget.tableWidget.setItem(2, 0, QTableWidgetItem(str(res.img_inf._format)))
            self.img_inf_widget.tableWidget.setItem(3, 0, QTableWidgetItem(str(res.img_inf.size)))
            self.img_inf_widget.tableWidget.setItem(4, 0, QTableWidgetItem(str(res.img_inf.width)))
            self.img_inf_widget.tableWidget.setItem(5, 0, QTableWidgetItem(str(res.img_inf.height)))
            self.img_inf_widget.show()

    def ui_category_widget_show(self):
        button = self.sender()
        if button:
            row = self.res_table.indexAt(button.pos()).row()
            image_id_item = self.res_table.item(row, 0)
            image_id = image_id_item.text()
            res = self.res_dict[int(image_id)]
            c_view_list = res.category_view
            self.category_widget = CategoryWidget()
            for c_view in c_view_list:
                cur_row = self.category_widget.tableWidget.rowCount()
                self.category_widget.tableWidget.insertRow(cur_row)
                self.category_widget.tableWidget.setItem(cur_row, 0, QTableWidgetItem(str(c_view.standard_category)))
                self.category_widget.tableWidget.setItem(cur_row, 1,
                                                         QTableWidgetItem(str(c_view.standard_category_box_amount)))
                self.category_widget.tableWidget.setItem(cur_row, 2, QTableWidgetItem(str(c_view.a_category)))
                self.category_widget.tableWidget.setItem(cur_row, 3,
                                                         QTableWidgetItem(str(c_view.a_category_box_amount)))
                self.category_widget.tableWidget.setItem(cur_row, 4, QTableWidgetItem(str(c_view.b_category)))
                self.category_widget.tableWidget.setItem(cur_row, 5,
                                                         QTableWidgetItem(str(c_view.b_category_box_amount)))
            self.category_widget.show()

    def ui_box_widget_show(self):
        button = self.sender()
        if button:
            row = self.res_table.indexAt(button.pos()).row()
            image_id_item = self.res_table.item(row, 0)
            image_id = image_id_item.text()
            res = self.res_dict[int(image_id)]
            b_view_list = res.box_view
            self.box_widget = BoxWidget()
            for b_view in b_view_list:
                cur_row = self.box_widget.tableWidget.rowCount()
                self.box_widget.tableWidget.insertRow(cur_row)
                self.box_widget.tableWidget.setItem(cur_row, 0, QTableWidgetItem(str(b_view.category)))
                self.box_widget.tableWidget.setItem(cur_row, 1, QTableWidgetItem(str(b_view.standard_box_point)))
                self.box_widget.tableWidget.setItem(cur_row, 2, QTableWidgetItem(str(b_view.a_box_point)))
                self.box_widget.tableWidget.setItem(cur_row, 3, QTableWidgetItem(str(b_view.b_box_point)))
                self.box_widget.tableWidget.setItem(cur_row, 4, QTableWidgetItem(str(b_view.a_deviation_value_fiducial_point)))
                self.box_widget.tableWidget.setItem(cur_row, 5, QTableWidgetItem(str(b_view.b_deviation_value_fiducial_point)))
                self.box_widget.tableWidget.setItem(cur_row, 6, QTableWidgetItem(str(b_view.standard_box_area)))
                self.box_widget.tableWidget.setItem(cur_row, 7, QTableWidgetItem(str(b_view.a_box_area)))
                self.box_widget.tableWidget.setItem(cur_row, 8, QTableWidgetItem(str(b_view.b_box_area)))
                if b_view.a_is_bigger:
                    self.box_widget.tableWidget.setItem(cur_row, 9, QTableWidgetItem('+' + str(b_view.a_standard_box_area_differ_rate) + '%'))
                else:
                    self.box_widget.tableWidget.setItem(cur_row, 9, QTableWidgetItem('-' + str(b_view.a_standard_box_area_differ_rate) + '%'))
                if b_view.b_is_bigger:
                    self.box_widget.tableWidget.setItem(cur_row, 10, QTableWidgetItem('+' + str(b_view.b_standard_box_area_differ_rate) + '%'))
                else:
                    self.box_widget.tableWidget.setItem(cur_row, 10, QTableWidgetItem('-' + str(b_view.b_standard_box_area_differ_rate) + '%'))

                self.box_widget.tableWidget.setItem(cur_row, 11, QTableWidgetItem(str(b_view.a_score)))
                self.box_widget.tableWidget.setItem(cur_row, 12, QTableWidgetItem(str(b_view.b_score)))
            self.box_widget.show()
