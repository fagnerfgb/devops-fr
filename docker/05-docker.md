#Auteur : Fagner Geraldes Braga  
#Date de création : 27/01/2025  
#Date de mise à jour : 27/01/2025  
#Version : 0.01  

## IMAGE DE L’APPLICATION AVEC DOCKERFILE

### Tous les fichiers Dockerfile de cette partie sont dans le dossier température/src/

### Dockerfile01
[Dockerfile01](projets/celsius-farenheit/src/Dockerfile01)

```bash
# Change le répertoire actuel pour accéder au dossier source du projet
cd docker/projets/celsius-farenheit/src/

# Construit une image Docker à partir de Dockerfile01 et lui attribue un tag spécifique
docker build -t fagnerfgb/celsius-farenheit:v1 -f Dockerfile01 .

# Lance un conteneur en arrière-plan, lié au port 8080, à partir de l'image construite
docker container run --rm -d -p 8080:8080 fagnerfgb/celsius-farenheit:v1

# Supprime tous les conteneurs existants (actifs et inactifs)
docker container rm -f $(docker container ls -qa)

# Supprime toutes les images Docker existantes (quelles que soient leurs balises)
docker image rm -f $(docker image ls -qa)

# Supprime toutes les images inutilisées pour libérer de l'espace
docker image prune
```