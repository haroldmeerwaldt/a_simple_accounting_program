from PySide2 import QtWidgets, QtCore
from modules.GUI_layouts import asap_layout
from modules.utilities import toolbox
from modules.worker_thread import background_execution
import pandas as pd
import os
import datetime
import sys
import traceback

class Signals(QtCore.QObject):
    pushbutton_add_working_day_clicked_signal = QtCore.Signal(dict)
    radiobutton_times_query_clicked_signal = QtCore.Signal(str, dict)
    pushbutton_times_run_query_clicked_signal = QtCore.Signal(dict)
    radiobutton_times_sort_clicked_signal = QtCore.Signal(str)
    display_times_query_df_in_tableview_signal = QtCore.Signal(pd.DataFrame)
    pushbutton_times_export_query_results_clicked_signal = QtCore.Signal()
    pushbutton_times_overwrite_clicked_signal = QtCore.Signal(dict, str)
    pushbutton_times_delete_clicked_signal = QtCore.Signal(str)
    def __init__(self):
        super().__init__()



class ASAPApplication(QtWidgets.QMainWindow):
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT
        self._initialize_user_interface()
        self.signals = Signals()
        self._initialize_background_execution_thread()
        self._connect_buttons_to_slots()
        self._connect_signals_to_slots()


    def _initialize_user_interface(self):
        self.ui = asap_layout.Ui_MainWindow()
        self.ui.setupUi(self)
        print(vars(self.ui))
        self.ui.tableView_times_query.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)



        self.widgets = Widgets(self.ui, self.DATE_FORMAT)
        self._initialize_combobox_lists()
        self._initialize_radiobuttons()


    def _initialize_combobox_lists(self):
        client_list = ['Jantje', 'Pietje']
        self.widgets.add_values_to_widget('comboBox_times_client', client_list)
        self.widgets.add_values_to_widget('comboBox_times_query_client', client_list)

        time_list = [str(SimpleTime(minutes=15*i)) for i in range(96)]
        print(time_list)

        self.widgets.add_values_to_widget('comboBox_times_start_time', time_list)
        self.widgets.set_widget_value('comboBox_times_start_time', '08:00')

        self.widgets.add_values_to_widget('comboBox_times_stop_time', time_list)
        self.widgets.set_widget_value('comboBox_times_stop_time', '17:00')

        self._update_difference_between_start_and_stop_time()

        month_list = [datetime.date(2000, m, 1).strftime('%B') for m in range(1, 13)]
        self.widgets.add_values_to_widget('comboBox_times_query_start_month', month_list)
        self.widgets.set_widget_value('comboBox_times_query_start_month', month_list[0])
        self.widgets.add_values_to_widget('comboBox_times_query_stop_month', month_list)
        self.widgets.set_widget_value('comboBox_times_query_stop_month', month_list[-1])

        current_year = int(datetime.datetime.now().strftime('%Y'))
        year_list = list(range(current_year-10, current_year + 1))
        self.widgets.add_values_to_widget('comboBox_times_query_start_year', year_list)
        self.widgets.set_widget_value('comboBox_times_query_start_year', year_list[0])
        self.widgets.add_values_to_widget('comboBox_times_query_stop_year', year_list)
        self.widgets.set_widget_value('comboBox_times_query_stop_year', year_list[-1])

    def _initialize_radiobuttons(self):
        self.widgets.set_widget_value('radioButton_times_sort_by_date_only', True)
        self.widgets.set_widget_value('radioButton_times_query_dates_only', True)



    def _initialize_background_execution_thread(self):
        self.background_execution_thread = QtCore.QThread()
        self.background_execution = background_execution.BackgroundExecution(self.signals, self.params)
        self.background_execution.moveToThread(self.background_execution_thread)
        self.background_execution_thread.start()

    def _connect_buttons_to_slots(self):
        self.ui.pushButton_add_working_day.clicked.connect(self._on_pushbutton_add_working_day_clicked)
        self.ui.pushButton_times_fill_in_today.clicked.connect(self._on_pushbutton_fill_in_today_clicked)
        self.ui.pushButton_times_increment_by_one_week.clicked.connect(self._on_pushbutton_increment_by_one_week_clicked)
        self.ui.lineEdit_times_date.editingFinished.connect(self._update_day_of_week)
        self.ui.comboBox_times_start_time.currentIndexChanged.connect(self._update_difference_between_start_and_stop_time)
        self.ui.comboBox_times_stop_time.currentIndexChanged.connect(self._update_difference_between_start_and_stop_time)
        self.ui.pushButton_times_clear_fields.clicked.connect(self._on_pushbutton_clear_fields_clicked)

        # self.ui.pushButton_times_query_dates_only.clicked.connect(self._on_pushbutton_times_query_clicked)
        # self.ui.pushButton_times_query_client_only.clicked.connect(self._on_pushbutton_times_query_clicked)
        # self.ui.pushButton_times_query_dates_and_client.clicked.connect(self._on_pushbutton_times_query_clicked)

        self.ui.pushButton_times_run_query.clicked.connect(self._on_pushbutton_times_run_query_clicked)

        self.ui.radioButton_times_query_dates_only.clicked.connect(self._on_radiobutton_times_query_clicked)
        self.ui.radioButton_times_query_client_only.clicked.connect(self._on_radiobutton_times_query_clicked)
        self.ui.radioButton_times_query_dates_and_client.clicked.connect(self._on_radiobutton_times_query_clicked)


        self.ui.radioButton_times_sort_by_date_only.clicked.connect(self._on_radiobutton_times_sort_clicked)
        self.ui.radioButton_times_sort_by_client_first.clicked.connect(self._on_radiobutton_times_sort_clicked)
        self.ui.radioButton_times_sort_by_month_then_by_client.clicked.connect(self._on_radiobutton_times_sort_clicked)

        self.ui.pushButton_times_export_query_results.clicked.connect(self._on_pushButton_times_export_query_results_clicked)

        self.ui.tableView_times_query.clicked.connect(self._on_tableview_times_query_clicked)

        self.ui.pushButton_times_overwrite.clicked.connect(self._on_pushbutton_times_overwrite_clicked)
        self.ui.pushButton_times_delete.clicked.connect(self._on_pushbutton_times_delete_clicked)

    def _connect_signals_to_slots(self):
        self.signals.pushbutton_add_working_day_clicked_signal.connect(self.background_execution.pushbutton_add_working_day_clicked_slot)
        self.signals.radiobutton_times_query_clicked_signal.connect(self.background_execution.radiobutton_times_query_clicked_slot)
        self.signals.pushbutton_times_run_query_clicked_signal.connect(self.background_execution.pushbutton_times_run_query_clicked_slot)
        self.signals.radiobutton_times_sort_clicked_signal.connect(self.background_execution.radiobutton_times_sort_clicked_slot)
        self.signals.display_times_query_df_in_tableview_signal.connect(self.display_times_query_df_in_tableview_slot)
        self.signals.pushbutton_times_export_query_results_clicked_signal.connect(self.background_execution.pushbutton_times_export_query_results_clicked_slot)
        self.signals.pushbutton_times_overwrite_clicked_signal.connect(self.background_execution.pushbutton_times_overwrite_clicked_slot)
        self.signals.pushbutton_times_delete_clicked_signal.connect(self.background_execution.pushbutton_times_delete_clicked_slot)


    def _on_pushbutton_add_working_day_clicked(self):
        relevant_widget_name_list = ['comboBox_times_client', 'lineEdit_times_date', 'info_label_day_of_week',
                                     'comboBox_times_start_time', 'comboBox_times_stop_time', 'info_label_times_hours']
        try:
            add_working_day_widget_value_dict = self.widgets.get_widget_value_dict(relevant_widget_name_list)
            self.signals.pushbutton_add_working_day_clicked_signal.emit(add_working_day_widget_value_dict)
        except ValueError:
            print('Date was provided in an invalid format. It should be DD-MM-YYYY')

    def _on_pushbutton_fill_in_today_clicked(self):
        today = datetime.date.today()
        today_string = today.strftime(self.DATE_FORMAT)
        self.widgets.set_widget_value('lineEdit_times_date', today_string)

        self._update_day_of_week()

    def _update_day_of_week(self):
        try:
            date_object = self.widgets.get_times_date_as_object()
            day_of_week_string = date_object.strftime("%A")
            self.widgets.set_widget_value('info_label_day_of_week', day_of_week_string)
        except ValueError:
            print('An invalid date was entered')

    def _on_pushbutton_increment_by_one_week_clicked(self):

        try:
            date_object = self.widgets.get_times_date_as_object()
            one_week_increment = datetime.timedelta(weeks=1)
            date_one_week_incremented_object = date_object + one_week_increment
            date_one_week_incremented_string = date_one_week_incremented_object.strftime(self.DATE_FORMAT)

            self.widgets.set_widget_value('lineEdit_times_date', date_one_week_incremented_string)

            self._update_day_of_week()
        except ValueError:
            print('An invalid date was entered')

    def _update_difference_between_start_and_stop_time(self):
        start_time_string = self.widgets.get_widget_value('comboBox_times_start_time')
        start_time = SimpleTime(string=start_time_string)

        stop_time_string = str(self.widgets.get_widget_value('comboBox_times_stop_time'))
        stop_time = SimpleTime(string=stop_time_string)

        time_difference = stop_time - start_time
        number_of_hours = float(time_difference)
        self.widgets.set_widget_value('info_label_times_hours', number_of_hours)

    def _on_pushbutton_clear_fields_clicked(self):
        widget_value_dict = {'lineEdit_times_date': '', 'info_label_day_of_week': '', 'comboBox_times_start_time': '08:00', 'comboBox_times_stop_time': '17:00'}
        self.widgets.set_widget_values_using_dict(widget_value_dict)

    def _on_pushbutton_times_run_query_clicked(self):
        times_query_widget_value_dict = self._generate_times_query_widget_value_dict()
        self.signals.pushbutton_times_run_query_clicked_signal.emit(times_query_widget_value_dict)

    def _on_radiobutton_times_query_clicked(self):
        radiobutton_name = self.sender().objectName()
        times_query_widget_value_dict = self._generate_times_query_widget_value_dict()
        self.signals.radiobutton_times_query_clicked_signal.emit(radiobutton_name, times_query_widget_value_dict)

    def _generate_times_query_widget_value_dict(self):
        relevant_widget_name_list = ['comboBox_times_query_start_month', 'comboBox_times_query_start_year',
                                     'comboBox_times_query_stop_month', 'comboBox_times_query_stop_year',
                                     'comboBox_times_query_client']
        times_query_widget_value_dict = self.widgets.get_widget_value_dict(relevant_widget_name_list)
        return times_query_widget_value_dict

    def display_times_query_df_in_tableview_slot(self, times_query_df):
        self.widgets.set_widget_value('tableView_times_query', times_query_df)

    def _on_radiobutton_times_sort_clicked(self):
        radiobutton_name = self.sender().objectName()
        self.signals.radiobutton_times_sort_clicked_signal.emit(radiobutton_name)

    def _on_pushButton_times_export_query_results_clicked(self):
        self.signals.pushbutton_times_export_query_results_clicked_signal.emit()

    def _on_tableview_times_query_clicked(self):
        current_row = self._get_current_row_of_tableview_times_query()
        tableview_times_query_widget = self.widgets.get_widget('tableView_times_query') # violates Law of Demeter, todo fix it
        row_dict = tableview_times_query_widget.get_df_row_as_dict(current_row)
        widget_value_dict = self._generate_widget_value_dict_from_row_dict(row_dict)
        self.widgets.set_widget_values_using_dict(widget_value_dict)

    def _get_current_row_of_tableview_times_query(self):
        selected_indices = self.ui.tableView_times_query.selectedIndexes()
        current_row = selected_indices[0].row()
        return current_row

    def _generate_widget_value_dict_from_row_dict(self, row_dict):
        widget_value_dict = dict()
        for row in self.params.get_times_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            widget_value_dict[widget_name] = row_dict[info_name]
        return widget_value_dict

    def _on_pushbutton_times_overwrite_clicked(self):
        current_row = self._get_current_row_of_tableview_times_query()
        tableview_times_query_widget = self.widgets.get_widget('tableView_times_query') # violates Law of Demeter, todo fix it
        row_dict = tableview_times_query_widget.get_df_row_as_dict(current_row)
        UID_to_be_overwritten = row_dict['UID']
        relevant_widget_name_list = ['comboBox_times_client', 'lineEdit_times_date', 'info_label_day_of_week',
                                     'comboBox_times_start_time', 'comboBox_times_stop_time', 'info_label_times_hours']
        try:
            overwrite_working_day_widget_value_dict = self.widgets.get_widget_value_dict(relevant_widget_name_list)
            self.signals.pushbutton_times_overwrite_clicked_signal.emit(overwrite_working_day_widget_value_dict, UID_to_be_overwritten)
        except ValueError:
            print('Date was provided in an invalid format. It should be DD-MM-YYYY')

    def _on_pushbutton_times_delete_clicked(self):
        current_row = self._get_current_row_of_tableview_times_query()
        tableview_times_query_widget = self.widgets.get_widget('tableView_times_query') # violates Law of Demeter, todo fix it
        row_dict = tableview_times_query_widget.get_df_row_as_dict(current_row)
        UID_to_be_deleted = row_dict['UID']
        self.signals.pushbutton_times_delete_clicked_signal.emit(UID_to_be_deleted)


    def closeEvent(self, event):
        self.background_execution_thread.quit()
        self.deleteLater()

