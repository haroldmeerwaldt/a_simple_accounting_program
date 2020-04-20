# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asap_layout.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 829)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 40, 1051, 561))
        self.tab_times = QWidget()
        self.tab_times.setObjectName(u"tab_times")
        self.groupBox = QGroupBox(self.tab_times)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(350, 20, 681, 511))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 170, 641, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 20, 160, 126))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_2)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.comboBox_3 = QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_3)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.comboBox_4 = QComboBox(self.formLayoutWidget)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_4)

        self.comboBox_5 = QComboBox(self.formLayoutWidget)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox_5)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(290, 50, 161, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(510, 20, 119, 138))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.groupBox_2 = QGroupBox(self.tab_times)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 311, 321))
        self.pushButton_add_working_day = QPushButton(self.groupBox_2)
        self.pushButton_add_working_day.setObjectName(u"pushButton_add_working_day")
        self.pushButton_add_working_day.setGeometry(QRect(180, 230, 75, 75))
        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(30, 40, 241, 151))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_times_client = QLabel(self.formLayoutWidget_2)
        self.label_times_client.setObjectName(u"label_times_client")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_times_client)

        self.label_times_date = QLabel(self.formLayoutWidget_2)
        self.label_times_date.setObjectName(u"label_times_date")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_times_date)

        self.comboBox_times_client = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_client.setObjectName(u"comboBox_times_client")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_times_client)

        self.label_times_start_time = QLabel(self.formLayoutWidget_2)
        self.label_times_start_time.setObjectName(u"label_times_start_time")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_times_start_time)

        self.label_times_stop_time = QLabel(self.formLayoutWidget_2)
        self.label_times_stop_time.setObjectName(u"label_times_stop_time")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_times_stop_time)

        self.comboBox_times_start_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_start_time.setObjectName(u"comboBox_times_start_time")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBox_times_start_time)

        self.comboBox_times_stop_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_stop_time.setObjectName(u"comboBox_times_stop_time")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBox_times_stop_time)

        self.lineEdit_times_date = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_times_date.setObjectName(u"lineEdit_times_date")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_times_date)

        self.pushButton_times_fill_in_today = QPushButton(self.formLayoutWidget_2)
        self.pushButton_times_fill_in_today.setObjectName(u"pushButton_times_fill_in_today")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pushButton_times_fill_in_today)

        self.label_times_hours = QLabel(self.formLayoutWidget_2)
        self.label_times_hours.setObjectName(u"label_times_hours")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_times_hours)

        self.info_label_times_hours = QLabel(self.formLayoutWidget_2)
        self.info_label_times_hours.setObjectName(u"info_label_times_hours")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.info_label_times_hours)

        self.pushButton_times_clear_fields = QPushButton(self.groupBox_2)
        self.pushButton_times_clear_fields.setObjectName(u"pushButton_times_clear_fields")
        self.pushButton_times_clear_fields.setGeometry(QRect(60, 230, 75, 75))
        self.tabWidget.addTab(self.tab_times, "")
        self.tab_clients = QWidget()
        self.tab_clients.setObjectName(u"tab_clients")
        self.tabWidget.addTab(self.tab_clients, "")
        self.tab_invoices = QWidget()
        self.tab_invoices.setObjectName(u"tab_invoices")
        self.tabWidget.addTab(self.tab_invoices, "")
        self.tab_configuration = QWidget()
        self.tab_configuration.setObjectName(u"tab_configuration")
        self.tabWidget.addTab(self.tab_configuration, "")
        self.textBrowser_console = QTextBrowser(self.centralwidget)
        self.textBrowser_console.setObjectName(u"textBrowser_console")
        self.textBrowser_console.setGeometry(QRect(40, 620, 1031, 131))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1111, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Query", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Overwrite", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start month", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"End month", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start year", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"End year", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Sort by date only", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Sort by client first", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Sort by month then by client", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Query dates only", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Query client only", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Query dates and client", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Export query results", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_add_working_day.setText(QCoreApplication.translate("MainWindow", u"Add \n"
"working day", None))
        self.label_times_client.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.label_times_date.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_times_start_time.setText(QCoreApplication.translate("MainWindow", u"Start time", None))
        self.label_times_stop_time.setText(QCoreApplication.translate("MainWindow", u"Stop time", None))
        self.pushButton_times_fill_in_today.setText(QCoreApplication.translate("MainWindow", u"Fill in today", None))
        self.label_times_hours.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.info_label_times_hours.setText("")
        self.pushButton_times_clear_fields.setText(QCoreApplication.translate("MainWindow", u"Clear fields", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_times), QCoreApplication.translate("MainWindow", u"Times", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clients), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_invoices), QCoreApplication.translate("MainWindow", u"Invoices", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_configuration), QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

