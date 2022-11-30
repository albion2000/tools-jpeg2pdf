# coding: utf-8

# toutes les chaines sont en unicode (même les docstrings)
#from __future__ import unicode_literals

import re
import os
import sys, getopt
#import unidecode
#import unicodedata
#import PyPdf2

# rules 
from PyPDF2 import PdfFileReader

logFileName = 'logCountPages.txt'
logFile = open(logFileName,'a')

def isPdf(fname):
	if (fname.lower().find(".pdf") == len(fname)-4) :
		return True
	return False

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

def same_string(a,b):
	return ((a.find(b)==0) and (b.find(a)==0))

def process() :

	# Set the directory you want to start from
	rootDir = '.'
	nbFiles = 0
	fails = 0
	totalPages = 0
				
	printandlog("")
	
	for dirName, subdirList, fileList in os.walk(rootDir):
		if dirName == '..' :
			continue
		if dirName == '.\\__pycache__' :
			continue
		for file in fileList :
			orig_full_path = dirName+"\\"+file
			if isPdf(orig_full_path) :
				reader = PdfFileReader(open(orig_full_path,"rb"))
				try:
					nbPages = reader.getNumPages()
					totalPages += nbPages
					printandlog("%i %s" % (nbPages,orig_full_path))
				sys.stdout.flush()
				nbFiles = nbFiles + 1
				except:
					printandlog("####### Could not properly open %s. It may be password protected, corrupted or just protected against modification" % (orig_full_path))
					fails+=1

	printandlog("Total %i documents" % (nbFiles))
	printandlog("Total %i pages" % (totalPages))
	printandlog("%i pdf(s) could not be properly open. These may be password protected, corrupted or just protected against modification" % (fails))
				
	# BELL	
	print('\a')
	printandlog('\n')
	

def print_syntax() :
	print('hello !')


def main(argv) :
	process()
		os.system("pause")

if __name__ == "__main__":
   main(sys.argv[1:])