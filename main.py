import PyPDF2
from sys import argv

len = len(argv)
pdffiles = []

if len >= 2:
    for i in range(1, len):
        if '.pdf' not in argv[i]:
            print('Invalid file(s) type!')
            exit(0)
    pdffiles = [argv[i] for i in range(1, len)]

else:
    print("No arguments entered!\nPlease Try Again.")
    exit(0)

merger = PyPDF2.PdfMerger()

try:
    for filename in pdffiles:
        file = open(filename, 'rb')
        reader = PyPDF2.PdfReader(file)
        merger.append(reader)

    file.close()
    merger.write(argv[1] + "_merged.pdf")

except (OSError, IOError) as e:
    print(e)
    exit(0)

