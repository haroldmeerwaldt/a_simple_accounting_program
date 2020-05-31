import openpyxl
import numpy as np

class InvoicesFromTemplate:
    def __init__(self, times, clients, invoices, params):
        self.times = times
        self.clients = clients
        self.invoices = invoices
        self.params = params
        self.template_workbook = openpyxl.load_workbook(params.invoice_template_path)
        self.template_worksheet = self.template_workbook.get_sheet_by_name('Template')
        self._generate_cell_addresses_from_template_dict()

    def _generate_cell_addresses_from_template_dict(self):
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


    def generate_invoice(self, invoice_dict):
        print(invoice_dict)
        # copy cell style
        # if cell.has_style:
        #     new_cell._style = copy(cell._style)