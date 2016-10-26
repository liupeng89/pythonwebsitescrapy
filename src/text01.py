# # coding: utf-8
#
# from selenium import webdriver
# # import urllib2
# # import codecs
# #
# # url = 'https://patents.google.com/patent/WO1997019087A1/en?q=purslane'
# #
# # textfile = codecs.open('selenium.txt', 'w+', 'utf-8')
# # dirver = webdriver.Firefox()
# #
# # dirver.get(url)
# #
# # pageSource = dirver.page_source
# #
# # # print pageSource
# # textfile.write(unicode(pageSource))
# # textfile.close()
# #
# # dirver.close()
#
# # textfile = codecs.open('urllib2.txt', 'w+', 'utf-8')
# #
# # pageSource = urllib2.urlopen(url)
# #
# # textfile.write(unicode(pageSource))
# #
# # textfile.close()
#
# # element = pageSource.find_element_by_id("gb")
# #
# # print element
#
# # dirver.close()
#
# # contentUrl = 'https://patents.google.com/patent/WO1997019087A1/en'
# # contentBrewser = webdriver.PhantomJS(executable_path='./phantomjs')
# # contentBrewser.get(contentUrl)
# # contentPage = contentBrewser.page_source
# # print contentPage
#
# #############################################################
# import  urllib2
# # import codecs
# from bs4 import BeautifulSoup
#
# # textfile  = codecs.open('webofscience.txt', 'w+', 'utf-8')
# pagesource = urllib2.urlopen('https://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&parentQid=&qid=2&SID=T2Um4dY7yQI1VseJAVy&&update_back2search_link_param=yes&page=3')
# # textfile.write(str(pagesource.read()))
# # print pagesource.read()
# # textfile.close()
#
# pageObj = BeautifulSoup(pagesource.read())
#
# sectionList = pageObj.findAll('div', {'class': 'search-results-content'})
# index = 0
# if sectionList == None:
#     print 'section none!'
# else :
#     print 'len :', len(sectionList)
#     # for sectionItem in sectionList:
#     #     print 'index ', index, ':', sectionItem.get_text()
#     #     index += 1
#

# ss = '''中文名：阿胶
#     汉语拼音：Ejiao    拉丁名：ASINICORIICO'''
# list = ss.split('\n')
# line = ''
# for li in list:
#     line += li
# print line