import datetime
import inspect
import logging
import os
import sys
import traceback
import zipfile

from PySide2 import QtCore

from modules.worker_thread import times, clients, invoices, invoice_generation


class BackgroundExecution(QtCore.QObject):
    def __init__(self, signals, params):
        super().__init__()
        self.signals = signals
        self.params = params

        self.logger = logging.getLogger('main.' + __name__)

        self.times = times.Times(self.signals, self.params)
        self.times_query = times.TimesQuery(self.signals, self.params, self.times)
        self.clients = clients.Clients(self.signals, self.params)
        self.clients_query = clients.ClientsQuery(self.signals, self.params, self.clients)
        self.invoices = invoices.Invoices(self.signals, self.params)
        self.invoices_query = invoices.InvoicesQuery(self.signals, self.params, self.invoices)

        self.invoices_from_template = invoice_generation.InvoicesFromTemplate(self.times, self.clients, self.invoices, params)

        self._backup_user_files()

    def _backup_user_files(self):
        backup = Backup(self.params)
        backup.generate_backup()

    ######################
    # times tab
    ######################

    # adding/overwriting
    def times_request_client_name_list_slot(self):
        clients_df = self.clients.get_clients_df()
        client_name_list = list(clients_df['Client name'])
        self.signals.times_deliver_client_name_list_signal.emit(client_name_list)

    def times_update_client_name_combobox(self):
        clients_df = self.clients.get_clients_df()
        client_name_list = list(clients_df['Client name'])
        self.signals.times_update_client_name_combobox_signal.emit(client_name_list)

    def times_request_client_code_slot(self, client_name):
        client_code = self.clients.get_client_code_based_on_client_name(client_name)
        self.signals.times_deliver_client_code_signal.emit(client_code)

    def pushbutton_add_working_day_clicked_slot(self, widget_value_dict, query_widget_value_dict):
        self.times.add_working_day_from_dict(widget_value_dict)
        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(query_widget_value_dict)

    # querying
    def radiobutton_times_query_clicked_slot(self, radiobutton_name, widget_value_dict):
        if radiobutton_name == 'radioButton_times_query_dates_only':
            self.times_query.set_query_selection('dates_only')
        elif radiobutton_name == 'radioButton_times_query_client_only':
            self.times_query.set_query_selection('client_only')
        elif radiobutton_name == 'radioButton_times_query_dates_and_client':
            self.times_query.set_query_selection('dates_and_client')

        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(widget_value_dict)

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

    def pushbutton_times_run_query_clicked_slot(self, widget_value_dict):
        self.times_query.run_query(widget_value_dict)
        self.times_query.sort_query_result()
        self.times_query.display_query_result_in_tableview()

    # tableview
    def pushbutton_times_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten, query_widget_value_dict):
        self.times.overwrite_working_day_from_dict(widget_value_dict, UID_to_be_overwritten)
        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_times_delete_clicked_slot(self, UID_to_be_removed, query_widget_value_dict):
        self.times.delete_working_day(UID_to_be_removed)
        if self.times_query.query_has_been_run_before():
            self.pushbutton_times_run_query_clicked_slot(query_widget_value_dict)

    ######################
    # clients tab
    ######################

    # adding/overwriting
    def request_next_index_within_year_slot(self, year):
        next_index = self.clients.get_next_index_within_year(year)
        self.signals.deliver_next_index_within_year_signal.emit(next_index)

    def pushbutton_add_client_clicked_slot(self, client_widget_value_dict, query_widget_value_dict):
        self.clients.add_client_from_dict(client_widget_value_dict)
        year = client_widget_value_dict['comboBox_clients_first_year']
        self.request_next_index_within_year_slot(year)

        self.times_update_client_name_combobox()
        self.invoices_update_client_name_combobox()
        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

    # querying
    def radiobutton_clients_query_clicked_slot(self, radiobutton_name, query_widget_value_dict):
        if radiobutton_name == 'radioButton_clients_query_using_years':
            self.clients_query.set_query_selection('using_years')
        elif radiobutton_name == 'radioButton_clients_query_return_all':
            self.clients_query.set_query_selection('return_all')

        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

    def radiobutton_clients_sort_clicked_slot(self, radiobutton_name):
        if radiobutton_name == 'radioButton_clients_sort_by_year_and_index':
            self.clients_query.sort_query_result_by_year_and_index()
        elif radiobutton_name == 'radioButton_clients_sort_by_client_name':
            self.clients_query.sort_query_result_by_client_name()

        self.clients_query.display_query_result_in_tableview()

    def pushbutton_clients_export_query_results_clicked_slot(self):
        self.clients_query.export_query_result()

    def pushbutton_clients_run_query_clicked_slot(self, widget_value_dict):
        self.clients_query.run_query(widget_value_dict)
        self.clients_query.sort_query_result()
        self.clients_query.display_query_result_in_tableview()

    # tableview
    def pushbutton_clients_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten, query_widget_value_dict):
        self.clients.overwrite_client_from_dict(widget_value_dict, UID_to_be_overwritten)
        self.times_update_client_name_combobox()
        self.invoices_update_client_name_combobox()
        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_clients_delete_clicked_slot(self, UID_to_be_removed, query_widget_value_dict):
        self.clients.delete_client(UID_to_be_removed)
        self.times_update_client_name_combobox()
        self.invoices_update_client_name_combobox()
        if self.clients_query.query_has_been_run_before():
            self.pushbutton_clients_run_query_clicked_slot(query_widget_value_dict)

    ######################
    # invoices tab
    ######################

    # adding/overwriting
    def invoices_request_client_name_list_slot(self):
        clients_df = self.clients.get_clients_df()
        client_name_list = [str(client_name) for client_name in clients_df['Client name']]
        self.signals.invoices_deliver_client_name_list_signal.emit(client_name_list)

    def invoices_update_client_name_combobox(self):
        clients_df = self.clients.get_clients_df()
        client_name_list = [str(client_name) for client_name in clients_df['Client name']]
        self.signals.invoices_update_client_name_combobox_signal.emit(client_name_list)

    def invoices_request_client_code_next_invoice_index_at_client_rates_and_compensations_slot(self, client_name):
        client_info_dict = self.clients.get_client_info_dict_based_on_client_name(client_name)
        if client_info_dict is not None:
            client_code = client_info_dict['UID']
            next_invoice_index_at_client = self.invoices.get_next_invoice_index_at_client(client_code)
            row_dict = {'Invoice index at client': next_invoice_index_at_client}
            client_to_invoice_dict = {'UID': 'Client code',
                                      'Standard rate during day (euro/h)': 'Rate during day (euro/h)',
                                      'Standard rate for shifts (euro/h)': 'Rate for shifts (euro/h)',
                                      'Standard compensation for commute (euro/km)': 'Compensation for commute (euro/km)',
                                      'Standard compensation for driving during work (euro/km)': 'Compensation for driving during work (euro/km)'} # todo move to nicer place
            for key_client, key_invoice in client_to_invoice_dict.items():
                row_dict[key_invoice] = client_info_dict[key_client]
            self.signals.invoices_deliver_client_code_next_invoice_index_at_client_rates_and_compensations_signal.emit(row_dict)

    def invoices_request_client_code_next_invoice_index_at_client_rates_slot(self, client_name):
        client_info_dict = self.clients.get_client_info_dict_based_on_client_name(client_name)
        client_code = client_info_dict['UID']
        next_invoice_index_at_client = self.invoices.get_next_invoice_index_at_client(client_code)
        row_dict = {'Invoice index at client': next_invoice_index_at_client,
                    'Client code': client_code}
        self.signals.invoices_deliver_client_code_next_invoice_index_at_client_rates_signal.emit(row_dict)

    def pushbutton_generate_invoice_clicked_slot(self, invoice_widget_value_dict, query_widget_value_dict):
        client_code = invoice_widget_value_dict['info_label_invoices_client_code']
        month = invoice_widget_value_dict['comboBox_invoices_month']
        year = invoice_widget_value_dict['comboBox_invoices_year']
        if self.invoices.there_is_already_an_invoice_for_this_client_month_and_year(client_code, month, year):
            self.logger.warning('There is already an invoice for this client in this month and year. No invoice generated')
        else:
            dict_to_be_added = self.invoices.generate_invoice_from_dict(invoice_widget_value_dict)
            self.invoices_from_template.generate_invoice(dict_to_be_added)

            client_name = invoice_widget_value_dict['comboBox_invoices_client_name']
            self.invoices_request_client_code_next_invoice_index_at_client_rates_slot(client_name)

            if self.invoices_query.query_has_been_run_before():
                self.pushbutton_invoices_run_query_clicked_slot(query_widget_value_dict)

    # querying
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
        self.invoices_query.run_query(widget_value_dict)
        self.invoices_query.sort_query_result()
        self.invoices_query.display_query_result_in_tableview()

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

    # tableview
    def pushbutton_invoices_overwrite_clicked_slot(self, widget_value_dict, UID_to_be_overwritten, query_widget_value_dict):
        self.invoices.overwrite_invoice_from_dict(widget_value_dict, UID_to_be_overwritten)
        if self.invoices_query.query_has_been_run_before():
            self.pushbutton_invoices_run_query_clicked_slot(query_widget_value_dict)

    def pushbutton_invoices_delete_clicked_slot(self, UID_to_be_removed, query_widget_value_dict):
        self.invoices.delete_invoice(UID_to_be_removed)
        if self.invoices_query.query_has_been_run_before():
            self.pushbutton_invoices_run_query_clicked_slot(query_widget_value_dict)