class Widgets:

    def __init__(self, ui, DATE_FORMAT):
        self.DATE_FORMAT = DATE_FORMAT
        qt_widget_dict = vars(ui)
        self._widget_dict = dict()
        for widget_name, qt_widget in qt_widget_dict.items():
            if 'pushButton' in widget_name:
                self._widget_dict[widget_name] = PushbuttonWidget(qt_widget)
            elif 'comboBox' in widget_name:
                self._widget_dict[widget_name] = ComboboxWidget(qt_widget)
            elif widget_name == 'lineEdit_times_date':
                self._widget_dict[widget_name] = LineeditTimesDateWidget(qt_widget, date_format=DATE_FORMAT)
            elif 'lineEdit' in widget_name:
                self._widget_dict[widget_name] = LineeditWidget(qt_widget)
            elif 'info_label' in widget_name:
                self._widget_dict[widget_name] = InfolabelWidget(qt_widget)
            elif 'radioButton' in widget_name:
                self._widget_dict[widget_name] = RadiobuttonWidget(qt_widget)
            elif 'tableView' in widget_name:
                self._widget_dict[widget_name] = TableviewWidget(qt_widget)

    def get_widget_value_dict(self, widget_name_list):
        widget_value_dict = dict()
        for widget_name in widget_name_list:
            widget_value_dict[widget_name] = self._widget_dict[widget_name].get_value()

        return widget_value_dict

    def set_widget_values_using_dict(self, widget_value_dict):
        for widget_name, value in widget_value_dict.items():
            self.set_widget_value(widget_name, value)

    def get_widget(self, widget_name):
        return self._widget_dict[widget_name]

    def get_widget_value(self, widget_name):
        widget = self.get_widget(widget_name)
        return widget.get_value()

    def set_widget_value(self, widget_name, value):
        widget = self.get_widget(widget_name)
        widget.set_value(value)

    def add_values_to_widget(self, widget_name, value_list):
        widget = self.get_widget(widget_name)
        widget.add_values(value_list)

    def get_times_date_as_object(self):
        date = self.get_widget_value('lineEdit_times_date')
        # date_object = datetime.datetime.strptime(date_string, self.DATE_FORMAT)
        return date



