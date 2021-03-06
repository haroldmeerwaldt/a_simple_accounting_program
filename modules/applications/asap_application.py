from PySide2 import QtWidgets, QtCore
from modules.GUI_layouts import asap_layout
from modules.applications import widgets, times_tab, clients_tab, invoices_tab
from modules.worker_thread import background_execution
from modules.utilities import toolbox
import pandas as pd
import logging


class Signals(QtCore.QObject):
    logging_message_signal = QtCore.Signal(str)

    # times tab
    times_request_client_name_list_signal = QtCore.Signal()
    times_deliver_client_name_list_signal = QtCore.Signal(list)
    times_update_client_name_combobox_signal = QtCore.Signal(list)
    times_request_client_code_signal = QtCore.Signal(str)
    times_deliver_client_code_signal = QtCore.Signal(str)
    pushbutton_add_working_day_clicked_signal = QtCore.Signal(dict, dict)
    radiobutton_times_query_clicked_signal = QtCore.Signal(str, dict)
    pushbutton_times_run_query_clicked_signal = QtCore.Signal(dict)
    radiobutton_times_sort_clicked_signal = QtCore.Signal(str)
    display_times_query_df_in_tableview_signal = QtCore.Signal(pd.DataFrame)
    pushbutton_times_export_query_results_clicked_signal = QtCore.Signal()
    pushbutton_times_overwrite_clicked_signal = QtCore.Signal(dict, str, dict)
    pushbutton_times_delete_clicked_signal = QtCore.Signal(str, dict)

    # clients tab
    pushbutton_add_client_clicked_signal = QtCore.Signal(dict, dict)
    request_next_index_within_year_signal = QtCore.Signal(int)
    deliver_next_index_within_year_signal = QtCore.Signal(int)
    radiobutton_clients_query_clicked_signal = QtCore.Signal(str, dict)
    pushbutton_clients_run_query_clicked_signal = QtCore.Signal(dict)
    radiobutton_clients_sort_clicked_signal = QtCore.Signal(str)
    display_clients_query_df_in_tableview_signal = QtCore.Signal(pd.DataFrame)
    pushbutton_clients_export_query_results_clicked_signal = QtCore.Signal()
    pushbutton_clients_overwrite_clicked_signal = QtCore.Signal(dict, str, dict)
    pushbutton_clients_delete_clicked_signal = QtCore.Signal(str, dict)
   
    # invoices tab
    invoices_request_client_name_list_signal = QtCore.Signal()
    invoices_deliver_client_name_list_signal = QtCore.Signal(list)
    invoices_update_client_name_combobox_signal = QtCore.Signal(list)
    invoices_request_client_code_next_invoice_index_at_client_rates_and_compensations_signal = QtCore.Signal(str)
    invoices_deliver_client_code_next_invoice_index_at_client_rates_and_compensations_signal = QtCore.Signal(dict)
    invoices_deliver_client_code_next_invoice_index_at_client_rates_signal = QtCore.Signal(dict)
    pushbutton_generate_invoice_clicked_signal = QtCore.Signal(dict, dict)
    radiobutton_invoices_query_clicked_signal = QtCore.Signal(str, dict)
    pushbutton_invoices_run_query_clicked_signal = QtCore.Signal(dict)
    radiobutton_invoices_sort_clicked_signal = QtCore.Signal(str)
    display_invoices_query_df_in_tableview_signal = QtCore.Signal(pd.DataFrame)
    pushbutton_invoices_export_query_results_clicked_signal = QtCore.Signal()
    pushbutton_invoices_overwrite_clicked_signal = QtCore.Signal(dict, str, dict)
    pushbutton_invoices_delete_clicked_signal = QtCore.Signal(str, dict)

    def __init__(self):
        super().__init__()


class ASAPApplication(QtWidgets.QMainWindow):
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT

        self._initialize_user_interface()
        self.signals = Signals()

        self._initialize_logger()
        self._initialize_background_execution_thread()
        self._initialize_tabs()
        self._display_welcome_message()


    def _initialize_user_interface(self):
        self.ui = asap_layout.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('A Simple Accounting Program')
        self._set_tableview_selection_modes()
        self.widgets = widgets.Widgets(self.ui, self.DATE_FORMAT)

    def _set_tableview_selection_modes(self):
        self.ui.tableView_times_query.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_clients_query.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_invoices_query.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def _initialize_background_execution_thread(self):
        self.background_execution_thread = QtCore.QThread()
        self.background_execution = background_execution.BackgroundExecution(self.signals, self.params)
        self.background_execution.moveToThread(self.background_execution_thread)
        self.background_execution_thread.start()

    def _initialize_tabs(self):
        self.times_tab = times_tab.TimesTab(self.ui, self.widgets, self.signals, self.background_execution, self.params)
        self.clients_tab = clients_tab.ClientsTab(self.ui, self.widgets, self.signals, self.background_execution, self.params)
        self.invoices_tab = invoices_tab.InvoicesTab(self.ui, self.widgets, self.signals, self.background_execution, self.params)
        self.times_tab.set_initial_values()
        self.times_tab.connect_buttons_to_slots()
        self.invoices_tab.set_initial_values()
        self.invoices_tab.connect_buttons_to_slots()

    def _initialize_logger(self):
        logger = logging.getLogger('main')
        logger.setLevel(logging.DEBUG)

        handler = toolbox.QLogHandler(self.signals.logging_message_signal, self.ui.textBrowser_console)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(fmt='{asctime} | {message}', datefmt='%H:%M:%S', style='{')

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    def _display_welcome_message(self):
        self.logger = logging.getLogger('main.' + __name__)
        self.logger.info('Welcome to A Simple Accounting Program!')

    def closeEvent(self, event):
        self.background_execution_thread.quit()
        self.deleteLater()


