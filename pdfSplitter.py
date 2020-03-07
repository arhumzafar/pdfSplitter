from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
 
 
pdf_document = "./DocumentName.pdf" #your target document and script should be in the same folder
pdf = PdfFileReader(pdf_document)
 
for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    pdf_writer.addPage(current_page)
 
    outputFileName = f"DocumentName{page}.pdf"
    with open(outputFileName, "wb") as out:
        pdf_writer.write(out) #these new documents will save to your current working directory
 
        print("Created: ", outputFileName)