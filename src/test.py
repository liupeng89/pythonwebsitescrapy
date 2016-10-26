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
        self.driver = webdriver.PhantomJS(executable_path='./phantomjs')

    def __del__(self):
        self.browser.close()
        self.driver.close()

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

        pageSource = self.browser.page_source

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

        print 'url number:' , len(sectionList)

        # # include all patents contents: title, abstract, classifications...
        # patentsItemList = ''
        #
        # # parse patent contents page
        # for section in sectionList:
        #
        #     # get the url of patent contents
        #     contentUrl = ''
        #     if section.article.a != None:
        #
        #         # the url of patent contents
        #         contentUrl = GooglePatentsScrapy.domains[0] + section.article.a['open-result']
        #
        #         # get patent content based on the url
        #         try:
        #             contentPage = urllib2.urlopen(contentUrl)
        #
        #         except Exception:
        #             print 'Open patent content error! '
        #
        #         # patent content parse result
        #         contentResult = self.parsePatentsContents(contentPage)
        #
        #
        #         # format the content parse result with ordered JSON
        #         contentStr = ''
        #         if contentResult != None:
        #             contentStr = '{"Title":"' + contentResult['Title'].strip() + '","Abstract":"' + contentResult[
        #                 'Abstract'].strip() + '","Description":"' + contentResult[
        #                              'Description'].strip() + '","Url":"' + contentUrl + '"}'
        #         contentStr.replace(r'\n', '')
        #         patentsItemList += contentStr + '\n'
        return ''


    # Parse page of patents contents
    def parsePatentsContents(self, pageSource):

        pageObj = BeautifulSoup(pageSource.read())

        try:
            # Parse content structures
            # Title
            titleStr = pageObj.h1.get_text()
            if '"' in titleStr:
                titleStr.replace('"', ' ')

            # Abstract
            abstractStr = ''
            abstractItems = pageObj.find('abstract')

            if abstractItems != None:
                abstractStr = abstractItems.div.get_text()
                if '"' in abstractStr:
                    abstractStr.replace('"', ' ')
            else:
                print 'Abstract in none!'

            # Classifications

            # Descriptions

        except AttributeError:
            print 'Attribute Error!'

        # parse result with JSON formatting
        parseResult = {'Title':titleStr, 'Abstract':abstractStr, 'Description':''}
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
        # resultTextFile = codecs.open( keyword + '.txt', 'w+', 'utf-8')

        currentPageNum = 0

        totalPageNum = totalPageList[index]

        while currentPageNum <= totalPageNum:
            # get search result page
            pageSource = googlePatentsScrapy.getPatentsSearchResult(keyword, currentPageNum)

            # parse search result page
            patentItems = googlePatentsScrapy.parsePatentsSearchResult(pageSource)

            # write to text file
            # resultTextFile.write(patentItems)

            currentPageNum += 1

            print 'current page number:', currentPageNum

        # one key word process end
        # resultTextFile.close()

        index += 1

    # Done

    del googlePatentsScrapy

    # write end
    # contentTextFile.close()
    print 'Successed!'











# from bs4 import  BeautifulSoup
# import codecs
# import urllib2
#
# text = codecs.open('text.txt', 'w+', 'utf-8')
#
# url = 'https://patents.google.com/?q=purslane&page=4'
#
# page = urllib2.urlopen(url)
#
# bf = BeautifulSoup(page.read())
#
# text.write(str(bf))
#
# text.close()

# print bf




####
# coding: utf-8

