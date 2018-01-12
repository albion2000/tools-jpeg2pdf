=======================================================
FRENCH HERE, ENGLISH BELOW

Typiquement cet outil est utilisé avant scandir2pdf

L'objectif principal de cet outil est d'assurer une conservation à plus long terme de la structure de répertoires, qui risque d'être corrompue/modifiée, à l'occasion de transferts entre "file systems/os" systèmes de fichiers et OS.

Reste à faire : 
	Parce que l'outil peut renommer les répertoires, il vérifie aussi si il ne tombe pas dans la situation où après renommage, deux sous répertoires auraient le même nom.
	Dans ce cas, aucun répertoire n'est touché. Les répertoires à problème sont indiqués. Il est laissé à l'utilisateur le soin de renommer un de ces répertoires.
	Actuellement, cette situation fera échouer le renommage du second fichier et stoppera les opérations.


Rien n'est fait sans validation de l'utilisateur. Pour cela les traitements sont fait en deux étapes.

Scrutation, détection des répertoires à problème, affichage du résultat simulé.
Si le résultat simulé affiché est accepté, il faut relancer l'outil avec l'option : -w 
Là le renommage sera effectif.




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

Je pourrais être plus restrictif, pour donner un aspect plus léché au fond, mais ce n'est pas nécessaire. Au delà, trop de personnes ne font pas l'effort de respecter les règles, juste par flemme ou étourderie.

Pour commencer, il est possible de faire un renommage automatique de tout ce qui existe déjà pour respecter ces règles. (par un programme informatique)

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

The primary purpose of this tool is to ensure a longer lifetime to a directry tree by reducing the risk of it being corrupted over transfers between file systems.

This is done by enforcing some naming conventions. On directories

justification and general principles : http://www.ufowaves.org/ltdsp/ltsdp/nommage

typically, this would be called before scandir2pdf

To be done : 
	Because the tool can rename the directories, it also checks that it does not fall in the situation where after renaming, two directories would have the same name.

	If that is the case, the problematic directories are pointed out, and the user must himself rename one of the faulty directories.


