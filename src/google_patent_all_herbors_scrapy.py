#coding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver


# All herborist list
# all_herborists_list = ['SOLIDAGINIS HERBA','ERYCIBES CAULIS','CARYOPHYLLI FLOS','ANISI STELLATI FRUCTUS','BOVIS CALCULUS ARTIFACTUS','GINSENG RADIX ET RHIZOMA','GINSENGFOLIUM','CATECHU','MURRAYAE FOLIUM ET CACUMEN','ASPONGOPUS','CANAVALIAE SEMEN','NOTOGINSENG RADIX ET RHIZOMA','SAURURI HERBA','SPARGANII RHIZOMA','BERBERIDIS RADIX','ZINGIBERIS RHIZOMA','ZINGIBERIS RHIZOMA PRAEPARATUM','TOXICODENDRI RESINA','INULAE RADIX','BOLBOSTEMMATIS RHIZOMA','PSEUDOLARICIS CORTEX','SMILACIS GLABRAE RHIZOMA','EUPOLYPHAGA STELEOPHAGA','CALLICARPAE MACROPHYLLAE FOLIUM','SARGENTODOXAE CAULIS','SOJAE SEMEN GERMINATUM','GLEDITSIAE SINENSIS FRUCTUS','ISATIDIS FOLIUM','HALITUM','JUJUBAE FRUCTUS','RHEI RADIX ET RHIZOMA','ALLII SATIVI BULBUS','CIRSII JAPONICI HERBA','CIRSII JAPONICI HERBA CARBONISATA','ARECAE PERICARPIUM','LIRIOPES RADIX','SOPHORAE TONKINENSIS RADIX ET RHIZOMA','CORNI FRUCTUS','DIOSCOREAE RHIZOMA','KAEMPFERIAE RHIZOMA','TURPINIAE FOLIUM','LONICERAE FLOS','CRATAEGI FRUCTUS','CRATAEGI FOLIUM','CREMASTRAE PSEUDOBULBUS PLEIONES PSEUDOBULBUS','HOMALOMENAE RHIZOMA','SENECIONIS SCANDENTIS HEBRA','EUPHORBIAE SEMEN','EUPHORBIAE SEMEN PULVERATUM','VLADIMIRIAE RADIX','CLEMATIDIS ARMANDII CAULIS','FRITILLARIAE CIRRHOSAE BULBUS','CYATHULAE RADIX','ACONITI RADIX','ACONITI RADIX COCTA','CHUANXIONG RHIZOMA','IRIDIS TECTORI RHIZOMA','TOOSENDAN FRUCTUS','CALLICARPAE CAULIS ET FOLIUMI','CHOEROSPONDIATIS FRUCTUS','DESMODII STYRACIFOLII HERBA','POGOSTEMONIS HERBA','LIGUSTRI LUCIDI FRUCTUS','SINOPODOPHYLLI FRUCTUS','GENDARUSSAE HERBA','FOENICULI FRUCTUS','STACHYURI MEDULLA HELWINGIAE MEDULLA','CIRSII HERBA','EUPHORBIAE HIRTAE HERBA','PORTULACAE HERBA','LASIOSPHAERA CALVATIA','STRYCHNI SEMEN','STRYCHNI SEMEN PULVERATUM','ARISTOLOCHIAE FRUCTUS','VERBENAE HERBA','VACCARIAE SEMEN','SAUSSUREAE INVOLUCRATAE HERBA','HYOSCYAMI SEMEN','ARISTOLOCHIAE HERBA','ASPARAGI RADIX','TRICHOSANTHIS RADIX','BAMBUSAE CONCRETIO SILICEA','ARISAEMATIS RHIZOMA','ARISAEMATIS RHIZOMA PREPARATUM','GASTRODIAE RHIZOMA','SEMIAQUILEGIAE RADIX','BORNEOLUM','CORIOLUS','CHAENOMELIS FRUCTUS','HIBISCI MUTABILIS FOLIUM','AUCKLANDIAE RADIX','EQUISETI HIEMALIS HERBA','AKEBIAE CAULIS','GOSSAMPIM FLOS','OROXYLI SEMEN','MOMORDICAE SEMEN','ACANTHOPANACIS CORTEX','SCHISANDRAE CHINENSIS FRUCTUS','GALLA CHINENSIS','PSEUDOSTELLARIAE RADIX','PLANTAGINIS SEMEN','PLANTAGINIS HERBA','OROSTACHYIS FIMBRIATAE HERBA','ARCAE CONCHA','BOVISC ALCULUS','ARCTII FRUCTUS','ACHYRANTHIS BIDENTATAE RADIX','TERMINALIAE BELLIRICAE FRUCTUS','CIMICIFUGAE RHIZOMA','WENYUJIN RHIZOMA CONCISUM','CITRI GRANDIS EXOCARPIUM','ROSAE CHINENSIS FLOS','SALVIAE MILTIORRHIZAE RADIX ET RHIZOMA','LINDERAE RADIX','ZAOCYS','MUME FRUCTUS','CANNABIS FRUCTUS','CROTONIS FRUCTUS','CROTONIS SEMEN PULVERATUM','MORINDAE OFFICINALIS RADIX','SILYBI FRUCTUS','BUBALI CORNU','POLYGONI ORIENTALIS FRUCTUS','HIRUDO','POLYGONATIODORATIRHIZOMA','MAHONIAE CAULIS','NARDOSTACHYOS RADIX ET RHIZOMA','GLYCYRRHIZAE RADIX ET RHIZOMA','GLYCYRRHIZAE RADIX ET RHIZOMA PRAEPARATA CUM MELLE','KANSUI RADIX','BORNEOLUM','ARTEMISIAE ARGYI FOLIUM','PYRROSIAE FOLIUM','LYSIONOTI HERBA','HALIOTIDIS CONCHA','ACORI TATARINOWII RHIZOMA','DENDROBII CAULIS','GRANATI PERICARPIUM','GYPSUM FIBROSUM','GYPSUM USTUM','MICROCTIS FOLIUM','GENTIANAE RADIX ET RHIZOMA','LONGAN ARILLUS','SAUROPI FOLIUM','FRITILLARIAE USSURIENSIS BULBUS','SIPHONOSTEGIAE HERBA','MENISPERMI RHIZOMA','GLEHNIAE RADIX','ILICIS CHINENSIS FOLIUM','ZINGIBERIS RHIZOMA RECENS','CURCULIGINIS RHIZOMA','AGRIMONIAE HERBA','BLETILLAE RHIZOMA','ATRACTYLODIS MACROCEPHALAE RHIZOMA','PULSATILLAE RADIX','PAEONIAE RADIX ALBA','ANGELICAE DAHURICAE RADIX','TYPHONII RHIZOMA','IMPERATAE RHIZOMA','ALUMEN','GINKGO SEMEN','CHELIDONII HERBA','CYNANCHI STAUNTONII RHIZOMA ET RADIX','LABLAB SEMEN ALBUM','AMPELOPSIS RADIX','DICTAMNI CORTEX','CYNANCHI ATRATI RADIX ET RHIZOMA','POLYGALAE JAPONICAE HERBA','TRICHOSANTHIS FRUCTUS','TRICHOSANTHIS SEMEN','TRICHOSANTHIS SEMEN TOSTUM','TRICHOSANTHIS PERICARPIUM','BENINCASAE EXOCARPIUM','CORDYCEPS','RABDOSIAE RUBESCENTIS HERBA','MALVAE FRUCTUS','NATRII SULFAS EXSICCATUS','SCROPHULARIAE RADIX','LOBELIAE CHINENSIS HERBA','SCUTELLARIAE BARBATAE HERBA','PINELLIAE RHIZOMA','PINELLIAE RHIZOMA PRAEPARATUM','PINELLIAE RHIZOMA PRAEPARATUMCUM ZINGIBERE ET ALUMINE','PINELLIAE RHIZOMA PRAEPARATUM CUM ALUMINE','CARYOPHYLLI FRUCTUS','LUFFAE FRUCTUS RETINERVUS','ERODII HERBA GERANII HERBA','PHERETIMA','ILLICII CORTEX','KOCHIAE FRUCTUS','LYCII CORTEX','REHMANNIAE RADIX','REHMANNIAE RADIX PRAEPARATA','SANGUISORBAE RADIX','EUPHORBIAE HUMIFUSAE HERBA','NATRII SULFAS','CISSAMPELOTIS HERBA','LINI SEMEN','MIRABILITUM PRAEPARATUM','CROCI STIGMA','CHEBULAE FRUCTUS IMMATURUS','TAMARICIS CACUMEN','PANACIS QUINQUEFOLII RADIX','LILII BULBUS','STEMONAE RADIX','ANGELICAE SINENSIS RADIX','SWERTIAE HERBA','CERA CHINENSIS','CISTANCHES HERBA','MYRISTICAE SEMEN','CINNAMOMI CORTEX','CINNABARIS','ARDISIAE CRENATAE RADIX','PANACIS JAPONICI RHIZOMA','BAMBUSAE CAULIS IN TAENIAS','CORYDALIS RHIZOMA','PHYSOCHLAINAE RADIX','PYRITUM','FRITILLARIAE PALLIDIFLORAE BULBUS','CRINIS CARBONISATUS','DRACONIS SANGUIS','SCORPIO','ALBIZIAE CORTEX','ALBIZIAE FLOS','CASSIAE SEMEN','BORNEOLUM SYNTHETICUM','PHELLODENDRI AMURENSIS CORTEX','JUNCI MEDULLA','ERIGERONTIS HERBA','BENZOINUM','STEPHANIAE TETRANDRAE RADIX','SAPOSHNIKOVIAE RADIX','KNOXIAE RADIX','CARTHAMI FLOS','ENTIANAE RHODANTHAE HERBA','HEDYSARI RADIX','HEDYSARI RADIX PRAEPARATA CUM MELLE','GALANGAE FRUCTUS','GINSENG RADIX ET RHIZOMA RUBRA','HYDRARGYRI OXYDUM RUBRUM','RHODIOLAE CRENULATAE RADIX ET RHIZOMA','OPHIOPOGONIS RADIX','HORDEI FRUCTUS GERMINATUS','POLYGALAE RADIX','VIGNAE SEMEN','HALLOYSITUM RUBRUM','PAEONIAERADIX RUBRA','GENKWA FLOS','ZANTHOXYLI PERICARPIUM','OPHICALCITUM','SINAPIS SEMEN','ATRACTYLODIS RHIZOMA','XANTHII FRUCTUS','EURYALES SEMEN','ALOE','PHRAGMITIS RHIZOMA','SAPPAN LIGNUM','STYRAX','EUCOMMIAE CORTEX','EUCOMMIAE FOLIUM','POLYGONIPERFOLIATIHERBA','EPIMEDII WUSHANENSIS FOLIUM','AMOMI FRUCTUS ROTUNDUS','ANEMONES RADDEANAE RHIZOMA','ZANTHOXYL夏 RADIX','GLECHOMAE HERBA','FORSYTHIAE FRUCTUS','EUODIAE FRUCTUS','MOUTAN CORTEX','VITICIS NEGUNDO FOLIUM','OSTREAE CONCHA','BOVIS CALCULUS SATIVUS','POLYGONI MULTIFLORI RADIX','POLYGONI MULTIFLORI RADIX PRAEPARATA','LYCOPODII HERBA','GLEDITSIAE SPINA','MELANTERITUM','CITRI SARCODACTYLIS FRUCTUS','PHYLLANTHI FRUCTUS','SETARIAE FRUCTUS GERMINATUS','ERIOCAULI FLOS','TESTUDINIS CARAPAX ET PLASTRUM','TESTUDINIS CARAPACIS ET PLASTRI COLLA','MAGNOLIAE FLOS','NOTOPTERYGII RHIZOMA ET RADIX','ASTRAGALI COMPLANATI SEMEN','HIPPOPHAE FRUCTUS','AQUILARIAE LIGNUM RESINATUM','MYRRHA','CHEBULAE FRUCTUS','PSORALEAE FRUCTUS','GANODERMA','ASINI CORII COLLA','FERULAE RESINA','CITRI RETICULATAE PERICARPIUM','ACON','LONICERAE JAPONICAE CAULIS','GALL1 GIGERII ENDOTHELIUM CORNEUM','SPATHOLOBI CAULIS','ABRIHERBA','CELOSIAE CRISTATAE FLOS','SINOMENII CAULIS','SWERTIAE MILEENSIS HERBA','CITRI RETICULATAE PERICARPIUM VIRIDE','CANARII FRUCTUS','CELOSIAE SEMEN','ARTEMISIAE ANNUAE HERBA','CHLORITI LAPIS','INDIGO NATURALIS','ROSAE RUGOSAE FLOS','PICRASMAE RAMULUS ET FOLIUM','PICRIAE HERBA','CORYDALIS BUNGEANAE HERBA','ARMENIACAE SEMEN AMARUM','SOPHORAE FLAVESCENTIS RADIX','MELIAE CORTEX','ABUTILI SEMEN','ERIOBOTRYAE FOLIUM','ISATIDIS RADIX','PINI POLLEN','LIQUIDAMBARIS RESINA','ACANTHOPANACIS SENTICOSI RADIX ET RHIZOMA SEU CAULIS','PRUNI SEMEN','CURCUMAE RADIX','POLYGONI CUSPIDATI RHIZOMA ET RADIX','LAMINARIAE THALLUS ECKLONIAE THALLUS','CHANGII RADIX','BERGENIAE RHIZOMA','APOCYNI VENETI FOLIUM','SIRAITIAE FRUCTUS','ANEMARRHENAE RHIZOMA','SEDI HERBA','POTENTILLAE CHINENSIS HERBA','QUISQUALIS FRUCTUS','PLATYCLADI CACUMEN','EUPATORII HERBA','CONYZAE HERBA','TINOSPORAE RADIX','INULAE HERBA','FAGOPYRI DIBOTRYIS RHIZOMA','BUNGARUS PARVUS','LYSIMACHIAE HERBA','PSAMMOSILENES RADIX','LONICERAE JAPONICAE FLOS','ROSAE LAEVIGATAE FRUCTUS','MICAE LAPIS AUREUS','OLIBANUM','SARCANDRAE HERBA','HOUTTUYNIAE HERBA','CIBOTII RHIZOMA','EUPHORBIAE PEKINENSIS RADIX','RHODODENDRI MOLLIS FLOS','SELAGINELLAE HERBA','CALAMINA','PINI LIGNUM NODI','LYCOPI HERBA','ALISMATIS RHIZOMA','DALBERGIAE ODORIFERAE LIGNUM','ASARI RADIX ET RHIZOMA','HYPERICI PERFORATI HERBA','MARGARITA','MARGARITIFERA CONCHA','SCHIZONEPETAE HERBA','SCHIZONEPETAE HERBA CARBONISATA','SCHIZONEPETAE SPICA','SCHIZONEPETAE SPICA CARBONISATA','RUBIAE RADIX ET RHIZOMA','PIPERIS LONGI FRUCTUS','LITSEAE FRUCTUS','ACONITI KUSNEZOFFII RADIX','ACONITI KUSNEZOFFII RADIX COCTA','ACONITI KUSNEZOFFII FOLIUM','ALPINIAE KATSUMADAI SEMEN','TSAOKO FRUCTUS','ARTEMISIAE SCOPARIAE HERBA','PORIA','PORIAE CUTIS','LEONURI FRUCTUS','TRIGONELLAE SEMEN','PICRORHIZAE RHIZOMA','PIPERIS FRUCTUS','LITCHI SEMEN','SCHISANDRAE SPHENANTHERAE FRUCTUS','ADENOPHORAE RADIX','BAPHICACANTHIS CUSIAE RHIZOMA ET RADIX','CAROTAE FRUCTUS','AURANTII FRUCTUS','AURANTII FRUCTUS IMMATURUS','PLATYCLADI SEMEN','GARDENIAE FRUCTUS','GARDENIAE FRUCTUS PRAEPARATUS','LYCII FRUCTUS','ILICIS CORNUTAE FOLIUM','KAKI CALYX','CLEMATIDIS RADIX ET RHIZOMA','MAGNOLIAE OFFICINALIS CORTEX','MAGNOLIAE OFFICINALIS FLOS','AMOMI FRUCTUS','PHARBITIDIS SEMEN','CALOMELAS','BRUCEAE FRUCTUS','ALLII TUBEROSI SEMEN','RANAE OVIDUCTUS','DRYNARIAE RHIZOMA','STALACTITUM','UNCARIAE RAMULUS CUM UNCIS','PERIPLOCAE CORTEX','CYPERI RHIZOMA','CITRI FRUCTUS','MOSLAE HERBA','PARIDIS RHIZOMA','ECHINOPSIS RADIX','LIMONITUM','ARISAEMA CUM BILE','STERCULIAE LYCHNOPHORAE SEMEN','LAMIOPHLOMIS HERBA','ANGELICAE PUBESCENTIS RADIX','IMPATIENTIS SEMEN','CURCUMAE LONGAE RHIZOMA','PEUCEDANI RADIX','POLYGONI MULTIFLORI CAULIS','LAGOTIDIS HERBA','DATURAE FLOS','DIOSCOREAE NIPPONICAE RHIZOMA','MANIS SQUAMA','ANDROGRAPHIS HERBA','TRACHELOSPERMI CAULIS ET FOLIUM','GENTIANAE MACROPHYLLAE RADIX','FRAXINI CORTEX','PANACIS MAJORIS RHIZOMA','RAPHANI SEMEN','NELUMBINIS SEMEN','NELUMBINIS PLUMULA','NELUMBINIS RECEPTACULUM','NELUMBINIS STAMEN','CURCUMAE RHIZOMA','NELUMBINIS FOLIUM','CINNAMOMI RAMULUS','PLATYCODONIS RADIX','PERSICAE SEMEN','PERSICAE RAMULUS','JUGLANDIS SEMEN','CORYDALIS DECUMBENTIS RHIZOMA','PRUNELLAE SPICA','BUPLEURI RADIX','CODONOPSIS RADIX','COMMELINAE HERBA','DENDROBII OFFICINALIS CAULIS','CENTELLAE HERBA','LAGGERAE HERBA','BELAMCANDAE RHIZOMA','CYNANCHI PANICULATI RADIX ET RHIZOMA','EUPHORBIAE EBRACTEOLATAE RADIX','CAMPSIS FLOS','PEGAEOPHYTIRADIXETRHIZOMA','ALPINIAE OFFICINARUM RHIZOMA','BISTORTAE RHIZOMA','DIOSCOREAE HYPOGLAUCAE RHIZOMA','PUERARIAE THOMSONII RADIX','LEONURI HERBA','ALPINIAE OXYPHYLLAE FRUCTUS','FRITILLARIAE THUNBERGII BULBUS','AESCULI SEMEN','HIPPOCAMPUS','PIPERIS KADSURAE CAULIS','SYNGNATHUS','LYGODII SPORA','SEPIAE ENDOCONCHA','SARGASSUM','SPIRODELAE HERBA','MARSDENIAE TENACISSIMAE CAULIS','TETRAPANACIS MEDULLA','AKEBIAE FRUCTUS','MORI FOLIUM','MORI CORTEX','MORI RAMULUS','TAXILLI HERBA','MORI FRUCTUS','MANTIDIS OOTHECA','DIOSCOREA PANTHAICAE RHIZOMA','SCUTELLARIAE RADIX','ASTRAGALI RADIX','ASTRAGALI RADIX PRAEPARATA CUM MELLE','COPTIDIS RHIZOMA','PHELLODENDRI CHINENSIS CORTEX','ABELMOSCHI COROLLA','POLYGONATI RHIZOMA','FIBRAUREAE CAULIS','THLASPI HERBA','SMILACIS CHINAE RHIZOMA','CUSCUTAE SEMEN','CICHORII HERBA','CHRYSANTHEMI FLOS','MUME FLOS','ILICIS ROTUNDAE CORTEX','DICHROAE RADIX','EUPATORII LINDLEYANI HERBA','STAUNTONIAE CAULIS ET FOLIUM','CHRYSANTHEMI INDICI FLOS','CNIDII FRUCTUS','SERPENTIS PERIOSTRACUM','GINKGO FOLIUM','STELLARIAE RADIX','MELO SEMEN','GLEDITSIAE FRUCTUS ABNORMALIS','POLYPORUS','SUIS FELLIS PULVIS','RANUNCULI TERNATI RADIX','EPHEDRAE HERBA','EPHEDRAE RADIX ET RHIZOMA','CERVI CORNU','CERVI CORNUS COLLA','CERVI CORNU DEGELATINATUM','CERVI CORNU PANTOTRICHUM','PYROLAE HERBA','PHYTOLACCAE RADIX','INULAE FLOS','SAIGAE TATARICAE CORNU','CLINOPODII HERBA','EPIMEDII FOLIUM','LOPHATHERI HERBA','SOJAE SEMEN PRAEPARATUM','BUDDLEJAE FLOS','DIPSACI RADIX','DRYOPTERIDIS CRASSIRHIZOMATIS RHIZOMA','DRYOPTERIDIS CRASSIRHIZOMATIS RHIZOMA CARBONISATUM','DIOSCOREAE SPONGIOSAE RHIZOMA','MYLABRIS','FARFARAE FLOS','PUERARIAE LOBATAE RADIX','DESCURAINIAE SEMEN LEPIDII SEMEN','POLYGONI AVICULARIS HERBA','BROUSSONE TIAEFRUCTUS','TRACHYCARPI PETIOLUS','SULFUR','REALGAR','FLUORITUM','VIOLAE HERBA','PEUCEDANI DECURSIVI RADIX','PERILLAE FRUCTUS','PERILLAE FOLIUM','PERILLAE CAULIS','ARNEBIAE RADIX','CALLICARPAE FORMOSANAE FOLIUM','OSMUNDAE RHIZOMA','ASTERIS RADIX ET RHIZOMA','MERETRICIS CONCHA CYCLINAE CONCHA','GECKO','SESAMI SEMEN NIGRUM','SOJAE SEMEN NIGRUM','NIGELLAE SEMEN','CYNOMORII HERBA','AJUGAE HERBA','CENTIPEDAE HERBA','SENNAE FOLIUM','FRITILLARIAE HUPEHENSIS BULBUS','TALCUM','TALCI PULVIS','ACHILLEAE HERBA','GEI HERBA','RICINISEMEN','TRIBULI FRUCTUS','TARAXACIHERBA','TYPHAEPOLLEN','AILANTHICORTEX','SOPHORAEFLOS','SOPHORAEFRUCTUS','OMPHALIA','LIQUIDAMBARISFRUCTUS','SCOLOPENDRA','VESPAENIDUS','PROPOLIS','CERAFLAVA','MEL','PHYSALISCALYXSEUFRUCTUS','ARDISIAE JAPONICAE HERBA','RHODODENDRIDAURICIFOLIUM','KADSURAECAULIS','VITICISFRUCTUS','POLYGONITINCTORIIFOLIUM','TORREYAESEMEN','ENTADAESEMEN','ARECAESEMEN','ARECAESEMENTOSTUM','ZIZIPHISPINOSAESEMEN','MAGNETITUM','SIEGESBECKIAEHERBA','VALERIANAEJATAMANSIRHIZOMAETRADIX','CICADAEPERIOSTRACUM','PAPAVERISPERICARPIUM','CAPSICIFRUCTUS','RHAPONTICIRADIX','HAEMATITUM','PRINSEPIAENUX','AGKISTRODON','VISCIHERBA','SYRINGAECORTEX','ECLIPTAEHERBA','ORYZAEFRUCTUSGERMINATUS','BOMBYXBATRYTICATUS','CARPESIIFRUCTUS','ALLII MACROSTEMONIS BULBUS','COICIS SEMEN','MENTHAE HAPLOCALYCIS HERBA','BELLADONNAE HERBA','CITRI EXOCARPIUM RUBRUM','CITRI RETICULATAE SEMEN','ACORI CALAMI RHIZOMA','LIGUSTICI RHIZOMA ET RADIX','SANTALI ALBI LIGNUM','PTEROCEPHALI HERBA','NELUMBINIS RHIZOMATIS NODUS','RUBI FRUCTUS','DIANTHI HERBA','POTENTILLAE DISCOLORIS HERBA','BUFONIS VENENUM','TRIONYCIS CARAPAX','MOSCHUS']
all_herborists_list = ['GINKGO FOLIUM']

