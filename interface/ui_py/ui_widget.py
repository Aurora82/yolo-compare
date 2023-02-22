# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(853, 747)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tab_widget = QTabWidget(Form)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setEnabled(True)
        self.setting_tab = QWidget()
        self.setting_tab.setObjectName(u"setting_tab")
        self.gridLayout_2 = QGridLayout(self.setting_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.setting_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.a_path_line_edit = QLineEdit(self.setting_tab)
        self.a_path_line_edit.setObjectName(u"a_path_line_edit")

        self.verticalLayout.addWidget(self.a_path_line_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.yolo_imp_path_select_push_button = QPushButton(self.setting_tab)
        self.yolo_imp_path_select_push_button.setObjectName(u"yolo_imp_path_select_push_button")

        self.horizontalLayout_2.addWidget(self.yolo_imp_path_select_push_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.setting_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.b_path_line_edit = QLineEdit(self.setting_tab)
        self.b_path_line_edit.setObjectName(u"b_path_line_edit")

        self.verticalLayout_2.addWidget(self.b_path_line_edit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.yolo_path_select_push_button = QPushButton(self.setting_tab)
        self.yolo_path_select_push_button.setObjectName(u"yolo_path_select_push_button")

        self.horizontalLayout.addWidget(self.yolo_path_select_push_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.setting_tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.standard_path_line_edit = QLineEdit(self.setting_tab)
        self.standard_path_line_edit.setObjectName(u"standard_path_line_edit")

        self.verticalLayout_3.addWidget(self.standard_path_line_edit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.standard_result_val_path_select_push_button = QPushButton(self.setting_tab)
        self.standard_result_val_path_select_push_button.setObjectName(u"standard_result_val_path_select_push_button")

        self.horizontalLayout_3.addWidget(self.standard_result_val_path_select_push_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.setting_tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.img_path_line_edit = QLineEdit(self.setting_tab)
        self.img_path_line_edit.setObjectName(u"img_path_line_edit")

        self.verticalLayout_4.addWidget(self.img_path_line_edit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.img_path_select_push_button = QPushButton(self.setting_tab)
        self.img_path_select_push_button.setObjectName(u"img_path_select_push_button")

        self.horizontalLayout_4.addWidget(self.img_path_select_push_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.setting_tab)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.deviation_number_slider = QSlider(self.setting_tab)
        self.deviation_number_slider.setObjectName(u"deviation_number_slider")
        self.deviation_number_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.deviation_number_slider)

        self.deviation_number_line_edit = QLineEdit(self.setting_tab)
        self.deviation_number_line_edit.setObjectName(u"deviation_number_line_edit")

        self.horizontalLayout_5.addWidget(self.deviation_number_line_edit)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 5)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.compare_start = QPushButton(self.setting_tab)
        self.compare_start.setObjectName(u"compare_start")

        self.gridLayout_2.addWidget(self.compare_start, 1, 0, 1, 1)

        self.tab_widget.addTab(self.setting_tab, "")
        self.result_view_tab = QWidget()
        self.result_view_tab.setObjectName(u"result_view_tab")
        self.gridLayout = QGridLayout(self.result_view_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.res_table = QTableWidget(self.result_view_tab)
        if (self.res_table.columnCount() < 14):
            self.res_table.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.res_table.setObjectName(u"res_table")
        self.res_table.setEnabled(True)

        self.gridLayout.addWidget(self.res_table, 0, 0, 1, 1)

        self.tab_widget.addTab(self.result_view_tab, "")

        self.gridLayout_3.addWidget(self.tab_widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"YOLO v5 Improvement Path:", None))
        self.yolo_imp_path_select_push_button.setText(QCoreApplication.translate("Form", u"Select File", None))
        self.label.setText(QCoreApplication.translate("Form", u"YOLO v5 Path:", None))
        self.yolo_path_select_push_button.setText(QCoreApplication.translate("Form", u"Select File", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Standard Result Val Path:", None))
        self.standard_result_val_path_select_push_button.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"IMG Path:", None))
        self.img_path_select_push_button.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Box Distance Deviation Number:", None))
        self.compare_start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.setting_tab), QCoreApplication.translate("Form", u"Setting", None))
        ___qtablewidgetitem = self.res_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"IMAGE ID", None));
        ___qtablewidgetitem1 = self.res_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IMG VIEW", None));
        ___qtablewidgetitem2 = self.res_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"IMG INF", None));
        ___qtablewidgetitem3 = self.res_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"CATEGORY VIEW", None));
        ___qtablewidgetitem4 = self.res_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"IMP CATE COVERAGE RATE", None));
        ___qtablewidgetitem5 = self.res_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"INTR CATE COVERAGE RATE", None));
        ___qtablewidgetitem6 = self.res_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"BOX VIEW", None));
        ___qtablewidgetitem7 = self.res_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"STANDARD BOX AMOUNT", None));
        ___qtablewidgetitem8 = self.res_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"IMP BOX AMOUNT", None));
        ___qtablewidgetitem9 = self.res_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"INTR BOX AMOUNT", None));
        ___qtablewidgetitem10 = self.res_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"IMP BOX COVERAGE RATE", None));
        ___qtablewidgetitem11 = self.res_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"INTR BOX COVERAGE RATE", None));
        ___qtablewidgetitem12 = self.res_table.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"IMP COMPREHENSIVE EVALUATION", None));
        ___qtablewidgetitem13 = self.res_table.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"INTR COMPREHENSIVE EVALUATION", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.result_view_tab), QCoreApplication.translate("Form", u"Result View", None))
    # retranslateUi

