#Auteur : Fagner Geraldes Braga  
#Date de création : 27/02/2025  
#Date de mise à jour : 27/02/2025  
#Version : 0.01  

## Cosign

### Installation

```bash
# Récupérer la dernière version disponible de Cosign depuis l'API GitHub
LATEST_VERSION=$(curl https://api.github.com/repos/sigstore/cosign/releases/latest | grep tag_name | cut -d : -f2 | tr -d "v\", ")

# Télécharger le fichier .deb correspondant à la dernière version de Cosign
curl -O -L "https://github.com/sigstore/cosign/releases/latest/download/cosign_${LATEST_VERSION}_amd64.deb"

# Installer Cosign à l'aide du gestionnaire de paquets Debian (dpkg)
sudo dpkg -i cosign_${LATEST_VERSION}_amd64.deb

# Supprimer le fichier .deb téléchargé après l'installation
rm -r cosign_*.deb
```

### Gerando par de chaves

```bash
# Générer une paire de clés pour la signature d'images avec Cosign
cosign generate-key-pair --output-key-prefix my-key
```

### Assinatura de imagem

### Dockerfile04
[Dockerfile04](/docker/projets/chaotique/Dockerfile04)

```bash
# Se déplacer dans le répertoire du projet
cd docker/projets/chaotique

# Construire l'image Docker avec le fichier Dockerfile04
docker build -t fagnerfgb/chaotique-signe:v1 -f Dockerfile04 ./src

# Ajouter une tag "latest" à l'image créée
docker tag fagnerfgb/chaotique-signe:v1 fagnerfgb/chaotique-signe:latest

# Se connecter à Docker Hub
docker login

# Pousser les images vers Docker Hub
docker push fagnerfgb/chaotique-signe:v1 && docker push fagnerfgb/chaotique-signe:latest

# Signer l'image avec la clé privée générée
cosign sign --key ~/my-key.key fagnerfgb/chaotique-signe:v1

# Vérifier la signature de l'image avec la clé publique
cosign verify --key ~/my-key.pub fagnerfgb/chaotique-signe:v1

# Signer l'image en ajoutant un attribut "owner" avec la valeur "Fagner Braga"
cosign sign --key ~/my-key.key -a owner="Fagner Braga" fagnerfgb/chaotique-signe:v1

# Vérifier de nouveau la signature après l'ajout des métadonnées
cosign verify --key ~/my-key.pub fagnerfgb/chaotique-signe:v1

# Exporter la clé privée comme variable d'environnement
export COSIGN_KEY=$(cat ~/my-key.key)

# Afficher toutes les variables d'environnement pour vérifier
env

# Signer l'image en utilisant la clé depuis la variable d'environnement
cosign sign --key env://COSIGN_KEY -a proprietario="Fagner Braga" fagnerfgb/chaotique-signe:v1

# Exporter la clé publique comme variable d'environnement
export COSIGN_PUB=$(cat ~/my-key.pub)

# Vérifier la signature en utilisant la clé publique depuis la variable d'environnement
cosign verify --key env://COSIGN_PUB fagnerfgb/chaotique-signe:v1
```