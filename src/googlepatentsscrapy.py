#coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import codecs
import urllib2

# Scrapy data from Google patents search based on the input key words

# Google patents scrapy
class GooglePatentsScrapy:

    # domains
    domains = ['https://patents.google.com/']

    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Firefox()
        # self.driver = webdriver.PhantomJS(executable_path='./phantomjs')

    def __del__(self):
        self.browser.close()
        # self.driver.close()

    # Get patents search results based on the input keyword and page number
    def getPatentsSearchResult(self, keywords, pageNumber):

        # split input key words by blank
        keywordStr = self.splitKeyWords(keywords)

        # join page number as the GET methods url parameters
        parameterStr = keywordStr + '&page=' + str(pageNumber)

        # component search result url with the domains, keywords and page number
        urlStr = self.url + parameterStr

        # get page source from Google through selenium tools
        self.browser.get(str(urlStr))
        # self.driver.get(str(urlStr))

        pageSource = self.browser.page_source
        # pageSource = self.driver.page_source
        return pageSource


    # Parse page of patents search result list
    def parsePatentsSearchResult(self, pageSource):

        if pageSource == None:
            return ''

        # parse html page with BeautifulSoup
        html = BeautifulSoup(pageSource)

        # find all search result items
        sectionList = html.find_all('search-result-item')

        if sectionList == None:
            return ''

        print 'url num:', len(sectionList)
        # include all patents contents: title, abstract, classifications...
        patentsItemList = ''

        # parse patent contents page
        for section in sectionList:

            # get the url of patent contents
            contentUrl = ''
            if section.article.a != None:

                # the url of patent contents
                contentUrl = GooglePatentsScrapy.domains[0] + section.article.a['open-result']

                # get patent content based on the url
                # try:
                #     contentPage = urllib2.urlopen(contentUrl)
                #
                # except Exception:
                #     print 'Open patent content error! '
                contentBrewser = webdriver.PhantomJS(executable_path='./phantomjs')

                contentBrewser.get(contentUrl)

                contentPage = contentBrewser.page_source

                # cleaning
                contentBrewser.quit()
                del contentBrewser

                # patent content parse result
                contentResult = self.parsePatentsContents(contentPage)

                # format the content parse result with ordered JSON
                contentStr = ''
                if contentResult != None:
                    contentStr = '{"Title":"' + contentResult['Title'].strip() + '","Abstract":"' + contentResult[
                        'Abstract'].strip() + '","Description":"' + contentResult[
                                     'Description'].strip() + '","Url":"' + contentUrl + '"}'
                contentStr.replace(r'\n', '')
                patentsItemList += contentStr + '\n'
        return patentsItemList


    # Parse page of patents contents
    def parsePatentsContents(self, pageSource):

        # Beautiful soup
        pageObj = BeautifulSoup(pageSource)

        try:
            # Parse content structures
            # Title
            titleStr = pageObj.h1.get_text()
            if '"' in titleStr:
                titleStr = titleStr.replace('"', ' ').replace('\n', ' ')
            if titleStr == '':
                titleStr = pageObj.find(itemprop='title').get_text().replace('\n', ' ')
            print 'title:', titleStr


            # Abstract
            abstractStr = ''
            abstractItems = pageObj.find(itemprop='abstract')

            if abstractItems != None:
                abstractStr = abstractItems.get_text().replace('\n', ' ')
                if '"' in abstractStr:
                    abstractStr = abstractStr.replace('"', ' ')
            else:
                print 'Abstract none!'

            print 'Abstract:', abstractStr

            # thumbnails
            thumbnailsItem = pageObj.find(itemprop='thumbnails')
            if thumbnailsItem != None:
                print 'find thumbnails'
            else:
                print 'thumbnails none!'

            # Classifications
            # classificationsItem = pageObj.find(itemprop='classifications')
            # if classificationsItem != None:
            #     print 'find classifications'
            # else:
            #     print 'classifications none'

            # Descriptions
            descriptionItem = pageObj.find(itemprop='description')
            descriptionStr = ''
            if descriptionItem != None:
                print 'find description'
                # print 'Descripiton:', descriptionItem.div.get_text()

                descriptionStr = descriptionItem.get_text().replace('\n', ' ')
                print 'Description:', descriptionStr
            else:
                print 'description none'

            sectionList = pageObj.find_all('section')
            if sectionList != None:
                print 'section len:', len(sectionList)
            else:
                print 'section none'

            # Claims
            claimsItem = pageObj.find(itemprop='claims')
            claimsStr = ''
            if claimsItem != None:
                print 'find claims'
                claimsStr += claimsItem.get_text().replace('\n', ' ')
                print 'Claims:', claimsStr
            else:
                print 'claims none'

            # search classification and
            # Classifications
            classificationsStr = ''
            # Images
            for sectionItem in sectionList:

                # Classifications
                if 'Classifications' == sectionItem.h2.get_text() or 'Classifications' in sectionItem.get_text():
                    classificationsStr += sectionItem.get_text().replace('\n', ' ')
                    print 'Classifications:', sectionItem.get_text().replace('\n', ' ')

            # exit()
        except AttributeError:
            print 'Attribute Error!'

        # parse result with JSON formatting
        parseResult = {'Title':titleStr, 'Abstract':abstractStr, 'Description':descriptionStr, 'Classifications':classificationsStr, 'Claims':claimsStr}
        return parseResult

    # Split input key words with blank
    def splitKeyWords(self, keywords):
        keywordStr = ''

        keywordsList = keywords.split(' ')
        index = 0
        if keywordsList != None:
            for kw in keywordsList:
                if index == len(keywordsList) - 1:
                    keywordStr += kw
                else:
                    keywordStr += kw + '+'
                index += 1

        return keywordStr

#######################################################################################################################
# Main function
if __name__ == '__main__':

    # key words list
    keywordsList = ['purslane']

    # all result page number
    totalPageList = [29]

    url = 'https://patents.google.com/?q='

    googlePatentsScrapy = GooglePatentsScrapy(url)

    # iterate all key words in list and save result to files
    index = 0
    for keyword in keywordsList:
        resultTextFile = codecs.open( keyword + '.txt', 'w+', 'utf-8')

        currentPageNum = 0

        totalPageNum = totalPageList[index]

        while currentPageNum < totalPageNum:
            # get search result page
            pageSource = googlePatentsScrapy.getPatentsSearchResult(keyword, currentPageNum)

            # parse search result page
            patentItems = googlePatentsScrapy.parsePatentsSearchResult(pageSource)

            # write to text file
            resultTextFile.write(patentItems)

            currentPageNum += 1

            print 'current page number:', currentPageNum

        # one key word process end
        resultTextFile.close()

        index += 1

    # Done

    del googlePatentsScrapy

    # write end
    # contentTextFile.close()
    print 'Successed!'



