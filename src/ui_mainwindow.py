# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 704)
        icon = QIcon()
        icon.addFile(u"images/LRD.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.left_radius_DSpinBox = QDoubleSpinBox(self.centralwidget)
        self.left_radius_DSpinBox.setObjectName(u"left_radius_DSpinBox")
        self.left_radius_DSpinBox.setMaximum(10000.000000000000000)
        self.left_radius_DSpinBox.setSingleStep(50.000000000000000)

        self.gridLayout_2.addWidget(self.left_radius_DSpinBox, 2, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.cavity_length_DSpinBox = QDoubleSpinBox(self.centralwidget)
        self.cavity_length_DSpinBox.setObjectName(u"cavity_length_DSpinBox")
        self.cavity_length_DSpinBox.setMaximum(10000.000000000000000)
        self.cavity_length_DSpinBox.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.cavity_length_DSpinBox, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.reset_Button = QPushButton(self.centralwidget)
        self.reset_Button.setObjectName(u"reset_Button")

        self.gridLayout_2.addWidget(self.reset_Button, 5, 1, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_2.addWidget(self.textEdit, 6, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.wavelength_DSpinBox = QDoubleSpinBox(self.centralwidget)
        self.wavelength_DSpinBox.setObjectName(u"wavelength_DSpinBox")
        self.wavelength_DSpinBox.setDecimals(3)
        self.wavelength_DSpinBox.setMaximum(10.000000000000000)
        self.wavelength_DSpinBox.setSingleStep(0.100000000000000)

        self.gridLayout_2.addWidget(self.wavelength_DSpinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.right_radius_DSpinBox = QDoubleSpinBox(self.centralwidget)
        self.right_radius_DSpinBox.setObjectName(u"right_radius_DSpinBox")
        self.right_radius_DSpinBox.setMaximum(10000.000000000000000)
        self.right_radius_DSpinBox.setSingleStep(50.000000000000000)

        self.gridLayout_2.addWidget(self.right_radius_DSpinBox, 3, 1, 1, 1)

        self.help_Button = QPushButton(self.centralwidget)
        self.help_Button.setObjectName(u"help_Button")

        self.gridLayout_2.addWidget(self.help_Button, 5, 0, 1, 1)

        self.key_step_DSpinBox = QDoubleSpinBox(self.centralwidget)
        self.key_step_DSpinBox.setObjectName(u"key_step_DSpinBox")
        self.key_step_DSpinBox.setMaximum(100.000000000000000)
        self.key_step_DSpinBox.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.key_step_DSpinBox, 4, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Laser Resonator Designer", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wavelength (\u03bcm)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cavity Length (mm)", None))
        self.reset_Button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Right Mirror Radius (mm)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Function Key Step (mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Left Mirror Radius (mm)", None))
        self.help_Button.setText(QCoreApplication.translate("MainWindow", u"Function Key Help", None))
    # retranslateUi