drugwebsitelist = ['阿胶','阿魏','矮地茶','艾片(左旋龙脑)','艾叶','安息香','八角茴香','巴豆','巴豆霜','巴戟天','菝葜','白扁豆','白矾','白附子','白果','白及','白蔹','白茅根','白前','白屈菜','白芍','白术','白头翁','白薇','白鲜皮','白芷','百部','百合','柏子仁','斑蝥','板蓝根','半边莲','半夏','半枝莲','薄荷','暴马子皮','北豆根','北刘寄奴','北沙参','荜茇','荜澄茄','蓖麻子','萹蓄','鳖甲','槟榔','冰片(合成龙脑)','补骨脂','布渣叶','苍耳子','苍术','藏菖蒲','草豆蔻','草果','草乌','草乌叶','侧柏叶','柴胡','蝉蜕','蟾酥','常山','炒瓜蒌子','车前草','车前子','沉香','陈皮','赤芍','赤石脂','赤小豆','茺蔚子','虫白蜡','臭灵丹草','楮实子','川贝母','川楝子','川木通','川木香','川牛膝','川射干','川乌','川芎','穿山甲','穿山龙','穿心莲','垂盆草','椿皮','磁石','刺五加','大豆黄卷','大腹皮','大黄','大蓟','大蓟炭','大青盐','大青叶','大蒜','大血藤','大叶紫珠','大枣','大皂角','丹参','胆南星','淡豆豉','淡竹叶','当归','当药','党参','刀豆','稻芽','灯心草','灯盏细辛(灯盏花)','地枫皮','地肤子','地骨皮','地黄','地锦草','地龙','地榆','滇鸡血藤','颠茄草','丁公藤','丁香','冬虫夏草','冬瓜皮','冬葵果','冬凌草','豆蔻','独活','独一味','杜仲','杜仲叶','断血流','煅石膏','莪术','鹅不食草','儿茶','法半夏','番泻叶','翻白草','防风','防己','飞扬草','榧子','粉萆藓','粉葛','枫香脂','蜂房','蜂胶','蜂蜡','蜂蜜','佛手','茯苓','茯苓皮','浮萍','附子','覆盆子','甘草','甘松','甘遂','干姜','干漆','杠板归','高良姜','高山辣根菜','藁本','葛根','功劳木','钩藤','狗脊','枸骨叶','枸杞子','谷精草','谷芽','骨碎补','瓜蒌皮','瓜蒌子','瓜萎','瓜子金','关黄柏','贯叶金丝桃','广东紫珠','广金钱草','广枣','龟甲','龟甲胶','桂枝','哈蟆油','蛤蚧','蛤壳','海金沙','海龙','海马','海螵蛸','海藻','诃子','合欢花','合欢皮','何首乌','荷叶','核桃仁','鹤虱','黑豆','黑芝麻','黑种草子','红参','红大戟','红豆蔻','红粉','红花','红景天','红芪','洪连','厚朴','厚朴花','胡黄连','胡椒','胡芦巴','湖北贝母','槲寄生','虎杖','花椒','花蕊石','华山参','滑石','滑石粉','化橘红','槐角','黄柏','黄精','黄连','黄芪','黄芩','黄山药','黄蜀葵花','黄藤','火麻仁','鸡骨草','鸡冠花','鸡内金','鸡血藤','积雪草','急性子','蒺藜','姜半夏','姜黄','僵蚕','降香','焦槟榔','焦栀子','芥子','金沸草','金果榄','金龙胆草','金礞石','金钱白花蛇','金钱草','金荞麦','金铁锁','金银花','金樱子','筋骨草','锦灯笼','京大戟','荆芥','荆芥穗','荆芥穗炭','荆芥炭','九里香','九香虫','韭菜子','救必应','桔梗','菊花','菊苣','橘核','橘红','卷柏','决明子','榼藤子','苦参','苦地丁','苦楝皮','苦木','苦杏仁','苦玄参','款冬花','昆布','辣椒','莱菔子','蓝布正','狼毒','老鹳草','雷丸','荔枝核','连钱草','连翘','莲房','莲须','莲子','莲子心','两面针','两头尖','蓼大青叶','灵芝','凌霄花','羚羊角','硫黄','龙胆','龙劂叶','龙眼肉','漏芦','芦根','芦荟','炉甘石','鹿角','鹿角胶','鹿角霜','鹿茸','鹿衔草','路路通','罗布麻叶','罗汉果','络石藤','麻黄','麻黄根','马鞭草','马勃','马齿苋','马兜铃','马钱子','马钱子粉','麦冬','麦芽','满山红','蔓荆子','芒硝','猫爪草','毛诃子','没药','玫瑰花','梅花','密蒙花','绵萆薢','绵马贯众','绵马贯众炭','明党参','墨旱莲','母丁香','牡丹皮','牡荆叶','牡蛎','木鳖子','木瓜','木棉花','木通','木香','木贼','南板蓝根','南鹤虱','南沙参','南五味子','闹羊花','牛蒡子','牛黄','牛膝','女贞子','藕节','胖大海','炮姜','佩兰','枇杷叶','片姜黄','平贝母','蒲公英','蒲黄','蕲蛇','千金子','千金子霜','千里光','千年健','牵牛子','前胡','芡实','茜草','羌活','秦艽','秦皮','青黛','青风藤','青果','青蒿','青礞石','青皮','青葙子','青叶胆','轻粉','清半夏','苘麻子','瞿麦','全蝎','拳参','人参','人参叶','人工牛黄','忍冬藤','肉苁蓉','肉豆蔻','肉桂','乳香','蕤仁','三白草','三棵针','三棱','三七','桑白皮','桑寄生','桑螵蛸','桑椹','桑叶','桑枝','沙棘','沙苑子','砂仁','山慈菇','山豆根','山麦冬','山柰','山香圆叶','山药','山银花','山楂','山楂叶','山茱萸','商陆','蛇床子','蛇蜕','射干','麝香','伸筋草','升麻','生姜','蓍草','石菖蒲','石吊兰','石膏','石斛','石决明','石榴皮','石韦','使君子','柿蒂','首乌藤','熟地黄','水飞蓟','水红花子','水牛角','水蛭','丝瓜络','四季青','松花粉','苏合香','苏木','酸枣仁','娑罗子','锁阳','太子参','檀香','桃仁','桃枝','体外培育牛黄','天冬','天花粉','天葵子','天麻','天南星','天然冰片(右旋龙脑)','天山雪莲','天仙藤','天仙子','天竺黄','甜瓜子','铁皮石斛','葶苈子','通草','通关藤','土贝母','土鳖虫(蟅虫)','土茯苓','土荆皮','土木香','菟丝子','瓦楞子','瓦松','王不留行','威灵仙','委陵菜','乌梅','乌梢蛇','乌药','巫山淫羊藿','吴茱萸','蜈蚣','五倍子','五加皮','五味子','西瓜霜','西河柳','西红花','西青果','西洋参','菥蓂','豨莶草','细辛','夏枯草','夏天无','仙鹤草','仙茅','香附','香加皮','香薷','香橼','小驳骨','小茴香','小蓟','小通草','小叶莲','薤白','辛夷','雄黄','徐长卿','续断','玄参','玄明粉','旋覆花','血竭','血余炭','鸦胆子','鸭跖草','亚乎奴(锡生藤)','亚麻子','延胡索(元胡)','洋金花','野菊花','野马追','野木瓜','一枝黄花','伊贝母','益母草','益智','薏苡仁','翼首草','茵陈','银柴胡','银杏叶','淫羊藿','罂粟壳','油松节','余甘子','鱼腥草','禹余粮','禹州漏芦','玉竹','郁金','郁李仁','预知子','芫花','远志','月季花','云芝','皂矾(绿矾)','皂角刺','泽兰','泽泻','浙贝母','珍珠','珍珠母','知母','栀子','蜘蛛香','枳壳','枳实','制草乌','制川乌','制何首乌','制天南星','炙甘草','炙红芪','炙黄芪','钟乳石','肿节风','重楼','朱砂','朱砂根','珠子参','猪胆粉','猪苓','猪牙皂','竹节参','竹茹','紫草','紫河车','紫花地丁','紫花前胡','紫萁贯众','紫石英','紫苏梗','紫苏叶','紫苏子','紫菀','紫珠叶','自然铜','棕榈']

