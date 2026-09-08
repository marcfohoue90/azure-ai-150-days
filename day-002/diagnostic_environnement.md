# Diagnostic de l'environnement du jour 2

## Objectif

Vérifier que mon poste de travail est prêt pour développer avec Python, Git, Docker et Azure.

## Résultat attendu

Disposer d'un environnement cohérent, avec des outils installés, accessibles depuis le terminal et utilisables dans VS Code.

## Risque principal

Un outil peut être installé sans être accessible dans le terminal. Ce problème vient souvent de la variable `PATH` ou d'une installation incomplète.

## Preuve de réussite

Les commandes de vérification fonctionnent, leurs résultats sont consignés dans ce fichier et une erreur contrôlée a été comprise puis corrigée.

## Environnement vérifié

### Windows

Le poste utilise Windows 10 Home. La version système affichée est 2009 et le numéro de build est 26200.

### WSL2

WSL est installé et fonctionnel. La distribution utilisée par défaut est Ubuntu 24.04. La version par défaut est WSL 2. La version installée de WSL est 2.6.1.0 et son noyau Linux est en version 6.6.87.2-1.

### Git

Git est installé et accessible depuis PowerShell. La version détectée est 2.54.0.windows.1. Le nom configuré pour les commits est `marcfohoue90`.

### Python

Python est installé et accessible depuis PowerShell. La version utilisée par défaut est Python 3.13.9.

### VS Code

VS Code est installé et accessible depuis PowerShell. La version détectée est 1.136.2 et l'installation est en 64 bits.

### Docker

Docker est installé et accessible depuis PowerShell. La version du client détectée est 29.7.2.

Le moteur Docker est démarré et répond au client. Docker Desktop 4.87.0 utilise un moteur Docker 29.7.2 sous Linux.

## Commandes exécutées

```powershell
wsl --status
wsl -- list --verbose
wsl --list --verbose
wsl --version
wsl --distribution Ubuntu-24.04 -- uname -a
git --version
git config --global --get user.name
git config --global --get user.email
python --version
py --list
python -c "print('Pyhton fonctionne')"
python -m pip --version
code --version
code .
docker --version
docker version
docker run --rm hello-world
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
Get-Command git, python, code, docker | Select-Object Name, Source
Get-ChildItem -LiteralPath day-002 -Force
rg -n -i "(api[_-]?key|access[_-]?key|client[_-]?secret|password\s*[:=]|bearer\s+)" day-002
Select-String -Path day-002\*.md -Pattern 'api[_-]?key|access[_-]?key|client[_-]?secret|password\s*[:=]|bearer\s+'
```

## Résultats observés

La commande `wsl --status` a confirmé que WSL est configuré avec Ubuntu 24.04 comme distribution par défaut et WSL 2 comme version par défaut.

La commande `wsl --list --verbose` a affiché trois distributions, toutes arrêtées et configurées avec WSL 2 : `Ubuntu-24.04`, `docker-desktop` et `Ubuntu`.

La commande `wsl --version` a confirmé la présence de WSL 2.6.1.0 et du noyau Linux 6.6.87.2-1. Elle a aussi affiché les composants graphiques de WSL et la version de Windows utilisée.

La commande `wsl --distribution Ubuntu-24.04 -- uname -a` a démarré Ubuntu 24.04 et a affiché ses informations système. Le noyau indiqué contient `microsoft-standard-WSL2`, ce qui confirme que la distribution fonctionne bien sous WSL 2.

La commande `git --version` a répondu `git version 2.54.0.windows.1`. Git est donc installé et son exécutable est accessible depuis le terminal.

La commande `git config --global --get user.name` a confirmé que le nom associé aux commits est `marcfohoue90`.

La commande `git config --global --get user.email` a confirmé qu'une adresse e-mail valide est configurée pour les commits. Elle n'est pas reproduite ici afin de ne pas publier de donnée personnelle.

La commande `python --version` a répondu `Python 3.13.9`. Python est donc installé et accessible depuis le terminal.

La commande `py --list` a affiché une seule installation reconnue : Python 3.13 en 64 bits. L'astérisque indique qu'elle est utilisée par défaut.

