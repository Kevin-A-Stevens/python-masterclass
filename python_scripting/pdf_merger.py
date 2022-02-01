# python3 pdf_merger.py ./PDF/dummy.pdf ./PDF/twopage.pdf ./PDF/tilt.pdf
import PyPDF2
import sys

inputs = sys.argv[1:] # grab all arguments

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("./PDF/super.pdf")
pdf_combiner(inputs)