docfilelist = ['一枝黄花','丁公藤','丁香','九里香','九香虫','人工牛黄','人参','人参叶','儿茶','八角茴香','刀豆','三七','三白草','三棱','三颗针','千年健','千里光','千金子','千金子霜','土木香','土贝母','土茯苓','土荆皮','土鳖虫(蟅虫)','大叶紫珠','大血藤','大皂角','大豆黄卷','大枣','大青叶','大青盐','大黄','大腹皮','大蒜','大蓟','大蓟炭','女贞子','小叶莲','小驳骨','小茴香','小通草','小蓟','山豆根','山麦冬','山柰','山茱萸','山药','山香圆叶','山银花','山慈菇','山楂','山楂叶','川乌','川木香','川木通','川牛膝','川贝母','川芎','川射干','川楝子','干姜','干漆','广东紫珠','广枣','广金钱草','广藿香','飞扬草','马齿苋','马勃','马钱子','马钱子粉','马兜铃','马鞭草','丹参','乌药','乌梢蛇','乌梅','云芝','五加皮','五味子','五倍子','化橘红','升麻','天山雪莲','天仙子','天仙藤','天冬','天花粉','天竺黄','天南星','天麻','天然冰片(右旋龙脑)','天葵子','太子参','巴豆','巴豆霜','巴戟天','月季花','木瓜','木芙蓉叶','木香','木贼','木通','木棉花','木蝴蝶','木鳖子','毛诃子','水飞蓟','水牛角','水红花子','水蛭','火麻仁','片姜黄','牛黄','牛蒡子','牛膝','王不留行','瓦松','瓦楞子','车前子','车前草','丝瓜络','仙茅','仙鹤草','冬瓜皮','冬虫夏草','冬凌草','冬葵果','功劳木','北刘寄奴','北沙参','北豆根','半边莲','半枝莲','半夏','四季青','布渣叶','平贝母','母丁香','玄参','玄明粉','玉竹','瓜子金','瓜蒌','瓜蒌子','瓜蒌皮','甘松','甘草','甘遂','生姜','白及','白头翁','白术','白芍','白芷','白附子','白屈菜','白果','白矾','白茅根','白前','白扁豆','白蔹','白鲜皮','白薇','石韦','石决明','石吊兰','石斛','石菖蒲','石榴皮','石膏','艾片(左旋龙脑)','艾叶','龙胆','龙眼肉','龙脷叶','亚乎奴(锡生藤)','亚麻子','伊贝母','全蝎','关黄柏','冰片(合成龙脑)','决明子','华山参','合欢皮','合欢花','地龙','地枫皮','地肤子','地骨皮','地黄','地榆','地锦草','安息香','延胡索(元胡)','当归','当药','朱砂','朱砂根','灯心草','灯盏细辛(灯盏花)','百合','百部','竹节参','竹茹','红大戟','红芪','红花','红花龙胆','红豆蔻','红参','红粉','红景天','老鹳草','肉苁蓉','肉豆蔻','肉桂','自然铜','芒硝','虫白蜡','血余炭','血竭','西瓜霜','西红花','西河柳','西青果','西洋参','防己','防风','两头尖','两面针','伸筋草','体外培育牛黄','何首乌','余甘子','佛手','吴茱萸','忍冬藤','杜仲','杜仲叶','杠板归','沉香','沙苑子','沙棘','没药','灵芝','牡丹皮','牡荆叶','牡蛎','皂角刺','皂矾(绿矾)','羌活','芡实','芥子','芦荟','芦根','芫花','花椒','花蕊石','苍术','苍耳子','苏木','苏合香','补骨脂','诃子','谷芽','谷精草','豆蔻','赤小豆','赤石脂','赤芍','辛夷','远志','连钱草','连翘','阿胶','阿魏','附子','陈皮','鸡内金','鸡血藤','鸡冠花','鸡骨草','麦冬','麦芽','龟甲','龟甲胶','乳香','京大戟','佩兰','使君子','侧柏叶','制川乌','制天南星','制何首乌','制草乌','刺五加','卷柏','垂盆草','委陵菜','岩白菜','巫山淫羊藿','昆布','明党参','松花粉','板蓝根','枇杷叶','枫香脂','油松节','法半夏','泽兰','泽泻','炉甘石','炒瓜蒌子','炙甘草','炙红芪','炙黄芪','狗脊','玫瑰花','知母','细辛','罗布麻叶','罗汉果','肿节风','苘麻子','苦木','苦玄参','苦地丁','苦杏仁','苦参','苦楝皮','虎杖','贯叶金丝桃','郁李仁','郁金','金龙胆草','金果榄','金沸草','金荞麦','金钱白花蛇','金钱草','金铁锁','金银花','金樱子','金礞石','闹羊花','降香','青风藤','青叶胆','青皮','青果','青葙子','青蒿','青黛','青礞石','鱼腥草','前胡','南五味子','南沙参','南板蓝根','南鹤虱','厚朴','厚朴花','哈蟆油','姜半夏','姜黄','威灵仙','急性子','枳壳','枳实','枸杞子','枸骨叶','柏子仁','柿蒂','栀子','洋金花','洪连','炮姜','牵牛子','独一味','独活','珍珠','珍珠母','砂仁','禹州漏芦','禹余粮','穿山甲','穿山龙','穿心莲','络石藤','胆南星','胖大海','胡芦巴','胡黄连','胡椒','茜草','茯苓','茯苓皮','茵陈','茺蔚子','荆芥','荆芥炭','荆芥穗','荆芥穗炭','草乌','草乌叶','草豆蔻','草果','荔枝核','荜茇','荜澄茄','轻粉','重楼','钟乳石','钩藤','韭菜子','首乌藤','香加皮','香附','香橼','香薷','骨碎补','鸦胆子','党参','凌霄花','夏天无','夏枯草','娑罗子','射干','徐长卿','拳参','柴胡','核桃仁','桂枝','桃仁','桃枝','桑叶','桑白皮','桑枝','桑寄生','桑椹','桑螵蛸','桔梗','浙贝母','浮萍','海马','海风藤','海龙','海金沙','海螵蛸','海藻','狼毒','珠子参','益母草','益智','秦皮','秦艽','积雪草','粉萆薢','粉葛','臭灵丹草','荷叶','莪术','莱菔子','莲子','莲子心','莲房','莲须','通关藤','通草','铁皮石斛','预知子','高山辣根菜','高良姜','鸭跖草','商陆','密蒙花','常山','救必应','断血流','旋覆花','梅花','淡竹叶','淡豆豉','淫羊藿','清半夏','猪牙皂','猪苓','猪胆粉','猫爪草','甜瓜子','续断','绵马贯众','绵马贯众炭','绵萆薢','羚羊角','菊花','菊苣','菝葜','菟丝子','菥蓂','蛇床子','蛇蜕','野马追','野木瓜','野菊花','银杏叶','银柴胡','鹿角','鹿角胶','鹿角霜','鹿茸','鹿衔草','麻黄','麻黄根','黄山药','黄芩','黄芪','黄连','黄柏','黄精','黄蜀葵花','黄藤','斑蝥','棕榈','楮实子','款冬花','湖北贝母','滑石','滑石粉','焦栀子','焦槟榔','番泻叶','硫黄','筋骨草','紫石英','紫花地丁','紫花前胡','紫苏子','紫苏叶','紫苏梗','紫草','紫珠叶','紫菀','紫萁贯众','萹蓄','葛根','葶苈子','蛤壳','蛤蚧','锁阳','雄黄','鹅不食草','黑芝麻','黑豆','黑种草子','椿皮','槐花','槐角','滇鸡血藤','满山红','煅石膏','矮地茶','蒲公英','蒲黄','蒺藜','蓍草','蓖麻子','蓝布正','蜂房','蜂胶','蜂蜜','蜂蜡','蜈蚣','路路通','锦灯笼','雷丸','榧子','榼藤子','槟榔','漏芦','磁石','罂粟壳','蓼大青叶','蔓荆子','蜘蛛香','蝉蜕','豨莶草','辣椒','酸枣仁','僵蚕','墨旱莲','暴马子皮','槲寄生','熟地黄','稻芽','蕤仁','蕲蛇','赭石','鹤虱','橘红','橘核','薄荷','薏苡仁','薤白','颠茄草','檀香','翼首草','藁本','藏菖蒲','瞿麦','翻白草','藕节','覆盆子','蟾酥','鳖甲','麝香']
print len(drugwebsitelist), ' : ', len(docfilelist)

# in drug, not in doc
for drugm in drugwebsitelist:
    if drugm not in docfilelist:
        print drugm

print '--------'

# in doc, not in drugwebsit
for docm in docfilelist:
    if docm not in drugwebsitelist:
        print docm

print 'diff end!'