La commande `python -c "print('Pyhton fonctionne')"` a exécuté une instruction Python et a affiché le texte demandé. Python peut donc exécuter du code. Le mot affiché contient une faute de frappe, mais cela n'affecte pas le fonctionnement de Python.

La commande `python -m pip --version` a confirmé que `pip` 26.1.2 est installé et associé à Python 3.13. Le chemin local de l'installation n'est pas reproduit ici.

La commande `code --version` a confirmé que VS Code 1.136.2 est installé et accessible depuis PowerShell. La sortie indique également une installation 64 bits.

La commande `code .` a ouvert le dossier `azure-ai-150-days` dans VS Code. Le projet peut donc être ouvert depuis le terminal dans le bon contexte.

La commande `docker --version` a répondu `Docker version 29.7.2`. Le client Docker est donc installé et accessible depuis le terminal.

La première exécution de `docker version` a affiché les informations du client, mais pas celles du serveur. Elle n'a pas trouvé le point de communication `dockerDesktopLinuxEngine`, ce qui indiquait que le moteur Docker Desktop n'était pas démarré.

Après le démarrage de Docker Desktop, une seconde exécution de `docker version` a affiché les sections `Client` et `Server`. Le moteur Docker 29.7.2 fonctionne sous Linux et peut exécuter des conteneurs.

La commande `docker run --rm hello-world` a téléchargé l'image de test officielle, créé un conteneur temporaire, exécuté son programme puis affiché `Hello from Docker!`. Le conteneur a été supprimé après son exécution grâce à l'option `--rm`.

La commande `Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber` a identifié Windows 10 Home, la version 2009 et le numéro de build 26200.

La commande `Get-Command git, python, code, docker | Select-Object Name, Source` a trouvé les quatre programmes dans les dossiers attendus. Leur accès depuis PowerShell est donc correctement configuré par la variable `PATH`. Les chemins complets ne sont pas reproduits ici car certains contiennent le nom du compte Windows.

La commande `Get-ChildItem -LiteralPath day-002 -Force` a confirmé que le dossier contient uniquement `README.md` et `diagnostic_environnement.md`.

La commande `rg` n'est pas disponible dans PowerShell sur ce poste. Cette absence n'empêche pas le travail, car `Select-String`, intégré à PowerShell, permet de réaliser la même vérification.

La commande `Select-String` n'a produit aucun résultat. Aucune des formes courantes de clé, mot de passe ou jeton recherchées n'a été détectée dans les fichiers du Jour 2.

## Erreur contrôlée ou cas limite

### Erreur

Exécution de `docker version` alors que Docker Desktop n'est pas démarré.

### Comportement observé

Docker a affiché les informations du client puis a renvoyé une erreur de connexion au moteur `dockerDesktopLinuxEngine`.

### Cause racine

Le client Docker est installé, mais le moteur Docker Desktop qui exécute les conteneurs est arrêté. Le point de communication Windows utilisé par le client n'existe donc pas encore.

### Correction

Démarrer Docker Desktop et attendre que son moteur soit prêt.

### Vérification après correction

Après le démarrage de Docker Desktop, `docker version` a affiché la section `Server`. La correction est validée.

## Exercices

### 1. Définition de l'environnement Windows, WSL2 et VS Code

Windows est le système d'exploitation principal de mon ordinateur. WSL2 est une fonctionnalité de Windows qui me permet d'utiliser un environnement Linux, comme Ubuntu, directement depuis Windows. Il est utile pour exécuter des commandes et des outils Linux sans installer ni gérer une machine virtuelle classique. VS Code est un éditeur de code qui me permet d'ouvrir mes projets, modifier les fichiers, utiliser le terminal et travailler avec des extensions adaptées à mes besoins. Cet environnement doit être prêt pour travailler avec Python, Git, Docker et Azure.

### 2. Rôle de Windows et de WSL2

Windows est mon environnement principal pour les logiciels natifs, comme VS Code, PowerShell et d'autres applications. WSL2 me permet d'utiliser des outils et des commandes Linux lorsque le contexte l'exige. Ensemble, ils me permettent d'être polyvalent et de choisir l'environnement adapté au travail à réaliser.

