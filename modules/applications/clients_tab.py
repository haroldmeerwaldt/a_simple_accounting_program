import datetime

from PySide2 import QtWidgets

from modules.utilities import toolbox

class ClientsTab(QtWidgets.QMainWindow):
    def __init__(self, ui, widgets, signals, background_execution, params):
        super().__init__()
        self.ui = ui
        self.widgets = widgets
        self.signals = signals
        self.background_execution = background_execution
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT

        self._initialize_combobox_lists()
        self._initialize_radiobuttons()

        self._connect_buttons_to_slots()
        self._connect_signals_to_slots()

    def _initialize_combobox_lists(self):
        current_year = int(datetime.datetime.now().strftime('%Y'))
        year_list = list(range(current_year-10, current_year + 1))
        self.widgets.add_values_to_widget('comboBox_clients_first_year', year_list)
        self.widgets.set_widget_value('comboBox_clients_first_year', year_list[-1])

    def _initialize_radiobuttons(self):
        self.widgets.set_widget_value('radioButton_clients_query_using_years', True)

    def _connect_buttons_to_slots(self):
        self.ui.pushButton_add_client.clicked.connect(self._on_pushbutton_add_client_clicked)
        self.ui.comboBox_clients_first_year.currentIndexChanged.connect(self._update_client_code)
        # self.ui.pushButton_times_clear_fields.clicked.connect(self._on_pushbutton_clear_fields_clicked)
        # self.ui.pushButton_times_run_query.clicked.connect(self._on_pushbutton_times_run_query_clicked)
        #
        # self.ui.radioButton_times_query_dates_only.clicked.connect(self._on_radiobutton_times_query_clicked)
        # self.ui.radioButton_times_query_client_only.clicked.connect(self._on_radiobutton_times_query_clicked)
        #
        # self.ui.pushButton_times_export_query_results.clicked.connect(self._on_pushButton_times_export_query_results_clicked)
        #
        # self.ui.tableView_times_query.clicked.connect(self._on_tableview_times_query_clicked)
        #
        # self.ui.pushButton_times_overwrite.clicked.connect(self._on_pushbutton_times_overwrite_clicked)
        # self.ui.pushButton_times_delete.clicked.connect(self._on_pushbutton_times_delete_clicked)

    def _connect_signals_to_slots(self):
        self.signals.pushbutton_add_client_clicked_signal.connect(self.background_execution.pushbutton_add_client_clicked_slot)
        # self.signals.radiobutton_times_query_clicked_signal.connect(self.background_execution.radiobutton_times_query_clicked_slot)
        # self.signals.pushbutton_times_run_query_clicked_signal.connect(self.background_execution.pushbutton_times_run_query_clicked_slot)
        # self.signals.radiobutton_times_sort_clicked_signal.connect(self.background_execution.radiobutton_times_sort_clicked_slot)
        # self.signals.display_times_query_df_in_tableview_signal.connect(self.display_times_query_df_in_tableview_slot)
        # self.signals.pushbutton_times_export_query_results_clicked_signal.connect(self.background_execution.pushbutton_times_export_query_results_clicked_slot)
        # self.signals.pushbutton_times_overwrite_clicked_signal.connect(self.background_execution.pushbutton_times_overwrite_clicked_slot)
        # self.signals.pushbutton_times_delete_clicked_signal.connect(self.background_execution.pushbutton_times_delete_clicked_slot)

    def _on_pushbutton_add_client_clicked(self):
        relevant_widget_name_list = ['lineEdit_clients_client_name', 'comboBox_clients_first_year', 'info_label_clients_client_code']
        add_client_widget_value_dict = self.widgets.get_widget_value_dict(relevant_widget_name_list)
        self.signals.pushbutton_add_client_clicked_signal.emit(add_client_widget_value_dict)

    def _update_client_code(self):
        first_year_string = self.widgets.get_widget_value('comboBox_clients_first_year')
        self.widgets.set_widget_value('info_label_clients_client_code', first_year_string)
