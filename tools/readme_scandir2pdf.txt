## scandir2pdf.py

jan 2018
==============================================================================

FRENCH. ENGLISH IS BELOW

PRELIMINAIRE
 * Lisez le fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.

Action
 * Pour chaque r�pertoire X, l'outil scandir2pdf regroupe les fichiers image du r�pertoire en un fichier X.pdf. Et le place au niveau sup�rieur de l'arborescence de r�pertoires.
 * le traitement est r�cursif sur les sous r�pertoires
 * En plus des affichages dans la console, les erreurs et rapport final sont �crits dans un fichier "logParse.txt" pour v�rification � la fin. Si vous relancez l'outil, les nouvelles informations sont ajout�es � la fin du fichier.

Usage 
 * Copier 'scandir2pdf.py' dans le r�pertoire racine de votre arborescence de fichiers.
 * Executer ce script (deux fa�ons entre autres)
   1. Double clicker sur le fichier 'scandir2pdf.py' dans l'explorateur windows. Cette m�thode a le d�faut que la fen�tre se ferme d�s la fin, ce qui ne laisse pas le temps de lire le rapport final. Mais vous pouvez retrouver tous les r�sultats en lisant le fichier "logParse.txt" cr��.
   1. ou bien Lancer une console windows dans votre r�pertoire, et taper 'scandir2pdf.py'. Pour cela : 
     1. Lancez l'explorateur windows et allez sur votre r�pertoire. 
     1. Cliquez sur le chemin complet dans l'explorateur, pour le faire apparaitre en surbrillance (s�l�ctionn�)
     1. Tapez 'cmd' � la place du chemin complet. appuyez sur 'enter'
     1. Cela doit ouvrir une console de ligne de commande dans votre r�pertoire. Tapez scandir2pdf.py puis 'enter'
 * Si vous obtenez imm�diatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas �t� ajout� � votre path syst�me ou n'est tout simplement pas install�.
 
Limitations
 * La premi�re version de l'outil ne prend en compte que les fichiers jpeg (.jpg ou .jpeg)
 * Il existe une limitation m�moire dans la version 32 bits de python qui peut faire �chouer la convertion en pdf de certains r�pertoires. C'est pourquoi il est recommand� d'installer la version 64 bits de python.

Notes 
 * Il est autoris� d'avoir dans un r�pertoire X des images et des sous r�pertoires contenant des images. Elles seront bien toutes trait�es. M�me si cette structure de fichiers ne peut pas refleter une organisation logique.  
 * les pdf produits on l'avantage de ne pas recompresser les images jpeg. Les images sont incorpor�es telles quelles.
 
Recommandations
 * Eviter d'avoir plus de 100 fichiers dans chaque repertoire

Requis
 * Scans format jpeg, avec extension de fichier en .jpg ou .jpeg
 * Un r�pertoire par �dition(num�ro) de journal
 * Les fichiers de scan nomm�s de telle sorte qu'ils apparaissent naturellement ordonn�s dans l'explorateur windows. Par exemple SCAN_0001.jpg, SCAN_0002.jpg, etc...
 * Une page par fichier
 * Image en orientation portrait.
 

==============================================================================

ENGLISH

PRELIMINARY
 * Read the installation_instructions.txt for being able to run the tool on your machine.

Use 
 * Copy 'scandir2pdf.py' to the root directory of your file three. Launch it, either by double click or from a windows command line window.

Action
 * For each directory X, the tool scandir2pdf regroups the image files in a file named X.pdf. And moves it to the upper stage in the file three.
 * It recursively parses sub directories for .jpeg and .jpg file 
 * Logs progress, erros and final report in the console and in the file "logParse.txt". New processings are appended at the end of the file.

Limitations
 * The first version of the tool only takes into account the jpeg files (.jpg or .jpeg)
 * There is a memory limitation in the 32 bits version of python that can make the convertion of some pdf. That's why the 64 bits version is recommended.
 
notes
 * It is accepted to have in a directory X images and sub directories with images. They will all be processed. Even if such a structure cannot reflect a logical organisation.
 * In the case of jpeg files, the pdf have the advantage of being produced without recompressing the images. They are incorporated as is. It is important because the better the quality, the better the ocr.

Recommendations
 * Avoid having more than 100 files per dir.
 * Not a good idea to name directories finishing with .jpg !!! But it still works.


Tools Requirements 
 * Scans in jpeg format, with file extension .jpg or .jpeg
 * One directory per journal issue
 * Scan files named so that they get naturally ordered. Easily obtained by numbering the scans. For example SCAN_0001.jpg, SCAN_0002.jpg, etc...
 * One page per scan
 * Images in portrait orientation.







