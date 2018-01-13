# Import the os module, for the os.walk function
import os
from PIL import Image
import sys

print('Searching for corrupted .jpg and .jpeg files')
print('Each . shows that one more directory was parsed')
print('This step does not check the whole file, but only the header and some consistency')
print('Press <ctrl>+C to abort')
# Set the directory you want to start from
rootDir = '.'
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

		thisisajpeg = 0
# this code also should work for other compressions
		extposjpg = fname.find(".jpg")
		if (extposjpg == len(fname)-4) :
		  thisisajpeg = 1
		extposjpg = fname.find(".jpeg")
		if (extposjpg == len(fname)-4) :
		  thisisajpeg = 1
		if (thisisajpeg==1):
			found = 1;
			allJPGFilesCount = allJPGFilesCount+1
			newTuple = (dirName+'/'+fname,);
			files = files + newTuple
			try :
				im = Image.open(dirName+'/'+fname)
# that's one way to enforce reading the whole file, but since it is not faster than img2pdf, this is not interesting.
# but could be for a general full sanity check
#				box = (10, 10, 20, 20)
#				region = im.crop(box)
			except IOError :
				print('\r\n'+dirName+'/'+fname+"----->invalid file, not a jpeg ?")
				badFilesCount = badFilesCount+1
	if (found==1) :
		allDirCount = allDirCount + 1
		
print('\r\n')
if (badFilesCount>0) :
	print('found %i bad file(s)' % badFilesCount);
else :
	print('All %i jpeg files in %i directories (containing jpeg images) passed the sanity check. No problem.' % (allJPGFilesCount,allDirCount));

# BELL	
print('\a')
os.system("pause")