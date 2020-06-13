import datetime
import logging

from PySide2 import QtWidgets

from modules.utilities import toolbox

class ClientsTab(QtWidgets.QMainWindow):
    add_overwrite_widget_name_list = ['lineEdit_clients_client_name', 'comboBox_clients_first_year', 'info_label_clients_index_within_year',
                                 'info_label_clients_client_code',
                                 'lineEdit_clients_person_name', 'lineEdit_clients_address', 'lineEdit_clients_postal_code_and_city',
                                 'lineEdit_clients_standard_rate_during_day', 'lineEdit_clients_standard_rate_for_shifts',
                                 'lineEdit_clients_standard_compensation_for_commute',
                                 'lineEdit_clients_standard_compensation_for_driving_during_work']
    query_widget_name_list = ['comboBox_clients_query_start_year', 'comboBox_clients_query_stop_year']
    def __init__(self, ui, widgets, signals, background_execution, params):
        super().__init__()
        self.ui = ui
        self.widgets = widgets
        self.signals = signals
        self.background_execution = background_execution
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT

        self.logger = logging.getLogger('main.' + __name__)

        self._connect_buttons_to_slots()
        self._connect_signals_to_slots()

        self._initialize_combobox_lists()
        self._initialize_radiobuttons()

    def _initialize_combobox_lists(self):
        current_year = int(datetime.datetime.now().strftime('%Y'))
        year_list = list(range(current_year-10, current_year + 1))

        self.widgets.set_allowed_widget_values('comboBox_clients_first_year', year_list)
        self.widgets.set_widget_value('comboBox_clients_first_year', year_list[-1])
        self._on_combobox_clients_first_year_currentindexchanged()

        self.widgets.set_allowed_widget_values('comboBox_clients_query_start_year', year_list)
        self.widgets.set_widget_value('comboBox_clients_query_start_year', year_list[0])
        self.widgets.set_allowed_widget_values('comboBox_clients_query_stop_year', year_list)
        self.widgets.set_widget_value('comboBox_clients_query_stop_year', year_list[-1])

    def _initialize_radiobuttons(self):
        self.widgets.set_widget_value('radioButton_clients_query_using_years', True)
        self.widgets.set_widget_value('radioButton_clients_sort_by_year_and_index', True)

    def _connect_buttons_to_slots(self):
        # adding/overwriting
        self.ui.comboBox_clients_first_year.currentIndexChanged.connect(self._on_combobox_clients_first_year_currentindexchanged)

        self.ui.pushButton_clients_clear_fields.clicked.connect(self._on_pushbutton_clear_fields_clicked)
        self.ui.pushButton_add_client.clicked.connect(self._on_pushbutton_add_client_clicked)

        # querying
        self.ui.radioButton_clients_query_using_years.clicked.connect(self._on_radiobutton_clients_query_clicked)
        self.ui.radioButton_clients_query_return_all.clicked.connect(self._on_radiobutton_clients_query_clicked)

        self.ui.radioButton_clients_sort_by_year_and_index.clicked.connect(self._on_radiobutton_clients_sort_clicked)
        self.ui.radioButton_clients_sort_by_client_name.clicked.connect(self._on_radiobutton_clients_sort_clicked)

        self.ui.pushButton_clients_export_query_results.clicked.connect(self._on_pushButton_clients_export_query_results_clicked)
        self.ui.pushButton_clients_run_query.clicked.connect(self._on_pushbutton_clients_run_query_clicked)

        # tableview
        self.ui.tableView_clients_query.clicked.connect(self._on_tableview_clients_query_clicked)
        
        self.ui.pushButton_clients_overwrite.clicked.connect(self._on_pushbutton_clients_overwrite_clicked)
        self.ui.pushButton_clients_delete.clicked.connect(self._on_pushbutton_clients_delete_clicked)

    def _connect_signals_to_slots(self):
        # adding/overwriting
        self.signals.request_next_index_within_year_signal.connect(self.background_execution.request_next_index_within_year_slot)
        self.signals.deliver_next_index_within_year_signal.connect(self._update_index_within_year_and_client_code)

        self.signals.pushbutton_add_client_clicked_signal.connect(self.background_execution.pushbutton_add_client_clicked_slot)

        # querying
        self.signals.radiobutton_clients_query_clicked_signal.connect(self.background_execution.radiobutton_clients_query_clicked_slot)
        self.signals.radiobutton_clients_sort_clicked_signal.connect(self.background_execution.radiobutton_clients_sort_clicked_slot)

        self.signals.pushbutton_clients_export_query_results_clicked_signal.connect(self.background_execution.pushbutton_clients_export_query_results_clicked_slot)
        self.signals.pushbutton_clients_run_query_clicked_signal.connect(self.background_execution.pushbutton_clients_run_query_clicked_slot)

        # tableview
        self.signals.display_clients_query_df_in_tableview_signal.connect(self.display_clients_query_df_in_tableview_slot)

        self.signals.pushbutton_clients_overwrite_clicked_signal.connect(self.background_execution.pushbutton_clients_overwrite_clicked_slot)
        self.signals.pushbutton_clients_delete_clicked_signal.connect(self.background_execution.pushbutton_clients_delete_clicked_slot)

    # adding/overwriting
    def _on_combobox_clients_first_year_currentindexchanged(self):
        first_year = self.widgets.get_widget_value('comboBox_clients_first_year')
        self.signals.request_next_index_within_year_signal.emit(first_year)

    def _update_index_within_year_and_client_code(self, next_index):
        self.widgets.set_widget_value('info_label_clients_index_within_year', next_index)
        first_year = self.widgets.get_widget_value('comboBox_clients_first_year')
        client_code = '.'.join([str(first_year), '{:02d}'.format(next_index)])
        self.widgets.set_widget_value('info_label_clients_client_code', client_code)

    def _on_pushbutton_clear_fields_clicked(self):
        current_year = int(datetime.datetime.now().strftime('%Y'))
        widget_value_dict = {'lineEdit_clients_client_name': '', 'comboBox_clients_first_year': current_year}
        self.widgets.set_widget_values_using_dict(widget_value_dict)

    def _on_pushbutton_add_client_clicked(self):
        print('in _add_client_clicked')
        client_name = self.widgets.get_widget_value('lineEdit_clients_client_name')
        if client_name == '':
            self.logger.warning('The client name is left empty. Please fill in a client name')
        else:
            add_client_widget_value_dict = self.widgets.get_widget_value_dict(self.add_overwrite_widget_name_list)
            clients_query_widget_value_dict = self._get_clients_query_widget_value_dict()
            self.signals.pushbutton_add_client_clicked_signal.emit(add_client_widget_value_dict, clients_query_widget_value_dict)
        print('out _add_client_clicked')

    # querying
    def _on_radiobutton_clients_query_clicked(self):
        radiobutton_name = self.sender().objectName()
        clients_query_widget_value_dict = self._get_clients_query_widget_value_dict()
        self.signals.radiobutton_clients_query_clicked_signal.emit(radiobutton_name, clients_query_widget_value_dict)

    def _get_clients_query_widget_value_dict(self):
        clients_query_widget_value_dict = self.widgets.get_widget_value_dict(self.query_widget_name_list)
        return clients_query_widget_value_dict

    def display_clients_query_df_in_tableview_slot(self, clients_query_df):
        self.widgets.set_widget_value('tableView_clients_query', clients_query_df)

    def _on_radiobutton_clients_sort_clicked(self):
        radiobutton_name = self.sender().objectName()
        self.signals.radiobutton_clients_sort_clicked_signal.emit(radiobutton_name)

    def _on_pushButton_clients_export_query_results_clicked(self):
        self.signals.pushbutton_clients_export_query_results_clicked_signal.emit()

    def _on_pushbutton_clients_run_query_clicked(self):
        clients_query_widget_value_dict = self._get_clients_query_widget_value_dict()
        self.signals.pushbutton_clients_run_query_clicked_signal.emit(clients_query_widget_value_dict)

    # tableview
    def _on_tableview_clients_query_clicked(self):
        current_row = self._get_current_row_of_tableview_clients_query()
        row_dict = self.widgets.get_tableview_df_row_as_dict('tableView_clients_query', current_row)
        widget_value_dict = self._create_widget_value_dict_from_row_dict(row_dict)
        self.widgets.set_widget_values_using_dict(widget_value_dict)

    def _get_current_row_of_tableview_clients_query(self):
        selected_indices = self.ui.tableView_clients_query.selectedIndexes()
        current_row = selected_indices[0].row()
        return current_row

    def _create_widget_value_dict_from_row_dict(self, row_dict):
        widget_value_dict = dict()
        for row in self.params.get_clients_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            widget_value_dict[widget_name] = row_dict[info_name]
        return widget_value_dict

    def _on_pushbutton_clients_overwrite_clicked(self):
        current_row = self._get_current_row_of_tableview_clients_query()
        row_dict = self.widgets.get_tableview_df_row_as_dict('tableView_clients_query', current_row)
        UID_to_be_overwritten = row_dict['UID']

        overwrite_client_widget_value_dict = self.widgets.get_widget_value_dict(self.add_overwrite_widget_name_list)
        clients_query_widget_value_dict = self._get_clients_query_widget_value_dict()
        self.signals.pushbutton_clients_overwrite_clicked_signal.emit(overwrite_client_widget_value_dict, UID_to_be_overwritten, clients_query_widget_value_dict)

    def _on_pushbutton_clients_delete_clicked(self):
        current_row = self._get_current_row_of_tableview_clients_query()
        row_dict = self.widgets.get_tableview_df_row_as_dict('tableView_clients_query', current_row)
        UID_to_be_deleted = row_dict['UID']
        clients_query_widget_value_dict = self._get_clients_query_widget_value_dict()
        self.signals.pushbutton_clients_delete_clicked_signal.emit(UID_to_be_deleted, clients_query_widget_value_dict)
