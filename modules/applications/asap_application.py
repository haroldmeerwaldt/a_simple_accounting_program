from PySide2 import QtWidgets, QtCore
from modules.GUI_layouts import asap_layout
from modules.applications import widgets, times_tab, clients_tab
from modules.worker_thread import background_execution
import pandas as pd


class Signals(QtCore.QObject):
    # times tab
    request_client_name_list_signal = QtCore.Signal()
    deliver_client_name_list_signal = QtCore.Signal(list)
    update_client_name_combobox_signal = QtCore.Signal(list)
    request_client_code_signal = QtCore.Signal(str)
    deliver_client_code_signal = QtCore.Signal(str)
    pushbutton_add_working_day_clicked_signal = QtCore.Signal(dict)
    radiobutton_times_query_clicked_signal = QtCore.Signal(str, dict)
    pushbutton_times_run_query_clicked_signal = QtCore.Signal(dict)
    radiobutton_times_sort_clicked_signal = QtCore.Signal(str)
    display_times_query_df_in_tableview_signal = QtCore.Signal(pd.DataFrame)
    pushbutton_times_export_query_results_clicked_signal = QtCore.Signal()
    pushbutton_times_overwrite_clicked_signal = QtCore.Signal(dict, str)
    pushbutton_times_delete_clicked_signal = QtCore.Signal(str)

    # clients tab
    pushbutton_add_client_clicked_signal = QtCore.Signal(dict)
    request_next_index_within_year_signal = QtCore.Signal(int)
    deliver_next_index_within_year_signal = QtCore.Signal(int)
    radiobutton_clients_query_clicked_signal = QtCore.Signal(str, dict)
    pushbutton_clients_run_query_clicked_signal = QtCore.Signal(dict)
    radiobutton_clients_sort_clicked_signal = QtCore.Signal(str)
    display_clients_query_df_in_tableview_signal = QtCore.Signal(pd.DataFrame)
    pushbutton_clients_export_query_results_clicked_signal = QtCore.Signal()
    pushbutton_clients_overwrite_clicked_signal = QtCore.Signal(dict, str)
    pushbutton_clients_delete_clicked_signal = QtCore.Signal(str)


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
        self._initialize_tabs()

    def _initialize_user_interface(self):
        self.ui = asap_layout.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableView_times_query.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_clients_query.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.widgets = widgets.Widgets(self.ui, self.DATE_FORMAT)

    def _initialize_background_execution_thread(self):
        self.background_execution_thread = QtCore.QThread()
        self.background_execution = background_execution.BackgroundExecution(self.signals, self.params)
        self.background_execution.moveToThread(self.background_execution_thread)
        self.background_execution_thread.start()

    def _initialize_tabs(self):
        self.times_tab = times_tab.TimesTab(self.ui, self.widgets, self.signals, self.background_execution, self.params)
        self.clients_tab = clients_tab.ClientsTab(self.ui, self.widgets, self.signals, self.background_execution, self.params)
        self.times_tab.set_initial_values()
        self.times_tab.connect_buttons_to_slots()


    def closeEvent(self, event):
        self.background_execution_thread.quit()
        self.deleteLater()


