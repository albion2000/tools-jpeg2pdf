# tools-jpeg2pdf

The primary source code repository for these tools is https://github.com/albion2000/tools-jpeg2pdf

The releases are here : https://github.com/albion2000/tools-jpeg2pdf/releases

Tools to help massive conversions from page scans to pdf documents ready for ocr using tools like Adobe Acrobat DC

They are functional, tested with Windows 10, on about 14000 pages, special cases will probably happen to you. Please report in case of problems.

One purpose is to keep the tools as simple as possible (KISS), refraining from feature creep. It might be better to create a new derived tool instead of crippling the current tool.

Some small adaptations will be necessary for it to run with linux, small changes like replacing '\' by '/' for the path. 

In short :

## naming_conventions.py & naming_conventions_do_rename.py

Read the installation_instructions.txt and readme_naming_conventions.txt

Copy 'naming_conventions.py' & 'naming_conventions_do_rename.py' to the root directory of your file tree.

The primary purpose of this tool is to ensure a longer lifetime to a directory tree by reducing the risk of it being corrupted over transfers between file systems.

It recursively parses sub directories.
It is able to rename the directories in order to follow some strict conventions.

mode for simulation, with no effect on the name of the directories, for validation purposes:
  * naming_conventions.py
  
mode for renaming effectively:
  * naming_conventions_do_rename.py

The use of this tool is optional, and would be typically used before using scandir2pdf.py

Rules followed : 
1)tries to convert as best as it can anything in ascii characters
2)go lower case
3)anything that is neither a letter nor a number nor a \ nor '-' is replaced by _
4)ae,oe handled, reduce '__' to '_', remove '_' at start and end. 

## check_jpegs.py & check_jpegs_full.py

Read the installation_instructions.txt and readme_check_jpegs.txt

Copy 'check_jpegs.py' & 'check_jpegs_full.py' to the root directory of your file tree.

It recursively parses sub directories for .jpeg and .jpg files

For a quick check that the files are not fully corrupted. 
It is, on purpose, a fast check in order to help detect rapidly bad files. 
Only the headers are checked, the images are not decompressed. 
This is a quick way to detect bad jpeg files, before using scandir2pdf.py
  * check_jpegs.py

For a full check, much slower (useful also for your family pictures)
  * check_jpegs_full.py

Each '.' shows that one more directory was parsed

When a file is reported corrupted, it does not mean that it is lost. Try to open it in your favorite image sw and save it back (using the best quality, in order to reduce compression losses). It is often enough.
If you can't open it, try to open it with other image tools. Not all handle file corruption the same way.


## scandir2pdf.py

Read the installation_instructions.txt and readme_scandir2pdf.txt for recommendations and use

Copy 'scandir2pdf.py' to the root directory of your file tree.

It recursively parses sub directories for .jpeg and .jpg file 

For each directory X, the tool scandir2pdf regroups the image files in a file named X.pdf. And moves it to the upper stage in the file tree.

It is built upon img2pdf, which ensures no jpeg recompression and the best possible quality.

Logs progress, errors and final report in the console and in the file "logParse.txt"

## after scandir2pdf you would use an OCR software of your choice.

## scandirpdf2txt.py

Read the installation_instructions.txt and readme_scandirpdf2txt.txt for recommendations and use

It recursively parses sub directories for .pdf files 

Provided that these where previously processed with an OCR Optical Character Recognition software, 
it will extract their text into .txt files 