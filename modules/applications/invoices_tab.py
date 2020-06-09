import datetime

from PySide2 import QtWidgets

from modules.utilities import toolbox

import logging


class InvoicesTab(QtWidgets.QMainWindow):
    add_overwrite_widget_name_list = ['comboBox_invoices_client_name', 'info_label_invoices_client_code',
                                 'info_label_invoices_invoice_index_at_client',
                                 'info_label_invoices_invoice_number', 'comboBox_invoices_month',
                                 'comboBox_invoices_year',
                                 'lineEdit_invoices_invoice_date', 'lineEdit_invoices_rate_during_day',
                                 'lineEdit_invoices_rate_for_shifts',
                                 'lineEdit_invoices_compensation_for_commute',
                                 'lineEdit_invoices_compensation_for_driving_during_work']
    query_widget_name_list = ['comboBox_invoices_query_start_month', 'comboBox_invoices_query_start_year',
                                 'comboBox_invoices_query_stop_month', 'comboBox_invoices_query_stop_year',
                                 'comboBox_invoices_query_client_name']
    def __init__(self, ui, widgets, signals, background_execution, params):
        super().__init__()
        self.ui = ui
        self.widgets = widgets
        self.signals = signals
        self.background_execution = background_execution
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT

        self.logger = logging.getLogger('main.' + __name__)

        self._connect_signals_to_slots()

    def _connect_signals_to_slots(self):
        # adding/overwriting
        self.signals.invoices_request_client_name_list_signal.connect(self.background_execution.invoices_request_client_name_list_slot)
        self.signals.invoices_deliver_client_name_list_signal.connect(self._initialize_client_combobox_lists)
        self.signals.invoices_update_client_name_combobox_signal.connect(self._update_client_combobox_lists)
        self.signals.invoices_request_client_code_next_invoice_index_at_client_rates_and_compensations_signal.connect(self.background_execution.invoices_request_client_code_next_invoice_index_at_client_rates_and_compensations_slot)
        self.signals.invoices_deliver_client_code_next_invoice_index_at_client_rates_and_compensations_signal.connect(self._update_client_info_with_dict)
        self.signals.invoices_deliver_client_code_next_invoice_index_at_client_rates_signal.connect(self._update_client_info_with_dict)

        self.signals.pushbutton_generate_invoice_clicked_signal.connect(self.background_execution.pushbutton_generate_invoice_clicked_slot)

        # querying
        self.signals.radiobutton_invoices_query_clicked_signal.connect(self.background_execution.radiobutton_invoices_query_clicked_slot)
        self.signals.radiobutton_invoices_sort_clicked_signal.connect(self.background_execution.radiobutton_invoices_sort_clicked_slot)

        self.signals.pushbutton_invoices_export_query_results_clicked_signal.connect(self.background_execution.pushbutton_invoices_export_query_results_clicked_slot)
        self.signals.pushbutton_invoices_run_query_clicked_signal.connect(self.background_execution.pushbutton_invoices_run_query_clicked_slot)

        # tableview
        self.signals.display_invoices_query_df_in_tableview_signal.connect(self.display_invoices_query_df_in_tableview_slot)

        self.signals.pushbutton_invoices_overwrite_clicked_signal.connect(self.background_execution.pushbutton_invoices_overwrite_clicked_slot)
        self.signals.pushbutton_invoices_delete_clicked_signal.connect(self.background_execution.pushbutton_invoices_delete_clicked_slot)

    def set_initial_values(self):
        self._initialize_combobox_lists()
        self._initialize_radiobuttons()

    def _initialize_combobox_lists(self):
        self.signals.invoices_request_client_name_list_signal.emit()
        self._initialize_all_month_combobox_lists()
        self._initialize_all_year_combobox_lists()

    def _initialize_all_month_combobox_lists(self):
        month_list = [datetime.date(2000, m, 1).strftime('%B') for m in range(1, 13)]

        self.widgets.set_allowed_widget_values('comboBox_invoices_month', month_list)
        self.widgets.set_widget_value('comboBox_invoices_month', month_list[0])

        self.widgets.set_allowed_widget_values('comboBox_invoices_query_start_month', month_list)
        self.widgets.set_widget_value('comboBox_invoices_query_start_month', month_list[0])
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_stop_month', month_list)
        self.widgets.set_widget_value('comboBox_invoices_query_stop_month', month_list[-1])

    def _initialize_all_year_combobox_lists(self):
        current_year = int(datetime.datetime.now().strftime('%Y'))
        year_list = list(range(current_year - 10, current_year + 1))

        self.widgets.set_allowed_widget_values('comboBox_invoices_year', year_list)
        self.widgets.set_widget_value('comboBox_invoices_year', year_list[-1])

        self.widgets.set_allowed_widget_values('comboBox_invoices_query_start_year', year_list)
        self.widgets.set_widget_value('comboBox_invoices_query_start_year', year_list[0])
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_stop_year', year_list)
        self.widgets.set_widget_value('comboBox_invoices_query_stop_year', year_list[-1])

    def _initialize_radiobuttons(self):
        self.widgets.set_widget_value('radioButton_invoices_sort_by_date_only', True)
        self.widgets.set_widget_value('radioButton_invoices_query_dates_only', True)

    def connect_buttons_to_slots(self):
        # adding/overwriting
        self.ui.comboBox_invoices_client_name.currentIndexChanged.connect(self._on_combobox_invoices_client_name_currentindexchanged)
        self.ui.pushButton_invoices_fill_in_today.clicked.connect(self._on_pushbutton_fill_in_today_clicked)

        self.ui.pushButton_invoices_clear_fields.clicked.connect(self._on_pushbutton_clear_fields_clicked)
        self.ui.pushButton_generate_invoice.clicked.connect(self._on_pushbutton_generate_invoice_clicked)

        # querying
        self.ui.radioButton_invoices_query_dates_only.clicked.connect(self._on_radiobutton_invoices_query_clicked)
        self.ui.radioButton_invoices_query_client_only.clicked.connect(self._on_radiobutton_invoices_query_clicked)
        self.ui.radioButton_invoices_query_dates_and_client.clicked.connect(self._on_radiobutton_invoices_query_clicked)

        self.ui.radioButton_invoices_sort_by_date_only.clicked.connect(self._on_radiobutton_invoices_sort_clicked)
        self.ui.radioButton_invoices_sort_by_client_first.clicked.connect(self._on_radiobutton_invoices_sort_clicked)
        self.ui.radioButton_invoices_sort_by_month_then_by_client.clicked.connect(self._on_radiobutton_invoices_sort_clicked)

        self.ui.pushButton_invoices_export_query_results.clicked.connect(self._on_pushButton_invoices_export_query_results_clicked)
        self.ui.pushButton_invoices_run_query.clicked.connect(self._on_pushbutton_invoices_run_query_clicked)

        # tableview
        self.ui.tableView_invoices_query.clicked.connect(self._on_tableview_invoices_query_clicked)

        self.ui.pushButton_invoices_overwrite.clicked.connect(self._on_pushbutton_invoices_overwrite_clicked)
        self.ui.pushButton_invoices_delete.clicked.connect(self._on_pushbutton_invoices_delete_clicked)

    # adding/overwriting
    def _initialize_client_combobox_lists(self, client_name_list):
        self._update_client_combobox_lists(client_name_list)
        first_client_name = self.widgets.get_widget_value('comboBox_invoices_client_name')
        self.signals.invoices_request_client_code_next_invoice_index_at_client_rates_and_compensations_signal.emit(first_client_name)

    def _update_client_combobox_lists(self, client_name_list):
        sorted_client_name_list = sorted(client_name_list)
        self.widgets.set_allowed_widget_values('comboBox_invoices_client_name', sorted_client_name_list)
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_client_name', sorted_client_name_list)

        try:
            first_client_name = sorted_client_name_list[0]
            self.widgets.set_widget_value('comboBox_invoices_client_name', first_client_name)
            self.widgets.set_widget_value('comboBox_invoices_query_client_name', first_client_name)
        except IndexError:
            self.logger.warning('No clients found. Please add a client in the client tab.')

    def _update_client_info_with_dict(self, client_info_dict):
        widget_value_dict = self._create_widget_value_dict_from_row_dict(client_info_dict)
        self.widgets.set_widget_values_using_dict(widget_value_dict)

        client_code = client_info_dict['Client code']
        invoice_index_at_client = client_info_dict['Invoice index at client']
        invoice_number = '{}.{:03d}'.format(client_code, invoice_index_at_client)
        self.widgets.set_widget_value('info_label_invoices_invoice_number', invoice_number)

    def _on_combobox_invoices_client_name_currentindexchanged(self):
        client_name = self.widgets.get_widget_value('comboBox_invoices_client_name')
        self.signals.invoices_request_client_code_next_invoice_index_at_client_rates_and_compensations_signal.emit(client_name)

    def _on_pushbutton_fill_in_today_clicked(self):
        today = datetime.date.today()
        today_string = today.strftime(self.DATE_FORMAT)
        self.widgets.set_widget_value('lineEdit_invoices_invoice_date', today_string)

    def _on_pushbutton_clear_fields_clicked(self):
        widget_value_dict = {'lineEdit_invoices_invoice_date': ''}
        self.widgets.set_widget_values_using_dict(widget_value_dict)
        self._initialize_combobox_lists()

    def _on_pushbutton_generate_invoice_clicked(self):
        try:
            invoice_widget_value_dict = self._get_invoice_widget_value_dict()
            query_widget_value_dict = self._get_invoices_query_widget_value_dict()
            self.signals.pushbutton_generate_invoice_clicked_signal.emit(invoice_widget_value_dict, query_widget_value_dict)
        except ValueError:
            self.logger.warning('Date was provided in an invalid format. Please use DD-MM-YYYY')

    def _get_invoice_widget_value_dict(self):
        widget_value_dict = self.widgets.get_widget_value_dict(self.add_overwrite_widget_name_list)
        return widget_value_dict

    # querying
    def _on_radiobutton_invoices_query_clicked(self):
        radiobutton_name = self.sender().objectName()
        invoices_query_widget_value_dict = self._get_invoices_query_widget_value_dict()
        self.signals.radiobutton_invoices_query_clicked_signal.emit(radiobutton_name, invoices_query_widget_value_dict)

    def _get_invoices_query_widget_value_dict(self):
        invoices_query_widget_value_dict = self.widgets.get_widget_value_dict(self.query_widget_name_list)
        return invoices_query_widget_value_dict

    def _on_radiobutton_invoices_sort_clicked(self):
        radiobutton_name = self.sender().objectName()
        self.signals.radiobutton_invoices_sort_clicked_signal.emit(radiobutton_name)

    def _on_pushButton_invoices_export_query_results_clicked(self):
        self.signals.pushbutton_invoices_export_query_results_clicked_signal.emit()

    def _on_pushbutton_invoices_run_query_clicked(self):
        invoices_query_widget_value_dict = self._get_invoices_query_widget_value_dict()
        self.signals.pushbutton_invoices_run_query_clicked_signal.emit(invoices_query_widget_value_dict)

    # tableview
    def display_invoices_query_df_in_tableview_slot(self, invoices_query_df):
        self.widgets.set_widget_value('tableView_invoices_query', invoices_query_df)

    def _on_tableview_invoices_query_clicked(self):
        current_row = self._get_current_row_of_tableview_invoices_query()
        row_dict = self.widgets.get_tableview_df_row_as_dict('tableView_invoices_query', current_row)
        widget_value_dict = self._create_widget_value_dict_from_row_dict(row_dict)
        self.widgets.set_widget_values_using_dict(widget_value_dict)

    def _get_current_row_of_tableview_invoices_query(self):
        selected_indices = self.ui.tableView_invoices_query.selectedIndexes()
        current_row = selected_indices[0].row()
        return current_row

    def _create_widget_value_dict_from_row_dict(self, row_dict):
        widget_value_dict = dict()
        for row in self.params.get_invoices_info_structure_df_itertuples():
            try:
                info_name = row.info_name
                widget_name = row.widget_name
                widget_value_dict[widget_name] = row_dict[info_name]
            except KeyError:
                pass
        return widget_value_dict

    def _on_pushbutton_invoices_overwrite_clicked(self):
        current_row = self._get_current_row_of_tableview_invoices_query()
        row_dict = self.widgets.get_tableview_df_row_as_dict('tableView_invoices_query', current_row)
        UID_to_be_overwritten = row_dict['UID']
        try:
            invoice_widget_value_dict = self._get_invoice_widget_value_dict()
            query_widget_value_dict = self._get_invoices_query_widget_value_dict()
            self.signals.pushbutton_invoices_overwrite_clicked_signal.emit(invoice_widget_value_dict, UID_to_be_overwritten, query_widget_value_dict)
        except ValueError:
            self.logger.warning('Date was provided in an invalid format. Please use DD-MM-YYYY')

    def _on_pushbutton_invoices_delete_clicked(self):
        current_row = self._get_current_row_of_tableview_invoices_query()
        row_dict = self.widgets.get_tableview_df_row_as_dict('tableView_invoices_query', current_row)
        UID_to_be_deleted = row_dict['UID']
        query_widget_value_dict = self._get_invoices_query_widget_value_dict()
        self.signals.pushbutton_invoices_delete_clicked_signal.emit(UID_to_be_deleted, query_widget_value_dict)
