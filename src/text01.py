# coding:utf-8
import requests
from bs4 import BeautifulSoup
import time

# https://scholar.google.com/scholar?start=710&q=GINKGO+FOLIUM&hl=en&as_sdt=0,5

# url string
basic_url = 'https://scholar.google.com/scholar?q=GINKGO+FOLIUM&hl=en&as_sdt=0,5&start='

# page_num = 0
page_num = 25
while(True):

    url = basic_url + str(page_num * 10)

    r = requests.get(url=url)

    print r.text

    bs_obj = BeautifulSoup(r.text)

    # find the gs_fl div
    div_items = bs_obj.find_all('div', {'class': 'gs_ri'})
    # check the last page of search result
    if div_items == None or len(div_items) == 0:
        print 'last page'
        break

    # not the last page
    for div_item in div_items:
        result_str = ''
        if div_item.a:
            # print div_item.get_text(), '-----', div_item.a['href']
            result_str = div_item.get_text().encode('utf-8') + '-----' + str(div_item.a['href'])
        else:
            # print div_item.get_text()
            result_str = div_item.get_text().encode('utf-8')

        print result_str
        print '----------------'

    print 'current page:', str(page_num)
    page_num += 1
    exit()

    r.close()
    time.sleep(10)
