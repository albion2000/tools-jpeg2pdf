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

def process(do_rename_dir, do_rename_files) :

	# Set the directory you want to start from
	rootDir = '.'
	nbFiles = 0
				
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
				printandlog("%i %s" % (reader.getNumPages(),orig_full_path)); 
				sys.stdout.flush()
				nbFiles = nbFiles + 1
				
	# BELL	
	print('\a')
	printandlog('\n')
	

def print_syntax() :
	print('hello !')


def main(argv) :
	if (len(sys.argv)==1): 
		process(0,0)
		os.system("pause")
	else : 
		try:
			opts, args = getopt.getopt(argv,"hw")
		except getopt.GetoptError:
			print_syntax()
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print_syntax()
				sys.exit()
			elif opt == '-w':
				process(0,1)
				os.system("pause")
				sys.exit()
			else : 
				print("ignored");
				os.system("pause")
				sys.exit()
		print_syntax()

if __name__ == "__main__":
   main(sys.argv[1:])