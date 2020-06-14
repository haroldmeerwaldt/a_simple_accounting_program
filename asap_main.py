import os
import sys

import pandas as pd
from PySide2 import QtWidgets

from modules.applications import asap_application


class Parameters:
    DATE_FORMAT = "%d-%m-%Y"
    subdirectory_dict = {'backup_directory': 'backups', 'invoices_directory': 'invoices', 'exports_directory': 'exports'}

    def __init__(self):
        self._generate_user_directories()
        self._generate_input_file_constants()
        self._generate_info_structure_dfs()
        self._generate_data_filenames()

    def _generate_user_directories(self):
        self.user_directory = os.path.expanduser('~/ASAP')
        if not os.path.exists(self.user_directory):
            os.makedirs(self.user_directory)

        for attribute, folder_name in self.subdirectory_dict.items():
            self._generate_subdirectory(attribute, folder_name)

    def _generate_subdirectory(self, attribute, folder_name):
        setattr(self, attribute, os.path.join(self.user_directory, folder_name))
        if not os.path.exists(getattr(self, attribute)):
            os.makedirs(getattr(self, attribute))

    def _generate_input_file_constants(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        input_file_constants_directory = os.path.join(current_directory, 'input_files')
        input_file_constants_path = os.path.join(input_file_constants_directory, 'input_file_constants.tsv')
        input_file_constants_df = pd.read_csv(input_file_constants_path, sep='\t')
        for row in input_file_constants_df.itertuples():
            if 'path' in row.parameter:
                value = os.path.abspath(os.path.join(input_file_constants_directory, row.value))
            else:
                value = row.value
            setattr(self, row.parameter, value)

    def _generate_info_structure_dfs(self):
        self.times_info_structure_df = pd.read_csv(self.times_info_structure_path, sep='\t')
        self.clients_info_structure_df = pd.read_csv(self.clients_info_structure_path, sep='\t')
        self.invoices_info_structure_df = pd.read_csv(self.invoices_info_structure_path, sep='\t')
        self.calculations_info_structure_df = pd.read_csv(self.calculations_info_structure_path, sep='\t')

    def _generate_data_filenames(self):
        self.times_filename = os.path.join(self.user_directory, 'times.xlsx')
        self.clients_filename = os.path.join(self.user_directory, 'clients.xlsx')
        self.invoices_filename = os.path.join(self.user_directory, 'invoices.xlsx')

    def get_times_info_structure_df_itertuples(self):
        return self.times_info_structure_df.itertuples()

    def get_clients_info_structure_df_itertuples(self):
        return self.clients_info_structure_df.itertuples()

    def get_invoices_info_structure_df_itertuples(self):
        return self.invoices_info_structure_df.itertuples()

    def get_calculations_info_structure_df_itertuples(self):
        return self.calculations_info_structure_df.itertuples()



def main():
    print('Starting up program, this may take a few seconds ...')

    params = Parameters()
    q_application = QtWidgets.QApplication(sys.argv)
    main_application = asap_application.ASAPApplication(params)

    main_application.show()
    q_application.exec_()

if __name__ == '__main__':
    main()