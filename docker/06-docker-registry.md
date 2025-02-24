#Auteur : Fagner Geraldes Braga  
#Date de création : 28/01/2025  
#Date de mise à jour : 28/01/2025  
#Version : 0.01  

## Docker Registry

### Création d’une image avec la nomenclature correcte pour l’envoi à DockerHub

### Dockerfile01
[Dockerfile01](projets/celsius-farenheit/Dockerfile01)

```bash
# Change le répertoire actuel pour accéder au dossier source du projet
cd docker/projets/celsius-farenheit

# Construit une image Docker à partir de Dockerfile01 et lui attribue un tag spécifique
docker build -t fagnerfgb/celsius-farenheit:v1 -f Dockerfile01 ./src

# Ajoute un nouveau tag "latest" à l'image existante avec le tag "v1"
docker tag fagnerfgb/celsius-farenheit:v1 fagnerfgb/celsius-farenheit:latest
```
### Envoyer l’image à DockerHub
```bash
# Connectez-vous à Docker Hub avec vos informations d'identification
docker login

# Poussez l'image avec le tag "v1" vers Docker Hub, puis poussez l'image avec le tag "latest"
docker push fagnerfgb/celsius-farenheit:v1 && docker push fagnerfgb/celsius-farenheit:latest

# Supprime toutes les images Docker existantes (quelles que soient leurs balises)
docker image rm -f $(docker image ls -qa)

# Supprime toutes les images inutilisées pour libérer de l'espace
docker image prune

# Téléchargez l'image "fagnerfgb/celsius-farenheit" depuis Docker Hub
docker pull fagnerfgb/celsius-farenheit
```