#Auteur : Fagner Geraldes Braga  
#Date de création : 05/03/2025  
#Date de mise à jour : 05/03/2025  
#Version : 0.01  

## Docker in Docker

### Docker in Docker avec le docker.sock

```bash
# Lancer un conteneur Ubuntu en mode interactif avec accès au socket Docker
docker container run -it -v /var/run/docker.sock:/var/run/docker.sock ubuntu /bin/bash
```

```bash
# Mettre à jour la liste des paquets et installer curl
apt update && apt install curl -y

# Télécharger l'image Nginx via l'API Docker
curl --unix-socket /var/run/docker.sock -X POST http://localhost/images/create?fromImage=nginx:latest

# Créer un conteneur à partir de l'image Nginx
curl --unix-socket /var/run/docker.sock -X POST -d '{"Image":"nginx"}' -H "Content-Type: application/json" http://localhost/containers/create

# Démarrer le conteneur avec l'ID 38a8716360cc
curl --unix-socket /var/run/docker.sock -X POST http://localhost/containers/38a8716360cc/start
```

### L'installation du Docker CLI
```bash
# Mettre à jour la liste des paquets
apt-get update

# Installer les certificats SSL et curl
apt-get install ca-certificates curl -y

# Créer un répertoire sécurisé pour les clés APT
install -m 0755 -d /etc/apt/keyrings

# Télécharger et ajouter la clé GPG officielle de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# Définir les permissions pour la clé GPG
chmod a+r /etc/apt/keyrings/docker.asc

# Ajouter le dépôt Docker à la liste des sources APT
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Mettre à jour la liste des paquets après l'ajout du dépôt Docker
apt-get update

# Installer uniquement le client Docker (sans le moteur)
apt-get install docker-ce-cli -y

# Vérifier les conteneurs en cours d'exécution
docker container ls
```

### Docker in Docker avec le DinD

```bash
# Exécuter un conteneur Docker-in-Docker (DinD) en mode détaché avec les privilèges nécessaires
docker container run -d --name dind-test --privileged docker:dind

# Accéder au shell interactif du conteneur en cours d'exécution
docker exec -it dind-test /bin/sh
```

```bash
# Lister les conteneurs en cours d'exécution
docker container ls

# Exécuter un conteneur en arrière-plan avec l'image Nginx
docker container run -d nginx

# Vérifier à nouveau les conteneurs en cours d'exécution
docker container ls
```

### Exécution du projet dans un conteneur et création de conteneurs
```bash
# Exécuter un conteneur temporaire avec l'image kubedevio/db-to-dev:v1
# en montant le socket Docker pour permettre l'accès à l'hôte Docker.
# La commande "criar" est exécutée à l'intérieur du conteneur.
docker container run --rm -v /var/run/docker.sock:/var/run/docker.sock kubedevio/db-to-dev:v1 criar

# Lister les conteneurs en cours d'exécution pour vérifier s'il y a des changements
docker container ls
```