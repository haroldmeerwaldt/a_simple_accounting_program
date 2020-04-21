import os
import pandas as pd

from PySide2 import QtCore

from modules.utilities import toolbox


class BackgroundExecution(QtCore.QObject):
    def __init__(self, signals):
        super().__init__()
        print('in background execution')
        self.signals = signals
        self.times = Times(self.signals)
        # self.pushbutton_method_dict = {'pushButton_add_working_day': self.times.}


    # @toolbox.print_when_called_and_return_exception_inside_thread
    def pushbutton_clicked_slot(self, pushbutton_name, snapshot_dict):
        print('testing', pushbutton_name, snapshot_dict)

    def pushbutton_add_working_day_clicked_slot(self, snapshot_dict):
        print('testing adding', snapshot_dict)





class Times:
    def __init__(self, signals):
        self.signals = signals
        self._load_input_file()

    def _load_input_file(self):
        user_directory = os.path.expanduser('~/ASAP')
        if not os.path.exists(user_directory):
            os.makedirs(user_directory)

        times_filename = os.path.join(user_directory, 'times.tsv')
        try:
            self.times_df = pd.read_csv(times_filename, sep='\t')
        except FileNotFoundError:
            column_list = ['UID', 'Client', 'Date', 'Start time', 'Stop time', 'Hours']
            self.times_df = pd.DataFrame(columns=column_list)


