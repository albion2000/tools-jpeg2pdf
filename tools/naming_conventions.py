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

def same_string(a,b):
	return ((a.find(b)==0) and (b.find(a)==0))

def process(do_rename) :

	print("A sound will be produced at the end of the processing.")
	print("What follows is also logged into the file logRename.txt\r\n")
	print('Press <ctrl>+C to abort')
	printandlog("########################################")

	# Set the directory you want to start from
	rootDir = '.'
	nbChanges = 0

# Simulation : we only parse the subs, don't need the full path
	if (not do_rename):
		nbDir = 0
		for dirName, subdirList, fileList in os.walk(rootDir):
			for subdir in subdirList :
				stripped = accentsTidy(subdir)
				nbDir = nbDir + 1
				if (same_string(stripped,subdir)) : 
					printandlogNoRC('.'); 
					sys.stdout.flush()
				else :
					nbChanges = nbChanges + 1 
					printandlog("\n"+dirName+"\\"+stripped+"  <--  "+dirName+"\\"+subdir); 
	else:
# Real Deal, we parse all the dirs using path from the rootDir, one by one. Slow, not smart, but small code.
		found = 1
		while (found) :
			found = 0
			nbDir = 0
			for dirName, subdirList, fileList in os.walk(rootDir):
				if dirName == '.' :
					continue
				if dirName == '..' :
					continue
				stripped = accentsTidy(dirName)
				nbDir = nbDir + 1
				if (same_string(stripped,dirName)) : 
					printandlogNoRC('.'); 
					sys.stdout.flush()
				else :
					if (not found) : 
						nbChanges = nbChanges + 1 
						printandlog("");
						printandlog(stripped+"  <--  "+dirName); 
						try:
							os.rename(dirName,stripped)
						except:
							print("Renaming was refused by the PC. Check that you don't have a file open in the file tree. You might need to close some file explorer");
							sys.exit()
						found = 1
						break
					


	# BELL	
	print('\a')
	printandlog('\n')
	
	if (nbChanges==0):
		printandlog("no change needed, all %i directories are already in compliance" % nbDir)
	else:
		if (do_rename):
			printandlog("%i change(s) done in a total of %i directories" % (nbChanges,nbDir))
		else:
			printandlog("%i change(s) needed in a total of %i directories" % (nbChanges,nbDir))
			printandlog("this was a simulation, if you are happy with this renaming proposal, do 'naming_conventions -w'");

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