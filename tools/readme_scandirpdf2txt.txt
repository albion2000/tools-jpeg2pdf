## scandirpdf2txt.py

feb 2018
==============================================================================

FRENCH. ENGLISH IS BELOW

PRELIMINAIRE
 * Lisez le fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.
 * De plus, il vous faudra r�cup�rer l'outil pdftotext.exe ici : 
	* http://www.xpdfreader.com/download.html , t�l�charger les Xpdf tools pour win ou linux. Dans le zip t�l�charg�, r�cup�rer juste xpdf-tools-win-4.00/bin64/pdftotext.exe
	* il faudra le copier avec scandirpdf2txt.py � la racine de votre arborescence de r�pertoires � traiter.
 * Copier 'scandirpdf2txt.py' dans le r�pertoire racine de votre arborescence de fichiers.
 * Y copier aussi pdftotext.exe.

Action
 * Le traitement est r�cursif sur les sous r�pertoires
 * En plus des affichages dans la console, les erreurs et rapport final sont �crits dans un fichier "logpdf2txt.txt" pour v�rification � la fin. Si vous relancez l'outil, les nouvelles informations sont ajout�es � la fin du fichier.
 * Il ne fait que cr��r (ou re-cr�er) des .txt 
 
Usage 
 * Executer ce script : Double clicker sur le fichier 'scandirpdf2txt.py' dans l'explorateur windows. Vous pouvez retrouver tous les r�sultats en lisant le fichier "logpdf2txt.txt" cr��.
 * Si vous obtenez imm�diatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas �t� ajout� � votre path syst�me ou n'est tout simplement pas install�. Veuillez suivre les instructions d'installation � la lettre.

==============================================================================

ENGLISH

PRELIMINARY
 * Read the installation_instructions.txt for being able to run the tool on your machine.

 * In addition, you need to 
 
	Download the Xpdf tools for win or linux

	http://www.xpdfreader.com/download.html

	the only file you need from the zip is 

	xpdf-tools-win-4.00/bin64/pdftotext.exe


USE 
 * Copy 'scandirpdf2txt.py' into the root of your tree of directories to process
 * Copy also 'pdftotext.exe' into the root of your tree of directories to process
 * Launch 'scandirpdf2txt.py', either by double click or from a windows command line window.


