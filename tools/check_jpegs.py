# Import the os module, for the os.walk function
import os
from PIL import Image
import sys


# this code also should work for other compressions, with little changes

def isJpeg(fname):
	if (fname.lower().find(".jpg") == len(fname)-4) :
		return True
	if (fname.lower().find(".jpeg") == len(fname)-4) :
		return True
	return False

def process(fullCheck):

	# Set the directory you want to start from
	rootDir = '.'
	currentPath = os.getcwd()

	print('Searching for corrupted .jpg and .jpeg files')
	print('Each . shows that one more directory was parsed')
	if (fullCheck):
		print('Full sanity check')
	else:
		print('This step does not check the whole file, but only the header and some consistency')
	print('Processing directory '+currentPath)
	print('Press <ctrl>+c to abort')
	badFilesCount = 0
	allJPGFilesCount = 0
	allDirCount = 0
	for dirName, subdirList, fileList in os.walk(rootDir):
		print('.', end=''); 
		sys.stdout.flush()
		files = ();
		found = 0;
		currentPath = os.getcwd();
		for fname in fileList:
	#		print('\t%s' % fname)
			if (isJpeg(fname)):
				found = 1;
				allJPGFilesCount = allJPGFilesCount+1
				newTuple = (dirName+'/'+fname,);
				files = files + newTuple
				try :
					im = Image.open(dirName+'/'+fname)
	# that's one way to enforce reading the whole file, but since it is not faster than img2pdf, this is not interesting.
	# but could be for a general full sanity check
					if (fullCheck):
						box = (10, 10, 20, 20)
						region = im.crop(box)
				except IOError :
					print('\r\n'+dirName+'/'+fname+"----->invalid file, not a jpeg ?",end='')
					badFilesCount = badFilesCount+1
		if (found==1) :
			allDirCount = allDirCount + 1

	print('\r\n')
	if (badFilesCount>0) :
		print('found %i bad file(s) among %i jpeg files in %i directories' % (badFilesCount,allJPGFilesCount,allDirCount));
	else :
		print('All %i jpeg files in %i directories (containing jpeg images) passed the sanity check. No problem.' % (allJPGFilesCount,allDirCount));

	# BELL	
	print('\a')
#	os.system("pause")


def print_syntax() :
	print('syntax for just checking the file headers, for quick validation purposes:')
	print('check_jpegs.py')
	print('syntax for full file checking:')
	print('check_jpegs.py -f')
	os.system("pause")



def main(argv) :
	if (len(sys.argv)==1): 
		process(0)
		os.system("pause")
	else : 
		try:
			opts, args = getopt.getopt(argv,"hf")
		except getopt.GetoptError:
			print_syntax()
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print_syntax()
				sys.exit()
			elif opt == '-f':
				process(1)
				os.system("pause")
				sys.exit()
			else : 
				print("ignored");
				os.system("pause")
				sys.exit()
		print_syntax()

if __name__ == "__main__":
	main(sys.argv[1:])

