import pyPdf

file = '/Users/heermaster/Documents/UM/2015chinesemedicinedict/CMD1.pdf'
# file = '/Users/heermaster/Documents/pdf/scrapy.pdf'

pdf = pyPdf.PdfFileReader(open(file, 'rb'))

# print len(pdf.pages)
index = 0
for page in pdf.pages:
    contents = page.extractText()
    # contents = contents.encode('utf-8')
    contentStr = contents.encode('utf-8')
    print type(contents.encode('utf-8')), contentStr
    if index == 1:
        exit()
    index += 1



