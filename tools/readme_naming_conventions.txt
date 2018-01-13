=======================================================
FRENCH HERE, ENGLISH BELOW

PRELIMINAIRE
 * Lisez et suivez les instructions du fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.

ACTION
 * L'objectif principal de cet outil optionnel est d'assurer une conservation � plus long terme de la structure de r�pertoires, qui risque d'�tre corrompue/modifi�e, � l'occasion de transferts entre "file systems/os" syst�mes de fichiers et OS.
 * Mode Simulation : d�tection des r�pertoires � probl�me, affichage du r�sultat simul�.
 * Mode effectif   : Renommage effectif, a effectuer si la simulation vous convient.

USAGE 
 * Copier 'naming_conventions.py' et 'naming_conventions_do_rename.py' dans le r�pertoire racine de votre arborescence de fichiers.

2 syntaxes

 * Executer ce script (deux fa�ons)
   * Pour lancer la simulation (pas de modification r�alis�e, pas de risque), double cliquez sur le fichier 'naming_conventions.py' dans l'explorateur windows.
   * Pour lancer le renommage, double cliquez sur le fichier 'naming_conventions_do_rename.py' dans l'explorateur windows.
 * Si vous obtenez imm�diatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas �t� ajout� � votre path syst�me. Veuillez suivre les instructions d'installation.

Les r�sultats sont dans la console et recopi�s � la fin du fichier logRename.txt

typiquement cet outil est utilis� avant scandir2pdf

NOTES

Reste � faire : 
	Parce que l'outil peut renommer les r�pertoires, il v�rifie aussi si il ne tombe pas dans la situation o� apr�s renommage, deux sous r�pertoires auraient le m�me nom.
	Dans ce cas, aucun r�pertoire n'est touch�. Les r�pertoires � probl�me sont indiqu�s. Il est laiss� � l'utilisateur le soin de renommer un de ces r�pertoires.
	Actuellement, cette situation fera �chouer le renommage du second fichier et stoppera les op�rations.

Copie de : http://www.ufowaves.org/ltdsp/ltsdp/nommage 

R�gles de nommage des fichiers et r�pertoires

Il s'agit ici de r�pondre � la probl�matique de la conservation non pas du contenu des fichiers, mais des noms des fichiers et des r�pertoires qui les contiennent.

�a �vite des situations o� par exemple un fichier devient : no_l___l_attaque.txt

alors que le fichier d'origine s'appelait : NO�L � L'ATTAQUE.TXT

si le fichier s'�tait nomm� d�s le d�part : noel_a_l_attaque.txt, il n'aurait pas �t� alt�r�.

Le probl�me se situe � plusieurs niveaux :

risque de perte d'informations lors de transferts ou recopies d'un syst�me vers un autre. En raison d'incompatibilit�s du syst�me de transfert ou bien du syst�me cible.
risque de perte d'informations en cas de certains types de crashs.
Avoir toute libert� dans le nommage signifie en gros :

pouvoir choisir des noms de fichiers aussi long que voulus
pouvoir mettre tous les caract�res que le syst�me actuel utilise : y compris ceux qui sont � probl�mes : espace, accents, caract�res sp�ciaux, points.
On aimerait bien avoir toute libert� sur les nommages, mais je recommande de volontairement restreindre les possibilit�s.

Il y a aussi une autre motivation envisageable : assurer l'uniformit� de l'apparence des noms de fichiers. Par exemple, se limiter au lettres minuscules, ou bien toujours commencer un nom de fichier par une majuscule.

Voici la meilleure recommandation que je puisse faire, fruit d'ann�es d'exp�rience en informatique :

Modifier
Les noms de r�pertoires

se limiter � des noms de 64 caract�res ou moins
interdiction absolue d'utiliser le caract�re ' ' : espace
n'utiliser aucun caract�re autre que les caract�res de base ASCII dans la liste suivante :
chiffres de '0' � '9'
lettres de 'a' � 'z'
lettres de 'A' � 'Z'
'_' tiret bas (fait office d'espaces)
Oui en effet, il est interdit d'utiliser les caract�res accentu�s.

Les noms de r�pertoire doivent-�tre aussi bref que possible. Les syst�mes de fichiers Windows ont encore des limitations sur la longueur de chemin complet des fichiers. Il est facile de d�passer le maximum autoris�.

Modifier
Les noms de fichiers

S'ajoute � la liste pr�c�dente un seul caract�re qui ne doit appara�tre qu'une fois : le point '.'
Il ne sert que de s�parateur avant les (en g�n�ral 3) caract�res de l'extension du fichier (.doc, .txt, .pdf, etc�)

Le nom d'un fichier n'est pas sens� d�crire ce qu'il contient. C'est � la base de donn�es du fond de la faire. Si bien que ces contraintes ne d�gradent pas vraiment le contenu du fond.

Exemple de fond respectant ces contraintes de nommage : fond des enquetes de g�rard deforge

Les noms de fichiers doivent-�tre aussi bref que possible. Ils ne doivent pas servir � donner d'autres indications qu'une identification sans ambigu�t� du document. Les syst�mes de fichiers Windows ont encore des limitations sur la longueur de chemin complet des fichiers. Il est facile de d�passer le maximum autoris�. Il faut aussi chercher � atteindre la plus grande uniformit� dans les nommages.


=======================================================

ENGLISH 

PRELIMINARY
 * Read the installation_instructions.txt for being able to run the tool on your machine.

 
ACTION

The primary purpose of this tool is to ensure a longer lifetime to a directry tree by reducing the risk of it being corrupted over transfers between file systems.

This is done by enforcing some naming conventions. On directories

justification and general principles : http://www.ufowaves.org/ltdsp/ltsdp/nommage

typically, this would be called before scandir2pdf

USE
 * Copy 'naming_conventions.py' & 'naming_conventions_do_rename.py' into the root directory of your files.
 * Simulation, with no effect on the name of the directories, for validation purposes: double click on naming_conventions.py
 * Renaming effectively : double click on naming_conventions_do_rename.py


To be done : 
	Because the tool can rename the directories, it also checks that it does not fall in the situation where after renaming, two directories would have the same name.
	If that is the case, the problematic directories are pointed out, and the user must himself rename one of the faulty directories.

log into file logRename.txt

rules followed

# tries to convert as best as it can anything in ascii characters
# go lower case
# anything that is neither a letter nor a number is replaced by _
# � becomes ae
# � becomes oe
# 'N�' decomes 'n_'
# remove too many '_'
# remove '_' at start or end of dir name
