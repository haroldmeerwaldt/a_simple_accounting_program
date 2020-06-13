import openpyxl
import datetime
import inspect
import os
import sys
import traceback

import numpy as np
import pandas as pd

from modules.utilities import toolbox


class Invoices:
    def __init__(self, signals, params):
        self.signals = signals
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT
        self.invoices_filename = params.invoices_filename
        self._generate_invoices_df_from_input_file()


    def get_next_invoice_index_at_client(self, client_code):
        try:
            valid_row_indices = self.invoices_df['Client code'] == client_code
            client_df = self.invoices_df.loc[valid_row_indices]
            highest_index = client_df['Invoice index at client'].max()
            if np.isnan(highest_index):
                highest_index = 0
            next_index = highest_index + 1
        except:
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)

        return next_index

    def _generate_invoices_df_from_input_file(self):
        try:
            self.invoices_df = pd.read_csv(self.invoices_filename, sep='\t')
        except FileNotFoundError:
            column_list = self.params.invoices_info_structure_df['info_name'].tolist()
            self.invoices_df = pd.DataFrame(columns=column_list)

        self.invoices_df['Invoice date'] = pd.to_datetime(self.invoices_df['Invoice date'], format=self.DATE_FORMAT)
        self.invoices_df['Client code'] = self.invoices_df['Client code'].astype(str)


    def get_invoices_df(self):
        return self.invoices_df

    def there_is_already_an_invoice_for_this_client_month_and_year(self, client_code, month, year):
        valid_row_indices_for_client = self.invoices_df['Client code'] == client_code
        client_invoice_info_df = self.invoices_df.loc[valid_row_indices_for_client]
        month_and_year_match_bool_series = (client_invoice_info_df['Month'] == month) & (client_invoice_info_df['Year'] == year)
        return any(month_and_year_match_bool_series)

    @toolbox.print_when_called_and_return_exception_inside_thread
    def generate_invoice_from_dict(self, widget_value_dict):
        dict_to_be_added = self._generate_dict_to_be_added_from_widget_value_dict(widget_value_dict)
        self._add_invoice_in_memory(dict_to_be_added)
        self._add_invoice_to_file(dict_to_be_added)
        return dict_to_be_added  # handle returning dict better


    def _generate_dict_to_be_added_from_widget_value_dict(self, widget_value_dict):
        dict_to_be_added = dict()
        for row in self.params.get_invoices_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            dict_to_be_added[info_name] = widget_value_dict[widget_name]
        return dict_to_be_added

    def _add_invoice_in_memory(self, dict_to_be_added):
        self.invoices_df = self.invoices_df.append(dict_to_be_added, ignore_index=True)

    def _add_invoice_to_file(self, dict_to_be_added):
        df_to_be_added = pd.DataFrame([dict_to_be_added], columns=self.invoices_df.columns)
        use_header = not os.path.exists(self.invoices_filename)
        toolbox.append_df_to_excel(df_to_be_added, self.invoices_filename, header=use_header) #, date_format=self.DATE_FORMAT)

    @toolbox.print_when_called_and_return_exception_inside_thread
    def overwrite_invoice_from_dict(self, widget_value_dict, UID_of_dropped_row):
        self._drop_rows_from_invoices_df_based_on_UID(UID_of_dropped_row)
        self._append_row_to_invoices_df_using_widget_value_dict(widget_value_dict)
        self._save_invoices_df_to_file()

    def _append_row_to_invoices_df_using_widget_value_dict(self, widget_value_dict):
        dict_to_be_overwritten_with = self._generate_dict_to_be_added_from_widget_value_dict(widget_value_dict)
        self.invoices_df = self.invoices_df.append(dict_to_be_overwritten_with, ignore_index=True)

    def delete_invoice(self, UID_of_dropped_row):
        self._drop_rows_from_invoices_df_based_on_UID(UID_of_dropped_row)
        self._save_invoices_df_to_file()

    def _drop_rows_from_invoices_df_based_on_UID(self, UID_of_dropped_row):
        self.invoices_df = self.invoices_df.set_index('UID')
        self.invoices_df = self.invoices_df.drop(index=UID_of_dropped_row)
        self.invoices_df = self.invoices_df.reset_index().rename(columns={'index': 'UID'})

    def _save_invoices_df_to_file(self):
        self.invoices_df.to_excel(self.invoices_filename, index=False, date_format=self.DATE_FORMAT)


