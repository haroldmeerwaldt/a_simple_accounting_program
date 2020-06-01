import inspect
import sys
import traceback

from PySide2 import QtCore

from modules.worker_thread import times, clients, invoices, invoice_generation


class BackgroundExecution(QtCore.QObject):
    def __init__(self, signals, params):
        super().__init__()
        self.signals = signals
        self.params = params
        self.times = times.Times(self.signals, self.params)
        self.times_query = times.TimesQuery(self.signals, self.params, self.times)
        self.clients = clients.Clients(self.signals, self.params)
        self.clients_query = clients.ClientsQuery(self.signals, self.params, self.clients)
        self.invoices = invoices.Invoices(self.signals, self.params)
        self.invoices_query = invoices.InvoicesQuery(self.signals, self.params, self.invoices)
        self.invoices_from_template = invoice_generation.InvoicesFromTemplate(self.times, self.clients, self.invoices, params)


    ######################
    # times tab
    ######################
    def times_request_client_name_list_slot(self):
        print('requesting client name list')
        try:
            clients_df = self.clients.get_clients_df()
            client_name_list = list(clients_df['Client name'])
            self.signals.times_deliver_client_name_list_signal.emit(client_name_list)
        except:
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)

    def times_update_client_name_combobox(self):
        print('requesting client name list')
        try:
            clients_df = self.clients.get_clients_df()
            client_name_list = list(clients_df['Client name'])
            print('client_name_list', client_name_list)
            self.signals.times_update_client_name_combobox_signal.emit(client_name_list)
        except:
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)


    def times_request_client_code_slot(self, client_name):
        client_code = self.clients.get_client_code_based_on_client_name(client_name)
        self.signals.times_deliver_client_code_signal.emit(client_code)

    def pushbutton_add_working_day_clicked_slot(self, widget_value_dict, query_widget_value_dict):
        self.times.add_working_day_from_dict(widget_value_dict)
        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_times_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten, query_widget_value_dict):
        self.times.overwrite_working_day_from_dict(widget_value_dict, UID_to_be_overwritten)
        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_times_delete_clicked_slot(self, UID_to_be_removed, query_widget_value_dict):
        self.times.delete_working_day(UID_to_be_removed)
        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(query_widget_value_dict)

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

    ######################
    # clients tab
    ######################
    def request_next_index_within_year_slot(self, year):
        next_index = self.clients.get_next_index_within_year(year)
        self.signals.deliver_next_index_within_year_signal.emit(next_index)

    def pushbutton_add_client_clicked_slot(self, client_widget_value_dict, query_widget_value_dict):
        self.clients.add_client_from_dict(client_widget_value_dict)
        year = client_widget_value_dict['comboBox_clients_first_year']
        self.request_next_index_within_year_slot(year)

        # clients_df = self.clients.get_clients_df()
        # client_name_list = list(clients_df['Client name'])
        # self.signals.update_client_name_combobox_signal.emit(client_name_list)
        self.times_update_client_name_combobox()
        self.invoices_update_client_name_combobox()
        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_clients_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten, query_widget_value_dict):
        self.clients.overwrite_client_from_dict(widget_value_dict, UID_to_be_overwritten)
        self.times_update_client_name_combobox()
        self.invoices_update_client_name_combobox()
        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_clients_delete_clicked_slot(self, UID_to_be_removed, query_widget_value_dict):
        print('UID_to_be_removed', UID_to_be_removed)
        self.clients.delete_client(UID_to_be_removed)
        self.times_update_client_name_combobox()
        self.invoices_update_client_name_combobox()
        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

    def radiobutton_clients_query_clicked_slot(self, radiobutton_name, query_widget_value_dict):
        if radiobutton_name == 'radioButton_clients_query_using_years':
            self.clients_query.set_query_selection('using_years')
        elif radiobutton_name == 'radioButton_clients_query_return_all':
            self.clients_query.set_query_selection('return_all')

        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

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

    ######################
    # invoices tab
    ######################
    def invoices_request_client_name_list_slot(self):
        clients_df = self.clients.get_clients_df()
        client_name_list = [str(client_name) for client_name in clients_df['Client name']]
        self.signals.invoices_deliver_client_name_list_signal.emit(client_name_list)

    def invoices_update_client_name_combobox(self):
        clients_df = self.clients.get_clients_df()
        client_name_list = [str(client_name) for client_name in clients_df['Client name']]
        self.signals.invoices_update_client_name_combobox_signal.emit(client_name_list)


    def invoices_request_client_code_next_invoice_index_at_client_rates_and_compensations_slot(self, client_name):
        print('in slot invoices_request_client_code_and_next_invoice_index_at_client_slot')
        try:
            client_info_dict = self.clients.get_client_info_dict_based_on_client_name(client_name)
            client_code = client_info_dict['UID']
            next_invoice_index_at_client = self.invoices.get_next_invoice_index_at_client(client_code)
            print(next_invoice_index_at_client)
            row_dict = {'Invoice index at client': next_invoice_index_at_client}
            client_to_invoice_dict = {'UID': 'Client code',
                                      'Standard rate during day (euro/h)': 'Rate during day (euro/h)',
                                      'Standard rate for shifts (euro/h)': 'Rate for shifts (euro/h)',
                                      'Standard compensation for commute (euro/km)': 'Compensation for commute (euro/km)',
                                      'Standard compensation for driving during work (euro/km)': 'Compensation for driving during work (euro/km)'}
            for key_client, key_invoice in client_to_invoice_dict.items():
                row_dict[key_invoice] = client_info_dict[key_client]
            self.signals.invoices_deliver_client_code_next_invoice_index_at_client_rates_and_compensations_signal.emit(row_dict)
        except Exception as e:
            print(e)
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)

    def invoices_request_client_code_next_invoice_index_at_client_rates_slot(self, client_name):
        print('in slot invoices_request_client_code_and_next_invoice_index_at_client_slot')
        try:
            client_info_dict = self.clients.get_client_info_dict_based_on_client_name(client_name)
            client_code = client_info_dict['UID']
            next_invoice_index_at_client = self.invoices.get_next_invoice_index_at_client(client_code)
            print(next_invoice_index_at_client)
            row_dict = {'Invoice index at client': next_invoice_index_at_client,
                        'Client code': client_code}
            self.signals.invoices_deliver_client_code_next_invoice_index_at_client_rates_signal.emit(row_dict)
        except Exception as e:
            print(e)
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)

    def pushbutton_generate_invoice_clicked_slot(self, invoice_widget_value_dict, query_widget_value_dict):
        print(inspect.currentframe().f_code.co_name)
        try:
            client_code = invoice_widget_value_dict['info_label_invoices_client_code']
            month = invoice_widget_value_dict['comboBox_invoices_month']
            year = invoice_widget_value_dict['comboBox_invoices_year']
            if self.invoices.there_is_already_an_invoice_for_this_client_month_and_year(client_code, month, year):
                print('There is already an invoice for this client in this month and year. No invoice generated')
            else:
                dict_to_be_added = self.invoices.generate_invoice_from_dict(invoice_widget_value_dict)
                self.invoices_from_template.generate_invoice(dict_to_be_added)

                client_name = invoice_widget_value_dict['comboBox_invoices_client_name']
                self.invoices_request_client_code_next_invoice_index_at_client_rates_slot(client_name)

                if self.invoices_query.query_has_been_run_before():
                    self.pushbutton_invoices_run_query_clicked_slot(query_widget_value_dict)
        except:
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)



    def pushbutton_invoices_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten, query_widget_value_dict):
        self.invoices.overwrite_invoice_from_dict(widget_value_dict, UID_to_be_overwritten)
        if self.invoices_query.query_has_been_run_before():
            self.pushbutton_invoices_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_invoices_delete_clicked_slot(self, UID_to_be_removed, query_widget_value_dict):
        self.invoices.delete_invoice(UID_to_be_removed)
        if self.invoices_query.query_has_been_run_before():
            self.pushbutton_invoices_run_query_clicked_slot(query_widget_value_dict)

    def radiobutton_invoices_query_clicked_slot(self, radiobutton_name, query_widget_value_dict):
        if radiobutton_name == 'radioButton_invoices_sort_by_date_only':
            self.invoices_query.set_query_selection('by_date_only')
        elif radiobutton_name == 'radioButton_invoices_sort_by_client_first':
            self.invoices_query.set_query_selection('by_client_first')
        elif radiobutton_name == 'radioButton_invoices_sort_by_month_then_by_client':
            self.invoices_query.set_query_selection('by_month_then_by_client')

        if self.invoices_query.query_has_been_run_before():
            self.pushbutton_invoices_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_invoices_run_query_clicked_slot(self, widget_value_dict):
        print(inspect.currentframe().f_code.co_name)
        print(widget_value_dict)
        try:
            self.invoices_query.run_query(widget_value_dict)
            self.invoices_query.sort_query_result()
            self.invoices_query.display_query_result_in_tableview()
        except:
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)
        print('finished slot successfully')

    def radiobutton_invoices_sort_clicked_slot(self, radiobutton_name):
        if radiobutton_name == 'radioButton_invoices_sort_by_date_only':
            self.invoices_query.sort_query_result_by_date_only()
        elif radiobutton_name == 'radioButton_invoices_sort_by_client_first':
            self.invoices_query.sort_query_result_by_client_first()
        elif radiobutton_name == 'radioButton_invoices_sort_by_month_then_by_client':
            self.invoices_query.sort_query_result_by_month_then_by_client()

        self.invoices_query.display_query_result_in_tableview()

    def pushbutton_invoices_export_query_results_clicked_slot(self):
        self.invoices_query.export_query_result()