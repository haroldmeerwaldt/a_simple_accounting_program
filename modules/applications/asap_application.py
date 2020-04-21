from PySide2 import QtWidgets, QtCore
from modules.GUI_layouts import asap_layout
from modules.utilities import toolbox
from modules.worker_thread import background_execution
import pandas as pd
import os
import datetime

class Signals(QtCore.QObject):
    pushbutton_add_working_day_clicked_signal = QtCore.Signal(dict)
    def __init__(self):
        super().__init__()



class ASAPApplication(QtWidgets.QMainWindow):
    DATE_FORMAT = "%d-%m-%Y"
    def __init__(self):
        super().__init__()
        self._initialize_user_interface()
        self.signals = Signals()
        self._initialize_background_execution_thread()
        self._connect_buttons_to_slots()


    def _initialize_user_interface(self):
        self.ui = asap_layout.Ui_MainWindow()
        self.ui.setupUi(self)
        print(vars(self.ui))

        df = pd.DataFrame({'a': [2, 4], 'b': [3, 5]})

        model = toolbox.PandasModel(df)

        self.ui.tableView.setModel(model)

        self.widgets = Widgets(self.ui, self.DATE_FORMAT)




    def _initialize_background_execution_thread(self):
        self.background_execution_thread = QtCore.QThread()
        self.background_execution = background_execution.BackgroundExecution(self.signals)
        self.background_execution.moveToThread(self.background_execution_thread)
        self.background_execution_thread.start()

    def _connect_buttons_to_slots(self):
        self.ui.pushButton_add_working_day.clicked.connect(self._on_pushbutton_add_working_day_clicked)
        self.ui.pushButton_times_fill_in_today.clicked.connect(self._on_pushbutton_fill_in_today_clicked)
        self.ui.pushButton_times_increment_by_one_week.clicked.connect(self._on_pushbutton_increment_by_one_week_clicked)

    def _connect_signals_to_slots(self):
        self.signals.pushbutton_add_working_day_clicked_signal.connect(self.background_execution)


    def _on_pushbutton_add_working_day_clicked(self):
        relevant_widget_name_list = ['comboBox_times_client', 'lineEdit_times_date', 'info_label_day_of_week',
                                     'comboBox_times_start_time', 'comboBox_times_stop_time', 'info_label_times_hours']
        add_working_day_snapshot_dict = self.widgets.get_snapshot_dict(relevant_widget_name_list)
        self.signals.pushbutton_add_working_day_clicked_signal.emit(add_working_day_snapshot_dict)

    def _on_pushbutton_fill_in_today_clicked(self):
        date_widget = self.widgets.get_widget('lineEdit_times_date')
        today = datetime.date.today()
        today_string = today.strftime(self.DATE_FORMAT)
        date_widget.set_value(today_string)

        self._update_day_of_week()

    def _update_day_of_week(self):
        date_object = self.widgets.get_times_date_as_object()

        day_of_week_widget = self.widgets.get_widget('info_label_day_of_week')
        day_of_week_string = date_object.strftime("%A")
        day_of_week_widget.set_value(day_of_week_string)

    def _on_pushbutton_increment_by_one_week_clicked(self):
        date_object = self.widgets.get_times_date_as_object()
        one_week_increment = datetime.timedelta(weeks=1)
        date_one_week_incremented_object = date_object + one_week_increment
        date_one_week_incremented_string = date_one_week_incremented_object.strftime(self.DATE_FORMAT)

        date_widget = self.widgets.get_widget('lineEdit_times_date')
        date_widget.set_value(date_one_week_incremented_string)


        self._update_day_of_week()


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
            elif 'lineEdit' in widget_name:
                self._widget_dict[widget_name] = LineeditWidget(qt_widget)
            elif 'info_label' in widget_name:
                self._widget_dict[widget_name] = InfolabelWidget(qt_widget)

    def get_snapshot_dict(self, widget_name_list):
        snapshot_dict = dict()
        for widget_name in widget_name_list:
            snapshot_dict[widget_name] = self._widget_dict[widget_name].get_value()

        return snapshot_dict

    def get_widget(self, widget_name):
        return self._widget_dict[widget_name]

    def get_times_date_as_object(self):
        date_widget = self.get_widget('lineEdit_times_date')
        date_string = date_widget.get_value()
        try:
            date_object = datetime.datetime.strptime(date_string, self.DATE_FORMAT)
            return date_object
        except ValueError:
            return None


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
        return self.qt_widget.currentText()

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
        return self.qt_widget.text()

    def set_value(self, value):
        return self.qt_widget.setText(str(value))