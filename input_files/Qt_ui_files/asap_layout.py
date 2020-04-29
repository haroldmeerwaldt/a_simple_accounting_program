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
        MainWindow.resize(1268, 829)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 40, 1221, 561))
        self.tab_times = QWidget()
        self.tab_times.setObjectName(u"tab_times")
        self.groupBox = QGroupBox(self.tab_times)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(350, 20, 861, 511))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 170, 831, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_times_overwrite = QPushButton(self.verticalLayoutWidget)
        self.pushButton_times_overwrite.setObjectName(u"pushButton_times_overwrite")

        self.horizontalLayout_2.addWidget(self.pushButton_times_overwrite)

        self.pushButton_times_delete = QPushButton(self.verticalLayoutWidget)
        self.pushButton_times_delete.setObjectName(u"pushButton_times_delete")

        self.horizontalLayout_2.addWidget(self.pushButton_times_delete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableView_times_query = QTableView(self.verticalLayoutWidget)
        self.tableView_times_query.setObjectName(u"tableView_times_query")

        self.verticalLayout.addWidget(self.tableView_times_query)

        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 20, 160, 126))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_times_query_start_month = QComboBox(self.formLayoutWidget)
        self.comboBox_times_query_start_month.setObjectName(u"comboBox_times_query_start_month")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_times_query_start_month)

        self.comboBox_times_query_stop_month = QComboBox(self.formLayoutWidget)
        self.comboBox_times_query_stop_month.setObjectName(u"comboBox_times_query_stop_month")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_times_query_stop_month)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.comboBox_times_query_start_year = QComboBox(self.formLayoutWidget)
        self.comboBox_times_query_start_year.setObjectName(u"comboBox_times_query_start_year")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_times_query_start_year)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.comboBox_times_query_stop_year = QComboBox(self.formLayoutWidget)
        self.comboBox_times_query_stop_year.setObjectName(u"comboBox_times_query_stop_year")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_times_query_stop_year)

        self.comboBox_times_query_client = QComboBox(self.formLayoutWidget)
        self.comboBox_times_query_client.setObjectName(u"comboBox_times_query_client")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox_times_query_client)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(370, 40, 161, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_times_sort_by_date_only = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_times_sort_by_date_only.setObjectName(u"radioButton_times_sort_by_date_only")

        self.verticalLayout_2.addWidget(self.radioButton_times_sort_by_date_only)

        self.radioButton_times_sort_by_client_first = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_times_sort_by_client_first.setObjectName(u"radioButton_times_sort_by_client_first")

        self.verticalLayout_2.addWidget(self.radioButton_times_sort_by_client_first)

        self.radioButton_times_sort_by_month_then_by_client = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_times_sort_by_month_then_by_client.setObjectName(u"radioButton_times_sort_by_month_then_by_client")

        self.verticalLayout_2.addWidget(self.radioButton_times_sort_by_month_then_by_client)

        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(650, 20, 119, 138))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_times_query_dates_only = QPushButton(self.layoutWidget)
        self.pushButton_times_query_dates_only.setObjectName(u"pushButton_times_query_dates_only")

        self.verticalLayout_3.addWidget(self.pushButton_times_query_dates_only)

        self.pushButton_times_query_client_only = QPushButton(self.layoutWidget)
        self.pushButton_times_query_client_only.setObjectName(u"pushButton_times_query_client_only")

        self.verticalLayout_3.addWidget(self.pushButton_times_query_client_only)

        self.pushButton_times_query_dates_and_client = QPushButton(self.layoutWidget)
        self.pushButton_times_query_dates_and_client.setObjectName(u"pushButton_times_query_dates_and_client")

        self.verticalLayout_3.addWidget(self.pushButton_times_query_dates_and_client)

        self.pushButton_times_export_query_results = QPushButton(self.layoutWidget)
        self.pushButton_times_export_query_results.setObjectName(u"pushButton_times_export_query_results")

        self.verticalLayout_3.addWidget(self.pushButton_times_export_query_results)

        self.groupBox_2 = QGroupBox(self.tab_times)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 311, 351))
        self.pushButton_add_working_day = QPushButton(self.groupBox_2)
        self.pushButton_add_working_day.setObjectName(u"pushButton_add_working_day")
        self.pushButton_add_working_day.setGeometry(QRect(180, 250, 75, 75))
        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(30, 40, 241, 196))
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

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_times_start_time)

        self.label_times_stop_time = QLabel(self.formLayoutWidget_2)
        self.label_times_stop_time.setObjectName(u"label_times_stop_time")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_times_stop_time)

        self.comboBox_times_start_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_start_time.setObjectName(u"comboBox_times_start_time")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.comboBox_times_start_time)

        self.comboBox_times_stop_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_stop_time.setObjectName(u"comboBox_times_stop_time")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.comboBox_times_stop_time)

        self.lineEdit_times_date = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_times_date.setObjectName(u"lineEdit_times_date")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_times_date)

        self.pushButton_times_fill_in_today = QPushButton(self.formLayoutWidget_2)
        self.pushButton_times_fill_in_today.setObjectName(u"pushButton_times_fill_in_today")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.pushButton_times_fill_in_today)

        self.label_times_hours = QLabel(self.formLayoutWidget_2)
        self.label_times_hours.setObjectName(u"label_times_hours")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_times_hours)

        self.info_label_times_hours = QLabel(self.formLayoutWidget_2)
        self.info_label_times_hours.setObjectName(u"info_label_times_hours")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.info_label_times_hours)

        self.pushButton_times_increment_by_one_week = QPushButton(self.formLayoutWidget_2)
        self.pushButton_times_increment_by_one_week.setObjectName(u"pushButton_times_increment_by_one_week")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pushButton_times_increment_by_one_week)

        self.info_label_day_of_week = QLabel(self.formLayoutWidget_2)
        self.info_label_day_of_week.setObjectName(u"info_label_day_of_week")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.info_label_day_of_week)

        self.label_day_of_week = QLabel(self.formLayoutWidget_2)
        self.label_day_of_week.setObjectName(u"label_day_of_week")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_day_of_week)

        self.pushButton_times_clear_fields = QPushButton(self.groupBox_2)
        self.pushButton_times_clear_fields.setObjectName(u"pushButton_times_clear_fields")
        self.pushButton_times_clear_fields.setGeometry(QRect(60, 250, 75, 75))
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
        self.textBrowser_console.setGeometry(QRect(40, 620, 1201, 131))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1268, 21))
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
        self.pushButton_times_overwrite.setText(QCoreApplication.translate("MainWindow", u"Overwrite", None))
        self.pushButton_times_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start month", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stop month", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start year", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stop year", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.radioButton_times_sort_by_date_only.setText(QCoreApplication.translate("MainWindow", u"Sort by date only", None))
        self.radioButton_times_sort_by_client_first.setText(QCoreApplication.translate("MainWindow", u"Sort by client first", None))
        self.radioButton_times_sort_by_month_then_by_client.setText(QCoreApplication.translate("MainWindow", u"Sort by month then by client", None))
        self.pushButton_times_query_dates_only.setText(QCoreApplication.translate("MainWindow", u"Query dates only", None))
        self.pushButton_times_query_client_only.setText(QCoreApplication.translate("MainWindow", u"Query client only", None))
        self.pushButton_times_query_dates_and_client.setText(QCoreApplication.translate("MainWindow", u"Query dates and client", None))
        self.pushButton_times_export_query_results.setText(QCoreApplication.translate("MainWindow", u"Export query results", None))
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
        self.pushButton_times_increment_by_one_week.setText(QCoreApplication.translate("MainWindow", u"Increment by one week", None))
        self.info_label_day_of_week.setText("")
        self.label_day_of_week.setText(QCoreApplication.translate("MainWindow", u"Day of week", None))
        self.pushButton_times_clear_fields.setText(QCoreApplication.translate("MainWindow", u"Clear fields", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_times), QCoreApplication.translate("MainWindow", u"Times", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clients), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_invoices), QCoreApplication.translate("MainWindow", u"Invoices", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_configuration), QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

