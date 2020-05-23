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

        self.comboBox_times_query_client_name = QComboBox(self.formLayoutWidget)
        self.comboBox_times_query_client_name.setObjectName(u"comboBox_times_query_client_name")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox_times_query_client_name)

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

        self.radioButton_times_query_return_all = QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton_times_query_return_all.setObjectName(u"radioButton_times_query_return_all")

        self.verticalLayout_7.addWidget(self.radioButton_times_query_return_all)

        self.pushButton_times_run_query = QPushButton(self.groupBox)
        self.pushButton_times_run_query.setObjectName(u"pushButton_times_run_query")
        self.pushButton_times_run_query.setGeometry(QRect(660, 40, 75, 75))
        self.pushButton_times_export_query_results = QPushButton(self.groupBox)
        self.pushButton_times_export_query_results.setObjectName(u"pushButton_times_export_query_results")
        self.pushButton_times_export_query_results.setGeometry(QRect(760, 40, 75, 75))
        self.groupBox_2 = QGroupBox(self.tab_times)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 311, 491))
        self.pushButton_add_working_day = QPushButton(self.groupBox_2)
        self.pushButton_add_working_day.setObjectName(u"pushButton_add_working_day")
        self.pushButton_add_working_day.setGeometry(QRect(180, 390, 75, 75))
        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(30, 40, 241, 320))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_times_client = QLabel(self.formLayoutWidget_2)
        self.label_times_client.setObjectName(u"label_times_client")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_times_client)

        self.comboBox_times_client_name = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_client_name.setObjectName(u"comboBox_times_client_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_times_client_name)

        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.info_label_times_client_code = QLabel(self.formLayoutWidget_2)
        self.info_label_times_client_code.setObjectName(u"info_label_times_client_code")
        self.info_label_times_client_code.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.info_label_times_client_code)

        self.label_times_date = QLabel(self.formLayoutWidget_2)
        self.label_times_date.setObjectName(u"label_times_date")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_times_date)

        self.lineEdit_times_date = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_times_date.setObjectName(u"lineEdit_times_date")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_times_date)

        self.label_day_of_week = QLabel(self.formLayoutWidget_2)
        self.label_day_of_week.setObjectName(u"label_day_of_week")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_day_of_week)

        self.info_label_day_of_week = QLabel(self.formLayoutWidget_2)
        self.info_label_day_of_week.setObjectName(u"info_label_day_of_week")
        self.info_label_day_of_week.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.info_label_day_of_week)

        self.pushButton_times_fill_in_today = QPushButton(self.formLayoutWidget_2)
        self.pushButton_times_fill_in_today.setObjectName(u"pushButton_times_fill_in_today")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pushButton_times_fill_in_today)

        self.pushButton_times_increment_by_one_week = QPushButton(self.formLayoutWidget_2)
        self.pushButton_times_increment_by_one_week.setObjectName(u"pushButton_times_increment_by_one_week")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.pushButton_times_increment_by_one_week)

        self.label_times_start_time = QLabel(self.formLayoutWidget_2)
        self.label_times_start_time.setObjectName(u"label_times_start_time")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_times_start_time)

        self.comboBox_times_start_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_start_time.setObjectName(u"comboBox_times_start_time")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.comboBox_times_start_time)

        self.label_times_stop_time = QLabel(self.formLayoutWidget_2)
        self.label_times_stop_time.setObjectName(u"label_times_stop_time")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_times_stop_time)

        self.comboBox_times_stop_time = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_stop_time.setObjectName(u"comboBox_times_stop_time")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.comboBox_times_stop_time)

        self.label_times_hours = QLabel(self.formLayoutWidget_2)
        self.label_times_hours.setObjectName(u"label_times_hours")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_times_hours)

        self.info_label_times_hours = QLabel(self.formLayoutWidget_2)
        self.info_label_times_hours.setObjectName(u"info_label_times_hours")
        self.info_label_times_hours.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.info_label_times_hours)

        self.label_12 = QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_commute_km = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_commute_km.setObjectName(u"lineEdit_commute_km")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.lineEdit_commute_km)

        self.label_18 = QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_distance_during_work_km = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_distance_during_work_km.setObjectName(u"lineEdit_distance_during_work_km")

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.lineEdit_distance_during_work_km)

        self.label_32 = QLabel(self.formLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_32)

        self.comboBox_times_type_of_hours = QComboBox(self.formLayoutWidget_2)
        self.comboBox_times_type_of_hours.setObjectName(u"comboBox_times_type_of_hours")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.comboBox_times_type_of_hours)

        self.pushButton_times_clear_fields = QPushButton(self.groupBox_2)
        self.pushButton_times_clear_fields.setObjectName(u"pushButton_times_clear_fields")
        self.pushButton_times_clear_fields.setGeometry(QRect(60, 390, 75, 75))
        self.tabWidget.addTab(self.tab_times, "")
        self.tab_clients = QWidget()
        self.tab_clients.setObjectName(u"tab_clients")
        self.groupBox_3 = QGroupBox(self.tab_clients)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 311, 511))
        self.pushButton_add_client = QPushButton(self.groupBox_3)
        self.pushButton_add_client.setObjectName(u"pushButton_add_client")
        self.pushButton_add_client.setGeometry(QRect(180, 430, 75, 75))
        self.pushButton_clients_clear_fields = QPushButton(self.groupBox_3)
        self.pushButton_clients_clear_fields.setObjectName(u"pushButton_clients_clear_fields")
        self.pushButton_clients_clear_fields.setGeometry(QRect(60, 430, 75, 75))
        self.gridLayoutWidget = QWidget(self.groupBox_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 20, 231, 403))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_times_date_2 = QLabel(self.gridLayoutWidget)
        self.label_times_date_2.setObjectName(u"label_times_date_2")

        self.gridLayout.addWidget(self.label_times_date_2, 1, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 5, 0, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 10, 0, 1, 1)

        self.info_label_clients_index_within_year = QLabel(self.gridLayoutWidget)
        self.info_label_clients_index_within_year.setObjectName(u"info_label_clients_index_within_year")
        self.info_label_clients_index_within_year.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.info_label_clients_index_within_year, 2, 1, 1, 1)

        self.label_day_of_week_2 = QLabel(self.gridLayoutWidget)
        self.label_day_of_week_2.setObjectName(u"label_day_of_week_2")

        self.gridLayout.addWidget(self.label_day_of_week_2, 3, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 7, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 8, 0, 1, 1)

        self.lineEdit_clients_standard_rate_for_shifts = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_standard_rate_for_shifts.setObjectName(u"lineEdit_clients_standard_rate_for_shifts")

        self.gridLayout.addWidget(self.lineEdit_clients_standard_rate_for_shifts, 8, 1, 1, 1)

        self.lineEdit_clients_standard_compensation_for_commute = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_standard_compensation_for_commute.setObjectName(u"lineEdit_clients_standard_compensation_for_commute")

        self.gridLayout.addWidget(self.lineEdit_clients_standard_compensation_for_commute, 9, 1, 1, 1)

        self.label_times_client_2 = QLabel(self.gridLayoutWidget)
        self.label_times_client_2.setObjectName(u"label_times_client_2")

        self.gridLayout.addWidget(self.label_times_client_2, 0, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 4, 0, 1, 1)

        self.lineEdit_clients_standard_rate_during_day = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_standard_rate_during_day.setObjectName(u"lineEdit_clients_standard_rate_during_day")

        self.gridLayout.addWidget(self.lineEdit_clients_standard_rate_during_day, 7, 1, 1, 1)

        self.comboBox_clients_first_year = QComboBox(self.gridLayoutWidget)
        self.comboBox_clients_first_year.setObjectName(u"comboBox_clients_first_year")

        self.gridLayout.addWidget(self.comboBox_clients_first_year, 1, 1, 1, 1)

        self.lineEdit_clients_standard_compensation_for_driving_during_work = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_standard_compensation_for_driving_during_work.setObjectName(u"lineEdit_clients_standard_compensation_for_driving_during_work")

        self.gridLayout.addWidget(self.lineEdit_clients_standard_compensation_for_driving_during_work, 10, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.info_label_clients_client_code = QLabel(self.gridLayoutWidget)
        self.info_label_clients_client_code.setObjectName(u"info_label_clients_client_code")
        self.info_label_clients_client_code.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.info_label_clients_client_code, 3, 1, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 9, 0, 1, 1)

        self.lineEdit_clients_client_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_client_name.setObjectName(u"lineEdit_clients_client_name")

        self.gridLayout.addWidget(self.lineEdit_clients_client_name, 0, 1, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 6, 0, 1, 1)

        self.lineEdit_clients_person_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_person_name.setObjectName(u"lineEdit_clients_person_name")

        self.gridLayout.addWidget(self.lineEdit_clients_person_name, 4, 1, 1, 1)

        self.lineEdit_clients_address = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_address.setObjectName(u"lineEdit_clients_address")

        self.gridLayout.addWidget(self.lineEdit_clients_address, 5, 1, 1, 1)

        self.lineEdit_clients_postal_code_and_city = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_clients_postal_code_and_city.setObjectName(u"lineEdit_clients_postal_code_and_city")

        self.gridLayout.addWidget(self.lineEdit_clients_postal_code_and_city, 6, 1, 1, 1)

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
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(450, 50, 186, 51))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_clients_sort_by_year_and_index = QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_clients_sort_by_year_and_index.setObjectName(u"radioButton_clients_sort_by_year_and_index")

        self.verticalLayout_3.addWidget(self.radioButton_clients_sort_by_year_and_index)

        self.radioButton_clients_sort_by_client_name = QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_clients_sort_by_client_name.setObjectName(u"radioButton_clients_sort_by_client_name")

        self.verticalLayout_3.addWidget(self.radioButton_clients_sort_by_client_name)

        self.tabWidget.addTab(self.tab_clients, "")
        self.tab_invoices = QWidget()
        self.tab_invoices.setObjectName(u"tab_invoices")
        self.groupBox_5 = QGroupBox(self.tab_invoices)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 20, 311, 511))
        self.pushButton_generate_invoice = QPushButton(self.groupBox_5)
        self.pushButton_generate_invoice.setObjectName(u"pushButton_generate_invoice")
        self.pushButton_generate_invoice.setGeometry(QRect(180, 430, 75, 75))
        self.pushButton_invoices_clear_fields = QPushButton(self.groupBox_5)
        self.pushButton_invoices_clear_fields.setObjectName(u"pushButton_invoices_clear_fields")
        self.pushButton_invoices_clear_fields.setGeometry(QRect(60, 430, 75, 75))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 20, 241, 399))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.info_label_invoices_client_code = QLabel(self.gridLayoutWidget_2)
        self.info_label_invoices_client_code.setObjectName(u"info_label_invoices_client_code")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_label_invoices_client_code.sizePolicy().hasHeightForWidth())
        self.info_label_invoices_client_code.setSizePolicy(sizePolicy)
        self.info_label_invoices_client_code.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.info_label_invoices_client_code, 1, 1, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 10, 0, 1, 1)

        self.label_times_client_3 = QLabel(self.gridLayoutWidget_2)
        self.label_times_client_3.setObjectName(u"label_times_client_3")

        self.gridLayout_2.addWidget(self.label_times_client_3, 0, 0, 1, 1)

        self.pushButton_invoices_fill_in_today = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_invoices_fill_in_today.setObjectName(u"pushButton_invoices_fill_in_today")

        self.gridLayout_2.addWidget(self.pushButton_invoices_fill_in_today, 7, 1, 1, 1)

        self.lineEdit_invoices_rate_during_day = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_invoices_rate_during_day.setObjectName(u"lineEdit_invoices_rate_during_day")

        self.gridLayout_2.addWidget(self.lineEdit_invoices_rate_during_day, 8, 1, 1, 1)

        self.lineEdit_invoices_rate_for_shifts = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_invoices_rate_for_shifts.setObjectName(u"lineEdit_invoices_rate_for_shifts")

        self.gridLayout_2.addWidget(self.lineEdit_invoices_rate_for_shifts, 9, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 6, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 9, 0, 1, 1)

        self.comboBox_invoices_client_name = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_invoices_client_name.setObjectName(u"comboBox_invoices_client_name")

        self.gridLayout_2.addWidget(self.comboBox_invoices_client_name, 0, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_day_of_week_3 = QLabel(self.gridLayoutWidget_2)
        self.label_day_of_week_3.setObjectName(u"label_day_of_week_3")

        self.gridLayout_2.addWidget(self.label_day_of_week_3, 5, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 8, 0, 1, 1)

        self.lineEdit_invoices_invoice_date = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_invoices_invoice_date.setObjectName(u"lineEdit_invoices_invoice_date")

        self.gridLayout_2.addWidget(self.lineEdit_invoices_invoice_date, 6, 1, 1, 1)

        self.lineEdit_invoices_compensation_for_commute = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_invoices_compensation_for_commute.setObjectName(u"lineEdit_invoices_compensation_for_commute")

        self.gridLayout_2.addWidget(self.lineEdit_invoices_compensation_for_commute, 10, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 11, 0, 1, 1)

        self.lineEdit_invoices_compensation_for_driving_during_work = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_invoices_compensation_for_driving_during_work.setObjectName(u"lineEdit_invoices_compensation_for_driving_during_work")

        self.gridLayout_2.addWidget(self.lineEdit_invoices_compensation_for_driving_during_work, 11, 1, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 7, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.label_33, 2, 0, 1, 1)

        self.label_times_date_3 = QLabel(self.gridLayoutWidget_2)
        self.label_times_date_3.setObjectName(u"label_times_date_3")

        self.gridLayout_2.addWidget(self.label_times_date_3, 4, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 3, 0, 1, 1)

        self.comboBox_invoices_year = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_invoices_year.setObjectName(u"comboBox_invoices_year")

        self.gridLayout_2.addWidget(self.comboBox_invoices_year, 5, 1, 1, 1)

        self.comboBox_invoices_month = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_invoices_month.setObjectName(u"comboBox_invoices_month")

        self.gridLayout_2.addWidget(self.comboBox_invoices_month, 4, 1, 1, 1)

        self.info_label_invoices_invoice_number = QLabel(self.gridLayoutWidget_2)
        self.info_label_invoices_invoice_number.setObjectName(u"info_label_invoices_invoice_number")
        sizePolicy.setHeightForWidth(self.info_label_invoices_invoice_number.sizePolicy().hasHeightForWidth())
        self.info_label_invoices_invoice_number.setSizePolicy(sizePolicy)
        self.info_label_invoices_invoice_number.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.info_label_invoices_invoice_number, 3, 1, 1, 1)

        self.info_label_invoices_invoice_index_at_client = QLabel(self.gridLayoutWidget_2)
        self.info_label_invoices_invoice_index_at_client.setObjectName(u"info_label_invoices_invoice_index_at_client")
        self.info_label_invoices_invoice_index_at_client.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.info_label_invoices_invoice_index_at_client, 2, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_invoices)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(350, 20, 861, 511))
        self.verticalLayoutWidget_7 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(20, 170, 831, 331))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_invoices_overwrite = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_invoices_overwrite.setObjectName(u"pushButton_invoices_overwrite")

        self.horizontalLayout_4.addWidget(self.pushButton_invoices_overwrite)

        self.pushButton_invoices_delete = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_invoices_delete.setObjectName(u"pushButton_invoices_delete")

        self.horizontalLayout_4.addWidget(self.pushButton_invoices_delete)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tableView_invoices_query = QTableView(self.verticalLayoutWidget_7)
        self.tableView_invoices_query.setObjectName(u"tableView_invoices_query")

        self.verticalLayout_5.addWidget(self.tableView_invoices_query)

        self.formLayoutWidget_6 = QWidget(self.groupBox_6)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(70, 20, 160, 136))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBox_invoices_query_start_month = QComboBox(self.formLayoutWidget_6)
        self.comboBox_invoices_query_start_month.setObjectName(u"comboBox_invoices_query_start_month")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.comboBox_invoices_query_start_month)

        self.comboBox_invoices_query_stop_month = QComboBox(self.formLayoutWidget_6)
        self.comboBox_invoices_query_stop_month.setObjectName(u"comboBox_invoices_query_stop_month")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.comboBox_invoices_query_stop_month)

        self.label_7 = QLabel(self.formLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.label_10 = QLabel(self.formLayoutWidget_6)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.comboBox_invoices_query_start_year = QComboBox(self.formLayoutWidget_6)
        self.comboBox_invoices_query_start_year.setObjectName(u"comboBox_invoices_query_start_year")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.comboBox_invoices_query_start_year)

        self.label_15 = QLabel(self.formLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.formLayoutWidget_6)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.formLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.comboBox_invoices_query_stop_year = QComboBox(self.formLayoutWidget_6)
        self.comboBox_invoices_query_stop_year.setObjectName(u"comboBox_invoices_query_stop_year")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.comboBox_invoices_query_stop_year)

        self.comboBox_invoices_query_client_name = QComboBox(self.formLayoutWidget_6)
        self.comboBox_invoices_query_client_name.setObjectName(u"comboBox_invoices_query_client_name")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.comboBox_invoices_query_client_name)

        self.verticalLayoutWidget_8 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(450, 40, 186, 80))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.radioButton_invoices_sort_by_date_only = QRadioButton(self.verticalLayoutWidget_8)
        self.radioButton_invoices_sort_by_date_only.setObjectName(u"radioButton_invoices_sort_by_date_only")

        self.verticalLayout_6.addWidget(self.radioButton_invoices_sort_by_date_only)

        self.radioButton_invoices_sort_by_client_first = QRadioButton(self.verticalLayoutWidget_8)
        self.radioButton_invoices_sort_by_client_first.setObjectName(u"radioButton_invoices_sort_by_client_first")

        self.verticalLayout_6.addWidget(self.radioButton_invoices_sort_by_client_first)

        self.radioButton_invoices_sort_by_month_then_by_client = QRadioButton(self.verticalLayoutWidget_8)
        self.radioButton_invoices_sort_by_month_then_by_client.setObjectName(u"radioButton_invoices_sort_by_month_then_by_client")

        self.verticalLayout_6.addWidget(self.radioButton_invoices_sort_by_month_then_by_client)

        self.verticalLayoutWidget_9 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(260, 40, 162, 88))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.radioButton_invoices_query_dates_only = QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_invoices_query_dates_only.setObjectName(u"radioButton_invoices_query_dates_only")

        self.verticalLayout_9.addWidget(self.radioButton_invoices_query_dates_only)

        self.radioButton_invoices_query_client_only = QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_invoices_query_client_only.setObjectName(u"radioButton_invoices_query_client_only")

        self.verticalLayout_9.addWidget(self.radioButton_invoices_query_client_only)

        self.radioButton_invoices_query_dates_and_client = QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_invoices_query_dates_and_client.setObjectName(u"radioButton_invoices_query_dates_and_client")

        self.verticalLayout_9.addWidget(self.radioButton_invoices_query_dates_and_client)

        self.radioButton_invoices_query_return_all = QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_invoices_query_return_all.setObjectName(u"radioButton_invoices_query_return_all")

        self.verticalLayout_9.addWidget(self.radioButton_invoices_query_return_all)

        self.pushButton_invoices_run_query = QPushButton(self.groupBox_6)
        self.pushButton_invoices_run_query.setObjectName(u"pushButton_invoices_run_query")
        self.pushButton_invoices_run_query.setGeometry(QRect(660, 40, 75, 75))
        self.pushButton_invoices_export_query_results = QPushButton(self.groupBox_6)
        self.pushButton_invoices_export_query_results.setObjectName(u"pushButton_invoices_export_query_results")
        self.pushButton_invoices_export_query_results.setGeometry(QRect(760, 40, 75, 75))
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

        self.tabWidget.setCurrentIndex(2)


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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.radioButton_times_sort_by_date_only.setText(QCoreApplication.translate("MainWindow", u"Sort by date only", None))
        self.radioButton_times_sort_by_client_first.setText(QCoreApplication.translate("MainWindow", u"Sort by client first", None))
        self.radioButton_times_sort_by_month_then_by_client.setText(QCoreApplication.translate("MainWindow", u"Sort by month then by client", None))
        self.radioButton_times_query_dates_only.setText(QCoreApplication.translate("MainWindow", u"Query using dates only", None))
        self.radioButton_times_query_client_only.setText(QCoreApplication.translate("MainWindow", u"Query using client only", None))
        self.radioButton_times_query_dates_and_client.setText(QCoreApplication.translate("MainWindow", u"Query using dates and client", None))
        self.radioButton_times_query_return_all.setText(QCoreApplication.translate("MainWindow", u"Return all", None))
        self.pushButton_times_run_query.setText(QCoreApplication.translate("MainWindow", u"Run query", None))
        self.pushButton_times_export_query_results.setText(QCoreApplication.translate("MainWindow", u"Export \n"
"query \n"
"results", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Add working days", None))
        self.pushButton_add_working_day.setText(QCoreApplication.translate("MainWindow", u"Add \n"
"working \n"
"day", None))
        self.label_times_client.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Client code", None))
        self.info_label_times_client_code.setText("")
        self.label_times_date.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_day_of_week.setText(QCoreApplication.translate("MainWindow", u"Day of week", None))
        self.info_label_day_of_week.setText("")
        self.pushButton_times_fill_in_today.setText(QCoreApplication.translate("MainWindow", u"Fill in today", None))
        self.pushButton_times_increment_by_one_week.setText(QCoreApplication.translate("MainWindow", u"Increment by one week", None))
        self.label_times_start_time.setText(QCoreApplication.translate("MainWindow", u"Start time", None))
        self.label_times_stop_time.setText(QCoreApplication.translate("MainWindow", u"Stop time", None))
        self.label_times_hours.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.info_label_times_hours.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Commute (km)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Distance driven\n"
"during work (km)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Type of hours", None))
        self.pushButton_times_clear_fields.setText(QCoreApplication.translate("MainWindow", u"Clear fields", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_times), QCoreApplication.translate("MainWindow", u"Times", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Add clients", None))
        self.pushButton_add_client.setText(QCoreApplication.translate("MainWindow", u"Add client", None))
        self.pushButton_clients_clear_fields.setText(QCoreApplication.translate("MainWindow", u"Clear fields", None))
        self.label_times_date_2.setText(QCoreApplication.translate("MainWindow", u"First year", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Standard\n"
"compensation\n"
"for driving\n"
"during work\n"
"(euro/km)", None))
        self.info_label_clients_index_within_year.setText("")
        self.label_day_of_week_2.setText(QCoreApplication.translate("MainWindow", u"Client code", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Standard rate\n"
"during day\n"
"(euro/h)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Standard rate\n"
"for shifts\n"
"(euro/h)", None))
        self.label_times_client_2.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Person name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Index within year", None))
        self.info_label_clients_client_code.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Standard\n"
"compensation\n"
"for commute\n"
"(euro/km)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Postal code\n"
"and city", None))
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
        self.radioButton_clients_sort_by_year_and_index.setText(QCoreApplication.translate("MainWindow", u"Sort by year and index", None))
        self.radioButton_clients_sort_by_client_name.setText(QCoreApplication.translate("MainWindow", u"Sort by client name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clients), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Generate invoices", None))
        self.pushButton_generate_invoice.setText(QCoreApplication.translate("MainWindow", u"Generate\n"
"invoice", None))
        self.pushButton_invoices_clear_fields.setText(QCoreApplication.translate("MainWindow", u"Clear fields", None))
        self.info_label_invoices_client_code.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Compensation\n"