# Domain url
domain_url = 'https://patents.google.com/?q='

# output data file
out_data_file = 'GINKGO_FOLIUM.txt'

domains = 'https://patents.google.com/'


# Parse page of patents contents
def parsePatentsContents(pageSource):
    # Beautiful soup
    pageObj = BeautifulSoup(pageSource)

    titleStr = ''
    abstractStr = ''
    descriptionStr = ''
    classificationsStr = ''
    claimsStr = ''
    download_str = ''

    try:
        # Parse content structures
        # Title
        title_item = pageObj.find(itemprop='title')
        if title_item != None:
            titleStr = title_item.get_text().encode('utf-8')

        # Abstract
        abstractItems = pageObj.find(itemprop='abstract')

        if abstractItems != None:
            abstractStr = abstractItems.get_text().replace('\n', ' ').encode('utf-8')
            if '"' in abstractStr:
                abstractStr = abstractStr.replace('"', ' ')
        else:
            print 'Abstract none!'

        # thumbnails
        thumbnailsItem = pageObj.find(itemprop='thumbnails')
        # if thumbnailsItem != None:
        #     print 'find thumbnails'
        # else:
        #     print 'thumbnails none!'

        # Classifications
        # classificationsItem = pageObj.find(itemprop='classifications')
        # if classificationsItem != None:
        #     print 'find classifications'
        #     print 'classifications none'

        # Descriptions
        descriptionItem = pageObj.find(itemprop='description')

        if descriptionItem != None:
            # print 'find description'
            # print 'Descripiton:', descriptionItem.div.get_text()

            descriptionStr = descriptionItem.get_text().replace('\n', ' ').encode('utf-8')
            # print 'Description:', descriptionStr
        else:
            print 'description none'

        sectionList = pageObj.find_all('section')
        # if sectionList != None:
        #     print 'section len:', len(sectionList)
        # else:
        #     print 'section none'

        # Claims
        claimsItem = pageObj.find(itemprop='claims')

        if claimsItem != None:
            # print 'find claims'
            claimsStr += claimsItem.get_text().replace('\n', ' ').encode('utf-8')
            # print 'Claims:', claimsStr
        else:
            print 'claims none'

        # search classification and
        # Classifications
        classificationsStr = ''
        # Images
        for sectionItem in sectionList:

            # Classifications
            if 'Classifications' == sectionItem.h2.get_text() or 'Classifications' in sectionItem.get_text():
                classificationsStr += sectionItem.get_text().replace('\n', ' ').encode('utf-8')


        # download url
        download_bar_item = pageObj.find(itemprop='pdfLink')
        # print download_bar_item
        if download_bar_item:
            if download_bar_item['href']:
                download_str = download_bar_item['href']

    except AttributeError:
        print 'Attribute Error!'

    # parse result with JSON formatting
    parseResult = {'Title': titleStr, 'Abstract': abstractStr, 'Description': descriptionStr,
                   'Classifications': classificationsStr, 'Claims': claimsStr, 'Downloadurl': download_str}


    return parseResult