class Widget:
    def __init__(self, qt_widget):
        self.qt_widget = qt_widget
        self.name = qt_widget.objectName()


class PushbuttonWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

class ComboboxWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self.qt_widget.currentData()

    def set_value(self, value):
        current_index = self.qt_widget.findData(value)
        self.qt_widget.setCurrentIndex(current_index)

    def add_values(self, value_list):
        for value in value_list:
            self.qt_widget.addItem(str(value), value)

class LineeditTimesDateWidget(Widget):
    def __init__(self, *args, date_format=None):
        super().__init__(*args)
        self.date_format = date_format

    def get_value(self):
        text = self.qt_widget.text()
        value = datetime.datetime.strptime(text, self.date_format)
        return value

    def set_value(self, value):
        return self.qt_widget.setText(str(value))


class LineeditWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self.qt_widget.text()

    def set_value(self, value):
        return self.qt_widget.setText(str(value))


class InfolabelWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        return self.qt_widget.setText(str(value))


class RadiobuttonWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self.qt_widget.isChecked()

    def set_value(self, value):
        return self.qt_widget.setChecked(value)

class TableviewWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def set_value(self, value_df):
        self._value_df = value_df
        model = toolbox.PandasModel(value_df)
        self.qt_widget.setModel(model)

    def get_value(self):
        return self._value_df

    def get_df_row_as_dict(self, row_number):
        row_series = self._value_df.iloc[row_number, :]
        row_dict = row_series.to_dict()
        return row_dict





