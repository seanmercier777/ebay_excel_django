import base64

from django.http import HttpResponse
from django.shortcuts import render
import io
from django.http import HttpResponse
from django.views.generic import View
import xlsxwriter
from ebay_excel_django.helper import *



def index(request):
    return render(request, "index.html")


# def generate_results_table(request):
#     result = ebay_scrape(make_urls(request.GET['keywords']))
#
#     response = HttpResponse(content_type="application/ms-excel")
#     response['Content-Disposition'] = 'attachment; filename=Excel.xls'
#
#     response.write(result.)
#
#     return response





def get_simple_table_data():
    # Simulate a more complex table read.
    return [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


def generate_results_table(request):

    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()

    # Even though the final file will be in memory the module uses temp
    # files during assembly for efficiency. To avoid this on servers that
    # don't allow temp files, for example the Google APP Engine, set the
    # 'in_memory' Workbook() constructor option as shown in the docs.
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Get some data to write to the spreadsheet.
    data = get_simple_table_data()

    # Write some test data.
    for row_num, columns in enumerate(data):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num, col_num, cell_data)

    # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'django_simple.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response