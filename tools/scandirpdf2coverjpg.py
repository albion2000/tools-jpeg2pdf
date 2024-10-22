# Import the os module, for the os.walk function
import os
import img2pdf
import sys

import PyPDF2
from wand.image import Image
import io

# parts of the code from https://gist.github.com/penghou620/80d9831056b76ee2025b3b7873b2ff4a

def pdf_page_to_jpg(src_pdf, pagenum = 0, resolution = 72,):
   
#    Returns specified PDF page as wand.image.Image png.
#    :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
#    :param int pagenum: Page number to take.
#    :param int resolution: Resolution for resulting png in DPI.
    
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(pagenum))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file = pdf_bytes, resolution = resolution)
    img.convert("jpg")

    return img


# Main
# ====

def convert(src_filename):
    
    src_pdf = PyPDF2.PdfFileReader(open(src_filename, "rb"))

    # What follows is a lookup table of page numbers within sample_log.pdf and the corresponding filenames.
    pages = [{"pagenum": 0,  "filename": src_filename},
			]

    # Convert each page to a png image.
    for page in pages:
        big_filename = page["filename"] + ".jpg"

        img = pdf_page_to_jpg(src_pdf, pagenum = page["pagenum"], resolution = 150)
        img.save(filename = big_filename)



logFileName = 'logpdf2coverpng.txt'

logFile = open(logFileName,'a')

def printandlog(str):
	print(str)
	logFile.write(str+"\n")
	return

def printandlogNoRC(str):
	print(str, end='')
	logFile.write(str)
	return

def printandlogTuple(tuple):
	print(tuple)
	logFile.write(''.join(tuple))
	return

def isPdf(fname):
	if (fname.lower().find(".pdf") == len(fname)-4) :
		return True
	return False

print("A sound will be produced at the end of the processing.")
print("What follows is also logged at the end of the file "+logFileName+"\r\n")
print('Press <ctrl>+C to abort')
printandlog("########################################")

# Set the directory you want to start from
rootDir = '.'
failedFiles = ();
failedfilesCount = 0
nbPdf = 0
for dirName, subdirList, fileList in os.walk(rootDir):
	files = ();
	found = 0;
	for fname in fileList:
		if (isPdf(fname)):
			print('.', end='')
			nbPdf = nbPdf + 1
			infile = dirName+'\\'+fname
			command = "extracting cover from "+infile
			printandlogNoRC(command)
			try :
				convert(infile);
#				if (not (os.system(command)==0)):
#					printandlog('  --->>> **********conversion from pdf to txt failed for some reason**********')
#					newFailedFilesTuple = (infile+'	',);
#					failedFiles = failedFiles + newFailedFilesTuple
#					failedfilesCount = failedfilesCount+1				
			except KeyboardInterrupt:
				sys.exit(0)
				break
			except : 
				printandlog('  --->>> **********conversion from pdf to cover image failed for some reason**********')
				newFailedFilesTuple = (infile+'	',);
				failedFiles = failedFiles + newFailedFilesTuple
				failedfilesCount = failedfilesCount+1
			printandlog(' ')
	 
if (failedfilesCount>0) :
	printandlog('\r\n\r\n%i cover(s) could not be extracted (see potential reason looking up), here is the list :' % failedfilesCount)
	printandlogTuple(failedFiles)
else: 
	printandlog('All covers extracted with NO ERROR')

print("See also at the end of the log file "+logFileName+"\r\n")

logFile.close()
# BELL
print('\a')
os.system("pause")
