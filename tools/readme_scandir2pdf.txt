## scandir2pdf.py

jan 2018
==============================================================================

FRENCH. ENGLISH IS BELOW

PRELIMINAIRE
 * Lisez le fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.

Action
 * Pour chaque répertoire X, l'outil scandir2pdf regroupe les fichiers image du répertoire en un fichier X.pdf. Et le place au niveau supérieur de l'arborescence de répertoires.
 * le traitement est récursif sur les sous répertoires
 * En plus des affichages dans la console, les erreurs et rapport final sont écrits dans un fichier "logParse.txt" pour vérification à la fin. Si vous relancez l'outil, les nouvelles informations sont ajoutées à la fin du fichier.

Usage 
 * Copier 'scandir2pdf.py' dans le répertoire racine de votre arborescence de fichiers.
 * Executer ce script (deux façons entre autres)
   1. Double clicker sur le fichier 'scandir2pdf.py' dans l'explorateur windows. Cette méthode a le défaut que la fenêtre se ferme dès la fin, ce qui ne laisse pas le temps de lire le rapport final. Mais vous pouvez retrouver tous les résultats en lisant le fichier "logParse.txt" créé.
   1. ou bien Lancer une console windows dans votre répertoire, et taper 'scandir2pdf.py'. Pour cela : 
     1. Lancez l'explorateur windows et allez sur votre répertoire. 
     1. Cliquez sur le chemin complet dans l'explorateur, pour le faire apparaitre en surbrillance (séléctionné)
     1. Tapez 'cmd' à la place du chemin complet. appuyez sur 'enter'
     1. Cela doit ouvrir une console de ligne de commande dans votre répertoire. Tapez scandir2pdf.py puis 'enter'
 * Si vous obtenez immédiatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas été ajouté à votre path système ou n'est tout simplement pas installé.
 
Limitations
 * La première version de l'outil ne prend en compte que les fichiers jpeg (.jpg ou .jpeg)
 * Il existe une limitation mémoire dans la version 32 bits de python qui peut faire échouer la convertion en pdf de certains répertoires. C'est pourquoi il est recommandé d'installer la version 64 bits de python.

Notes 
 * Il est autorisé d'avoir dans un répertoire X des images et des sous répertoires contenant des images. Elles seront bien toutes traitées. Même si cette structure de fichiers ne peut pas refleter une organisation logique.  
 * les pdf produits on l'avantage de ne pas recompresser les images jpeg. Les images sont incorporées telles quelles.
 
Recommandations
 * Eviter d'avoir plus de 100 fichiers dans chaque repertoire

Requis
 * Scans format jpeg, avec extension de fichier en .jpg ou .jpeg
 * Un répertoire par édition(numéro) de journal
 * Les fichiers de scan nommés de telle sorte qu'ils apparaissent naturellement ordonnés dans l'explorateur windows. Par exemple SCAN_0001.jpg, SCAN_0002.jpg, etc...
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







