from PySide2 import QtWidgets, QtCore
from modules.GUI_layouts import asap_layout
from modules.utilities import toolbox
from modules.worker_thread import background_execution
import pandas as pd


class ASAPApplication(QtWidgets.QMainWindow):
    test_signal = QtCore.Signal(str)
    def __init__(self):
        super().__init__()
        self._initialize_user_interface()

    def _initialize_user_interface(self):
        self.ui = asap_layout.Ui_MainWindow()
        self.ui.setupUi(self)
        print(vars(self.ui))

        df = pd.DataFrame({'a': [2, 4], 'b': [3, 5]})

        model = toolbox.PandasModel(df)

        self.ui.tableView.setModel(model)

        self._initialize_background_execution_thread()

        self._connect_buttons_to_slots()

    def _initialize_background_execution_thread(self):
        self.background_execution_thread = QtCore.QThread()
        self.background_execution = background_execution.BackgroundExecution()
        self.background_execution.moveToThread(self.background_execution_thread)
        self.background_execution_thread.start()

    def _connect_buttons_to_slots(self):
        self.ui.pushButton_add_working_day.clicked.connect(lambda x: self.background_execution.test('this is a test'))

    def closeEvent(self, event):
        self.background_execution_thread.quit()
        self.deleteLater()

