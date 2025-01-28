#Auteur : Fagner Geraldes Braga  
#Date de création : 28/01/2025  
#Date de mise à jour : 28/01/2025  
#Version : 0.01  

### Amélioration du fichier Dockerfile
### Dockerfile-alpine01
[Dockerfile-alpine01](projets/celsius-farenheit/src/Dockerfile-alpine01)

```bash
# Construire une nouvelle image Docker en utilisant Dockerfile-alpine01 et la taguer comme "fagnerfgb/celsius-farenheit:v2"
docker build -t fagnerfgb/celsius-farenheit:v2 -f Dockerfile-alpine01 .

# Mettre à jour le tag "latest" pour pointer vers l'image "v2"
docker tag fagnerfgb/celsius-farenheit:v2 fagnerfgb/celsius-farenheit:latest

# Lancer un conteneur en arrière-plan avec le port 8080 exposé pour l'image "v2"
docker container run -d -p 8080:8080 fagnerfgb/celsius-farenheit:v2

# Supprime tous les conteneurs existants (actifs et inactifs)
docker container rm -f $(docker container ls -qa)

# Supprime toutes les images Docker existantes (quelles que soient leurs balises)
docker image rm -f $(docker image ls -qa)

# Supprime toutes les images inutilisées pour libérer de l'espace
docker image prune
```