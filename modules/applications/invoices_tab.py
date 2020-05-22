import datetime

from PySide2 import QtWidgets

from modules.utilities import toolbox


class InvoicesTab(QtWidgets.QMainWindow):
    def __init__(self, ui, widgets, signals, background_execution, params):
        super().__init__()
        self.ui = ui
        self.widgets = widgets
        self.signals = signals
        self.background_execution = background_execution
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT

        self._connect_signals_to_slots()

    def _connect_signals_to_slots(self):
        self.signals.invoices_request_client_name_list_signal.connect(self.background_execution.invoices_request_client_name_list_slot)
        self.signals.invoices_deliver_client_name_list_signal.connect(self._initialize_client_combobox_lists)
        self.signals.invoices_update_client_name_combobox_signal.connect(self._update_client_combobox_lists)
        self.signals.invoices_request_client_code_signal.connect(self.background_execution.invoices_request_client_code_slot)
        self.signals.invoices_deliver_client_code_signal.connect(self._update_client_code)
        self.signals.pushbutton_add_working_day_clicked_signal.connect(self.background_execution.pushbutton_add_working_day_clicked_slot)
        self.signals.radiobutton_invoices_query_clicked_signal.connect(self.background_execution.radiobutton_invoices_query_clicked_slot)
        self.signals.pushbutton_invoices_run_query_clicked_signal.connect(self.background_execution.pushbutton_invoices_run_query_clicked_slot)
        self.signals.radiobutton_invoices_sort_clicked_signal.connect(self.background_execution.radiobutton_invoices_sort_clicked_slot)
        self.signals.display_invoices_query_df_in_tableview_signal.connect(self.display_invoices_query_df_in_tableview_slot)
        self.signals.pushbutton_invoices_export_query_results_clicked_signal.connect(self.background_execution.pushbutton_invoices_export_query_results_clicked_slot)
        self.signals.pushbutton_invoices_overwrite_clicked_signal.connect(self.background_execution.pushbutton_invoices_overwrite_clicked_slot)
        self.signals.pushbutton_invoices_delete_clicked_signal.connect(self.background_execution.pushbutton_invoices_delete_clicked_slot)


    def set_initial_values(self):
        self._initialize_combobox_lists()
        self._initialize_radiobuttons()

    def _initialize_combobox_lists(self):
        self.signals.invoices_request_client_name_list_signal.emit()

        month_list = [datetime.date(2000, m, 1).strftime('%B') for m in range(1, 13)]
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_start_month', month_list)
        self.widgets.set_widget_value('comboBox_invoices_query_start_month', month_list[0])
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_stop_month', month_list)
        self.widgets.set_widget_value('comboBox_invoices_query_stop_month', month_list[-1])

        current_year = int(datetime.datetime.now().strftime('%Y'))
        year_list = list(range(current_year-10, current_year + 1))
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_start_year', year_list)
        self.widgets.set_widget_value('comboBox_invoices_query_start_year', year_list[0])
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_stop_year', year_list)
        self.widgets.set_widget_value('comboBox_invoices_query_stop_year', year_list[-1])

    def _initialize_client_combobox_lists(self, client_name_list):
        self._update_client_combobox_lists(client_name_list)

        first_client_name = self.widgets.get_widget_value('comboBox_invoices_client_name')
        self.signals.invoices_request_client_code_signal.emit(first_client_name)

    def _update_client_combobox_lists(self, client_name_list):
        sorted_client_name_list = sorted(client_name_list)
        self.widgets.set_allowed_widget_values('comboBox_invoices_client_name', sorted_client_name_list)
        self.widgets.set_allowed_widget_values('comboBox_invoices_query_client_name', sorted_client_name_list)

        first_client_name = sorted_client_name_list[0]
        self.widgets.set_widget_value('comboBox_invoices_client_name', first_client_name)
        self.widgets.set_widget_value('comboBox_invoices_query_client_name', first_client_name)

    def _update_client_code(self, client_code):
        self.widgets.set_widget_value('info_label_invoices_client_code', client_code)

    def _initialize_radiobuttons(self):
        self.widgets.set_widget_value('radioButton_invoices_sort_by_date_only', True)
        self.widgets.set_widget_value('radioButton_invoices_query_dates_only', True)

    def connect_buttons_to_slots(self):
        self.ui.comboBox_invoices_client_name.currentIndexChanged.connect(self._on_combobox_invoices_client_name_currentindexchanged)

        self.ui.pushButton_add_working_day.clicked.connect(self._on_pushbutton_add_working_day_clicked)
        self.ui.pushButton_invoices_fill_in_today.clicked.connect(self._on_pushbutton_fill_in_today_clicked)
        self.ui.pushButton_invoices_clear_fields.clicked.connect(self._on_pushbutton_clear_fields_clicked)

        self.ui.pushButton_invoices_run_query.clicked.connect(self._on_pushbutton_invoices_run_query_clicked)

        self.ui.radioButton_invoices_query_dates_only.clicked.connect(self._on_radiobutton_invoices_query_clicked)
        self.ui.radioButton_invoices_query_client_only.clicked.connect(self._on_radiobutton_invoices_query_clicked)
        self.ui.radioButton_invoices_query_dates_and_client.clicked.connect(self._on_radiobutton_invoices_query_clicked)

        self.ui.radioButton_invoices_sort_by_date_only.clicked.connect(self._on_radiobutton_invoices_sort_clicked)
        self.ui.radioButton_invoices_sort_by_client_first.clicked.connect(self._on_radiobutton_invoices_sort_clicked)
        self.ui.radioButton_invoices_sort_by_month_then_by_client.clicked.connect(self._on_radiobutton_invoices_sort_clicked)

        self.ui.pushButton_invoices_export_query_results.clicked.connect(self._on_pushButton_invoices_export_query_results_clicked)

        self.ui.tableView_invoices_query.clicked.connect(self._on_tableview_invoices_query_clicked)

        self.ui.pushButton_invoices_overwrite.clicked.connect(self._on_pushbutton_invoices_overwrite_clicked)
        self.ui.pushButton_invoices_delete.clicked.connect(self._on_pushbutton_invoices_delete_clicked)


    def _on_combobox_invoices_client_name_currentindexchanged(self):
        client_name = self.widgets.get_widget_value('comboBox_invoices_client_name')
        self.signals.invoices_request_client_code_signal.emit(client_name)

    def _on_pushbutton_add_working_day_clicked(self):
        relevant_widget_name_list = ['comboBox_invoices_client_name', 'info_label_invoices_client_code', 'lineEdit_invoices_date', 'info_label_day_of_week',
                                     'comboBox_invoices_start_time', 'comboBox_invoices_stop_time', 'info_label_invoices_hours']
        try:
            add_working_day_widget_value_dict = self.widgets.get_widget_value_dict(relevant_widget_name_list)
            self.signals.pushbutton_add_working_day_clicked_signal.emit(add_working_day_widget_value_dict)
        except ValueError:
            print('Date was provided in an invalid format. It should be DD-MM-YYYY')

    def _on_pushbutton_fill_in_today_clicked(self):
        today = datetime.date.today()
        today_string = today.strftime(self.DATE_FORMAT)
        self.widgets.set_widget_value('lineEdit_invoices_date', today_string)

        self._update_day_of_week()

    def _update_day_of_week(self):
        try:
            date_object = self.widgets.get_invoices_date_as_object()
            day_of_week_string = date_object.strftime("%A")
            self.widgets.set_widget_value('info_label_day_of_week', day_of_week_string)
        except ValueError:
            print('An invalid date was entered')

    def _on_pushbutton_increment_by_one_week_clicked(self):

        try:
            date_object = self.widgets.get_invoices_date_as_object()
            one_week_increment = datetime.timedelta(weeks=1)
            date_one_week_incremented_object = date_object + one_week_increment
            date_one_week_incremented_string = date_one_week_incremented_object.strftime(self.DATE_FORMAT)

            self.widgets.set_widget_value('lineEdit_invoices_date', date_one_week_incremented_string)

            self._update_day_of_week()
        except ValueError:
            print('An invalid date was entered')

    def _update_difference_between_start_and_stop_time(self):
        start_time_string = self.widgets.get_widget_value('comboBox_invoices_start_time')
        start_time = toolbox.SimpleTime(string=start_time_string)

        stop_time_string = str(self.widgets.get_widget_value('comboBox_invoices_stop_time'))
        stop_time = toolbox.SimpleTime(string=stop_time_string)

        time_difference = stop_time - start_time
        number_of_hours = float(time_difference)
        self.widgets.set_widget_value('info_label_invoices_hours', number_of_hours)

    def _on_pushbutton_clear_fields_clicked(self):
        widget_value_dict = {'lineEdit_invoices_date': '', 'info_label_day_of_week': '', 'comboBox_invoices_start_time': '08:00', 'comboBox_invoices_stop_time': '17:00'}
        self.widgets.set_widget_values_using_dict(widget_value_dict)

    def _on_pushbutton_invoices_run_query_clicked(self):
        invoices_query_widget_value_dict = self._generate_invoices_query_widget_value_dict()
        self.signals.pushbutton_invoices_run_query_clicked_signal.emit(invoices_query_widget_value_dict)

    def _on_radiobutton_invoices_query_clicked(self):
        radiobutton_name = self.sender().objectName()
        invoices_query_widget_value_dict = self._generate_invoices_query_widget_value_dict()
        self.signals.radiobutton_invoices_query_clicked_signal.emit(radiobutton_name, invoices_query_widget_value_dict)

    def _generate_invoices_query_widget_value_dict(self):
        relevant_widget_name_list = ['comboBox_invoices_query_start_month', 'comboBox_invoices_query_start_year',
                                     'comboBox_invoices_query_stop_month', 'comboBox_invoices_query_stop_year',
                                     'comboBox_invoices_query_client_name']
        invoices_query_widget_value_dict = self.widgets.get_widget_value_dict(relevant_widget_name_list)
        return invoices_query_widget_value_dict

    def display_invoices_query_df_in_tableview_slot(self, invoices_query_df):
        self.widgets.set_widget_value('tableView_invoices_query', invoices_query_df)

    def _on_radiobutton_invoices_sort_clicked(self):
        radiobutton_name = self.sender().objectName()
        self.signals.radiobutton_invoices_sort_clicked_signal.emit(radiobutton_name)

    def _on_pushButton_invoices_export_query_results_clicked(self):
        self.signals.pushbutton_invoices_export_query_results_clicked_signal.emit()

    def _on_tableview_invoices_query_clicked(self):
        current_row = self._get_current_row_of_tableview_invoices_query()
        tableview_invoices_query_widget = self.widgets.get_widget('tableView_invoices_query') # violates Law of Demeter, todo fix it
        row_dict = tableview_invoices_query_widget.get_df_row_as_dict(current_row)
        widget_value_dict = self._generate_widget_value_dict_from_row_dict(row_dict)
        self.widgets.set_widget_values_using_dict(widget_value_dict)

    def _get_current_row_of_tableview_invoices_query(self):
        selected_indices = self.ui.tableView_invoices_query.selectedIndexes()
        current_row = selected_indices[0].row()
        return current_row

    def _generate_widget_value_dict_from_row_dict(self, row_dict):
        widget_value_dict = dict()
        for row in self.params.get_invoices_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            widget_value_dict[widget_name] = row_dict[info_name]
        return widget_value_dict

    def _on_pushbutton_invoices_overwrite_clicked(self):
        current_row = self._get_current_row_of_tableview_invoices_query()
        tableview_invoices_query_widget = self.widgets.get_widget('tableView_invoices_query') # violates Law of Demeter, todo fix it
        row_dict = tableview_invoices_query_widget.get_df_row_as_dict(current_row)
        UID_to_be_overwritten = row_dict['UID']
        relevant_widget_name_list = ['comboBox_invoices_client_name', 'info_label_invoices_client_code', 'lineEdit_invoices_date', 'info_label_day_of_week',
                                     'comboBox_invoices_start_time', 'comboBox_invoices_stop_time', 'info_label_invoices_hours']
        try:
            overwrite_working_day_widget_value_dict = self.widgets.get_widget_value_dict(relevant_widget_name_list)
            self.signals.pushbutton_invoices_overwrite_clicked_signal.emit(overwrite_working_day_widget_value_dict, UID_to_be_overwritten)
        except ValueError:
            print('Date was provided in an invalid format. It should be DD-MM-YYYY')

    def _on_pushbutton_invoices_delete_clicked(self):
        current_row = self._get_current_row_of_tableview_invoices_query()
        tableview_invoices_query_widget = self.widgets.get_widget('tableView_invoices_query') # violates Law of Demeter, todo fix it
        row_dict = tableview_invoices_query_widget.get_df_row_as_dict(current_row)
        UID_to_be_deleted = row_dict['UID']
        self.signals.pushbutton_invoices_delete_clicked_signal.emit(UID_to_be_deleted)