"for commute\n"
"(euro/km)", None))
        self.label_times_client_3.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.pushButton_invoices_fill_in_today.setText(QCoreApplication.translate("MainWindow", u"Fill in today", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Invoice date", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Rate for\n"
"shifts (euro/h)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Client code", None))
        self.label_day_of_week_3.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Rate during\n"
"day (euro/h)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Compensation\n"
"for driving\n"
"during work\n"
"(euro/km)", None))
        self.label_28.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Invoice index\n"
"at client", None))
        self.label_times_date_3.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Invoice number", None))
        self.info_label_invoices_invoice_number.setText("")
        self.info_label_invoices_invoice_index_at_client.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Query invoices", None))
        self.pushButton_invoices_overwrite.setText(QCoreApplication.translate("MainWindow", u"Overwrite", None))
        self.pushButton_invoices_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Start month", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stop month", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Start year", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Stop year", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.radioButton_invoices_sort_by_date_only.setText(QCoreApplication.translate("MainWindow", u"Sort by date only", None))
        self.radioButton_invoices_sort_by_client_first.setText(QCoreApplication.translate("MainWindow", u"Sort by client first", None))
        self.radioButton_invoices_sort_by_month_then_by_client.setText(QCoreApplication.translate("MainWindow", u"Sort by month then by client", None))
        self.radioButton_invoices_query_dates_only.setText(QCoreApplication.translate("MainWindow", u"Query using dates only", None))
        self.radioButton_invoices_query_client_only.setText(QCoreApplication.translate("MainWindow", u"Query using client only", None))
        self.radioButton_invoices_query_dates_and_client.setText(QCoreApplication.translate("MainWindow", u"Query using dates and client", None))
        self.radioButton_invoices_query_return_all.setText(QCoreApplication.translate("MainWindow", u"Return all", None))
        self.pushButton_invoices_run_query.setText(QCoreApplication.translate("MainWindow", u"Run query", None))
        self.pushButton_invoices_export_query_results.setText(QCoreApplication.translate("MainWindow", u"Export \n"
"query \n"
"results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_invoices), QCoreApplication.translate("MainWindow", u"Invoices", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_configuration), QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

