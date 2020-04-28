import os
import pandas as pd
import datetime
import sys
import traceback

from PySide2 import QtCore

from modules.utilities import toolbox


class BackgroundExecution(QtCore.QObject):
    def __init__(self, signals, params):
        super().__init__()
        print('in background execution')
        self.signals = signals
        self.params = params
        self.times = Times(self.signals, self.params)


    # @toolbox.print_when_called_and_return_exception_inside_thread
    def pushbutton_clicked_slot(self, pushbutton_name, snapshot_dict):
        print('testing', pushbutton_name, snapshot_dict)

    def pushbutton_add_working_day_clicked_slot(self, snapshot_dict):
        print('testing adding', snapshot_dict)
        self.times.add_dict_to_file(snapshot_dict)


    def pushbutton_times_query_clicked_slot(self, pushbutton_name, snapshot_dict):
        if pushbutton_name == 'pushButton_times_query_dates_only':
            self.times.query_dates_only(snapshot_dict)
        elif pushbutton_name == 'pushButton_times_query_client_only':
            self.times.query_client_only(snapshot_dict)
        elif pushbutton_name == 'pushButton_times_query_dates_and_client':
            self.times.query_dates_and_client(snapshot_dict)


class Times:
    def __init__(self, signals, params):
        self.signals = signals
        self.params = params
        self._load_input_file()

    def _load_input_file(self):
        user_directory = os.path.expanduser('~/ASAP')
        if not os.path.exists(user_directory):
            os.makedirs(user_directory)

        self.times_filename = os.path.join(user_directory, 'times.tsv')
        try:
            self.times_df = pd.read_csv(self.times_filename, sep='\t')
        except FileNotFoundError:
            column_list = ['UID'] + self.params.times_info_structure_df['info_name'].tolist()
            self.times_df = pd.DataFrame(columns=column_list)

        self.times_df['Date'] = pd.to_datetime(self.times_df['Date'])

    def add_dict_to_file(self, widget_value_dict):
        dict_to_be_added = dict()
        for row in self.params.get_times_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            dict_to_be_added[info_name] = widget_value_dict[widget_name]

        dict_to_be_added['UID'] = self._generate_UID(dict_to_be_added)

        self.times_df = self.times_df.append(dict_to_be_added, ignore_index=True)
        df_to_be_added = pd.DataFrame([dict_to_be_added], columns=self.times_df.columns)
        use_header = not os.path.exists(self.times_filename)
        df_to_be_added.to_csv(self.times_filename, sep='\t', mode='a', index=False, header=use_header)

    def _generate_UID(self, dict_to_be_added):
        list_of_info_in_UID = [dict_to_be_added[key] for key in ['Client', 'Date', 'Start time']]
        UID = '_'.join(list_of_info_in_UID)
        return UID

    def query_dates_only(self, snapshot_dict):
        print(snapshot_dict)
        try:
            start_date_string = snapshot_dict['comboBox_times_query_start_month'] + ' ' + str(snapshot_dict['comboBox_times_query_start_year'])
            print(start_date_string)
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

            # print(type(start_date), type(stop_date))
            print(start_date_string, start_date, stop_date_string, stop_date)
            print(self.times_df['Date'])
            valid_row_indices = (start_date <= self.times_df['Date']) & (self.times_df['Date'] < stop_date)
            self.query_result_df = self.times_df.loc[valid_row_indices]
            print(self.query_result_df)
            print(len(self.query_result_df))

        except:
            type, value, tb = sys.exc_info()
            traceback.print_tb(tb)





    def query_client_only(self, snapshot_dict):
        pass

    def query_dates_and_client(self, snapshot_dict):
        pass
