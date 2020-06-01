import copy
import os
import openpyxl
import numpy as np

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


    def generate_invoice(self, invoice_dict):
        print(invoice_dict)
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
                    # new_cell._style = copy.copy(cell._style)
                    new_cell.font = copy.copy(cell.font)
                    new_cell.border = copy.copy(cell.border)
                    new_cell.fill = copy.copy(cell.fill)
                    new_cell.number_format = copy.copy(cell.number_format)
                    new_cell.protection = copy.copy(cell.protection)
                    new_cell.alignment = copy.copy(cell.alignment)



        invoice_filename_info_list = ['Client name', 'Month', 'Year']
        invoice_filename = '_'.join([str(invoice_dict[key]) for key in invoice_filename_info_list])
        invoice_filename = invoice_filename + '_' + invoice_dict['Invoice date'].strftime('%Y%m%d') + '.xlsx'
        invoice_path = os.path.join(self.params.user_directory, invoice_filename)
        print(invoice_path)
        invoice_workbook.save(invoice_path)

        # copy cell style
        # if cell.has_style:
        #     new_cell._style = copy(cell._style)