## scandirpdf2txt.py

feb 2018
==============================================================================

FRENCH. ENGLISH IS BELOW

PRELIMINAIRE
 * Lisez le fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.
 * De plus, il vous faudra récupérer l'outil pdftotext.exe ici : 
	* http://www.xpdfreader.com/download.html , télécharger les Xpdf tools pour win ou linux. Dans le zip téléchargé, récupérer juste xpdf-tools-win-4.00/bin64/pdftotext.exe
	* il faudra le copier avec scandirpdf2txt.py à la racine de votre arborescence de répertoires à traiter.
 * Copier 'scandirpdf2txt.py' dans le répertoire racine de votre arborescence de fichiers.
 * Y copier aussi pdftotext.exe.

Action
 * Le traitement est récursif sur les sous répertoires
 * En plus des affichages dans la console, les erreurs et rapport final sont écrits dans un fichier "logpdf2txt.txt" pour vérification à la fin. Si vous relancez l'outil, les nouvelles informations sont ajoutées à la fin du fichier.
 * Il ne fait que créér (ou re-créer) des .txt 
 
Usage 
 * Executer ce script : Double clicker sur le fichier 'scandirpdf2txt.py' dans l'explorateur windows. Vous pouvez retrouver tous les résultats en lisant le fichier "logpdf2txt.txt" créé.
 * Si vous obtenez immédiatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas été ajouté à votre path système ou n'est tout simplement pas installé. Veuillez suivre les instructions d'installation à la lettre.

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


