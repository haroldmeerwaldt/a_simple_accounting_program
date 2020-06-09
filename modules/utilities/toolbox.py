from PySide2 import QtCore
import functools
import inspect
import sys
import traceback
import threading
import logging

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


class SimpleTime:
    def __init__(self, string=None, hours=None, minutes=None):
        if hours is not None or minutes is not None:
            carry_hours = 0

            try:
                self.minutes = int(minutes)
            except TypeError:
                self.minutes = 0

            while self.minutes > 59:
                self.minutes = self.minutes - 60
                carry_hours = carry_hours + 1

            try:
                self.hours = int(hours + carry_hours)
            except TypeError:
                self.hours = carry_hours
        elif string is not None:
            hours_minutes_list = string.split(':')
            if len(hours_minutes_list) != 2:
                raise ValueError('if a string is provided, it should be in format HH:MM')
            self.hours = int(hours_minutes_list[0])
            self.minutes = int(hours_minutes_list[1])
        else:
            raise ValueError('Either a string in format HH:MM should be provided or hours and minutes as numbers')

    def __add__(self, other):
        carry_hours = 0

        sum_minutes = self.minutes - other.minutes
        while sum_minutes > 59:
            sum_minutes = sum_minutes - 60
            carry_hours = carry_hours + 1

        sum_hours = self.hours + other.hours + carry_hours
        while sum_hours > 23:
            sum_hours = sum_hours - 24

        return SimpleTime(hours=sum_hours, minutes=sum_minutes)


    def __sub__(self, other):
        delta_hours = self.hours - other.hours
        if delta_hours < 0:
            delta_hours = delta_hours + 24

        delta_minutes = self.minutes - other.minutes
        if delta_minutes < 0:
            delta_minutes = delta_minutes + 60
            delta_hours = delta_hours - 1

        return SimpleTime(hours=delta_hours, minutes=delta_minutes)

    def __str__(self):
        return "{:02d}:{:02d}".format(self.hours, self.minutes)

    def __float__(self):
        return float(self.hours + self.minutes/60)




class QLogHandler(logging.Handler):

    def __init__(self, logging_message_signal, textbrowser):
        super().__init__()

        self.logging_message_signal = logging_message_signal
        self.textbrowser = textbrowser
        self.scrollbar = self.textbrowser.verticalScrollBar()
        self.logging_message_signal.connect(lambda text: self.add_message_to_textbrowser(text))


    def emit(self, record):
        self.logging_message_signal.emit(self.format(record))

    def __repr__(self):
        return f"<{self.__class__.__name__} : {logging.getLevelName(self.level)}>"

    def add_message_to_textbrowser(self, text):
        self.textbrowser.append(text)

        scrollbar_is_at_end = (self.scrollbar.maximum() - self.scrollbar.value()) <= 10
        if scrollbar_is_at_end:
            self.scrollbar.setValue(self.scrollbar.maximum())


