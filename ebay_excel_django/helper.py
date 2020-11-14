from bs4 import BeautifulSoup
import requests

def make_urls(names, ebayStore):

    if ebayStore is None:
        ebayStore = "probstein123" #pwcc_auctions

    url = f"https://www.ebay.com/sch/m.html?_odkw=&Grade=10&_ssn={ebayStore}&_armrs=1&LH_Complete=1&_dcat=212&LH_Sold=1&_osacat=212&_from=R40&_trksid=p2046732.m570.l1313&_sacat=212&_ipg=200&_nkw="

    urls = []

    for name in names:
        devUrl = url + name.replace(" ", "+")
        urls.append(devUrl)
        for x in range(2, 5):
            urls.append(devUrl + f'&_pgn={x}')


    #href="https://www.ebay.com/sch/Sports-Trading-Cards/212/m.html?Grade=10&_ssn=probstein123&_armrs=1&LH_Complete=1&_dcat=212&LH_Sold=1&_from=R40&_nkw=_pgn=2&_skc=200&rt=nc"
    #https://www.ebay.com/sch/m.html?_odkw=&_ssn=probstein123&Grade=10&_armrs=1&LH_Complete=1&_dcat=212&LH_Sold=1&_osacat=212&_from=R40&_trksid=p2046732.m570.l1313&_nkw=2020+Mosaic+Justin+Herbert+Silver+Prizm+PSA+10&_sacat=212

    return urls

def ebay_scrape(urls, worksheet):
    worksheet.title = 'Ebay Sheet'

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
            #print(date)

            global_sheet_count += 1

            worksheet.write(global_sheet_count, 0, name)
            worksheet.write(global_sheet_count, 1, price)
            worksheet.write(global_sheet_count, 2, date)

        if soup.find("a", {"aria-label": f"{x + 2} Pagination for search results"}) == None:
            break

    return worksheet