# check the end pages of query result
def is_end_page(page_source):
    # parse html page with BeautifulSoup
    html = BeautifulSoup(page_source)

    # find all search result items
    articleList = html.find_all('article', {'class': 'result'})

    # the end pages of one herborist
    if articleList == None or len(articleList) == 0:
        return True
    else:
        return False


#################################################
if __name__ == '__main__':
    print '----begin----'

    browser = webdriver.Firefox()

    # save to data file
    with open(out_data_file, 'w') as out_file:

        # iterate all herborist
        for herborist_item in all_herborists_list:

            # page number
            page_num = 0

            # iterate all pages of one herbor
            while True:
                url = domain_url + str.lower(herborist_item) + '&page=' + str(page_num)

                browser.get(url)

                pageSource = browser.page_source

                if not is_end_page(pageSource):
                    # not end
                    # find all search result items
                    html = BeautifulSoup(pageSource)
                    sectionList = html.find_all('search-result-item')
                    if sectionList == None or len(sectionList) == 0:
                        break

                    # iterate the seciton of result list
                    for section in sectionList:
                        # get the url of patent contents
                        contentUrl = ''
                        if section.article.a != None:

                            # the url of patent contents
                            contentUrl = domains + section.article.a['open-result'].encode('utf-8')

                            # get patent content based on the url
                            # try:
                            #     contentPage = urllib2.urlopen(contentUrl)
                            #
                            # except Exception:
                            #     print 'Open patent content error! '
                            contentBrewser = webdriver.PhantomJS(executable_path='./phantomjs')
                            # print contentUrl
                            contentBrewser.get(contentUrl)

                            contentPage = contentBrewser.page_source


                            # get the

                            # cleaning
                            contentBrewser.quit()
                            del contentBrewser

                            # patent content parse result
                            contentResult = parsePatentsContents(contentPage)

                            # format the content parse result with ordered JSON
                            contentStr = ''
                            if contentResult != None:
                                # print '--type:', type(contentResult['Title']), contentResult['Title'].encode('utf-8')
                                print '---type:', type(contentUrl), repr(contentUrl)

                                # title string
                                title_str = ''
                                if contentResult['Title']:
                                    title_str = contentResult['Title'].encode('utf-8').strip()
                                    # print ' title type:', type(title_str)
                                # abstract string
                                abstract_str = ''
                                # if contentResult['Abstract']:
                                #     abstract_str = contentResult['Abstract'].encode('utf-8').strip()
                                #     print 'abstract type:', abstract_str
                                # description
                                # description_str = ''
                                # if contentResult['Description']:
                                #     print repr(contentResult['Description'].replace('\xc2\xb0',''))
                                #     # description_str = contentResult['Description'].replace('\xc2\xb0','').replace('\xc2\xae','').encode('utf-8').strip()
                                #     description_str = contentResult['Description'].replace('\\x[a-z0-9][a-z0-9]\\x[a-z0-9][a-z0-9]', '').encode('utf-8').strip()
                                #
                                #     print 'description type:', type(description_str)

                                # download url
                                download_url_str = ''
                                if contentResult['Downloadurl']:
                                    download_url_str = contentResult['Downloadurl'].encode('utf-8').strip()

                                    # print 'download str:', download_url_str


                                contentStr = '{"herb":"' + herborist_item + '","Title":"' + \
                                             title_str + '","Abstract":"' + \
                                             abstract_str + \
                                             '","Description":"","Url":"' + contentUrl + '","DownloadUrl":"' + download_url_str +'"}'
                            contentStr.replace('\n', '')

                            # print str(contentStr)
                            out_file.write(str(contentStr) + '\n')

                            # print contentStr

                else:
                    #end
                    break

    browser.quit()
    del browser

    print '----end-----'