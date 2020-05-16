import datetime
import os

import pandas as pd

from modules.utilities import toolbox


class Clients:
    def __init__(self, signals, params):
        self.signals = signals
        self.params = params
        self.clients_filename = params.clients_filename
        self._generate_clients_df_from_input_file()

    def _generate_clients_df_from_input_file(self):
        try:
            self.clients_df = pd.read_csv(self.clients_filename, sep='\t')
        except FileNotFoundError:
            column_list = self.params.clients_info_structure_df['info_name'].tolist()
            self.clients_df = pd.DataFrame(columns=column_list)

    @toolbox.print_when_called_and_return_exception_inside_thread
    def add_working_day_from_dict(self, widget_value_dict):
        dict_to_be_added = self._generate_dict_to_be_added_from_widget_value_dict(widget_value_dict)
        dict_to_be_added['UID'] = self._generate_UID(dict_to_be_added)
        self._add_working_day_in_memory(dict_to_be_added)
        self._add_working_day_to_file(dict_to_be_added)

    def _generate_dict_to_be_added_from_widget_value_dict(self, widget_value_dict):
        dict_to_be_added = dict()
        for row in self.params.get_clients_info_structure_df_itertuples():
            info_name = row.info_name
            widget_name = row.widget_name
            dict_to_be_added[info_name] = widget_value_dict[widget_name]
        return dict_to_be_added