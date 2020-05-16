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
    def pushbutton_add_client_clicked_slot(self, widget_value_dict):
        self.clients.add_client_from_dict(widget_value_dict)




