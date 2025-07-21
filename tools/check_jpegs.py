# Import the os module, for the os.walk function
import os
from PIL import Image
import sys

logFileName = 'check_jpegs.log'
logFile = open(logFileName,'a', encoding="utf-8")

def printandlog(str):
    print(str)
    logFile.write(str+"\n")
    return

def printandlogNoRC(str):
    print(str, end='')
    logFile.write(str)
    return


# this code also should work for other compressions, with little changes

def isJpeg(fname):
    if (fname.lower().endswith(".jpg")) :
        return True
    if (fname.lower().endswith(".jpeg")) :
        return True
    return False

def process(fullCheck):

    # Set the directory you want to start from
    rootDir = '.'
    currentPath = os.getcwd()

    printandlog('Searching for corrupted .jpg and .jpeg files')
    printandlog('Each . shows that one more directory was parsed')
    if (fullCheck):
        printandlog('Full sanity check')
    else:
        printandlog('This step does not check the whole file, but only the header and some consistency')
        printandlog('Use check_jpeg_full for a deeper sanity check')
    printandlog('Processing directory '+currentPath)
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
    #       print('\t%s' % fname)
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
                    printandlogNoRC('\r\n'+dirName+'/'+fname+"----->invalid file, not a jpeg ?")
                    badFilesCount = badFilesCount+1
        if (found==1) :
            allDirCount = allDirCount + 1

    printandlog('\r\n')
    if (badFilesCount>0) :
        logs = f"found {badFilesCount} bad file(s) among {allJPGFilesCount} jpeg files in {allDirCount} directories"
        printandlog(logs);
    else :
        logs = f"All {allJPGFilesCount} jpeg files in {allDirCount} directories (containing jpeg images) passed the sanity check. No problem."
        printandlog(logs);

    # BELL  
    print('\a')
#   os.system("pause")


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

