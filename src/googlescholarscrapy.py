#coding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time

'''
    Google scholar scrapy
'''




##################################
if __name__ == '__main__':
    print 'begin'

    domain_url = ''

    # basic_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0,5&start=10&q=GINKGO+FOLIUM'
    basic_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0,5'

    search_items = ['GINKGO FOLIUM']

    # data file
    data_file = 'google_scholar_data.txt'
    # browser
    browser = webdriver.Firefox()

    #
    with open(data_file, 'w') as out_file:

        #
        for search_item in search_items:
            # split the item with space to create the query condition
            items = search_item.split(' ')
            if items == None:
                continue

            # combine the key words to get the query conditons
            search_url = basic_url + '&q='
            for it_str in items:
                search_url += it_str + '+'
            # remove the last + char
            search_url.rstrip('+')
            print search_url

            # page number
            page_number = 0

            # get the contents of query result
            while(True):
                # add the page number to search url
                search_url += '&start=' + str(page_number * 10)
                # get the search result
                browser.get(search_url)

                # contents
                pageSource = browser.page_source
                if pageSource == None:
                    continue

                # to bs4
                page_obj = BeautifulSoup(pageSource)

                # find the gs_fl div
                div_items = page_obj.find_all('div',{'class':'gs_ri'})
                # check the last page of search result
                if div_items == None or len(div_items) == 0:
                    print 'last page'
                    break

                # not the last page
                for div_item in div_items:
                    result_str = ''
                    if div_item.a:
                        print div_item.get_text(), '-----', div_item.a['href']
                        result_str = div_item.get_text().encode('utf-8') + '-----' + str(div_item.a['href'])
                    else:
                        print div_item.get_text()
                        result_str = div_item.get_text().encode('utf-8')

                    print '----------------'

                    out_file.write(result_str + '\n')




                print 'current page:', page_number
                page_number += 1

                time.sleep(5)



                # exit()



    print 'end'

    # clean the browser
    browser.close()
    del browser