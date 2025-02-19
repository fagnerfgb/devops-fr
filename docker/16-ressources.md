#Auteur : Fagner Geraldes Braga  
#Date de création : 19/02/2025  
#Date de mise à jour : 19/02/2025  
#Version : 0.01  

## Gestion des ressources

### Processeur

```bash
# Se déplacer vers le répertoire du projet
cd docker/projets/caos/src

# Exécuter un conteneur nommé "caos" en arrière-plan sur le port 8080:3000
docker container run --name caos -d -p 8080:3000 fagnerfgb/caos:v1

# Afficher les statistiques en temps réel des conteneurs en cours d'exécution
docker stats

# Supprimer le conteneur "caos" de force
docker container rm -f caos

# Exécuter un conteneur avec une limite de CPU (50% d'un CPU disponible)
docker container run --name caos -d -p 8080:3000 --cpu-period=100000 --cpu-quota=50000 fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de force
docker container rm -f caos

# Exécuter un conteneur avec une limite de CPU (50% d'un CPU) et forcer l'utilisation du CPU 0
docker container run --name caos -d -p 8080:3000 --cpu-period=100000 --cpu-quota=50000 --cpuset-cpus=0 fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de force
docker container rm -f caos

# Exécuter un conteneur avec 1.5 CPU alloués et restreint aux CPU 0 et 1
docker container run --name caos -d -p 8080:3000 --cpus=1.5 --cpuset-cpus=0-1 fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de force
docker container rm -f caos

# Exécuter un conteneur avec 2 CPU alloués et restreint aux CPU 0 et 1
docker container run --name caos -d -p 8080:3000 --cpus=2 --cpuset-cpus=0-1 fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de force
docker container rm -f caos
```

### Mémoire vive

```bash
# Exécuter un conteneur nommé "caos" en arrière-plan sur le port 8080:3000
docker container run --name caos -d -p 8080:3000 fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de force
docker container rm -f caos

# Exécuter un conteneur avec une limite de 50 Mo de RAM et 100 Mo de mémoire swap
docker container run --name caos -d -p 8080:3000 --memory=50M --memory-swap=100M fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de force
docker container rm -f caos

# Exécuter un conteneur avec une limite stricte de 50 Mo de RAM sans swap supplémentaire
docker container run --name caos -d -p 8080:3000 --memory=50M --memory-swap=50M fagnerfgb/caos:v1

# Supprimer le conteneur "caos" de force
docker container rm -f caos
```

### Docker compose

[compose](/docker/projets/caos/src/compose-recursos.yaml)

```bash
# Démarrer les services définis dans le fichier compose-recursos.yaml en mode détaché
docker compose -f compose-recursos.yaml up -d

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans compose-recursos.yaml
docker compose -f compose-recursos.yaml down
```
