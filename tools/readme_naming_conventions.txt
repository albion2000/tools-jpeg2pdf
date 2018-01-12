=======================================================
FRENCH HERE, ENGLISH BELOW

Typiquement cet outil est utilis� avant scandir2pdf

L'objectif principal de cet outil est d'assurer une conservation � plus long terme de la structure de r�pertoires, qui risque d'�tre corrompue/modifi�e, � l'occasion de transferts entre "file systems/os" syst�mes de fichiers et OS.

Reste � faire : 
	Parce que l'outil peut renommer les r�pertoires, il v�rifie aussi si il ne tombe pas dans la situation o� apr�s renommage, deux sous r�pertoires auraient le m�me nom.
	Dans ce cas, aucun r�pertoire n'est touch�. Les r�pertoires � probl�me sont indiqu�s. Il est laiss� � l'utilisateur le soin de renommer un de ces r�pertoires.
	Actuellement, cette situation fera �chouer le renommage du second fichier et stoppera les op�rations.


Rien n'est fait sans validation de l'utilisateur. Pour cela les traitements sont fait en deux �tapes.

Scrutation, d�tection des r�pertoires � probl�me, affichage du r�sultat simul�.
Si le r�sultat simul� affich� est accept�, il faut relancer l'outil avec l'option : -w 
L� le renommage sera effectif.




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

Je pourrais �tre plus restrictif, pour donner un aspect plus l�ch� au fond, mais ce n'est pas n�cessaire. Au del�, trop de personnes ne font pas l'effort de respecter les r�gles, juste par flemme ou �tourderie.

Pour commencer, il est possible de faire un renommage automatique de tout ce qui existe d�j� pour respecter ces r�gles. (par un programme informatique)

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

The primary purpose of this tool is to ensure a longer lifetime to a directry tree by reducing the risk of it being corrupted over transfers between file systems.

This is done by enforcing some naming conventions. On directories

justification and general principles : http://www.ufowaves.org/ltdsp/ltsdp/nommage

typically, this would be called before scandir2pdf

To be done : 
	Because the tool can rename the directories, it also checks that it does not fall in the situation where after renaming, two directories would have the same name.

	If that is the case, the problematic directories are pointed out, and the user must himself rename one of the faulty directories.