class SimpleTime:
    def __init__(self, string=None, hours=None, minutes=None):
        if hours is not None or minutes is not None:
            carry_hours = 0

            try:
                self.minutes = int(minutes)
            except TypeError:
                self.minutes = 0

            while self.minutes > 59:
                self.minutes = self.minutes - 60
                carry_hours = carry_hours + 1

            try:
                self.hours = int(hours + carry_hours)
            except TypeError:
                self.hours = carry_hours
        elif string is not None:
            hours_minutes_list = string.split(':')
            if len(hours_minutes_list) != 2:
                raise ValueError('if a string is provided, it should be in format HH:MM')
            self.hours = int(hours_minutes_list[0])
            self.minutes = int(hours_minutes_list[1])
        else:
            raise ValueError('Either a string in format HH:MM should be provided or hours and minutes as numbers')

    def __add__(self, other):
        carry_hours = 0

        sum_minutes = self.minutes - other.minutes
        while sum_minutes > 59:
            sum_minutes = sum_minutes - 60
            carry_hours = carry_hours + 1

        sum_hours = self.hours + other.hours + carry_hours
        while sum_hours > 23:
            sum_hours = sum_hours - 24

        return SimpleTime(hours=sum_hours, minutes=sum_minutes)


    def __sub__(self, other):
        delta_hours = self.hours - other.hours
        if delta_hours < 0:
            delta_hours = delta_hours + 24

        delta_minutes = self.minutes - other.minutes
        if delta_minutes < 0:
            delta_minutes = delta_minutes + 60
            delta_hours = delta_hours - 1

        return SimpleTime(hours=delta_hours, minutes=delta_minutes)

    def __str__(self):
        return "{:02d}:{:02d}".format(self.hours, self.minutes)

    def __float__(self):
        return float(self.hours + self.minutes/60)
