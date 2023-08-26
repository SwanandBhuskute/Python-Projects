import PyPDF2

pdf_files = ["Electrostatic Potential and Capacitance.pdf", "vectors.pdf"]

merger = PyPDF2.PdfMerger()

for f in pdf_files:
    pdf_file = open(f, 'rb')
    pdf_read = PyPDF2.PdfReader(pdf_file)
    merger.append(pdf_read)

pdf_file.close()
merger.write("merged.pdf")