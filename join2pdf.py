import PyPDF2
print('Enter first pdf file to join with.')
pdf1 = input()
print('Enter second pdf file to join with first pdf file.')
pdf2 = input()
print('Enter the name for newly created pdf file.')
pdf3 = input()
pdf1File = open(pdf1, 'rb')
pdf2File = open(pdf2, 'rb')
pdf1Reader =PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
	pageObj = pdf1Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
	pageObj = pdf2Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

pdfOutputFile = open(pdf3, 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
