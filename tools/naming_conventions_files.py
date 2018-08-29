# coding: utf-8

# toutes les chaines sont en unicode (même les docstrings)
from __future__ import unicode_literals

import re
import os
import sys, getopt
import unidecode
import unicodedata


# rules 


def ridoffbadchars(s) :
	r = s;
# as a last resort get rid of still unknown unicode characters	
	r = re.sub("\uf018","_",r);
	r = re.sub("\uf019","_",r);
	r = re.sub("\uf020","_",r);
	r = re.sub("\uf021","_",r);
	r = re.sub("\uf022","_",r);
	r = re.sub("\uf023","_",r);
	r = re.sub("\uf024","_",r);
	r = re.sub("\uf025","_",r);
	r = re.sub("\uf026","_",r);
	r = re.sub("\uf027","_",r);
	r = re.sub("\uf028","_",r);
	r = re.sub("\uf029","_",r);
	r = re.sub("\uf030","_",r);
	r = re.sub("\uf031","_",r);
	
	return r;
	

def accentsTidyP1(s) :
# special case of '.\' to keep for the root dirs...
	if ((s[0]=='.') and (s[1]=='\\')) :
		return '.'+'\\'+accentsTidy(s[2:]);

# tries to convert as best as it can anything in ascii characters (special case : '°' becomes 'deg' !)
	r = unidecode.unidecode(s)
	
# go lower case
	r = r.lower();
# æ becomes ae
	r = re.sub("/æ/g","ae",r);
# œ becomes oe
	r = re.sub("/œ/g","oe",r);
	
	return r;

def accentsTidyP2(s) :
# N° decomes n_
	r = re.sub("ndeg ","#",s);
	r = re.sub("ndeg","#",s);
# remove too many '_'
	r = re.sub("__","_",r);
	r = re.sub("__","_",r);
# remove too many '_-_'
	r = re.sub("_-_","-",r);
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

	r = re.sub("degdeg","deg",r);
	r = re.sub("degdeg","deg",r);
	r = re.sub("degdeg","deg",r);
	r = re.sub("degdeg","deg",r);
	r = re.sub("degdeg","deg",r);

	r = re.sub('_deg$','',r);
	r = re.sub('deg$','',r);

# as a last resort get rid of still unknown unicode characters	
	r = ridoffbadchars(r);
			
	return r;

def accentsTidy(s) :
	r = accentsTidyP1(s);
# anything that is neither a letter nor a number nor a \ nor '-' is replaced by _
	r = re.sub("[^-\d\w\\\/]",'_',r);
	return accentsTidyP2(r);

def accentsTidyFiles(s) :
	r = accentsTidyP1(s)
# anything that is neither a letter nor a number nor a \ nor '-' nor '.' is replaced by _
	r = re.sub("[^-.(&)#\d\w\\\/]",'_',r);
#only keep the last '.'
	pcount = r.count('.')
	if (pcount>1) :
		r = r.replace('.','_',pcount-1);
	return accentsTidyP2(r);



logFileName = 'logrename.txt'
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

def same_string(a,b):
	return ((a.find(b)==0) and (b.find(a)==0))

def process(do_rename_dir, do_rename_files) :

	print("A sound will be produced at the end of the processing.")
	print("What follows is also logged into the file logRename.txt\r\n")
	print('Press <ctrl>+C to abort')
	printandlog("########################################")

	# Set the directory you want to start from
	rootDir = '.'
	nbChanges = 0

# Simulation : we only parse the subs, don't need the full path
	if (not do_rename_dir):
		nbDir = 0
		for dirName, subdirList, fileList in os.walk(rootDir):
			for subdir in subdirList :
				if subdir == '__pycache__' :
					continue
				stripped = accentsTidy(subdir)
				nbDir = nbDir + 1
				if (same_string(stripped,subdir)) : 
					printandlogNoRC('.'); 
					sys.stdout.flush()
				else :
					nbChanges = nbChanges + 1 
					printandlog("\n"+dirName+"\\"+stripped+"  <--  "+dirName+"\\"+ridoffbadchars(subdir)); 				
	else:
# Real Deal, we parse all the dirs using path from the rootDir, one by one, in O(n2)... Slow, not smart, but small code.
		found = 1
		while (found) :
			found = 0
			nbDir = 0
			for dirName, subdirList, fileList in os.walk(rootDir):
				if dirName == '.' :
					continue
				if dirName == '..' :
					continue
				if dirName == '.\\__pycache__' :
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
						printandlog(stripped+"  <--  "+ridoffbadchars(dirName)); 
						try:
							os.rename(dirName,stripped)
						except:
							print("Renaming was refused by the PC. Check that you don't have a file open in the file tree. You might need to close some file explorer");
							return;
						found = 1
						break


	# BELL	
	print('\a')
	printandlog('\n')
	
	if (nbChanges==0):
		printandlog("no change needed, all %i directories are already in compliance" % nbDir)
	else:
		if (do_rename_dir):
			printandlog("%i change(s) done in a total of %i directories" % (nbChanges,nbDir))
		else:
			printandlog("%i change(s) needed in a total of %i directories" % (nbChanges,nbDir))
			printandlog("this was a simulation, if you are happy with this renaming proposal, use 'naming_conventions_do_rename.py'");
	print("\nAll this was logged at the end of the file "+logFileName);

	nbFiles = 0
	nbFileChanges = 0
				
	if (not do_rename_files):
		for dirName, subdirList, fileList in os.walk(rootDir):
			if dirName == '..' :
				continue
			if dirName == '.\\__pycache__' :
				continue
			for file in fileList :
				stripped = accentsTidyFiles(file)
				nbFiles = nbFiles + 1
				if (same_string(stripped,file)) : 
					printandlogNoRC('*'); 
					sys.stdout.flush()
				else :
					nbFileChanges = nbFileChanges + 1 
					printandlog("\n"+dirName+"\\"+stripped+"  <--  "+ridoffbadchars(file)); 
				
	else:
# Real Deal, we parse all the files using path from the rootDir, one by one, in O(n2)... Slow, not smart, but small code.
		found = 1
		while (found) :
			found = 0
			for dirName, subdirList, fileList in os.walk(rootDir):
				if dirName == '.\\__pycache__' :
					continue
			
				for file in fileList :
					stripped = accentsTidyFiles(file)
					nbFiles = nbFiles + 1
					if (same_string(stripped,file)) : 
						printandlogNoRC('*'); 
						sys.stdout.flush()
					else :
						nbFileChanges = nbFileChanges + 1 
						orig_full_path = dirName+"\\"+file
						stripped_full_path = dirName+"\\"+stripped;
						printandlog("\n"+dirName+"\\"+stripped+"  <--  "+ridoffbadchars(file)); 
						try:
							os.rename(orig_full_path,stripped_full_path)
						except:
							print("Renaming was refused by the PC. Check that you don't have a file open in the file tree. You might need to close some file explorer");
							return;
						found = 1

						
	# BELL	
	print('\a')
	printandlog('\n')
	
	if (nbFileChanges==0):
		printandlog("no change needed, all %i files are already in compliance" % nbFiles)
	else:
		if (do_rename_files):
			printandlog("%i change(s) done in a total of %i files" % (nbFileChanges,nbFiles))
		else:
			printandlog("%i change(s) needed in a total of %i files" % (nbFileChanges,nbFiles))
			printandlog("this was a simulation, if you are happy with this renaming proposal, use 'naming_conventions_do_rename.py'");
	print("\nAll this was logged at the end of the file "+logFileName);


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
	os.system("pause")


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