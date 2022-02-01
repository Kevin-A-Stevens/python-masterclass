import PyPDF2

with open("./PDF/dummy.pdf", "rb") as file:  # rb = read binary
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)  # 1
    print(reader.getPage(0))

    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("./PDF/tilt.pdf", "wb") as new_file:
        writer.write(new_file)






