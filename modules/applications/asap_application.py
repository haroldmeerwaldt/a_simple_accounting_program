from PyQt5 import QtWidgets
from modules.GUI_layouts import asap_layout


class ASAPApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._initialize_user_interface()

    def _initialize_user_interface(self):
        self.ui = asap_layout.Ui_MainWindow()
        self.ui.setupUi(self)
        print(vars(self.ui))