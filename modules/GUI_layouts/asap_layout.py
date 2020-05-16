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
        self.formLayoutWidget.setGeometry(QRect(70, 20, 160, 136))
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
        self.verticalLayoutWidget_2.setGeometry(QRect(450, 40, 186, 80))
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

        self.verticalLayoutWidget_5 = QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(260, 40, 162, 88))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.radioButton_times_query_dates_only = QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton_times_query_dates_only.setObjectName(u"radioButton_times_query_dates_only")

        self.verticalLayout_7.addWidget(self.radioButton_times_query_dates_only)

        self.radioButton_times_query_client_only = QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton_times_query_client_only.setObjectName(u"radioButton_times_query_client_only")

        self.verticalLayout_7.addWidget(self.radioButton_times_query_client_only)

        self.radioButton_times_query_dates_and_client = QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton_times_query_dates_and_client.setObjectName(u"radioButton_times_query_dates_and_client")

        self.verticalLayout_7.addWidget(self.radioButton_times_query_dates_and_client)

        self.radioButton = QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_7.addWidget(self.radioButton)

        self.pushButton_times_run_query = QPushButton(self.groupBox)
        self.pushButton_times_run_query.setObjectName(u"pushButton_times_run_query")
        self.pushButton_times_run_query.setGeometry(QRect(660, 40, 75, 75))
        self.pushButton_times_export_query_results = QPushButton(self.groupBox)
        self.pushButton_times_export_query_results.setObjectName(u"pushButton_times_export_query_results")
        self.pushButton_times_export_query_results.setGeometry(QRect(760, 40, 75, 75))
        self.groupBox_2 = QGroupBox(self.tab_times)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 311, 381))
        self.pushButton_add_working_day = QPushButton(self.groupBox_2)
        self.pushButton_add_working_day.setObjectName(u"pushButton_add_working_day")
        self.pushButton_add_working_day.setGeometry(QRect(180, 290, 75, 75))
        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(30, 40, 241, 234))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_times_client = QLabel(self.formLayoutWidget_2)
        self.label_times_client.setObjectName(u"label_times_client")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_times_client)

        self.label_times_date = QLabel(self.formLayoutWidget_2)
        self.label_times_date.setObjectName(u"label_times_date")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_times_date)

        self.comboBox_times_client = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_client.setObjectName(u"comboBox_times_client")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_times_client)

        self.label_times_start_time = QLabel(self.formLayoutWidget_2)
        self.label_times_start_time.setObjectName(u"label_times_start_time")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_times_start_time)

        self.label_times_stop_time = QLabel(self.formLayoutWidget_2)
        self.label_times_stop_time.setObjectName(u"label_times_stop_time")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_times_stop_time)

        self.comboBox_times_start_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_start_time.setObjectName(u"comboBox_times_start_time")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.comboBox_times_start_time)

        self.comboBox_times_stop_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_stop_time.setObjectName(u"comboBox_times_stop_time")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.comboBox_times_stop_time)

        self.lineEdit_times_date = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_times_date.setObjectName(u"lineEdit_times_date")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_times_date)

        self.pushButton_times_fill_in_today = QPushButton(self.formLayoutWidget_2)
        self.pushButton_times_fill_in_today.setObjectName(u"pushButton_times_fill_in_today")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pushButton_times_fill_in_today)

        self.label_times_hours = QLabel(self.formLayoutWidget_2)
        self.label_times_hours.setObjectName(u"label_times_hours")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_times_hours)

        self.info_label_times_hours = QLabel(self.formLayoutWidget_2)
        self.info_label_times_hours.setObjectName(u"info_label_times_hours")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.info_label_times_hours)

        self.pushButton_times_increment_by_one_week = QPushButton(self.formLayoutWidget_2)
        self.pushButton_times_increment_by_one_week.setObjectName(u"pushButton_times_increment_by_one_week")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.pushButton_times_increment_by_one_week)

        self.info_label_day_of_week = QLabel(self.formLayoutWidget_2)
        self.info_label_day_of_week.setObjectName(u"info_label_day_of_week")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.info_label_day_of_week)

        self.label_day_of_week = QLabel(self.formLayoutWidget_2)
        self.label_day_of_week.setObjectName(u"label_day_of_week")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_day_of_week)

        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.info_label_times_client_code = QLabel(self.formLayoutWidget_2)
        self.info_label_times_client_code.setObjectName(u"info_label_times_client_code")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.info_label_times_client_code)

        self.label_12 = QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_12)

        self.info_label_times_invoice_number = QLabel(self.formLayoutWidget_2)
        self.info_label_times_invoice_number.setObjectName(u"info_label_times_invoice_number")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.info_label_times_invoice_number)

        self.pushButton_times_clear_fields = QPushButton(self.groupBox_2)
        self.pushButton_times_clear_fields.setObjectName(u"pushButton_times_clear_fields")
        self.pushButton_times_clear_fields.setGeometry(QRect(60, 290, 75, 75))
        self.tabWidget.addTab(self.tab_times, "")
        self.tab_clients = QWidget()
        self.tab_clients.setObjectName(u"tab_clients")
        self.groupBox_3 = QGroupBox(self.tab_clients)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 311, 221))
        self.pushButton_add_client = QPushButton(self.groupBox_3)
        self.pushButton_add_client.setObjectName(u"pushButton_add_client")
        self.pushButton_add_client.setGeometry(QRect(180, 130, 75, 75))
        self.formLayoutWidget_3 = QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(30, 40, 241, 71))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_times_client_2 = QLabel(self.formLayoutWidget_3)
        self.label_times_client_2.setObjectName(u"label_times_client_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_times_client_2)

        self.lineEdit_clients_client_name = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_clients_client_name.setObjectName(u"lineEdit_clients_client_name")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_clients_client_name)

        self.label_times_date_2 = QLabel(self.formLayoutWidget_3)
        self.label_times_date_2.setObjectName(u"label_times_date_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_times_date_2)

        self.comboBox_clients_first_year = QComboBox(self.formLayoutWidget_3)
        self.comboBox_clients_first_year.setObjectName(u"comboBox_clients_first_year")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.comboBox_clients_first_year)

        self.label_day_of_week_2 = QLabel(self.formLayoutWidget_3)
        self.label_day_of_week_2.setObjectName(u"label_day_of_week_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_day_of_week_2)

        self.info_label_clients_client_code = QLabel(self.formLayoutWidget_3)
        self.info_label_clients_client_code.setObjectName(u"info_label_clients_client_code")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.info_label_clients_client_code)

        self.pushButton_clients_clear_fields = QPushButton(self.groupBox_3)
        self.pushButton_clients_clear_fields.setObjectName(u"pushButton_clients_clear_fields")
        self.pushButton_clients_clear_fields.setGeometry(QRect(60, 130, 75, 75))
        self.groupBox_4 = QGroupBox(self.tab_clients)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(350, 20, 861, 511))
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 170, 831, 331))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_clients_overwrite = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_clients_overwrite.setObjectName(u"pushButton_clients_overwrite")

        self.horizontalLayout_3.addWidget(self.pushButton_clients_overwrite)

        self.pushButton_clients_delete = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_clients_delete.setObjectName(u"pushButton_clients_delete")

        self.horizontalLayout_3.addWidget(self.pushButton_clients_delete)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.tableView_clients_query = QTableView(self.verticalLayoutWidget_3)
        self.tableView_clients_query.setObjectName(u"tableView_clients_query")

        self.verticalLayout_4.addWidget(self.tableView_clients_query)

        self.formLayoutWidget_4 = QWidget(self.groupBox_4)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(70, 50, 160, 51))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.formLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.comboBox_clients_query_start_year = QComboBox(self.formLayoutWidget_4)
        self.comboBox_clients_query_start_year.setObjectName(u"comboBox_clients_query_start_year")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.comboBox_clients_query_start_year)

        self.label_9 = QLabel(self.formLayoutWidget_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.comboBox_clients_query_stop_year = QComboBox(self.formLayoutWidget_4)
        self.comboBox_clients_query_stop_year.setObjectName(u"comboBox_clients_query_stop_year")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.comboBox_clients_query_stop_year)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(261, 50, 161, 51))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.radioButton_clients_query_using_years = QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_clients_query_using_years.setObjectName(u"radioButton_clients_query_using_years")

        self.verticalLayout_8.addWidget(self.radioButton_clients_query_using_years)

        self.radioButton_clients_query_return_all = QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_clients_query_return_all.setObjectName(u"radioButton_clients_query_return_all")

        self.verticalLayout_8.addWidget(self.radioButton_clients_query_return_all)

        self.pushButton_clients_export_query_results = QPushButton(self.groupBox_4)
        self.pushButton_clients_export_query_results.setObjectName(u"pushButton_clients_export_query_results")
        self.pushButton_clients_export_query_results.setGeometry(QRect(760, 40, 75, 75))
        self.pushButton_clients_run_query = QPushButton(self.groupBox_4)
        self.pushButton_clients_run_query.setObjectName(u"pushButton_clients_run_query")
        self.pushButton_clients_run_query.setGeometry(QRect(660, 40, 75, 75))
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

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Query working days", None))
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
        self.radioButton_times_query_dates_only.setText(QCoreApplication.translate("MainWindow", u"Query using dates only", None))
        self.radioButton_times_query_client_only.setText(QCoreApplication.translate("MainWindow", u"Query using client only", None))
        self.radioButton_times_query_dates_and_client.setText(QCoreApplication.translate("MainWindow", u"Query using dates and client", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Return all", None))
        self.pushButton_times_run_query.setText(QCoreApplication.translate("MainWindow", u"Run query", None))
        self.pushButton_times_export_query_results.setText(QCoreApplication.translate("MainWindow", u"Export \n"
"query \n"
"results", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Add working days", None))
        self.pushButton_add_working_day.setText(QCoreApplication.translate("MainWindow", u"Add \n"
"working \n"
"day", None))
        self.label_times_client.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.label_times_date.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_times_start_time.setText(QCoreApplication.translate("MainWindow", u"Start time", None))
        self.label_times_stop_time.setText(QCoreApplication.translate("MainWindow", u"Stop time", None))
        self.pushButton_times_fill_in_today.setText(QCoreApplication.translate("MainWindow", u"Fill in today", None))
        self.label_times_hours.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.info_label_times_hours.setText("")
        self.pushButton_times_increment_by_one_week.setText(QCoreApplication.translate("MainWindow", u"Increment by one week", None))
        self.info_label_day_of_week.setText("")
        self.label_day_of_week.setText(QCoreApplication.translate("MainWindow", u"Day of week", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Client code", None))
        self.info_label_times_client_code.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Invoice number", None))
        self.info_label_times_invoice_number.setText("")
        self.pushButton_times_clear_fields.setText(QCoreApplication.translate("MainWindow", u"Clear fields", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_times), QCoreApplication.translate("MainWindow", u"Times", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Add clients", None))
        self.pushButton_add_client.setText(QCoreApplication.translate("MainWindow", u"Add client", None))
        self.label_times_client_2.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.label_times_date_2.setText(QCoreApplication.translate("MainWindow", u"First year", None))
        self.label_day_of_week_2.setText(QCoreApplication.translate("MainWindow", u"Client code", None))
        self.info_label_clients_client_code.setText("")
        self.pushButton_clients_clear_fields.setText(QCoreApplication.translate("MainWindow", u"Clear fields", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Query clients", None))
        self.pushButton_clients_overwrite.setText(QCoreApplication.translate("MainWindow", u"Overwrite", None))
        self.pushButton_clients_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Start year", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Stop year", None))
        self.radioButton_clients_query_using_years.setText(QCoreApplication.translate("MainWindow", u"Query using years", None))
        self.radioButton_clients_query_return_all.setText(QCoreApplication.translate("MainWindow", u"Return all", None))
        self.pushButton_clients_export_query_results.setText(QCoreApplication.translate("MainWindow", u"Export \n"
"query \n"
"results", None))
        self.pushButton_clients_run_query.setText(QCoreApplication.translate("MainWindow", u"Run query", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clients), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_invoices), QCoreApplication.translate("MainWindow", u"Invoices", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_configuration), QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

