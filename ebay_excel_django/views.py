from django.shortcuts import render
import io
from django.http import HttpResponse
import xlsxwriter
from ebay_excel_django.helper import *



def index(request):
    return render(request, "index.html")




def generate_results_table(request):

    #keyword = request.GET['keywords']
    keyword = 'michael'

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet = workbook.add_worksheet()

    #This retreives the data
    #ebay_scrape(make_urls(request.GET['keywords']))
    ebay_scrape(make_urls(keyword), worksheet)
    #worksheet.write(2, 1, 3)# Row, Column, Value # Starts at zero

    # close workbook
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return response




# def generate_results_table(request):
#     keywords = request.GET['keywords'])
#     output = io.BytesIO()
#     workbook = xlsxwriter.Workbook(output)
#
#     worksheet = workbook.add_worksheet()
#
#
#     #result = ebay_scrape(make_urls(request.GET['keywords']))
#
#     response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#
#     return response




#
# def get_simple_table_data():
#     # Simulate a more complex table read.
#     return [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]


#This version works
# def generate_results_table(request):
#     output = io.BytesIO()
#     workbook = xlsxwriter.Workbook(output)
#
#     worksheet = workbook.add_worksheet()
#     worksheet.write(2, 1, 3)
#
#     # close workbook
#     workbook.close()
#     output.seek(0)
#     response = HttpResponse(output.read(),
#                             content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#     return response

