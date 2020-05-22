import datetime
import os

import pandas as pd

from modules.utilities import toolbox


class Times:
    def __init__(self, signals, params):
        self.signals = signals
        self.params = params
        self.DATE_FORMAT = params.DATE_FORMAT
        self.times_filename = params.times_filename
        self._generate_times_df_from_input_file()

    def _generate_times_df_from_input_file(self):
        try:
            self.times_df = pd.read_csv(self.times_filename, sep='\t')
        except FileNotFoundError:
            column_list = ['UID'] + self.params.times_info_structure_df['info_name'].tolist()
            self.times_df = pd.DataFrame(columns=column_list)

        self.times_df['Date'] = pd.to_datetime(self.times_df['Date'], format=self.DATE_FORMAT)

    def get_times_df(self):
        return self.times_df

    @toolbox.print_when_called_and_return_exception_inside_thread
    def add_working_day_from_dict(self, widget_value_dict):
        dict_to_be_added = self._generate_dict_to_be_added_from_widget_value_dict(widget_value_dict)
        dict_to_be_added['UID'] = self._generate_UID(dict_to_be_added)
        self._add_working_day_in_memory(dict_to_be_added)
        self._add_working_day_to_file(dict_to_be_added)

    def _generate_dict_to_be_added_from_widget_value_dict(self, widget_value_dict):
        dict_to_be_added = dict()
        for row in self.params.get_times_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            dict_to_be_added[info_name] = widget_value_dict[widget_name]
        return dict_to_be_added

    def _generate_UID(self, dict_to_be_added):
        client_name = dict_to_be_added['Client name']
        date = dict_to_be_added['Date']
        date_string = date.strftime(self.DATE_FORMAT)
        start_time = dict_to_be_added['Start time']
        list_of_info_in_UID = [client_name, date_string, start_time]
        UID = '_'.join(list_of_info_in_UID)
        return UID

    def _add_working_day_in_memory(self, dict_to_be_added):
        self.times_df = self.times_df.append(dict_to_be_added, ignore_index=True)

    def _add_working_day_to_file(self, dict_to_be_added):
        df_to_be_added = pd.DataFrame([dict_to_be_added], columns=self.times_df.columns)
        use_header = not os.path.exists(self.times_filename)
        df_to_be_added.to_csv(self.times_filename, sep='\t', mode='a', index=False, header=use_header, date_format=self.DATE_FORMAT)

    @toolbox.print_when_called_and_return_exception_inside_thread
    def overwrite_working_day_from_dict(self, widget_value_dict, UID_of_dropped_row):
        self._drop_rows_from_times_df_based_on_UID(UID_of_dropped_row)
        self._append_row_to_times_df_using_widget_value_dict(widget_value_dict)
        self._save_times_df_to_tsv_file()

    def _append_row_to_times_df_using_widget_value_dict(self, widget_value_dict):
        dict_to_be_overwritten_with = self._generate_dict_to_be_added_from_widget_value_dict(widget_value_dict)
        dict_to_be_overwritten_with['UID'] = self._generate_UID(dict_to_be_overwritten_with)
        self.times_df = self.times_df.append(dict_to_be_overwritten_with, ignore_index=True)

    def delete_working_day(self, UID_of_dropped_row):
        self._drop_rows_from_times_df_based_on_UID(UID_of_dropped_row)
        self._save_times_df_to_tsv_file()

    def _drop_rows_from_times_df_based_on_UID(self, UID_of_dropped_row):
        self.times_df = self.times_df.set_index('UID')
        self.times_df = self.times_df.drop(index=UID_of_dropped_row)
        self.times_df = self.times_df.reset_index().rename(columns={'index': 'UID'})

    def _save_times_df_to_tsv_file(self):
        self.times_df.to_csv(self.times_filename, sep='\t', index=False, date_format=self.DATE_FORMAT)


class TimesQuery:
    def __init__(self, signals, params, times):
        self.signals = signals
        self.params = params
        self.times = times
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

    def query_dates_only(self, snapshot_dict):
        start_date, stop_date = self._extract_start_and_stop_date_from_snapshot_dict(snapshot_dict)
        times_df = self.times.get_times_df()

        valid_row_indices = (start_date <= times_df['Date']) & (times_df['Date'] < stop_date)
        self.query_result_df = times_df.loc[valid_row_indices]

    def query_client_only(self, snapshot_dict):
        client_name = snapshot_dict['comboBox_times_query_client_name']
        times_df = self.times.get_times_df()

        valid_row_indices = times_df['Client name'] == client_name
        self.query_result_df = times_df.loc[valid_row_indices]

    def query_dates_and_client(self, snapshot_dict):
        start_date, stop_date = self._extract_start_and_stop_date_from_snapshot_dict(snapshot_dict)
        client_name = snapshot_dict['comboBox_times_query_client_name']
        times_df = self.times.get_times_df()

        valid_row_indices = (start_date <= times_df['Date']) & (times_df['Date'] < stop_date) & (times_df['Client name'] == client_name)
        self.query_result_df = times_df.loc[valid_row_indices]

    def _extract_start_and_stop_date_from_snapshot_dict(self, snapshot_dict):
        start_date_string = snapshot_dict['comboBox_times_query_start_month'] + ' ' + str(snapshot_dict['comboBox_times_query_start_year'])
        start_date = datetime.datetime.strptime(start_date_string, '%B %Y')

        stop_date_string = snapshot_dict['comboBox_times_query_stop_month'] + ' ' + str(snapshot_dict['comboBox_times_query_stop_year'])
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
        displayed_query_result_df['Date'] = displayed_query_result_df['Date'].dt.strftime(self.DATE_FORMAT)
        self.signals.display_times_query_df_in_tableview_signal.emit(displayed_query_result_df)

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
            self.query_result_df = self.query_result_df.sort_values(by=['Date'])

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
        export_filename = 'export_times_query_results_{}.tsv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
        user_directory = self.params.user_directory
        export_path = os.path.join(user_directory, export_filename)
        self.query_result_df.to_csv(export_path, sep='\t', index=False, date_format=self.DATE_FORMAT)