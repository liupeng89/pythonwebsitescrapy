#coding: utf-8
# Scrapy data from web of science website.
# request result with post data
# The SID value in search url will change every time when we open the website. So should change SID every run this code!

import urllib2
import json

from bs4 import BeautifulSoup

class WebOfScienceScrapy:

    def __init__(self, keywords, urls, totalpages):
        self.keywords = keywords
        self.urls = urls
        self.totalpages = totalpages


    def __del__(self):
        del self.keywords
        del self.urls
        del self.totalpages

    # Get the search result and save to text file
    def scrapyPageAndSaveToFile(self):

        if keywords == None or len(keywords) == 0:
            return
        # iterate all keywords
        index = 0 # index of all list
        for keyword in self.keywords:
            # key word as the data file name

            # textFile = codecs.open(keyword + '_webofscience.txt', 'w+', 'utf-8')
            textFile = open(keyword + '_webofscience.txt', 'w+')
            print 'keyword', index + 1, ':\n'

            currentPageNum = 1
            # total page number of keyword search result
            totalPageNum = self.totalpages[index]
            # search result of all pages
            while currentPageNum <= totalPageNum:
                # parse the search result to get the url of each paper
                urlOfResultPage = self.urls[index]
                urlOfResultPage += str(currentPageNum)

                # get the page of the index + 1
                pageSource = urllib2.urlopen(urlOfResultPage)

                if pageSource == None:
                    continue

                # parse the page to get all paper urls in this result page
                pageObj = BeautifulSoup(pageSource.read())

                searchResultsContentList = pageObj.findAll('div', {'class': 'search-results-content'})
                if searchResultsContentList == None or len(searchResultsContentList) == 0:
                    continue
                else:
                    print 'search resutl items: ', len(searchResultsContentList)

                for searchResultsContentItem in searchResultsContentList:

                    # get the url of paper in each section
                    paperUrl = self.getPaperUrl(searchResultsContentItem)
                    print 'paper url:', paperUrl
                    # parse json result of content
                    jsonParseResult = self.parsePaperContent(paperUrl)

                    if jsonParseResult == None:
                        continue
                    # write to text file
                    # print jsonParseResult
                    textFile.write(json.dumps(jsonParseResult) + '\n')
                    # print jsonParseResult
                currentPageNum += 1

            textFile.close()


    # get the url of paper in each section
    def getPaperUrl(self, item):


        ahrefStr = item.div.div.a['href']
        print 'a href:', ahrefStr

        # generate the url of each paper from search results
        ahrefStr = 'https://apps.webofknowledge.com' + ahrefStr

        return ahrefStr

    # parse the paper content page to get data
    def parsePaperContent(self, paperUrl):

        pageSource = urllib2.urlopen(paperUrl)

        if pageSource == None:
            return None

        pageObj = BeautifulSoup(pageSource.read())

        # title
        titleItem = pageObj.find('div', {'class': 'title'})
        titleStr = ''
        if titleItem != None:
            titleStr = titleItem.get_text().encode('utf-8').replace('\n','')
            # titleStr = titleStr.replace('\n','')

        # block record info
        writerStr = ''
        publishStr = ''
        abstractStr = ''
        keywordsStr = ''
        otherinfo = ''

        blockRecordInfoList = pageObj.findAll('div', {'class': 'block-record-info'})
        if blockRecordInfoList != None and len(blockRecordInfoList) > 0 :
            # index 0 is writer
            if blockRecordInfoList[0] != None:
                writerStr = blockRecordInfoList[0].get_text().encode('utf-8').replace('\n', ' ')

            # index 1 is Publication info
            if blockRecordInfoList[1] != None:
                publishStr = blockRecordInfoList[1].get_text().encode('utf-8').replace('\n', ' ')

            # index 2 is abstract
            if blockRecordInfoList[2] != None:
                abstractStr = blockRecordInfoList[2].get_text().encode('utf-8').replace('\n', ' ').replace('Abstract', '')
            # index 3 is keywords
            if blockRecordInfoList[3] != None:
                keywordsStr = blockRecordInfoList[3].get_text().encode('utf-8').replace('\n', ' ').replace(' KeywordsAuthor','').replace('Keywords:','').replace('Plus:','')
            # index 4 is Author Information
            if blockRecordInfoList[4] != None:
                for current_index in range(4, len(blockRecordInfoList)):
                    otherinfo += blockRecordInfoList[current_index].get_text().encode('utf-8').replace('\n', '')
                    current_index += 1

            # index 5... other information

        # url
        urlStr = paperUrl

        # generate the json result
        jsonResult = {'Title': titleStr, 'Publish':publishStr,'Writer': writerStr, 'Abstract': abstractStr, 'Keywords': keywordsStr,'Others':otherinfo, 'Url': urlStr}

        return jsonResult

#########################################################################################################
if __name__ == '__main__':

    # The first step -- get the SID from website because the SID will change every time when we open the website.

    # the keywords need to query
    keywords = ['purslane']
    # the url of keywords search results
    urls = ['https://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&parentQid=&qid=1&SID=Q1EgjZyvo1xjISgjB73&&update_back2search_link_param=yes&page=']
    # total page number of each keyword
    totalpages = [40]

    webOfScienceScrapy = WebOfScienceScrapy(keywords, urls, totalpages)
    print 'Scray beginning!'
    webOfScienceScrapy.scrapyPageAndSaveToFile()
    print 'Scray ending!'