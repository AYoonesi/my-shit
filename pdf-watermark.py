import PyPDF2

# Openning initial pdf
file = open('Candide.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)
page = reader.getPage(0)

# Opening my watermark
water = open('w.pdf', 'rb')
reader2 = PyPDF2.PdfFileReader(water)
waterpage = reader2.getPage(0)

# Merging both pdfs
page.mergePage(waterpage)
writer =PyPDF2.PdfFileWriter()
writer.addPage(page)

# The remaining pages to be added
for pageNum in range(1, reader.numPages):
    pageObj = reader.getPage(pageNum)
    writer.addPage(pageObj)
    
# Saving and closing the file
resultFile = open('Candide - @Ghasayan.pdf', 'wb')
writer.write(resultFile)
file.close()
water.close()
resultFile.close()
