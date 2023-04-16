rem This is to do once after the python installation
pip install img2pdf
pip install unidecode
pip install pillow
pip install PyPDF2

pip install wand

rem wand is needed only for the tools scandirpdf2cover, scandirpdf2jpg and scanditpdf2png that extract images from pdfs
rem wand requires ghostscript to be installed (the pc windows version, not the python version) install the 64bit if you use python 64bits
rem https://ghostscript.com/releases/gsdnld.html
rem wand requires also imageMagick to be installed.  (the pc windows version, not the python version) install the 64bit if you use python 64bits
rem https://www.imagemagick.org/script/download.php#windows

@PAUSE
