#Auteur : Fagner Geraldes Braga  
#Date de création : 24/02/2025  
#Date de mise à jour : 24/02/2025  
#Version : 0.01  

## Docker Scout

### Installation

```bash
# Télécharger et exécuter le script d'installation de Docker Scout CLI en toute sécurité
curl -sSfL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh | sh -s --
```
### Construction de l'image

### Dockerfile
[Dockerfile](/docker/projets/chaotique/Dockerfile)

```bash
# Se déplacer vers le répertoire du projet
cd docker/projets/chaotique/

# Construire l'image Docker à partir du Dockerfile situé dans ./src
docker build -t fagnerfgb/chaotique:v1 -f Dockerfile ./src

# Ajouter un tag "latest" à l'image créée
docker tag fagnerfgb/chaotique:v1 fagnerfgb/chaotique:latest

# Exécuter un conteneur à partir de l'image en exposant le port 8080
docker container run --name chaotique -d -p 8080:8080 fagnerfgb/chaotique:v1

# Supprimer le conteneur chaotique s'il existe
docker container rm -f chaotique
```

### Vérification de l’image

```bash
# Afficher un résumé de l'analyse de l'image
docker scout quickview fagnerfgb/chaotique:v1

# Vérifier les vulnérabilités de sécurité (CVEs) dans l'image
docker scout cves fagnerfgb/chaotique:v1

# Afficher les CVEs au format Markdown
docker scout cves --format markdown fagnerfgb/chaotique:v1

# Enregistrer le résultat des CVEs dans un fichier Markdown
docker scout cves --format markdown fagnerfgb/chaotique:v1 > verifier.md

# Analyser rapidement la structure du répertoire actuel comme une source d’image
docker scout quickview fs://.

# Vérifier les vulnérabilités dans la structure du répertoire actuel
docker scout cves fs://.
```

### Ajouter un dépôt dans Docker Scout

```bash
# Se connecter à Docker Hub
docker login

# Pousser les tags v1 et latest de l'image vers Docker Hub
docker push fagnerfgb/chaotique:v1 && docker push fagnerfgb/chaotique:latest

# Activer la surveillance de Docker Scout pour ce dépôt
docker scout repo enable fagnerfgb/chaotique --org fagnerfgb
```

### Première amélioration de l’image

### Dockerfile01 e Dockerfile02
[Dockerfile01](/docker/projets/chaotique/Dockerfile01) [Dockerfile02](/docker/projets/chaotique/Dockerfile02)

```bash
# Obtenir les recommandations de Docker Scout pour améliorer l'image v1
docker scout recommendations fagnerfgb/chaotique:v1

# Construire la nouvelle version v2 de l'image avec Dockerfile01
docker build -t fagnerfgb/chaotique:v2 -f Dockerfile01 ./src

# Taguer la nouvelle version comme "latest"
docker tag fagnerfgb/chaotique:v2 fagnerfgb/chaotique:latest

# Envoyer la version v2 et latest vers Docker Hub
docker push fagnerfgb/chaotique:v2 && docker push fagnerfgb/chaotique:latest

# Construire la nouvelle version v3 de l'image avec Dockerfile02
docker build -t fagnerfgb/chaotique:v3 -f Dockerfile02 ./src

# Taguer la nouvelle version comme "latest"
docker tag fagnerfgb/chaotique:v3 fagnerfgb/chaotique:latest

# Envoyer la version v3 et latest vers Docker Hub
docker push fagnerfgb/chaotique:v3 && docker push fagnerfgb/chaotique:latest

# Comparer les versions v2 et v3 pour identifier les améliorations et les différences
docker scout compare --to fagnerfgb/chaotique:v2 fagnerfgb/chaotique:v3
```

### Deuxième amélioration de l’image

### Dockerfile02
[Dockerfile02](/docker/projets/chaotique/Dockerfile02)

```bash
# Vérifie les recommandations d'amélioration pour l'image chaotique:v3
docker scout recommendations fagnerfgb/chaotique:v3

# Liste les vulnérabilités de sécurité dans l'image chaotique:v3
docker scout cves fagnerfgb/chaotique:v3

# Installe les dépendances du projet dans le répertoire src
npm install ./src

# Corrige automatiquement les vulnérabilités dans les dépendances du projet
npm audit fix --force

# Vérifie les vulnérabilités directement dans le code source avant de générer une nouvelle image
docker scout cves fs://.

# Construit la nouvelle image chaotique:v4 en utilisant Dockerfile02
docker build -t fagnerfgb/chaotique:v4 -f Dockerfile02 ./src

# Crée un tag "latest" pour la nouvelle image chaotique:v4
docker tag fagnerfgb/chaotique:v4 fagnerfgb/chaotique:latest

# Pousse les images chaotique:v4 et chaotique:latest vers Docker Hub
docker push fagnerfgb/chaotique:v4 && docker push fagnerfgb/chaotique:latest

# Vérifie à nouveau s'il y a des vulnérabilités dans l'image chaotique:v4
docker scout cves fagnerfgb/chaotique:v4

# Exécute la nouvelle version chaotique:v4 dans un conteneur nommé chaotique
docker container run --name chaotique -d -p 8080:8080 fagnerfgb/chaotique:v4

# Supprime le conteneur chaotique pour libérer des ressources
docker container rm -f chaotique
```

### Paquets et SBOM

```bash
# Analyse l'image chaotique:v4 pour générer une SBOM (Software Bill of Materials)
docker scout sbom fagnerfgb/chaotique:v4

# Génère une SBOM sous forme de liste pour une meilleure lisibilité
docker scout sbom --format=list fagnerfgb/chaotique:v4
```