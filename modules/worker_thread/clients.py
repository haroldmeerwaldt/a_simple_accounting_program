import sys
import traceback

import datetime
import os
import numpy as np

import pandas as pd

from modules.utilities import toolbox


class Clients:
    def __init__(self, signals, params):
        self.signals = signals
        self.params = params
        self.clients_filename = params.clients_filename
        self._generate_clients_df_from_input_file()


    def get_next_index_within_year(self, year):
        valid_row_indices = self.clients_df['First year'] == year
        year_df = self.clients_df.loc[valid_row_indices]
        highest_index = year_df['Index within year'].max()
        if np.isnan(highest_index):
            highest_index = 0
        next_index = highest_index + 1
        return next_index

    def get_clients_df(self):
        return self.clients_df

    def get_client_code_based_on_client_name(self, client_name):
        valid_row_indices = self.clients_df['Client name'] == client_name
        client_code_list = self.clients_df.loc[valid_row_indices, 'UID'].tolist()
        print('client_code_list', client_code_list)

        if len(client_code_list) == 0:
            print('client code was not found')
        elif len(client_code_list) == 1:
            client_code = client_code_list[0]
            return client_code
        elif len(client_code_list) > 1:
            print('multiple client codes were found')

    def _generate_clients_df_from_input_file(self):
        try:
            self.clients_df = pd.read_csv(self.clients_filename, sep='\t')
        except FileNotFoundError:
            column_list = self.params.clients_info_structure_df['info_name'].tolist()
            self.clients_df = pd.DataFrame(columns=column_list)
        self.clients_df = self.clients_df.astype({'UID': str, 'Client name': str, 'First year': int})


    @toolbox.print_when_called_and_return_exception_inside_thread
    def add_client_from_dict(self, widget_value_dict):
        dict_to_be_added = self._generate_dict_to_be_added_from_widget_value_dict(widget_value_dict)

        self._add_client_in_memory(dict_to_be_added)
        self._add_client_to_file(dict_to_be_added)

    def _generate_dict_to_be_added_from_widget_value_dict(self, widget_value_dict):
        dict_to_be_added = dict()
        for row in self.params.get_clients_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            dict_to_be_added[info_name] = widget_value_dict[widget_name]
        return dict_to_be_added

    def _add_client_in_memory(self, dict_to_be_added):
        self.clients_df = self.clients_df.append(dict_to_be_added, ignore_index=True)

    def _add_client_to_file(self, dict_to_be_added):
        df_to_be_added = pd.DataFrame([dict_to_be_added], columns=self.clients_df.columns)
        use_header = not os.path.exists(self.clients_filename)
        try:
            df_to_be_added.to_csv(self.clients_filename, sep='\t', mode='a', index=False, header=use_header)
        except PermissionError:
            print('{} is currently open. Please close the file and try again'.format(self.clients_filename))

    @toolbox.print_when_called_and_return_exception_inside_thread
    def overwrite_client_from_dict(self, widget_value_dict, UID_of_dropped_row):
        self._drop_rows_from_clients_df_based_on_UID(UID_of_dropped_row)
        self._append_row_to_clients_df_using_widget_value_dict(widget_value_dict)
        self._save_clients_df_to_tsv_file()

    def _append_row_to_clients_df_using_widget_value_dict(self, widget_value_dict):
        dict_to_be_overwritten_with = self._generate_dict_to_be_added_from_widget_value_dict(widget_value_dict)
        self.clients_df = self.clients_df.append(dict_to_be_overwritten_with, ignore_index=True)

    def delete_client(self, UID_of_dropped_row):
        self._drop_rows_from_clients_df_based_on_UID(UID_of_dropped_row)
        self._save_clients_df_to_tsv_file()

    def _drop_rows_from_clients_df_based_on_UID(self, UID_of_dropped_row):
        self.clients_df = self.clients_df.set_index('UID')
        self.clients_df = self.clients_df.drop(index=UID_of_dropped_row)
        self.clients_df = self.clients_df.reset_index().rename(columns={'index': 'UID'})

    def _save_clients_df_to_tsv_file(self):
        self.clients_df.to_csv(self.clients_filename, sep='\t', index=False)

class ClientsQuery:
    def __init__(self, signals, params, clients):
        self.signals = signals
        self.params = params
        self.clients = clients
        self.DATE_FORMAT = params.DATE_FORMAT
        self.query_result_df = None
        self.query_selection = 'using_years'
        self.query_sort_method = 'by_year_and_index'

    def set_query_selection(self, query_selection):
        self.query_selection = query_selection

    def _is_query_selection(self, query_selection):
        return self.query_selection == query_selection

    def query_has_been_run_before(self):
        return self.query_result_df is not None

    def run_query(self, widget_value_dict):
        if self._is_query_selection('using_years'):
            self.query_using_years(widget_value_dict)
        elif self._is_query_selection('return_all'):
            self.query_return_all()

    def query_using_years(self, snapshot_dict):
        start_year = snapshot_dict['comboBox_clients_query_start_year']
        stop_year = snapshot_dict['comboBox_clients_query_stop_year']
        clients_df = self.clients.get_clients_df()

        valid_row_indices = (start_year <= clients_df['First year']) & (clients_df['First year'] <= stop_year)
        self.query_result_df = clients_df.loc[valid_row_indices]

    def query_return_all(self):
        clients_df = self.clients.get_clients_df()
        self.query_result_df = clients_df.copy()

    def display_query_result_in_tableview(self):
        displayed_query_result_df = self.query_result_df.copy()
        self.signals.display_clients_query_df_in_tableview_signal.emit(displayed_query_result_df)

    def sort_query_result(self):
        if self.query_sort_method == 'by_year_and_index':
            self.sort_query_result_by_year_and_index()
        elif self.query_sort_method == 'by_client_name':
            self.sort_query_result_by_client_name()

    def sort_query_result_by_year_and_index(self):
        self.query_sort_method = 'by_year_and_index'
        if self.query_result_df is not None:
            self.query_result_df = self.query_result_df.sort_values(by=['First year', 'Index within year'])

    def sort_query_result_by_client_name(self):
        self.query_sort_method = 'by_client_name'
        if self.query_result_df is not None:
            self.query_result_df = self.query_result_df.sort_values(by=['Client name'])

    def export_query_result(self):
        export_filename = 'export_clients_query_results_{}.tsv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
        user_directory = self.params.user_directory
        export_path = os.path.join(user_directory, export_filename)
        self.query_result_df.to_csv(export_path, sep='\t', index=False, date_format=self.DATE_FORMAT)
