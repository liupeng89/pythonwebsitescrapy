# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
import codecs
from selenium import webdriver
import time

class TCMDictionaryScrapy:

    def __init__(self):
        pass


    def __del__(self):
        pass


######################################################
if __name__ == '__main__':

    # basic url
    urls = 'http://tool.zyy123.com/yaodian/index.html'

    # textFile = open('tcmdictionary.txt', 'w', 'utf-8')
    # with
    textFile = codecs.open('tcmdictionary.txt', 'w+')
    # browser = webdriver.Firefox()
    # 1 - 487 TCMs
    for index in range(138, 488):
        print index

        # url
        url = urls.replace('index', str(index))
        print url

        # get page_ source
        page_source = urllib2.urlopen(url)

        # browser.get(str(url))
        # page_source = browser.page_source
        if page_source == None:
            print 'Not open page '
            continue
        # beautiful soup
        bsObj = BeautifulSoup(page_source.read(), 'lxml')

        if bsObj == None:
            print 'No bs object'
            continue

        # parser
        # print bsObj
        title = bsObj.find('p', {'class':'s_ioc1'})
        # print title.get_text().encode('utf-8').strip()
        titleStr = title.get_text().encode('utf8').strip()

        #content
        content = bsObj.find('div', {'class':'response_ans'})
        # print content.get_text().encode('utf-8').strip()
        contentStr = content.get_text().encode('utf8').strip()
        # print type(contentStr)

        #write to file
        # json = {'Title':titleStr, 'Content':contentStr}
        # textFile.write(str(json).decode('utf-8') + '\n')
        jsonStr = '{"Title":"' + titleStr + '","Content":"' + contentStr + '"}'
        # print type(jsonStr)
        textFile.write(jsonStr + '\n')
        # print jsonStr

        #clean

        # time.sleep(4)


    print 'end!'
    textFile.close()
    # del browser