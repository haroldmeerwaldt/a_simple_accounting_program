from PySide2 import QtCore
from modules.utilities import toolbox

class BackgroundExecution(QtCore.QObject):
    def __init__(self):
        super().__init__()
        print('in background execution')

    @toolbox.print_when_called_and_return_exception_inside_thread
    def test(self, string):
        print(string)
