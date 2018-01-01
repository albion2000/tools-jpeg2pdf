# Import the os module, for the os.walk function
import os
import img2pdf
import sys

logFile = open('logParse.txt','a')


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

#os.getcwd()

print("A sound will be produced at the end of the processing.")
print("What follows is also logged into the file logParse.txt\r\n")
print('Press <ctrl>+C to abort')
printandlog("########################################")

# Set the directory you want to start from
rootDir = '.'
failedFiles = ();
failedfilesCount = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    files = ();
    found = 0;
    currentPath = os.getcwd();
    nbpages = 0
    for fname in fileList:
        thisisajpeg = 0
        extposjpg = fname.find(".jpg")
        if (extposjpg == len(fname)-4) :
          thisisajpeg = 1
        extposjpg = fname.find(".jpeg")
        if (extposjpg == len(fname)-4) :
          thisisajpeg = 1
        if (thisisajpeg==1):
          found = 1;
          nbpages = nbpages + 1
          newTuple = (dirName+'/'+fname,);
          files = files + newTuple 
    if (found==1):
#  extract the name of the directory
      outfile = dirName+'.pdf';
      printandlogNoRC('-->%s (%i pages)' % (outfile,nbpages))
      with open(outfile,"wb") as f:
        try :  
          f.write(img2pdf.convert(*files))
          f.flush()
          f.close()
          printandlog(' ')
        except MemoryError:
          f.close()
          printandlog('--->>> **********convertion to pdf failed by lack of memory???**********')
          newFailedFilesTuple = (outfile+'  ',);
          failedFiles = failedFiles + newFailedFilesTuple
          failedfilesCount = failedfilesCount+1
        except img2pdf.ImageOpenError:
          f.close()
          printandlog('--->>> convertion to pdf failed due to a bad jpeg file format???')
          newFailedFilesTuple = (outfile+'  ',);
          failedFiles = failedFiles + newFailedFilesTuple
          failedfilesCount = failedfilesCount+1
          
if (failedfilesCount>0) :
  printandlog('\r\n\r\n%i files could not be converted for some reason, here is the list :' % failedfilesCount)
  printandlogTuple(failedFiles)
  printandlog('\r\nIf it is by lack of memory you might just try to go parse directly these only. It can work. Using the 64 bits version of python might help also.');
else: 
  printandlog('All files converted with NO ERROR')

logFile.close()
# BELL
print('\a')
