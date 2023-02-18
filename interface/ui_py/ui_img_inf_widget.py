# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_img_inf_widget.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Img_Inf_Form(object):
    def setupUi(self, Img_Inf_Form):
        if not Img_Inf_Form.objectName():
            Img_Inf_Form.setObjectName(u"Img_Inf_Form")
        Img_Inf_Form.resize(400, 300)
        self.gridLayout_2 = QGridLayout(Img_Inf_Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(Img_Inf_Form)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(330)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Img_Inf_Form)

        QMetaObject.connectSlotsByName(Img_Inf_Form)
    # setupUi

    def retranslateUi(self, Img_Inf_Form):
        Img_Inf_Form.setWindowTitle(QCoreApplication.translate("Img_Inf_Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Img_Inf_Form", u"Information", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Img_Inf_Form", u"name", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Img_Inf_Form", u"path", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Img_Inf_Form", u"format", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Img_Inf_Form", u"size", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Img_Inf_Form", u"width", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Img_Inf_Form", u"height", None));
    # retranslateUi

