from selenium import webdriver
import time
import codecs
import urllib2

from bs4 import BeautifulSoup

class GoogleSeleniumScrapy:

    domains = ['https://patents.google.com/']

    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Firefox()
        # self.driver = webdriver.PhantomJS(executable_path='./phantomjs')

    def __del__(self):
        self.browser.close()
        # self.driver.close()

    # get page based on the parameters and page number
    def get_page(self, parameters, page_number):

        # parse url and parameters
        parameterStr = self.parse_url_string(parameters)

        # get page number
        parameterStr += '&page=' + str(page_number)

        # parse url string
        urlStr = self.url + parameterStr

        # get page from browser
        self.browser.get(str(urlStr))
        # self.driver.get(str(urlStr))

        page_source = self.browser.page_source

        return page_source

    # open page
    # def open_page(self, url):

    #save content to file
    # def save_to_file(self, page_source):
    #
    #     # write to file
    #     content_text = codecs.open("content.txt", "w+", 'utf-8')
    #
    #     content_text.write(page_source)
    #
    #     # print page_source
    #     print 'write end'

    # parse request parameters
    def parse_url_string(self, parameters):
        paramStr = ''
        parametersList = parameters.split(" ")
        index = 0
        for param in parametersList:
            if index == len(parametersList) - 1:
                paramStr += param
            else:
                paramStr += param + '+'
            index += 1
        return paramStr

    # parse the patent search result html
    def parse_search_html(self, page_source):

        html = BeautifulSoup(page_source)

        sectionList = html.find_all('search-result-item')


        sectionItem =''
        for section in sectionList:

            # print '---------------------------------------------'
            # title
            # title = section.article.a.select('#htmlContent')
            # print 'title: ' + title[0].get_text()

            # url
            ahrefurl = ''
            if section.article.a != None:

                ahrefurl = GoogleSeleniumScrapy.domains[0] + section.article.a['open-result']
            print 'url: ', ahrefurl
            jsonResult = self.parse_patent_html(ahrefurl)

            # write to file
            contentStr = ""
            if jsonResult != None:
                contentStr = '{"Title":"' + jsonResult['Title'].strip() + '","Abstraction":"' + jsonResult[
                    'Abstraction'].strip() + '","Description":"' + jsonResult['Description'].strip() + '","Url":"'+ahrefurl+'"}'
            contentStr.replace(r'\n', '')
            print contentStr
            sectionItem += contentStr + '\n'
        return sectionItem

    # parse the patents content html based on the url
    def parse_patent_html(self, url):

        try:
            # page = urllib2.urlopen(url)

            contentBrewser = webdriver.Firefox()

            contentBrewser.get(url)

            page = contentBrewser.page_source

            contentBrewser.close()

            del contentBrewser

        except Exception:
            print 'open error!'

        pageObj = BeautifulSoup(page.read())

        # print pageObj
        #
        # exit()

        try:
            # title
            title = pageObj.h1.get_text()
            if '"' in title:
                title.replace('"', ' ')
            # print title

            # abstract
            abstractStr = ''
            abstracts = pageObj.find('abstract')

            if abstracts != None:
                abstractStr = abstracts.div.get_text()
                if '"' in abstractStr:
                    abstractStr.replace('"', ' ')
            else:
                print 'Abstract is none'
            # print 'Abstract:' , abstractStr



            # classifications
            # classifications = pageObj.find('classifications')
            # if classifications != None:
                # print 'Classifications:' , classifications
            # else:
            #     print 'Classifications is none'

            # description
            # descriptions = pageObj.find('section',{'itemprop':'description'})
            #
            # if descriptions != None:
            #     # print 'Descriptions: ', descriptions
            #     # find all items of description
            #     ps = descriptions.div.findAll('p')
            #
            #     itemStr = ''
            #     for p in ps:
            #
            #         # remove \n \r \t and blank
            #         pStr = p.get_text()
            #         if pStr == "\n" or pStr == "":
            #             continue
            #         else:
            #             itemStr += pStr.strip()
            #
            #         # if not p.get_text() or not p or p.get_text() == '' or p.get_text() == '\n' or p.get_text() == '\r' or p.get_text() == '\t' or p.get_text() == ' ':
            #         #     continue
            #         # else:
            #         #     itemStr += p.get_text().strip('\n')
            #     # print 'itemstr:', itemStr
            #
            # else:
            #     print 'Descriptions is none'

        except AttributeError:
            print 'Attribute error!'

        # result = {'Title':title,'Abstraction':abstractStr,'Description':itemStr}
        result = {'Title': title, 'Abstraction': abstractStr, 'Description': ''}
        return result

        # return json

#-------------------------------------------------------------------------------------------------------------
# main function
if __name__ == '__main__':

    parameters = 'purslane'

    url = 'https://patents.google.com/?q='
    # url = 'https://www.google.com/#newwindow=1&q='

    googleseleniumscrap = GoogleSeleniumScrapy(url)

    current_page_num = 0
    total_page_num = 29

    # write to file
    content_text = codecs.open("content.txt", "w+", 'utf-8')


    while current_page_num < total_page_num:

        page_source = googleseleniumscrap.get_page(parameters, current_page_num)
        # print page_source
        # parse page contents
        jsonResult = googleseleniumscrap.parse_search_html(page_source)

        # print jsonResult
        content_text.write(jsonResult)
        current_page_num += 1
        print "current num:", current_page_num

        # if current_page_num > 5:
        #     exit()
    # del object
    del googleseleniumscrap
    # write end
    content_text.close()
    print 'successed!'