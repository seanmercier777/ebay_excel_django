from django.core.exceptions import ValidationError
from django.forms import forms
from django.shortcuts import render
import io
from django.http import HttpResponse, HttpResponseRedirect
import xlsxwriter
from django.urls import reverse
from datetime import datetime
from django.core.exceptions import ValidationError





from ebay_excel_django.helper import *


def index(request):
    request.indexActive = 'active'
    return render(request, "index.html", context={'indexActive': 'active'})


def generate_results_table(request):
    keyword = request.GET.get('keywords')
    store = request.GET.get('store')

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet = workbook.add_worksheet()

    # This retreives the data
    ebay_scrape(make_urls([keyword], store), worksheet)

    # close workbook
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return response


def player(request):
    request.indexActive = 'active'
    return render(request, "player.html", context={'playerActive': 'active'})


def player_import(request):
    startDate = request.GET.get('startdate')
    endDate = request.GET.get('enddate')
    csvFile = request.GET.get('file')

    csv_file = request.FILES["file"]

    keyword = request.GET.get('keywords')
    store = request.GET.get('store')

    raise ValidationError(
        ('Invalid value: %(value)s'),
        code='invalid',
        params={'value': '42'},
    )

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet = workbook.add_worksheet()

    # This retreives the data
    ebay_scrape(make_urls([keyword], store), worksheet)

    # close workbook
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return response


def call_player():
    return








def upload_csv(request):
    data = {}
    # if "GET" == request.method:
    #     return render(request, "ebay_excel_django/index.html", data)

    csv_file = request.FILES["csv_file"]
    start_date = request.POST["startdate"]
    end_date = request.POST["enddate"]




    start_date = datetime.strptime(start_date,'%Y-%m-%d')
    end_date = datetime.strptime(end_date,'%Y-%m-%d')



    file_data = csv_file.read().decode("utf-8")

    lines = file_data.split(",")

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet = workbook.add_worksheet()

    ebay_scrape(make_urls(lines, fromCsv=True), worksheet, start_date, end_date)


    # close workbook
    workbook.close()
    output.seek(0)

    return HttpResponse(output.read(),
                 content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


    # return HttpResponse(data_dict,
    #              content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

