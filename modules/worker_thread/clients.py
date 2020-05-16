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
        print(year_df)
        print(year_df['Index within year'])
        print(year_df['Index within year'].max())
        highest_index = year_df['Index within year'].max()
        if np.isnan(highest_index):
            highest_index = 0
        next_index = highest_index + 1
        return next_index


    def _generate_clients_df_from_input_file(self):
        try:
            self.clients_df = pd.read_csv(self.clients_filename, sep='\t')
        except FileNotFoundError:
            column_list = self.params.clients_info_structure_df['info_name'].tolist()
            self.clients_df = pd.DataFrame(columns=column_list)

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
        df_to_be_added.to_csv(self.clients_filename, sep='\t', mode='a', index=False, header=use_header)