class Backup:
    def __init__(self, params):
        self.user_directory = params.user_directory
        self.backup_directory = params.backup_directory
        self.user_directory_depth = len(self.user_directory.split(os.sep))

        self.logger = logging.getLogger('main.' + __name__)

        now = datetime.datetime.now()
        zipfile_name = now.strftime("%Y%m%d_%H%M%S_ASAP_user_files_backup.zip")
        self.zipfile_path = os.path.join(self.backup_directory, zipfile_name)

    def generate_backup(self):
        with zipfile.ZipFile(self.zipfile_path, 'w') as zip_object:
            for directory, subfolders, filenames in os.walk(self.user_directory):
                if directory != self.backup_directory:
                    directory_depth = len(directory.split(os.sep))

                    if directory_depth == self.user_directory_depth:
                        directory_in_archive = ''
                    else:
                        subdirectory_in_archive_list = directory.split(os.sep)[-(directory_depth-self.user_directory_depth):]
                        directory_in_archive = os.path.join(*subdirectory_in_archive_list)

                    for filename in filenames:
                        file_path = os.path.join(directory, filename)
                        file_path_in_archive = os.path.join(directory_in_archive, filename)
                        zip_object.write(file_path, file_path_in_archive)

        self.logger.info('Backup of user files generated and stored at: {}'.format(self.zipfile_path))