## check_jpegs.py 

jan 2018
==============================================================================

ENGLISH. FRENCH IS BELOW

PRELIMINARY
 * Read the installation_instructions.txt for being able to run the tool on your machine.

ACTION
 * It recursively parses sub directories for .jpeg and .jpg file
 * It quickly checks that the files are not corrupted.
 * This tool takes no irreversible action. It changes no file to the file tree. 
 
USE
 * Copy 'check_jpegs.py' to the root directory of your file three.
 * Double click on the file 'check_jpegs.py'

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
 * Cet outil ne r�alise aucune action irreversible. Il ne change aucun fichier. 

USAGE 
 * Copier 'check_jpegs.py' dans le r�pertoire racine de votre arborescence de fichiers.
 * Double cliquez sur 'check_jpegs.py'

NOTES
 * Seuls les ent�tes de fichiers sont v�rifi�es, elles ne sont pas d�compress�es.
 * Chaque '.' indique d'un r�pertoire suppl�mentaire a �t� trait�
 * Quoi faire avec le r�sultat du "check" ? Fichier corrompu ? Ne signifie pas qu'il est perdu. Essayez de le charger avec tous vos logiciels capables de charger et sauvegarder des jpeg (� la meilleure qualit� pour r�duire les alt�rations dues � la compression). Cela suffit souvent pour r�cup�rer le fichier.
 