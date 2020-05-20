import sys
import traceback

from PySide2 import QtCore

from modules.worker_thread import times, clients


class BackgroundExecution(QtCore.QObject):
    def __init__(self, signals, params):
        super().__init__()
        print('in background execution')
        self.signals = signals
        self.params = params
        self.times = times.Times(self.signals, self.params)
        self.times_query = times.TimesQuery(self.signals, self.params, self.times)
        self.clients = clients.Clients(self.signals, self.params)
        self.clients_query = clients.ClientsQuery(self.signals, self.params, self.clients)


    # times tab
    def pushbutton_add_working_day_clicked_slot(self, widget_value_dict):
        self.times.add_working_day_from_dict(widget_value_dict)

    def pushbutton_times_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten):
        self.times.overwrite_working_day_from_dict(widget_value_dict, UID_to_be_overwritten)

    def pushbutton_times_delete_clicked_slot(self, UID_to_be_removed):
        self.times.delete_working_day(UID_to_be_removed)

    def radiobutton_times_query_clicked_slot(self, radiobutton_name, widget_value_dict):
        if radiobutton_name == 'radioButton_times_query_dates_only':
            self.times_query.set_query_selection('dates_only')
        elif radiobutton_name == 'radioButton_times_query_client_only':
            self.times_query.set_query_selection('client_only')
        elif radiobutton_name == 'radioButton_times_query_dates_and_client':
            self.times_query.set_query_selection('dates_and_client')

        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(widget_value_dict)

    def pushbutton_times_run_query_clicked_slot(self, widget_value_dict):
        self.times_query.run_query(widget_value_dict)
        self.times_query.sort_query_result()
        self.times_query.display_query_result_in_tableview()

    def radiobutton_times_sort_clicked_slot(self, radiobutton_name):
        if radiobutton_name == 'radioButton_times_sort_by_date_only':
            self.times_query.sort_query_result_by_date_only()
        elif radiobutton_name == 'radioButton_times_sort_by_client_first':
            self.times_query.sort_query_result_by_client_first()
        elif radiobutton_name == 'radioButton_times_sort_by_month_then_by_client':
            self.times_query.sort_query_result_by_month_then_by_client()

        self.times_query.display_query_result_in_tableview()

    def pushbutton_times_export_query_results_clicked_slot(self):
        self.times_query.export_query_result()


    # clients tab
    def request_next_index_within_year_slot(self, year):
        print('in slot')
        try:
            next_index = self.clients.get_next_index_within_year(year)
            self.signals.deliver_next_index_within_year_signal.emit(next_index)
        except:
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)


    def pushbutton_add_client_clicked_slot(self, widget_value_dict):
        self.clients.add_client_from_dict(widget_value_dict)
        year = widget_value_dict['comboBox_clients_first_year']
        self.request_next_index_within_year_slot(year)

    def pushbutton_clients_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten):
        self.clients.overwrite_client_from_dict(widget_value_dict, UID_to_be_overwritten)

    def pushbutton_clients_delete_clicked_slot(self, UID_to_be_removed):
        print('UID_to_be_removed', UID_to_be_removed)
        self.clients.delete_client(UID_to_be_removed)

    def radiobutton_clients_query_clicked_slot(self, radiobutton_name, widget_value_dict):
        if radiobutton_name == 'radioButton_clients_query_using_years':
            self.clients_query.set_query_selection('using_years')
        elif radiobutton_name == 'radioButton_clients_query_return_all':
            self.clients_query.set_query_selection('return_all')

        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(widget_value_dict)

    def pushbutton_clients_run_query_clicked_slot(self, widget_value_dict):
        self.clients_query.run_query(widget_value_dict)
        self.clients_query.sort_query_result()
        self.clients_query.display_query_result_in_tableview()

    def radiobutton_clients_sort_clicked_slot(self, radiobutton_name):
        if radiobutton_name == 'radioButton_clients_sort_by_year_and_index':
            self.clients_query.sort_query_result_by_year_and_index()
        elif radiobutton_name == 'radioButton_clients_sort_by_client_name':
            self.clients_query.sort_query_result_by_client_name()

        self.clients_query.display_query_result_in_tableview()

    def pushbutton_clients_export_query_results_clicked_slot(self):
        self.clients_query.export_query_result()