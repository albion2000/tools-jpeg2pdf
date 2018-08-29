
from PyPDF2 import PdfFileReader
from pprint import pprint
import sys

import re
import os
import getopt
import unidecode
import unicodedata

# pip install pypdf

logFileName = 'log_check_pdf.txt'
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

def isPDF(fname):
	if (fname.lower().find(".pdf") == len(fname)-4) :
		return True
	return False

def main(argv) :

	rootDir = '.'
	nbFiles = 0
	nbFileWrong = 0
    
	print('Searching for corrupted .pdf files')
	print('Each * shows that one more pdf file was checked ok')
	print('Processing directory '+rootDir)
	printandlog("########################################")
				
	for dirName, subdirList, fileList in os.walk(rootDir):
		if dirName == '..' :
			continue
		if dirName == '.\\__pycache__' :
			continue
		for filename in fileList :
			fullfilename = dirName+"\\"+filename
			if (isPDF(fullfilename)):
				nbFiles = nbFiles + 1
				try :
					mypdf = PdfFileReader(fullfilename)
					fonts = set()
					embedded = set()
					try :
						for page in mypdf.pages:
							obj = page.getObject()
						printandlogNoRC('*'); 
						sys.stdout.flush()
					except:
						printandlogNoRC("\n"+fullfilename+" MAY BE corrupted")
						nbFileWrong = nbFileWrong + 1 
					
				except:
					printandlogNoRC("\n"+fullfilename+" IS PROBABLY corrupted")
					nbFileWrong = nbFileWrong + 1 

						
	# BELL	
	print('\a')
	printandlog('\n')
	
	if (nbFileWrong==0):
		printandlog("All OK, all %i pdf files are OK" % nbFiles)
	else:
		printandlog("%i corrupted in a total of %i pdf files" % (nbFileWrong,nbFiles))

	print("\nAll this was logged at the end of the file "+logFileName);


if __name__ == "__main__":
   main(sys.argv[1:])