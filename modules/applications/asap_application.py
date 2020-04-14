from PySide2 import QtWidgets
from modules.GUI_layouts import asap_layout
from modules.utilities import toolbox
import pandas as pd


class ASAPApplication(QtWidgets.QMainWindow):
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