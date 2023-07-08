rem This is to do once after the python installation
pip install pillow=8.0.1
pip install PyPDF2==1.26.0
pip install img2pdf==0.4.4
pip install unidecode

pip install wand==0.6.7

rem wand is needed only for the tools scandirpdf2cover, scandirpdf2jpg and scanditpdf2png that extract images from pdfs
rem wand requires ghostscript to be installed (the pc windows version, not the python version) install the 64bit if you use python 64bits
rem https://ghostscript.com/releases/gsdnld.html
rem wand requires also imageMagick to be installed.  (the pc windows version, not the python version) install the 64bit if you use python 64bits
rem https://www.imagemagick.org/script/download.php#windows

@PAUSE