### 3. Terminal et extensions VS Code

Le terminal permet d'exécuter des commandes et d'observer leur résultat. Selon la commande utilisée, elles peuvent agir sur les fichiers, les dossiers ou les programmes dans Windows, WSL ou Docker. Je l'utilise pour lancer une commande, vérifier une version ou diagnostiquer une erreur. Une extension VS Code est un ajout qui apporte des fonctions utiles à l'éditeur, par exemple l'aide pour Python, Git, Docker ou WSL. Je l'utilise lorsque je veux une aide visuelle dans l'éditeur, comme l'affichage des erreurs ou la complétion du code.

### 4. Exemple de problème réel

Lorsque Docker est installé, Docker Desktop doit aussi être démarré. Sinon, `docker version` peut afficher les informations du client, mais échouer pour le serveur. Dans ce cas, aucun conteneur ne peut être exécuté et le projet qui en dépend ne peut pas démarrer. Je détecte ce problème grâce au message d'erreur de `docker version`, puis je vérifie que Docker Desktop est lancé avant d'utiliser Docker.

### 5. Preuve technique du bon fonctionnement

Le fichier `diagnostic_environnement.md` est ma preuve principale. Pour vérifier que mon environnement est prêt, j'utilise des commandes dans le terminal afin de connaître la version des outils installés. Je vérifie aussi que les outils sont accessibles grâce à la variable `PATH`. Enfin, je réalise un test complet, comme l'exécution du conteneur `hello-world`, pour vérifier que toute la chaîne fonctionne.

### 6. Compromis identifié

WSL2 permet d'utiliser des outils Linux tout en gardant Windows comme environnement principal. En contrepartie, l'environnement devient plus complexe, car il faut savoir dans quel terminal travailler, où se trouvent les fichiers et comment Docker utilise WSL2.

### 7. Premier diagnostic en cas de problème

Si une commande cesse de fonctionner, je commence par réduire le problème : je vérifie ce qui fonctionne encore et ce qui échoue. Je lis ensuite attentivement le message d'erreur et vérifie la commande saisie. Je vérifie que l'outil est accessible avec une commande de version, comme `git --version` ou `python --version`, puis je contrôle l'état du service concerné, par exemple Docker Desktop pour Docker ou `wsl --status` pour WSL. Avant de modifier une configuration, je cherche ce qui a changé récemment et je collecte des preuves.

### 8. Explication du sujet du jour

J'ai vérifié mon environnement de travail pour m'assurer que les outils nécessaires sont installés, accessibles et réellement fonctionnels. Windows est mon environnement principal, tandis que WSL2 me donne accès aux outils Linux. Git, Python, VS Code et Docker servent à développer, versionner et exécuter des projets. Les commandes de diagnostic et le test Docker ont confirmé que toute la chaîne fonctionne. Cette configuration apporte de la souplesse, mais elle demande aussi de comprendre quel environnement utilise chaque outil.

## Notions à retenir

1. WSL2 permet d'utiliser un environnement Linux depuis Windows.
2. Le terminal permet d'exécuter des commandes et d'observer leur résultat.
3. Les extensions ajoutent des fonctions à VS Code selon les besoins du projet.
4. La variable `PATH` permet au terminal de trouver les programmes exécutables.
5. Un workspace est le dossier de référence d'un projet. Il rassemble les fichiers, les dossiers, la documentation et les réglages nécessaires au travail.

## Limite, risque et compromis

Le risque principal est de croire qu'un outil fonctionne simplement parce qu'il est installé. Docker a montré que le client peut être disponible alors que le moteur est arrêté. La limite de cette séance est que les contrôles ont été réalisés sur ce poste et à cet instant. Le compromis consiste à consacrer du temps aux vérifications pour réduire les erreurs pendant les futurs projets.

## Bilan personnel

Aujourd'hui, j'ai vérifié les outils essentiels de mon environnement de travail. J'ai compris le rôle de Windows, WSL2, Git, Python, VS Code, Docker et de la variable `PATH`. J'ai aussi diagnostiqué puis corrigé un problème réel avec Docker Desktop. Je sais maintenant commencer par des vérifications simples et observables avant de modifier une configuration.
