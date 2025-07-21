echo This is to do only once after the python installation
pip install pillow==8.0.1
pip install PyPDF2==1.26.0
pip install img2pdf==0.4.4
pip install unidecode

pip install wand==0.6.7

echo Additional installations may be required, depending on your needs !
echo wand is needed only for the tools like scandirpdf2cover, scandirpdf2jpg and scanditpdf2png that extract images from pdfs
echo wand requires ghostscript to be installed (the pc windows version, not the python version) install the 64bit if you use python 64bits
echo https://ghostscript.com/releases/gsdnld.html
echo wand requires also imageMagick to be installed.  (the pc windows version, not the python version) install the 64bit if you installed python 64bits
echo https://www.imagemagick.org/script/download.php#windows

@PAUSE
