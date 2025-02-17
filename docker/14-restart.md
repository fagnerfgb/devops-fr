#Auteur : Fagner Geraldes Braga  
#Date de création : 17/02/2025  
#Date de mise à jour : 17/02/2025  
#Version : 0.01  

## Résilience et gestion des ressources 

### Construction et exécution de l’image

```bash
# Accéder au répertoire du projet CAOS
cd docker/projets/caos/src/

# Construire une image Docker à partir du Dockerfile et la nommer "fagnerfgb/caos:v1"
docker build -t fagnerfgb/caos:v1 -f Dockerfile .

# Exécuter un conteneur à partir de l'image construite, en le nommant "caos" et en mappant le port 8080 de l'hôte au port 3000 du conteneur
docker container run --name caos -d -p 8080:3000 fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de manière forcée
docker container rm -f caos
```

### Docker Restart - On-failure
```bash
# Surveiller en temps réel la liste de tous les conteneurs (en cours d'exécution et arrêtés)
watch 'docker container ls -a'
```

```bash
# Exécuter un conteneur nommé "caos" en arrière-plan avec une politique de redémarrage en cas d'échec
docker container run --name caos -d -p 8080:3000 --restart=on-failure fagnerfgb/caos:v1

# Supprimer de force le conteneur "caos"
docker container rm -f caos

# Exécuter un conteneur nommé "caos" avec une limite de redémarrage de 3 tentatives en cas d'échec
docker container run --name caos -d -p 8080:3000 --restart=on-failure:3 fagnerfgb/caos:v1

# Supprimer de force le conteneur "caos"
docker container rm -f caos
```

```bash
# Exécuter un conteneur nommé "caos" avec une limite de redémarrage de 3 tentatives en cas d'échec
docker container run --name caos -d -p 8080:3000 --restart=on-failure:3 fagnerfgb/caos:v1

# Arrêter le service Docker
sudo systemctl stop docker

# Démarrer le service Docker
sudo systemctl start docker

# Supprimer de force le conteneur "caos"
docker container rm -f caos
```

### Docker Restart - Unless-stopped
```bash
# Surveiller en temps réel la liste de tous les conteneurs (en cours d'exécution et arrêtés)
watch 'docker container ls -a'
```

```bash
# Exécuter un conteneur nommé "caos" qui redémarre automatiquement sauf s'il est arrêté manuellement
docker container run --name caos -d -p 8080:3000 --restart=unless-stopped fagnerfgb/caos:v1

# Arrêter le service Docker
sudo systemctl stop docker

# Démarrer le service Docker
sudo systemctl start docker

# Arrêter le conteneur "caos" manuellement
docker container stop caos

# Démarrer à nouveau le conteneur "caos"
docker container start caos

# Supprimer de force le conteneur "caos"
docker container rm -f caos
```

### Docker Restart - Always
```bash
# Surveiller en temps réel la liste de tous les conteneurs (en cours d'exécution et arrêtés)
watch 'docker container ls -a'
```

```bash
# Exécuter un conteneur nommé "caos" qui redémarre toujours, quel que soit l'état précédent
docker container run --name caos -d -p 8080:3000 --restart=always fagnerfgb/caos:v1

# Arrêter le conteneur "caos"
docker container stop caos

# Arrêter le service Docker
sudo systemctl stop docker

# Démarrer le service Docker
sudo systemctl start docker

# Supprimer de force le conteneur "caos"
docker container rm -f caos
```

### Docker Restart - Docker Compose
### Compose.yaml
[compose](/docker/projets/caos/src/compose.yaml)

```bash
# Surveiller en temps réel la liste de tous les conteneurs (en cours d'exécution et arrêtés)
watch 'docker container ls -a'
```
```bash

# Démarrer les services définis dans le fichier docker-compose.yaml en arrière-plan (mode détaché)
docker compose up -d
```