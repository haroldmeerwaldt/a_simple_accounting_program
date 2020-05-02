import os
import pandas as pd
import sys

from PySide2 import QtWidgets

from modules.applications import asap_application


class Parameters:
    DATE_FORMAT = "%d-%m-%Y"
    def __init__(self):
        self._get_input_file_constants()
        self._get_times_info_structure()


    def _get_input_file_constants(self):
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

    def _get_times_info_structure(self):
        self.times_info_structure_df = pd.read_csv(self.times_info_structure_path, sep='\t')

    def get_times_info_structure_df_itertuples(self):
        return self.times_info_structure_df.itertuples()


def main():
    print('Starting up program, this may take a few seconds ...')

    params = Parameters()

    q_application = QtWidgets.QApplication(sys.argv)
    main_application = asap_application.ASAPApplication(params)
    main_application.show()



    q_application.exec_()



if __name__ == '__main__':
    print(sys.executable)
    main()