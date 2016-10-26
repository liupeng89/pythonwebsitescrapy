import urllib
import urllib2
import re
import random



class GooglePatentsScrapy:
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
                           'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
                           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
                            (KHTML, like Gecko) Element Browser 5.0', \
                          'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
                          'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
                            'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
                           'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
                            Version/6.0 Mobile/10A5355d Safari/8536.25', \
                          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/28.0.1468.0 Safari/537.36', \
                           'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']

    def __init__(self, url):
        self.url = url

    # parse parameters
    def parseParameters(self):
        parametersList = self.url.split(" ")

        urlStr = ''
        index = 0
        for param in parametersList:
            if index == len(parametersList) - 1:
                urlStr += param
            else:
                urlStr += param + '+'
            index += 1

        print 'urlStr:' + urlStr
        return urlStr

    # get page based on url
    def getPage(self):

        # p1+p2+p3 parameters
        params = self.parseParameters()

        urlStr = 'https://patents.google.com/?q=' + params

        #user_agent
        agent_index = random.randint(0, 9)
        user_agent = GooglePatentsScrapy.user_agents[agent_index]

        request = urllib2.Request(urlStr)
        request.add_header('User-agent', user_agent)

        response = urllib2.urlopen(request)

        html = response.read()

        print html

# process
if __name__ == "main":


paramters = 'hadoop hive mapreduce'
goolgePetents = GooglePatentsScrapy(paramters)

goolgePetents.getPage()





