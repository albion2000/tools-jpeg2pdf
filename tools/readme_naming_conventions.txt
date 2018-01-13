=======================================================
FRENCH HERE, ENGLISH BELOW

PRELIMINAIRE
 * Lisez et suivez les instructions du fichier installation_instructions.txt pour pouvoir lancer l'outil sur votre machine.

ACTION
 * L'objectif principal de cet outil optionnel est d'assurer une conservation à plus long terme de la structure de répertoires, qui risque d'être corrompue/modifiée, à l'occasion de transferts entre "file systems/os" systèmes de fichiers et OS.
 * Mode Simulation : détection des répertoires à problème, affichage du résultat simulé.
 * Mode effectif   : Renommage effectif, a effectuer si la simulation vous convient.

USAGE 
 * Copier 'naming_conventions.py' et 'naming_conventions_do_rename.py' dans le répertoire racine de votre arborescence de fichiers.

2 syntaxes

 * Executer ce script (deux façons)
   * Pour lancer la simulation (pas de modification réalisée, pas de risque), double cliquez sur le fichier 'naming_conventions.py' dans l'explorateur windows.
   * Pour lancer le renommage, double cliquez sur le fichier 'naming_conventions_do_rename.py' dans l'explorateur windows.
 * Si vous obtenez immédiatement une erreur du type "n'est pas reconnu en tant que commande interne", cela peut signifier que python n'a pas été ajouté à votre path système. Veuillez suivre les instructions d'installation.

Les résultats sont dans la console et recopiés à la fin du fichier logRename.txt

typiquement cet outil est utilisé avant scandir2pdf

NOTES

Reste à faire : 
	Parce que l'outil peut renommer les répertoires, il vérifie aussi si il ne tombe pas dans la situation où après renommage, deux sous répertoires auraient le même nom.
	Dans ce cas, aucun répertoire n'est touché. Les répertoires à problème sont indiqués. Il est laissé à l'utilisateur le soin de renommer un de ces répertoires.
	Actuellement, cette situation fera échouer le renommage du second fichier et stoppera les opérations.

Copie de : http://www.ufowaves.org/ltdsp/ltsdp/nommage 

Règles de nommage des fichiers et répertoires

Il s'agit ici de répondre à la problématique de la conservation non pas du contenu des fichiers, mais des noms des fichiers et des répertoires qui les contiennent.

Ça évite des situations où par exemple un fichier devient : no_l___l_attaque.txt

alors que le fichier d'origine s'appelait : NOËL À L'ATTAQUE.TXT

si le fichier s'était nommé dès le départ : noel_a_l_attaque.txt, il n'aurait pas été altéré.

Le problème se situe à plusieurs niveaux :

risque de perte d'informations lors de transferts ou recopies d'un système vers un autre. En raison d'incompatibilités du système de transfert ou bien du système cible.
risque de perte d'informations en cas de certains types de crashs.
Avoir toute liberté dans le nommage signifie en gros :

pouvoir choisir des noms de fichiers aussi long que voulus
pouvoir mettre tous les caractères que le système actuel utilise : y compris ceux qui sont à problèmes : espace, accents, caractères spéciaux, points.
On aimerait bien avoir toute liberté sur les nommages, mais je recommande de volontairement restreindre les possibilités.

Il y a aussi une autre motivation envisageable : assurer l'uniformité de l'apparence des noms de fichiers. Par exemple, se limiter au lettres minuscules, ou bien toujours commencer un nom de fichier par une majuscule.

Voici la meilleure recommandation que je puisse faire, fruit d'années d'expérience en informatique :

Modifier
Les noms de répertoires

se limiter à des noms de 64 caractères ou moins
interdiction absolue d'utiliser le caractère ' ' : espace
n'utiliser aucun caractère autre que les caractères de base ASCII dans la liste suivante :
chiffres de '0' à '9'
lettres de 'a' à 'z'
lettres de 'A' à 'Z'
'_' tiret bas (fait office d'espaces)
Oui en effet, il est interdit d'utiliser les caractères accentués.

Les noms de répertoire doivent-être aussi bref que possible. Les systèmes de fichiers Windows ont encore des limitations sur la longueur de chemin complet des fichiers. Il est facile de dépasser le maximum autorisé.

Modifier
Les noms de fichiers

S'ajoute à la liste précédente un seul caractère qui ne doit apparaître qu'une fois : le point '.'
Il ne sert que de séparateur avant les (en général 3) caractères de l'extension du fichier (.doc, .txt, .pdf, etc…)

Le nom d'un fichier n'est pas sensé décrire ce qu'il contient. C'est à la base de données du fond de la faire. Si bien que ces contraintes ne dégradent pas vraiment le contenu du fond.

Exemple de fond respectant ces contraintes de nommage : fond des enquetes de gérard deforge

Les noms de fichiers doivent-être aussi bref que possible. Ils ne doivent pas servir à donner d'autres indications qu'une identification sans ambiguïté du document. Les systèmes de fichiers Windows ont encore des limitations sur la longueur de chemin complet des fichiers. Il est facile de dépasser le maximum autorisé. Il faut aussi chercher à atteindre la plus grande uniformité dans les nommages.


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
# æ becomes ae
# œ becomes oe
# 'N°' decomes 'n_'
# remove too many '_'
# remove '_' at start or end of dir name
