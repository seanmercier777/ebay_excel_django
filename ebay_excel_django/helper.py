from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

def make_urls(names):
    url = f"https://www.ebay.com/sch/m.html?_odkw=&Grade=10&_ssn=probstein123&_armrs=1&LH_Complete=1&_dcat=212&LH_Sold=1&_osacat=212&_from=R40&_trksid=p2046732.m570.l1313&_sacat=212&_ipg=10&_nkw="

    urls = []

    for name in names:
        urls.append(url + name.replace(" ", "+"))

    return urls



def ebay_scrape(urls, worksheet):
    worksheet.title = 'Ebay Sheet'
    # worksheet['A1'] = "Title"
    # worksheet['B1'] = "Price"
    # worksheet['C1'] = "Date"

    worksheet.write(0, 0, "Title")
    worksheet.write(0, 1, "Price")
    worksheet.write(0, 2, "Date")

    #return worksheet

    for url in urls:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        results = soup.find("ul", {"id": "ListViewInner"})

        results = soup.findAll("li", {"class": "sresult lvresult clearfix li"})

        for idx, result in enumerate(results):
            name = result.find("h3", {"class": "lvtitle"}).text
            print(name)

            price = result.find("li", {"class": "lvprice prc"}).text
            print(price)

            date = result.find("li", {"class": "timeleft"}).text
            print(date)

            idxToSheet = idx+1

            worksheet.write(idxToSheet, 0, name)
            worksheet.write(idxToSheet, 1, price)
            worksheet.write(idxToSheet, 2, date)

        break


    return worksheet





# def ebay_scrape(urls):
#     workbook = Workbook()
#     sheet = workbook.active
#     sheet.title = 'Ebay Sheet'
#     sheet['A1'] = "Title"
#     sheet['B1'] = "Price"
#     sheet['C1'] = "Date"
#
#     for url in urls:
#         res = requests.get(url)
#         res.raise_for_status()
#         soup = BeautifulSoup(res.text, 'html.parser')
#
#         results = soup.find("ul", {"id": "ListViewInner"})
#
#         results = soup.findAll("li", {"class": "sresult lvresult clearfix li"})
#
#         for idx, result in enumerate(results):
#             name = result.find("h3", {"class": "lvtitle"}).text
#             print(name)
#
#             price = result.find("li", {"class": "lvprice prc"}).text
#             print(price)
#
#             date = result.find("li", {"class": "timeleft"}).text
#             print(date)
#
#             idxToSheet = idx+2
#             sheet[f'A{str(idxToSheet)}'] = name
#             sheet[f'B{str(idxToSheet)}'] = price
#             sheet[f'C{str(idxToSheet)}'] = date
#
#         break
#
#
#     workbook.save(filename="ebay_output.xlsx")
#
#     return workbook