class InvoicesQuery:
    def __init__(self, signals, params, invoices):
        self.signals = signals
        self.params = params
        self.invoices = invoices
        self.DATE_FORMAT = params.DATE_FORMAT
        self.query_result_df = None
        self.query_selection = 'dates_only'
        self.query_sort_method = 'by_date_only'

    def set_query_selection(self, query_selection):
        self.query_selection = query_selection

    def _is_query_selection(self, query_selection):
        return self.query_selection == query_selection

    def query_has_been_run_before(self):
        return self.query_result_df is not None

    def run_query(self, widget_value_dict):
        if self._is_query_selection('dates_only'):
            self.query_dates_only(widget_value_dict)
        elif self._is_query_selection('client_only'):
            self.query_client_only(widget_value_dict)
        elif self._is_query_selection('dates_and_client'):
            self.query_dates_and_client(widget_value_dict)
        elif self._is_query_selection('return_all'):
            self.query_return_all(widget_value_dict)

    def query_dates_only(self, snapshot_dict):
        start_date, stop_date = self._extract_start_and_stop_date_from_snapshot_dict(snapshot_dict)
        invoices_df = self.invoices.get_invoices_df()
        valid_row_indices = (start_date <= invoices_df['Invoice date']) & (invoices_df['Invoice date'] < stop_date)
        self.query_result_df = invoices_df.loc[valid_row_indices]


    def query_client_only(self, snapshot_dict):
        client_name = snapshot_dict['comboBox_invoices_query_client_name']
        invoices_df = self.invoices.get_invoices_df()

        valid_row_indices = invoices_df['Client name'] == client_name
        self.query_result_df = invoices_df.loc[valid_row_indices]

    def query_dates_and_client(self, snapshot_dict):
        start_date, stop_date = self._extract_start_and_stop_date_from_snapshot_dict(snapshot_dict)
        client_name = snapshot_dict['comboBox_invoices_query_client_name']
        invoices_df = self.invoices.get_invoices_df()

        valid_row_indices = (start_date <= invoices_df['Date']) & (invoices_df['Date'] < stop_date) & (invoices_df['Client name'] == client_name)
        self.query_result_df = invoices_df.loc[valid_row_indices]

    def query_return_all(self):
        invoices_df = self.invoices.get_invoices_df()
        self.query_result_df = invoices_df.copy()

    def _extract_start_and_stop_date_from_snapshot_dict(self, snapshot_dict):
        start_date_string = snapshot_dict['comboBox_invoices_query_start_month'] + ' ' + str(snapshot_dict['comboBox_invoices_query_start_year'])
        start_date = datetime.datetime.strptime(start_date_string, '%B %Y')

        stop_date_string = snapshot_dict['comboBox_invoices_query_stop_month'] + ' ' + str(snapshot_dict['comboBox_invoices_query_stop_year'])
        stop_date = datetime.datetime.strptime(stop_date_string, '%B %Y')
        stop_date_month = stop_date.month
        stop_date_year = stop_date.year
        if stop_date_month == 12:
            stop_date_month = 1
            stop_date_year = stop_date_year + 1
        else:
            stop_date_month = stop_date_month + 1
        stop_date = datetime.datetime(year=stop_date_year, month=stop_date_month, day=1, hour=0, minute=0, second=0)
        return start_date, stop_date

    def display_query_result_in_tableview(self):
        displayed_query_result_df = self.query_result_df.copy()
        displayed_query_result_df['Invoice date'] = displayed_query_result_df['Invoice date'].dt.strftime(self.DATE_FORMAT)
        self.signals.display_invoices_query_df_in_tableview_signal.emit(displayed_query_result_df)

    def sort_query_result(self):
        if self.query_sort_method == 'by_date_only':
            self.sort_query_result_by_date_only()
        elif self.query_sort_method == 'by_client_first':
            self.sort_query_result_by_client_first()
        if self.query_sort_method == 'by_month_then_by_client':
            self.sort_query_result_by_month_then_by_client()

    def sort_query_result_by_date_only(self):
        self.query_sort_method = 'by_date_only'
        if self.query_result_df is not None:
            self.query_result_df = self.query_result_df.sort_values(by=['Invoice date'])

    def sort_query_result_by_client_first(self):
        self.query_sort_method = 'by_client_first'
        if self.query_result_df is not None:
            self.query_result_df = self.query_result_df.sort_values(by=['Client name', 'Date'])

    @toolbox.print_when_called_and_return_exception_inside_thread
    def sort_query_result_by_month_then_by_client(self):
        self.query_sort_method = 'by_month_then_by_client'
        if self.query_result_df is not None:
            query_result_df_copy = self.query_result_df.copy() # making a copy first and working on it prevents pandas SettingWithCopyWarning
            date_series = query_result_df_copy['Date']
            query_result_df_copy['Month'] = [date.month for date in date_series]
            query_result_df_copy = query_result_df_copy.sort_values(by=['Month', 'Client name'])
            query_result_df_copy = query_result_df_copy.drop(labels='Month', axis='columns')
            self.query_result_df = query_result_df_copy.copy()

    def export_query_result(self):
        export_filename = 'export_invoices_query_results_{}.xlsx'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
        exports_directory = self.params.exports_directory
        export_path = os.path.join(exports_directory, export_filename)
        self.query_result_df.to_excel(export_path, index=False, date_format=self.DATE_FORMAT)




