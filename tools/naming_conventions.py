# coding: utf-8

import re
import os
import sys, getopt
import unidecode
import unicodedata

# rules 

def accentsTidy(s) :
# tries to convert as best as it can anything in ascii characters (° becomes deg !)
	r = unidecode.unidecode(s)
# go lower case
	r = r.lower();
# anything that is neither a letter nor a number nor a \ is replaced by _
	r = re.sub("[^\d\w\.\\\/]",'_',r);
# æ becomes ae
	r = re.sub("/æ/g","ae",r);
# œ becomes oe
	r = re.sub("/œ/g","oe",r);
# N° decomes n
	r = re.sub("ndeg","n_",r);
# remove too many '_'
	r = re.sub("__","_",r);
	r = re.sub("__","_",r);
# remove '_' at start or end of dir name in the chain of subs (_sub1_\_sub2_\_sub3_) => (sub1\sub2\sub3)
# replace '\_' by '\', '_\' by '\'
	litteral_backslash = r"\\";
	litteral_b1 = r"\\_";
	litteral_b2 = r"_\\";
	r = re.sub(litteral_b1,litteral_backslash,r);
	r = re.sub(litteral_b2,litteral_backslash,r);
# important, a '_' at beginning or end of dir chain should also be removed, else won't be able to rename	
	r = re.sub('^_','',r);
	r = re.sub('_$','',r);	
	return r;

logFile = open('logRename.txt','a')

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

def process(do_rename) :

	print("A sound will be produced at the end of the processing.")
	print("What follows is also logged into the file logRename.txt\r\n")
	print('Press <ctrl>+C to abort')
	printandlog("########################################")

	# Set the directory you want to start from
	rootDir = '.'
	nbChanges = 0
	found = 1
	while (found) :
		found = 0
		for dirName, subdirList, fileList in os.walk(rootDir):
			stripped = accentsTidy(dirName)
			if ((stripped.find(dirName)==0) and (dirName.find(stripped)==0)) : 
				printandlogNoRC('.'); 
				sys.stdout.flush()
			else :
				if (not found) : 
					nbChanges = nbChanges + 1 
					if (do_rename) :
						printandlog("");
						printandlogNoRC(stripped+"  <--  "+dirName); 
						os.rename(dirName,stripped)
						found = 1
						break
					else :
						printandlog(stripped+"  <--  "+dirName); 
					


	# BELL	
	print('\a')
	printandlog('\r\n')
	
	if (nbChanges==0):
		printandlog("no changes needed, all directories already in compliance")
	else:
		if (do_rename):
			printandlog("%i changes done" % nbChanges)
		else:
			printandlog("%i changes needed" % nbChanges)
			printandlog("this was a simulation, if you are happy with this renaming proposal, do 'naming_coventions -w'");

def test() :
	s = 'æÁÀÂÄÃÅÇÉÈÊËÍÏÎÌÑÓÒÔÖÕÚÙÛÜÝœ- áàâäãåçéèêëíìîïñóòôöõúùûüý ÿ'
	print(s)
	s1 = accentsTidy(s)
	print(s1)
	s2 = unicodedata.normalize('NFD', s1).encode('ascii', 'ignore')     
	print();
	print(s1)
	print();

def print_syntax() :
	print('syntax for simulation, with no effect on the name of the directories, for validation purposes:')
	print('naming_conventions.py')
	print('syntax for renaming effectively:')
	print('naming_conventions.py -w')


def main(argv) :
	if (len(sys.argv)==1): 
		process(0)
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
				process(1)
				sys.exit()
			else : 
				print("ignored");
				sys.exit()
		print_syntax()

if __name__ == "__main__":
   main(sys.argv[1:])