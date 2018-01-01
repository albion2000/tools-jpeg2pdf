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
 * Traverse récursivement l'arborescence de fichiers à la recherche de .jpeg et .jpg
 * Détecte rapidement les fichiers corrompus.


USAGE 
 * Copier 'check_jpegs.py' dans le répertoire racine de votre arborescence de fichiers.
 * Executer ce script (deux façons entre autres)
   1. Lancer une console windows dans votre répertoire, et taper 'check_jpegs.py'. Pour cela : 
     1. Lancez l'explorateur windows et allez sur votre répertoire. 
     1. Cliquez sur le chemin complet dans l'explorateur, pour le faire apparaître en surbrillance (sélectionné)
     1. Tapez 'cmd' à la place du chemin complet. appuyez sur 'enter'
     1. Cela doit ouvrir une console de ligne de commande dans votre répertoire. Tapez check_jpegs.py puis 'enter'
   1. ou bien (non recommandé) Double cliquer sur le fichier 'check_jpegs.py' dans l'explorateur windows. Cette méthode a le défaut que la fenêtre se ferme dès la fin, ce qui ne laisse pas le temps de lire le rapport final. 
 * Si vous obtenez immédiatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas été ajouté à votre path système.

NOTES
 * Seuls les entêtes de fichiers sont vérifiées, elles ne sont pas décompressées.
 * Chaque '.' indique d'un répertoire supplémentaire a été traité
 * Quoi faire avec le résultat du "check" ? Fichier corrompu ? Ne signifie pas qu'il est perdu. Essayez de le charger avec tous vos logiciels capables de charger et sauvegarder des jpeg (à la meilleure qualité pour réduire les altérations dues à la compression). Cela suffit souvent pour récupérer le fichier.
 