#Auteur : Fagner Geraldes Braga  
#Date de création : 18/02/2025  
#Date de mise à jour : 18/02/2025  
#Version : 0.01  

## Healthcheck

### Compose.yaml
[compose](/docker/projets/caos/src/compose.yaml)

```bash
# Se déplacer dans le répertoire du projet contenant le fichier docker-compose.yaml
cd docker/projets/caos/src/

# Démarrer les services en arrière-plan
docker compose up -d

# Arrêter et supprimer les conteneurs et réseaux associés
docker compose down
```
### Healthcheck - Ligne de commande
```bash
# Surveiller en temps réel la liste de tous les conteneurs (en cours d'exécution et arrêtés)
watch 'docker container ls -a'
```

```bash
# Exécuter un conteneur nommé "caos" en arrière-plan
docker container run --name caos -d \
  # Mapper le port 8080 de l'hôte sur le port 3000 du conteneur
  -p 8080:3000 \
  # Définir une commande de vérification de l'état du conteneur
  --health-cmd "curl -f http://localhost:3000/health" \
  # Définir un délai maximal de réponse pour la commande de santé
  --health-timeout 5s \
  # Nombre maximum de tentatives avant de considérer le conteneur en échec
  --health-retries 3 \
  # Intervalle entre chaque vérification de l'état du conteneur
  --health-interval 10s \
  # Temps d'attente avant de commencer les vérifications de l'état après le démarrage
  --health-start-period 30s \
  # Image Docker à utiliser
  fagnerfgb/caos:v1

# Supprimer de force le conteneur nommé "caos" s'il est en cours d'exécution ou arrêté
docker container rm -f caos
```

### Healthcheck - Docker compose

### compose-healthcheck.yaml
[compose-healthcheck.yaml](/docker/projets/caos/src/compose-healthcheck.yaml)

```bash
# Surveiller en temps réel la liste de tous les conteneurs (en cours d'exécution et arrêtés)
watch 'docker container ls -a'
```

```bash
# Démarrer les services définis dans le fichier compose-healthcheck.yaml en mode détaché
docker compose -f compose-healthcheck.yaml up -d

# Arrêter et supprimer les services définis dans le fichier compose-healthcheck.yaml
docker compose -f compose-healthcheck.yaml down
```

### Healthcheck - Dockerfile

### Dockerfile-healthcheck
[Dockerfile-healthcheck](/docker/projets/caos/src/Dockerfile-healthcheck)

```bash
# Surveiller en temps réel la liste de tous les conteneurs (en cours d'exécution et arrêtés)
watch 'docker container ls -a'
```

```bash
# Construire une image Docker à partir du Dockerfile-healthcheck avec le tag fagnerfgb/caos:v2
docker build -t fagnerfgb/caos:v2 -f Dockerfile-healthcheck .

# Démarrer un conteneur nommé "caos" en mode détaché, exposant le port 3000 sur l'hôte via le port 8080
docker container run --name caos -d -p 8080:3000 fagnerfgb/caos:v2

# Supprimer de force le conteneur "caos"
docker container rm -f caos
```

### compose-healthcheck-image.yaml
[compose](/docker/projets/caos/src/compose-healthcheck-image.yaml)

```bash
# Démarrer les services définis dans le fichier compose-healthcheck-image.yaml en arrière-plan
docker compose -f compose-healthcheck-image.yaml up -d

# Arrêter et supprimer les services définis dans le fichier compose-healthcheck-image.yaml
docker compose -f compose-healthcheck-image.yaml down
```