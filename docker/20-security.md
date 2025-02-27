#Auteur : Fagner Geraldes Braga  
#Date de création : 27/02/2025  
#Date de mise à jour : 27/02/2025  
#Version : 0.01  

## Linux Capabilities et Docker Privileged

```bash
# Lancer un conteneur Ubuntu en mode interactif et supprimer automatiquement après l'arrêt
docker container run --rm --name ubuntu -it ubuntu /bin/bash
```

```bash
# Monter le répertoire /etc sur /mnt en utilisant bind
mount -o bind /etc /mnt

# Quitter la session actuelle
exit
```

```bash
# Lancer un conteneur Ubuntu en mode interactif avec la capacité SYS_ADMIN
docker container run --rm --name ubuntu -it --cap-add=SYS_ADMIN ubuntu /bin/bash
```

```bash
# Monter le répertoire /etc sur /mnt en utilisant bind
mount -o bind /etc /mnt

# Quitter la session actuelle
exit
```

```bash
# Lancer un conteneur Ubuntu en mode interactif avec des privilèges élevés
docker container run --rm --name ubuntu -it --privileged ubuntu /bin/bash
```

```bash
# Monter le répertoire /etc sur /mnt en utilisant bind
mount -o bind /etc /mnt

# Quitter la session actuelle
exit
```
## Imagens Distroless

### Dockerfile05
[Dockerfile05](/docker/projets/chaotique/Dockerfile05)

```bash
# Accéder au répertoire du projet
cd docker/projets/chaotique

# Construire l'image Docker à partir de Dockerfile05 et la taguer comme version v6
docker build -t fagnerfgb/chaotique:v6 -f Dockerfile05 ./src

# Taguer la version v6 comme "latest"
docker tag fagnerfgb/chaotique:v6 fagnerfgb/chaotique:latest

# Se connecter au Docker Hub
docker login

# Pousser les images v6 et latest vers le Docker Hub
docker push fagnerfgb/chaotique:v6 && docker push fagnerfgb/chaotique:latest

# Exécuter un conteneur en arrière-plan avec l'image v6
docker container run --name chaotique -d -p 8080:8080 fagnerfgb/chaotique:v6

# Supprimer le conteneur après utilisation
docker container rm -f chaotique
```