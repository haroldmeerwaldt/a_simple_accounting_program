from PySide2 import QtWidgets, QtCore
from modules.GUI_layouts import asap_layout
from modules.utilities import toolbox
from modules.worker_thread import background_execution
import pandas as pd
import os

class Signals(QtCore.QObject):
    pushbutton_clicked_signal = QtCore.Signal(str, dict)
    def __init__(self):
        super().__init__()



class ASAPApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self._initialize_user_interface()
        self.signals = Signals()
        self._initialize_background_execution_thread()
        self._connect_buttons_to_slots()


    def _initialize_user_interface(self):
        self.ui = asap_layout.Ui_MainWindow()
        self.ui.setupUi(self)
        print(vars(self.ui))

        df = pd.DataFrame({'a': [2, 4], 'b': [3, 5]})

        model = toolbox.PandasModel(df)

        self.ui.tableView.setModel(model)



    def _initialize_background_execution_thread(self):
        self.background_execution_thread = QtCore.QThread()
        self.background_execution = background_execution.BackgroundExecution(self.signals)
        self.background_execution.moveToThread(self.background_execution_thread)
        self.background_execution_thread.start()

    def _connect_buttons_to_slots(self):
        pushbutton_name_dict = {pushbutton_name: pushbutton for pushbutton_name, pushbutton in vars(self.ui).items() if 'pushButton' in pushbutton_name}
        for pushbutton_name, pushbutton in pushbutton_name_dict.items():
            pushbutton.clicked.connect(self._on_pushbutton_clicked)
        # self.ui.pushButton_add_working_day.clicked.connect(lambda x: self.background_execution.test('this is a test'))

        self.signals.pushbutton_clicked_signal.connect(self.background_execution.pushbutton_clicked_slot)

    def _on_pushbutton_clicked(self):
        print('sending')
        pushbutton_name = self.sender().objectName()
        ui_snapshot_dict = self._generate_ui_snapshot_dict()
        self._send_pushbutton_name_and_ui_snapshot_dict_to_background_execution_thread(pushbutton_name, ui_snapshot_dict)

    def _send_pushbutton_name_and_ui_snapshot_dict_to_background_execution_thread(self, pushbutton_name, ui_snapshot_dict):
        self.signals.pushbutton_clicked_signal.emit(pushbutton_name, ui_snapshot_dict)

    def _generate_ui_snapshot_dict(self):
        ui_snapshot_dict = dict()
        for widget_name, widget in vars(self.ui).items():
            if 'comboBox' in widget_name:
                ui_snapshot_dict[widget_name] = widget.currentData() # or .currentText()
        return ui_snapshot_dict


    def closeEvent(self, event):
        self.background_execution_thread.quit()
        self.deleteLater()

