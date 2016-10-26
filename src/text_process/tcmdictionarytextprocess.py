# coding: utf-8
# Process the text data of TCMDictionary
import json
import re
import csv

from sets import Set

class TCMDictionaryProcess:

    def __init__(self, path):
        self.path = path
        self.keywordSet = Set()
        self.all_keywords_set = Set()

        self.convertingkeywords = {}

        # list pattern
        self.list_pattern = re.compile(u'【[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+】[^(【|】|"|})]+')
        # list keyword pattern
        self.list_keyword_pattern = re.compile(u'【[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+】')
        # title pattern
        self.title_pattern = re.compile(u'"Title":"[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ffa-zA-Z]+"')
        # field order list
        self.field_order_list = ['编号','中文名','拼音名','别名','英文名','功能主治','临床应用','药理作用','生境分布','化学成份',
                                 '含量测定','性味','鉴别','性状','来源','摘录','贮藏','注意','采集','制剂',
                                 '出处','原形态','制法','炮制','备注','栽培','归经','毒性','各家论述','集解','用法用量','附方']

    def __del__(self):
        pass

    # read file
    def read(self):
        with open(self.path,mode='r') as file:
            data = file.read()

            lines = data.split('\n')
            index = 0

            jsonList = []

            # get all key words in each line
            for line in lines:
                # get all key words in each line
                all_kw = self.get_all_key_words(line)
                if all_kw != None:
                    self.all_keywords_set |= all_kw

            # self.print_set(self.all_keywords_set)
            # add name of TCM to all keywords set
            self.all_keywords_set.add(str('中文名'))
            self.all_keywords_set.add(str('编号'))

            # convert chinese keyword to char
            # self.print_set(self.all_keywords_set)

            # exit()



            # print 'jsondata len:', len(jsondata)
            # exit()
            # print jsondata.keys()
            # parse each line contents
            index = 0
            for line in lines:

                jsondata = {}
                for kw in self.all_keywords_set:
                    jsondata.setdefault(kw, '')

                noStr = str(10000000 + index * 100)

                jsondata.setdefault(str('中文名'),'')
                jsondata[str('编号')] = noStr


                jsondata = self.parseItemToJSON(line, jsondata)

                # index += 1
                # print jsondata
                # values = jsondata.values()
                # for v in values:
                #     print '--', v
                # jsondata[str('名字')] =
                if jsondata == None:
                    continue
                print jsondata[str('中文名')]

                jsonList.append(jsondata)

                index += 1
            print '----------------------'
            # self.print_set(self.all_keywords_set)

            # process json data list
            # Todo
            # print len(jsonList)
            self.print_list_json_data(jsonList)
            # exit()
            # save data to csv file
            target = 'data.csv'
            self.save_to_csv_file(target, jsonList)

    # save data to csv file
    def save_to_csv_file(self, target, jsonlist):
        if list == None:
            return
        # save
        with open(target, mode='w') as csvfile:
            # write the field first
            writer = csv.DictWriter(csvfile, fieldnames=self.field_order_list)

            writer.writeheader()

            # writer the contents with iterative all list

            # iterative all list
            index = 0
            for jn in jsonlist:
                print index, jn[str('中文名')]
                writer.writerow(jn)
                index += 1

            print 'write csv file end!'

    # save data to json file
    def save_to_json_file(self, target, jsonlist):
        if jsonlist == None:
            return

        # save data to json file
        with open(target, mode='w') as jsonfile:

            pass

    # get all key words in each line of data
    def get_all_key_words(self, line):

        if line == '':
            return None

        keywords_set = Set()
        # parse line
        line_unicode = unicode(line, encoding='utf-8')

        # list keyword pattern
        # list_keyword_pattern = re.compile(u'【[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+】')

        keyword_list = re.findall(self.list_keyword_pattern, line_unicode)
        if keyword_list == None:
            return None

        for kw in keyword_list:
            keywords_set.add(kw.encode('utf-8').replace('【', '').replace('】', ''))

        return keywords_set

    # parse item of each line to json format data
    def parseItemToJSON(self, line, jsondata):
        # print '--', len(jsondata)
        if line == '':
            return None
        line_unicode = unicode(line, encoding='utf-8')

        items = re.findall(self.list_pattern, line_unicode)

        titles = re.findall(self.title_pattern, line_unicode)
        if titles == None:
            return None
        titleStr = titles[0].encode('utf-8').replace('"','').split(':')[1]

        if items == None:
            return None
        index = 0
        # parse contents
        if __name__ == '__main__':
            for kw in self.all_keywords_set:
                # print 'key: ', kw
                # add string to json
                contentStr = jsondata[kw]
                # print 'default value: ', contentStr

                for item in items:
                    item = item.encode(encoding='utf-8')
                    # print item, type(item), type(kw)
                    if item.find(kw) != -1:
                        # print kw, ' -- ', item
                        # content
                        contentStr += '#' + item.split('】')[1]
                        # print '=====',contentStr

                # update the json data
                # print kw, '---:---', contentStr
                jsondata[kw] = contentStr

                # No

        jsondata[str('中文名')] = titleStr

        return jsondata

    # parse the line string to JSON
    def parseItemToJson(self, line):

        if line == '':
            return None

        all_keyword_set = Set()
        # convert to the unicode format
        line_unicode = unicode(line, encoding='utf-8')

        # list of items
        list = re.findall(self.list_pattern, line_unicode)
        # title
        title = re.findall(self.title_pattern, line_unicode)
        titleStr = ''
        # title
        if title and len(title) > 0:
            titleStr = title[0].replace('"','').split(':')[1]

        # list of items

        # the keywords of items
        list_keywords = re.findall(self.list_keyword_pattern, line_unicode)
        if list_keywords == None:
            return None
        keyword_set = Set()
        keyword_index = 1
        for key in list_keywords:
            key  = key.encode('utf-8')
            # unicode to utf-8
            # print type(key)
            key = key.replace('【', '').replace('】', '')
            # for kw in keyword_set:
            #     pass
            self.all_keywords_set.add(key)

        # self.print_set()

        json = dict()

        return json

    #
    def print_set(self, set):
        print '------print set-------'
        if set == None:
            return
        for s in set:
            print s
    # print the list of json data
    def print_list_json_data(self, list):
        index = 0
        if list == None:
            return
        for jn in list:
            print index, '----------', jn[str('中文名')]

            index += 1


    def get_all_keywords(self):

        pass

#################################################################
if __name__ == '__main__':

    # item
    # path = '/Users/heermaster/Documents/python/googlepatentsscrapy/src/item.txt'
    # TCM Dictionary.txt
    path = '/Users/heermaster/Documents/python/googlepatentsscrapy/src/TCM Dictionary.txt'

    tcmdictionaryprocess = TCMDictionaryProcess(path=path)

    tcmdictionaryprocess.read()

    # Process text
