# Import the os module, for the os.walk function
import os
import img2pdf
import sys

logFileName = 'logpdf2txt.txt'

logFile = open(logFileName,'a')

try :
	checkItisHere = open("pdftotext.exe","rb")
except : 
	print("for this tool to run, you need also pdftotext.exe along here");
	sys.exit()
	
checkItisHere.close()


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
			infile = '\"'+dirName+'\\'+fname+'\"'
			command = "pdftotext.exe -raw "+infile
			printandlogNoRC(command)
			try :
				if (not (os.system(command)==0)):
					printandlog('  --->>> **********conversion from pdf to txt failed for some reason**********')
					newFailedFilesTuple = (infile+'	',);
					failedFiles = failedFiles + newFailedFilesTuple
					failedfilesCount = failedfilesCount+1				
			except KeyboardInterrupt:
				sys.exit(0)
				break
			except : 
				printandlog('  --->>> **********conversion from pdf to txt failed for some reason**********')
				newFailedFilesTuple = (infile+'	',);
				failedFiles = failedFiles + newFailedFilesTuple
				failedfilesCount = failedfilesCount+1
			printandlog(' ')
	 
if (failedfilesCount>0) :
	printandlog('\r\n\r\n%i file(s) could not be converted (see potential reason looking up), here is the list :' % failedfilesCount)
	printandlogTuple(failedFiles)
else: 
	printandlog('All files converted with NO ERROR')

print("See also at the end of the log file "+logFileName+"\r\n")

logFile.close()
# BELL
print('\a')
os.system("pause")
