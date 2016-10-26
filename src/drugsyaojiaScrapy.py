# coding: utf-8
import time
import urllib2
from bs4 import BeautifulSoup

'''
    Scrapy data from: http://drugs.yaojia.org/

    The basic website: http://www.yaojia.org/thread-26281-1-1.html?_dsign=5ea81f5c
'''

class DrugyaojiaScrapy(object):
    def __init__(self, path, url):
        self.path = path     # save data file
        self.url = url       # url of website

    def __del__(self):
        pass

    # parse the website
    def parse(self):

        # parse website from 13-624 page
        with open(self.path, 'w') as file:



            for page_num in range(13, 625):

                print 'num:', page_num
                # page source
                page_source = urllib2.urlopen(self.url + str(page_num))
                if page_source == None:
                    print 'page source is None!'
                    continue
                # bs4
                bsObj = BeautifulSoup(page_source.read())

                if bsObj == None:
                    print 'bs object is none!'
                    continue

                dts = bsObj.find_all('dt')

                dds = bsObj.find_all('dd')

                jsondata = '{'
                if len(dds) != len(dts):
                    print '__len__not__match:', page_num
                    continue
                else:
                    length = len(dts)
                    for index in range(0, length):
                        dtStr = dts[index].get_text().encode('utf-8').strip().replace('\r\n', '').replace('"','')
                        ddStr = dds[index].get_text().encode('utf-8').strip().replace('\r\n', '').replace('"','')

                        if dtStr == '' and index == 1:
                            jsondata += '"摘要":"' + ddStr + '",'

                        elif index == length - 1:    # end the json data
                            jsondata += '"' + dtStr + '":"' + ddStr + '"}'
                        elif str('中文名') in ddStr:
                            ddStrList = ddStr.split('    ')
                            if ddStrList != None:
                                for ddlist in ddStrList:
                                    ddItemStr = ddlist.split('：')
                                    if ddItemStr != None and len(ddItemStr) == 2:

                                        jsondata += '"' + ddItemStr[0] + '":"' + ddItemStr[1] + '",'
                                    else:
                                        print 'infor error : ', ddStr
                        else:
                            jsondata += '"' + dtStr + '":"' + ddStr + '",'

                file.write(jsondata + '\n')

                time.sleep(1)

        print 'write end!'



###########################################
if __name__ == '__main__':

    url = 'http://drugs.yaojia.org/index.php?m=drugs&c=index&a=show&catid=7&id='
    path = '/Users/heermaster/Documents/python/googlepatentsscrapy/src/drugsyaojiajsondata.txt'

    drugsyaojiascrapy = DrugyaojiaScrapy(path, url)

    print 'begin parse'
    drugsyaojiascrapy.parse()

    print 'end parse'

