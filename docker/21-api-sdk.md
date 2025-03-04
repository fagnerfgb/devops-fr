#Auteur : Fagner Geraldes Braga  
#Date de création : 04/03/2025  
#Date de mise à jour : 04/03/2025  
#Version : 0.01  

## Docker API et Docker SDK

### Docker API

```bash
# Lister les fichiers dans le répertoire /var/run
ls /var/run

# Afficher la version de Docker installée
docker version

# Obtenir la version de l'API Docker via le socket Unix
curl --unix-socket /var/run/docker.sock http://localhost/version

# Mettre à jour la liste des paquets
sudo apt update

# Installer jq pour formater la sortie JSON
sudo apt-get install jq -y

# Obtenir la version de l'API Docker et la formater avec jq
curl --unix-socket /var/run/docker.sock http://localhost/version | jq .

# Obtenir les informations du daemon Docker et les formater avec jq
curl --unix-socket /var/run/docker.sock http://localhost/info | jq .
```

```bash
# Télécharger l'image Nginx depuis Docker Hub en utilisant l'API Docker
curl --unix-socket /var/run/docker.sock -X POST http://localhost/images/create?fromImage=nginx:latest

# Créer un conteneur basé sur l'image Nginx
curl --unix-socket /var/run/docker.sock -X POST -d '{"Image":"nginx"}' -H "Content-Type: application/json" http://localhost/containers/create

# Démarrer un conteneur spécifique avec son ID (exemple : 1d4f20a8fcacb4e1294f8c2dbb9925bc560894b2364480e10bd1e524390c5679)
curl --unix-socket /var/run/docker.sock -X POST http://localhost/containers/1d4f20a8fcacb4e1294f8c2dbb9925bc560894b2364480e10bd1e524390c5679/start

# Lister les conteneurs en cours d'exécution
curl --unix-socket /var/run/docker.sock -X GET http://localhost/containers/json

# Lister les conteneurs en cours d'exécution avec une sortie formatée en JSON
curl --unix-socket /var/run/docker.sock -X GET http://localhost/containers/json | jq .

# Lister tous les conteneurs (en cours d'exécution et arrêtés) avec une sortie formatée en JSON
curl --unix-socket /var/run/docker.sock -X GET http://localhost/containers/json?all=true | jq .

# Créer un conteneur basé sur Nginx avec le port 80 redirigé vers le port 8080 de l'hôte
curl --unix-socket /var/run/docker.sock -X POST -d '{"Image":"nginx","HostConfig": {"PortBindings":{"80/tcp" : [{"HostIp":"0.0.0.0","HostPort": "8080"}]}}}' -H "Content-Type: application/json" http://localhost/containers/create

# Démarrer un conteneur spécifique avec son ID (exemple : dde5e383e2b43e22ba2bc4a03f3dd0ab1127f3d260650c240f81e80ae4fa0b28)
curl --unix-socket /var/run/docker.sock -X POST http://localhost/containers/dde5e383e2b43e22ba2bc4a03f3dd0ab1127f3d260650c240f81e80ae4fa0b28/start

# Lister tous les conteneurs (en cours d'exécution et arrêtés) avec une sortie formatée en JSON
curl --unix-socket /var/run/docker.sock -X GET http://localhost/containers/json?all=true | jq .

# Supprimer un conteneur spécifique avec son ID en forçant la suppression
curl --unix-socket /var/run/docker.sock -X DELETE http://localhost/containers/dde5e383e2b43e22ba2bc4a03f3dd0ab1127f3d260650c240f81e80ae4fa0b28?force=true
```

### Docker SDK

```bash
# Mettre à jour la liste des paquets disponibles
sudo apt update

# Installer pipx, un gestionnaire pour exécuter des applications Python isolées
sudo apt install pipx -y

# Assurer que le chemin de pipx est correctement ajouté à l'environnement de l'utilisateur
pipx ensurepath

# Exécuter la même commande avec sudo pour s'assurer que le chemin est bien configuré pour l'utilisateur root
sudo pipx ensurepath

# Installer virtualenv via pipx pour gérer des environnements virtuels Python isolés
pipx install virtualenv
```

```bash
# Se déplacer dans le répertoire du projet Python
cd docker/projets/python

# Créer un environnement virtuel nommé "dockerenv"
virtualenv dockerenv

# Activer l'environnement virtuel
source dockerenv/bin/activate

# Installer la bibliothèque Docker pour interagir avec l'API Docker depuis Python
pip install docker

# Exécuter le script Python 01.py
python3 01.py

# Lister tous les conteneurs, y compris ceux arrêtés
docker container ls -a

# Exécuter les autres scripts Python du projet
python3 02.py
python3 03.py
python3 04.py
python3 05.py
python3 06.py
```

```bash
# Se déplacer dans le répertoire du projet de développement de base de données
cd docker/projets/db-dev/src

# Créer un environnement virtuel nommé "dockerenv"
virtualenv dockerenv

# Activer l'environnement virtuel
source dockerenv/bin/activate

# Installer la bibliothèque Docker pour interagir avec l'API Docker depuis Python
pip install docker

# Créer une nouvelle base de données avec les paramètres par défaut
python3 index.py criar

# Créer une base de données personnalisée avec un nom, un utilisateur et un mot de passe
python3 index.py criar --banco exemplo --user fagner --pwd senha1234

# Lister toutes les bases de données disponibles
python3 index.py listar

# Supprimer une base de données spécifique en utilisant son ID
python3 index.py remover --id 21e3c0821d2d0a8d59c65f0f7a06ff9750ad683824d2e36d089fc6afc1e04570

# Supprimer une autre base de données spécifique en utilisant son ID
python3 index.py remover --id f60ec759420458c35b394d2bff52c748f1312c0a1f292577e4ddfafc5bcc4b1e
```