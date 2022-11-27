# Import the os module, for the os.walk function
import os
import img2pdf
import sys
import shutil

import PyPDF2
from wand.image import Image	
import io

from PyPDF2 import PdfFileWriter, PdfFileReader


# Main
# ====

def convert(src_filename):

	with open(src_filename, "rb") as fin:
		src_pdf = PdfFileReader(fin)
		dst_pdf = PdfFileWriter()

		number_of_pages = src_pdf.getNumPages()
	# Create Sub Dir using the truncated_fname
		truncated_fname = src_filename[0:len(src_filename)-4]

		dst_filename = truncated_fname+".tmp.pdf"

		for x in range(number_of_pages):
			page = src_pdf.getPage(x)
			dst_pdf.addPage(page)

		dst_pdf.removeText()

		with open(dst_filename, 'wb') as f:
		   dst_pdf.write(f)
		
		f.close()
		fin.close()
		shutil.copyfile(dst_filename,src_filename)  
		os.remove(dst_filename);


logFileName = 'logpdf2noocr.txt'

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
			command = "removing OCR from"+infile
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
				printandlog('  --->>> **********removal of OCR failed for some reason**********')
				newFailedFilesTuple = (infile+'	',);
				failedFiles = failedFiles + newFailedFilesTuple
				failedfilesCount = failedfilesCount+1
			printandlog(' ')
	 
if (failedfilesCount>0) :
	printandlog('\r\n\r\n%i documents could not be processed (see potential reason looking up), here is the list :' % failedfilesCount)
	printandlogTuple(failedFiles)
else: 
	printandlog('All pdf processed with NO ERROR')

print("See also at the end of the log file "+logFileName+"\r\n")

logFile.close()
# BELL
print('\a')
os.system("pause")
