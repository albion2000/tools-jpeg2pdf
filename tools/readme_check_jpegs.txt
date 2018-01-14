## check_jpegs.py 

jan 2018
==============================================================================

ENGLISH. FRENCH IS BELOW

PRELIMINARY
 * Read the installation_instructions.txt for being able to run the tool on your machine.

ACTION
 * It recursively parses sub directories for .jpeg and .jpg file
 * It checks that the files are not corrupted.
 * This tool takes no irreversible action. It changes no file to the file tree. 
 
USE
 * Copy 'check_jpegs.py' & 'check_jpegs_full.py' to the root directory of your file three.
 * either Double click on the file 'check_jpegs.py' for a quick sanity check. It is, on purpose, a fast check in order to help detect rapidly bad files. Only the headers are checked, the images are not decompressed.
 * or Double click on the file 'check_jpegs_full.py' instead for a full sanity check

NOTES
 * Each '.' shows that one more directory was parsed
 * When a file is reported as corrupted, it does not mean that it is lost. Try to open it in your favorite image sw and save it back (using the best quality, in order to reduce compression losses). It is often enough. If you can't open it, try to open it with other image tools. Not all handle file corruption the same way.


==============================================================================

FRENCH

PRELIMINAIRE
 * Lisez le fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.

ACTION
 * Traverse récursivement l'arborescence de fichiers à la recherche de .jpeg et .jpg
 * Détecte les fichiers corrompus.
 * Cet outil ne réalise aucune action irreversible. Il ne change aucun fichier. 

USAGE 
 * Copier 'check_jpegs.py' & 'check_jpegs_full.py' dans le répertoire racine de votre arborescence de fichiers.
 * Double cliquez sur 'check_jpegs.py' pour repérer rapidement les images dont les entêtes seraient corrompues. Seuls les entêtes de fichiers sont vérifiées, elles ne sont pas décompressées.
 * ou bien double cliquez sur 'check_jpegs_full.py' pour une vérification en profondeur de l'intégrité des images 

NOTES
 * Chaque '.' indique d'un répertoire supplémentaire a été traité
 * Quoi faire avec le résultat du "check" ? Fichier corrompu ? Ne signifie pas qu'il est perdu. Essayez de le charger avec tous vos logiciels capables de charger et sauvegarder des jpeg (à la meilleure qualité pour réduire les altérations dues à la compression). Cela suffit souvent pour récupérer le fichier.
 