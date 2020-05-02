from PySide2 import QtCore
import functools
import inspect
import sys
import traceback
import threading

class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
                # return self._data.iloc[index.row(), index.column()]
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

def print_when_called_and_return_exception_inside_thread(decorated_function):
    @functools.wraps(decorated_function)
    def wrapper(*args, **kwargs):
        calling_frame = inspect.stack()[1]
        filename = calling_frame.filename
        line_number = calling_frame.lineno

        module = decorated_function.__module__
        function_name = decorated_function.__name__

        current_thread = threading.current_thread()
        thread = '{} ({})'.format(current_thread.name, current_thread.ident)

        argument_names = decorated_function.__code__.co_varnames
        parameters = dict(
            args=dict(zip(argument_names, args)),
            kwargs=kwargs)

        print('>>>> File "{}", line {}, in {}'.format(filename, line_number, module), end=', ')
        print_dict = {'function_name': function_name,
                      'thread': thread,
                      **parameters}
        print(', '.join(['{}={}'.format(str(k), repr(v)) for k, v in print_dict.items()]))

        try:
            out = decorated_function(*args, **kwargs)
            print('<<<< Function executed successfully with result: {}'.format(out))
            return out
        except Exception:
            # type, value, tb = sys.exc_info()
            # traceback.print_tb(tb)
            exc_info = sys.exc_info()
            stack = traceback.extract_stack()
            tb = traceback.extract_tb(exc_info[2])
            full_tb = stack[:-1] + tb
            exc_line = traceback.format_exception_only(*exc_info[:2])
            print("Traceback (most recent call last):")
            print("".join(traceback.format_list(full_tb)), end='')
            print("".join(exc_line))



    return wrapper