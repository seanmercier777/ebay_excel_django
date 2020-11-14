from django.shortcuts import render
import io
from django.http import HttpResponse
import xlsxwriter
from ebay_excel_django.helper import *

def index(request):
    return render(request, "index.html")

def generate_results_table(request):
    keyword = request.GET.get('keywords')
    store = request.GET.get('store')

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet = workbook.add_worksheet()

    #This retreives the data
    ebay_scrape(make_urls([keyword], store), worksheet)

    # close workbook
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return response



