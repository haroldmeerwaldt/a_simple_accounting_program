import datetime

from modules.utilities import toolbox

from PySide2 import QtCore


class Widgets:

    def __init__(self, ui, DATE_FORMAT):
        self.DATE_FORMAT = DATE_FORMAT
        qt_widget_dict = vars(ui)
        self._widget_dict = dict()
        for widget_name, qt_widget in qt_widget_dict.items():
            if 'pushButton' in widget_name:
                self._widget_dict[widget_name] = PushbuttonWidget(qt_widget)
            elif 'comboBox' in widget_name:
                self._widget_dict[widget_name] = ComboboxWidget(qt_widget)
            elif widget_name in ['lineEdit_times_date', 'lineEdit_invoices_invoice_date']:
                self._widget_dict[widget_name] = LineeditTimesDateWidget(qt_widget, date_format=DATE_FORMAT)
            elif 'lineEdit' in widget_name:
                self._widget_dict[widget_name] = LineeditWidget(qt_widget)
            elif 'info_label' in widget_name:
                self._widget_dict[widget_name] = InfolabelWidget(qt_widget)
            elif 'radioButton' in widget_name:
                self._widget_dict[widget_name] = RadiobuttonWidget(qt_widget)
            elif 'tableView' in widget_name:
                self._widget_dict[widget_name] = TableviewWidget(qt_widget)

    def get_widget_value_dict(self, widget_name_list):
        widget_value_dict = dict()
        for widget_name in widget_name_list:
            widget_value_dict[widget_name] = self._widget_dict[widget_name].get_value()

        return widget_value_dict

    def set_widget_values_using_dict(self, widget_value_dict):
        for widget_name, value in widget_value_dict.items():
            self.set_widget_value(widget_name, value)

    def get_widget(self, widget_name):
        return self._widget_dict[widget_name]

    def get_widget_value(self, widget_name):
        widget = self.get_widget(widget_name)
        return widget.get_value()

    def set_widget_value(self, widget_name, value):
        widget = self.get_widget(widget_name)
        widget.set_value(value)

    def set_allowed_widget_values(self, widget_name, value_list):
        widget = self.get_widget(widget_name)
        widget.set_allowed_values(value_list)

    def get_times_date_as_object(self):
        date = self.get_widget_value('lineEdit_times_date')
        # date_object = datetime.datetime.strptime(date_string, self.DATE_FORMAT)
        return date

    def get_tableview_df_row_as_dict(self, tableview_name, row_number):
        tableview_widget = self.get_widget(tableview_name)
        row_dict = tableview_widget.get_df_row_as_dict(row_number)
        return row_dict


class Widget:
    def __init__(self, qt_widget):
        self.qt_widget = qt_widget
        self.name = qt_widget.objectName()


class PushbuttonWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)


class ComboboxWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self.qt_widget.currentData()

    def set_value(self, value):
        current_index = self._find_data(value)
        self.qt_widget.setCurrentIndex(current_index)

    def _find_data(self, data): # the findData method belonging to QComboBox does not work as expected: https://stackoverflow.com/questions/34024525/why-doesnt-qcombobox-finddata-accept-an-object-as-input
        for index in range(self.qt_widget.count()):
            if self.qt_widget.itemData(index) == data:
                return index
        return -1

    def set_allowed_values(self, value_list):
        self.qt_widget.clear()
        for value in value_list:
            if self._find_data(value) == -1:
                self.qt_widget.addItem(str(value), value)



class LineeditTimesDateWidget(Widget):
    def __init__(self, *args, date_format=None):
        super().__init__(*args)
        self.date_format = date_format

    def get_value(self):
        text = self.qt_widget.text()
        value = datetime.datetime.strptime(text, self.date_format)
        return value

    def set_value(self, value):
        return self.qt_widget.setText(str(value))


class LineeditWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self.qt_widget.text()

    def set_value(self, value):
        return self.qt_widget.setText(str(value))


class InfolabelWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        return self.qt_widget.setText(str(value))


class RadiobuttonWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def get_value(self):
        return self.qt_widget.isChecked()

    def set_value(self, value):
        return self.qt_widget.setChecked(value)


class TableviewWidget(Widget):
    def __init__(self, *args):
        super().__init__(*args)

    def set_value(self, value_df):
        self._value_df = value_df
        model = toolbox.PandasModel(value_df)
        self.qt_widget.setModel(model)

    def get_value(self):
        return self._value_df

    def get_df_row_as_dict(self, row_number):
        row_series = self._value_df.iloc[row_number, :]
        row_dict = row_series.to_dict()
        return row_dict