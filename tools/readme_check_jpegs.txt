## check_jpegs.py 

jan 2018
==============================================================================

ENGLISH. FRENCH IS BELOW

PRELIMINARY
 * Read the installation_instructions.txt for being able to run the tool on your machine.

ACTION
 * It recursively parses sub directories for .jpeg and .jpg file
 * It quickly checks that the files are not corrupted.

USE
 * Copy 'check_jpegs.py' to the root directory of your file three.

NOTES
 * It is, on purpose, a fast check in order to help detect rapidly bad files.
 * Only the headers are checked, the images are not decompressed.
 * Each '.' shows that one more directory was parsed
 * When a file is reported as corrupted, it does not mean that it is lost. Try to open it in your favorite image sw and save it back (using the best quality, in order to reduce compression losses). It is often enough. If you can't open it, try to open it with other image tools. Not all handle file corruption the same way.


==============================================================================

FRENCH

PRELIMINAIRE
 * Lisez le fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.

ACTION
 * Traverse r�cursivement l'arborescence de fichiers � la recherche de .jpeg et .jpg
 * D�tecte rapidement les fichiers corrompus.


USAGE 
 * Copier 'check_jpegs.py' dans le r�pertoire racine de votre arborescence de fichiers.
 * Executer ce script (deux fa�ons entre autres)
   1. Lancer une console windows dans votre r�pertoire, et taper 'check_jpegs.py'. Pour cela : 
     1. Lancez l'explorateur windows et allez sur votre r�pertoire. 
     1. Cliquez sur le chemin complet dans l'explorateur, pour le faire appara�tre en surbrillance (s�lectionn�)
     1. Tapez 'cmd' � la place du chemin complet. appuyez sur 'enter'
     1. Cela doit ouvrir une console de ligne de commande dans votre r�pertoire. Tapez check_jpegs.py puis 'enter'
   1. ou bien (non recommand�) Double cliquer sur le fichier 'check_jpegs.py' dans l'explorateur windows. Cette m�thode a le d�faut que la fen�tre se ferme d�s la fin, ce qui ne laisse pas le temps de lire le rapport final. 
 * Si vous obtenez imm�diatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas �t� ajout� � votre path syst�me.

NOTES
 * Seuls les ent�tes de fichiers sont v�rifi�es, elles ne sont pas d�compress�es.
 * Chaque '.' indique d'un r�pertoire suppl�mentaire a �t� trait�
 * Quoi faire avec le r�sultat du "check" ? Fichier corrompu ? Ne signifie pas qu'il est perdu. Essayez de le charger avec tous vos logiciels capables de charger et sauvegarder des jpeg (� la meilleure qualit� pour r�duire les alt�rations dues � la compression). Cela suffit souvent pour r�cup�rer le fichier.
 