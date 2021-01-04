from bs4 import BeautifulSoup
import requests
from datetime import datetime

def make_urls(names, ebayStore=None, fromCsv=False):

    if ebayStore is None:
        ebayStore = "probstein123" #pwcc_auctions

    #Search Paramters
    grade = "10"
    completed = "1"
    sold = "1"

    if fromCsv:
        url = f"https://www.ebay.com/sch/m.html?_odkw=&" \
          f"Grade=10&" \
          f"_ssn={ebayStore}&" \
          f"_armrs=1&" \
          f"LH_Complete=1&" \
          f"_dcat=212&" \
          f"LH_Sold=1&" \
          f"_osacat=212&" \
          f"_from=R40&" \
          f"_trksid=p2046732.m570.l1313&" \
          f"_sacat=212&" \
          f"_ipg=200&" \
          f"Player="
    else:
        url = f"https://www.ebay.com/sch/m.html?_odkw=&Grade=10&_ssn={ebayStore}&_armrs=1&LH_Complete=1&_dcat=212&LH_Sold=1&_osacat=212&_from=R40&_trksid=p2046732.m570.l1313&_sacat=212&_ipg=200&_nkw="

    urls = []


    #https://www.ebay.com/sch/Sports-Trading-Cards/212/m.html?Grade=10&_ssn=probstein123&_armrs=1&LH_Complete=1&LH_Sold=1&_from=R40&_ipg=200&_dcat=212&rt=nc&LH_AllListings=1&Player=LeBron%2520James

    for name in names:

        if fromCsv:
            name = name.replace("\r\n", "")
            devUrl = url + name.replace(" ", "%2520")
        else:
            devUrl = url + name.replace(" ", "+")


        urls.append(devUrl)
        for x in range(2, 5):
            urls.append(devUrl + f'&_pgn={x}')


    #href="https://www.ebay.com/sch/Sports-Trading-Cards/212/m.html?Grade=10&_ssn=probstein123&_armrs=1&LH_Complete=1&_dcat=212&LH_Sold=1&_from=R40&_nkw=_pgn=2&_skc=200&rt=nc"
    #https://www.ebay.com/sch/m.html?_odkw=&_ssn=probstein123&Grade=10&_armrs=1&LH_Complete=1&_dcat=212&LH_Sold=1&_osacat=212&_from=R40&_trksid=p2046732.m570.l1313&_nkw=2020+Mosaic+Justin+Herbert+Silver+Prizm+PSA+10&_sacat=212

    return urls

def ebay_scrape(urls, worksheet, start_date = None, end_date = None):
    worksheet.title = 'Ebay Sheet'
    worksheet.name = 'EbaySheet'

    worksheet.write(0, 0, "Title")
    worksheet.write(0, 1, "Price")
    worksheet.write(0, 2, "Date")

    global_sheet_count = 0

    for x, url in enumerate(urls):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        results = soup.findAll("li", {"class": "sresult lvresult clearfix li"})

        for idx, result in enumerate(results):
            name = result.find("h3", {"class": "lvtitle"}).text
            #print(name)

            price = result.find("li", {"class": "lvprice prc"}).text
            #print(price)

            date = result.find("li", {"class": "timeleft"}).text

            if start_date is not None:
                datelist = date.split(" ")
                dateParsed = datelist[0].replace("-", " ")
                dateParsed = dateParsed.replace('\n', '')

                values = dateParsed.startswith('J', 0, 1)

                if dateParsed.startswith('J', 0, 1):
                    dateParsed = dateParsed + " 2021"
                else:
                    dateParsed = dateParsed + " 2020"


                dateParsed = datetime.strptime(dateParsed, '%b %d %Y')

                if dateParsed < start_date or dateParsed > end_date:
                    break

            global_sheet_count += 1

            worksheet.write(global_sheet_count, 0, name)
            worksheet.write(global_sheet_count, 1, price)
            worksheet.write(global_sheet_count, 2, date)

        if soup.find("a", {"aria-label": f"{x + 2} Pagination for search results"}) == None:
            break

    return worksheet

