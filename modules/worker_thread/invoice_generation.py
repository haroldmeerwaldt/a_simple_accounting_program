import datetime
import copy
import os
import openpyxl
import numpy as np
from modules.utilities import toolbox

class InvoicesFromTemplate:
    def __init__(self, times, clients, invoices, params):
        self.times = times
        self.clients = clients
        self.invoices = invoices
        self.params = params
        self.template_workbook = openpyxl.load_workbook(params.invoice_template_path)
        self.worksheet_name = self.template_workbook.sheetnames[0]
        self.template_worksheet = self.template_workbook.get_sheet_by_name(self.worksheet_name)
        self._generate_cell_addresses_from_template_dict()

    def _generate_cell_addresses_from_template_dict(self):
        print('times')
        self.times_cell_coordinate_dict = dict()
        for info_structure_row in self.params.get_times_info_structure_df_itertuples():
            info_name = info_structure_row.info_name
            invoice_template_tag = info_structure_row.invoice_template_tag
            if isinstance(invoice_template_tag, str):
                for row in range(1, self.template_worksheet.max_row + 1):
                    for col in range(1, self.template_worksheet.max_column + 1):
                        cell = self.template_worksheet.cell(row=row, column=col)
                        if cell.value == invoice_template_tag:
                            self.times_cell_coordinate_dict[info_name] = cell.coordinate
                            print(info_name, self.times_cell_coordinate_dict[info_name])

        print('clients')
        self.clients_cell_coordinate_dict = dict()
        for info_structure_row in self.params.get_clients_info_structure_df_itertuples():
            info_name = info_structure_row.info_name
            invoice_template_tag = info_structure_row.invoice_template_tag
            if isinstance(invoice_template_tag, str):
                for row in range(1, self.template_worksheet.max_row + 1):
                    for col in range(1, self.template_worksheet.max_column + 1):
                        cell = self.template_worksheet.cell(row=row, column=col)
                        if cell.value == invoice_template_tag:
                            self.clients_cell_coordinate_dict[info_name] = cell.coordinate
                            print(info_name, self.clients_cell_coordinate_dict[info_name])

        print('invoices')
        self.invoices_cell_coordinate_dict = dict()
        for info_structure_row in self.params.get_invoices_info_structure_df_itertuples():
            info_name = info_structure_row.info_name
            invoice_template_tag = info_structure_row.invoice_template_tag
            if isinstance(invoice_template_tag, str):
                for row in range(1, self.template_worksheet.max_row + 1):
                    for col in range(1, self.template_worksheet.max_column + 1):
                        cell = self.template_worksheet.cell(row=row, column=col)
                        if cell.value == invoice_template_tag:
                            self.invoices_cell_coordinate_dict[info_name] = cell.coordinate
                            print(info_name, self.invoices_cell_coordinate_dict[info_name])

        print('calculations')
        self.calculated_cell_coordinate_dict = dict()
        for info_structure_row in self.params.get_calculations_info_structure_df_itertuples():
            info_name = info_structure_row.info_name
            invoice_template_tag = info_structure_row.invoice_template_tag
            if isinstance(invoice_template_tag, str):
                for row in range(1, self.template_worksheet.max_row + 1):
                    for col in range(1, self.template_worksheet.max_column + 1):
                        cell = self.template_worksheet.cell(row=row, column=col)
                        if cell.value == invoice_template_tag:
                            self.calculated_cell_coordinate_dict[info_name] = cell.coordinate
                            print(info_name, self.calculated_cell_coordinate_dict[info_name])



    @toolbox.print_when_called_and_return_exception_inside_thread
    def generate_invoice(self, invoice_dict):
        print('invoice_dict', invoice_dict)
        invoice_workbook = openpyxl.Workbook()
        blank_worksheet_name = invoice_workbook.sheetnames[0]
        blank_worksheet = invoice_workbook.get_sheet_by_name(blank_worksheet_name)
        invoice_workbook.remove_sheet(blank_worksheet)
        invoice_worksheet = invoice_workbook.create_sheet(self.worksheet_name) # todo get somewhere else

        for row in range(1, self.template_worksheet.max_row + 1):
            for col in range(1, self.template_worksheet.max_column + 1):
                cell = self.template_worksheet.cell(row=row, column=col)
                new_cell = invoice_worksheet.cell(row=row, column=col)
                new_cell.value = cell.value
                if cell.has_style:
                    new_cell.font = copy.copy(cell.font)
                    new_cell.border = copy.copy(cell.border)
                    new_cell.fill = copy.copy(cell.fill)
                    new_cell.number_format = copy.copy(cell.number_format)
                    new_cell.protection = copy.copy(cell.protection)
                    new_cell.alignment = copy.copy(cell.alignment)

        print('substituting')
        client_name = invoice_dict['Client name']
        client_info_dict = self.clients.get_client_info_dict_based_on_client_name(client_name)

        invoice_month = invoice_dict['Month']
        invoice_year = invoice_dict['Year']

        print('before start date')
        start_date, stop_date = self._extract_start_and_stop_date_from_month_and_year(invoice_month, invoice_year)
        print('after start date')
        full_times_df = self.times.get_times_df()
        valid_row_indices = (start_date <= full_times_df['Date']) & (full_times_df['Date'] < stop_date) & (full_times_df['Client name'] == client_name)
        invoice_times_df = full_times_df.loc[valid_row_indices]
        print('invoice_times_df', invoice_times_df)

        for key, val in invoice_dict.items():
            print(key)
            try:
                coordinate = self.invoices_cell_coordinate_dict[key]
                print(coordinate)
                cell = invoice_worksheet[coordinate]
                cell.value = val
            except KeyError:
                pass

        for key, val in client_info_dict.items():
            print(key)
            try:
                coordinate = self.clients_cell_coordinate_dict[key]
                print(coordinate)
                cell = invoice_worksheet[coordinate]
                cell.value = val
            except KeyError:
                pass

        for index, row in invoice_times_df.iterrows():
            print('row', row)
            for key, val in row.iteritems():
                try:
                    coordinate = self.times_cell_coordinate_dict[key]
                    print(coordinate)
                    cell = invoice_worksheet[coordinate]
                    cell.value = val
                except KeyError:
                    pass

        def set_calculated_value(info_name, value):
            coordinate = self.calculated_cell_coordinate_dict[info_name]
            cell = invoice_worksheet[coordinate]
            cell.value = value

        set_calculated_value('Calculated hours', '=24*({}-{})'.format(self.times_cell_coordinate_dict['Stop time'], self.times_cell_coordinate_dict['Start time']))
        if True:  #todo differentiate different types of work
            set_calculated_value('Calculated amount for hours', '={}*{}'.format(self.invoices_cell_coordinate_dict['Rate during day (euro/h)'], self.calculated_cell_coordinate_dict['Calculated hours']))

        set_calculated_value('Calculated amount for commute', '={}*{}'.format(self.invoices_cell_coordinate_dict['Compensation for commute (euro/km)'], self.times_cell_coordinate_dict['Commute (km)']))
        set_calculated_value('Calculated amount for distance during work', '={}*{}'.format(self.invoices_cell_coordinate_dict['Compensation for driving during work (euro/km)'], self.times_cell_coordinate_dict['Distance during work (km)']))
        set_calculated_value('Calculated amount for working day', '={}+{}+{}'.format(self.calculated_cell_coordinate_dict['Calculated amount for hours'], self.calculated_cell_coordinate_dict['Calculated amount for commute'], self.calculated_cell_coordinate_dict['Calculated amount for distance during work']))

        set_calculated_value('Calculated total amount', '={}'.format(self.calculated_cell_coordinate_dict['Calculated amount for working day']))

        invoice_filename_info_list = ['Client name', 'Month', 'Year']
        invoice_filename = '_'.join([str(invoice_dict[key]) for key in invoice_filename_info_list])
        invoice_filename = invoice_filename + '_' + invoice_dict['Invoice date'].strftime('%Y%m%d') + '.xlsx'
        invoice_path = os.path.join(self.params.user_directory, invoice_filename)
        print(invoice_path)
        invoice_workbook.save(invoice_path)

        # copy cell style
        # if cell.has_style:
        #     new_cell._style = copy(cell._style)

    def _extract_start_and_stop_date_from_month_and_year(self, month, year):
        date_string = month + ' ' + str(year)
        start_date = datetime.datetime.strptime(date_string, '%B %Y')

        stop_date = datetime.datetime.strptime(date_string, '%B %Y')
        stop_date_month = stop_date.month
        stop_date_year = stop_date.year
        if stop_date_month == 12:
            stop_date_month = 1
            stop_date_year = stop_date_year + 1
        else:
            stop_date_month = stop_date_month + 1
        stop_date = datetime.datetime(year=stop_date_year, month=stop_date_month, day=1, hour=0, minute=0, second=0)
        return start_date, stop_date
