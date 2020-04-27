import os
import pandas as pd

from PySide2 import QtCore

from modules.utilities import toolbox


class BackgroundExecution(QtCore.QObject):
    def __init__(self, signals, params):
        super().__init__()
        print('in background execution')
        self.signals = signals
        self.params = params
        self.times = Times(self.signals, self.params)
        self.times_query = TimesQuery()
        # self.pushbutton_method_dict = {'pushButton_add_working_day': self.times.}


    # @toolbox.print_when_called_and_return_exception_inside_thread
    def pushbutton_clicked_slot(self, pushbutton_name, snapshot_dict):
        print('testing', pushbutton_name, snapshot_dict)

    def pushbutton_add_working_day_clicked_slot(self, snapshot_dict):
        print('testing adding', snapshot_dict)
        self.times.add_dict_to_file(snapshot_dict)





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

    def add_dict_to_file(self, widget_value_dict):
        dict_to_be_added = dict()
        for row in self.params.get_times_info_structure_df_itertuples():
            print(row)
            info_name = row.info_name
            widget_name = row.widget_name
            dict_to_be_added[info_name] = widget_value_dict[widget_name]

        dict_to_be_added['UID'] = self._generate_UID(dict_to_be_added)

        self.times_df = self.times_df.append(dict_to_be_added, ignore_index=True)
        df_to_be_added = pd.DataFrame([dict_to_be_added], columns=self.times_df.columns)
        df_to_be_added.to_csv(self.times_filename, sep='\t', mode='a', index=False)

    def _generate_UID(self, dict_to_be_added):
        list_of_info_in_UID = [dict_to_be_added[key] for key in ['Client', 'Date', 'Start time']]
        UID = '_'.join(list_of_info_in_UID)
        return UID


class TimesQuery:
    def __init__(self):
        pass
