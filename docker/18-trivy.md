#Auteur : Fagner Geraldes Braga  
#Date de création : 24/02/2025  
#Date de mise à jour : 24/02/2025  
#Version : 0.01  

## Trivy

### Installation

```bash
# Installer les paquets nécessaires pour télécharger et ajouter des clés GPG
sudo apt-get install wget apt-transport-https gnupg lsb-release -y

# Télécharger la clé publique de Trivy et l'ajouter au trousseau de clés GPG
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null

# Ajouter le dépôt Trivy à la liste des sources APT
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list

# Mettre à jour les dépôts APT
sudo apt-get update

# Installer Trivy
sudo apt-get install trivy
```

### Analyse du dockerfile

### Dockerfile03
[Dockerfile03](/docker/projets/chaotique/Dockerfile03)

```bash
# Analyser le fichier Dockerfile03 dans le répertoire actuel pour détecter des vulnérabilités ou des mauvaises configurations
trivy config --file-patterns "dockerfile:Dockerfile03" .
```
### Balayage de l’image

### Dockerfile04
[Dockerfile04](/docker/projets/chaotique/Dockerfile04)

```bash
# Analyser l'image v1 de la configuration Docker pour détecter les vulnérabilités
trivy image fagnerfgb/chaotique:v1

# Analyser l'image v4 de la configuration Docker pour détecter les vulnérabilités
trivy image fagnerfgb/chaotique:v4

# Analyser l'image v4 avec plusieurs scanners : vulnérabilités, mauvaises configurations, secrets, et licences
trivy image --scanners vuln,misconfig,secret,license fagnerfgb/chaotique:v4

# Installer les dépendances du projet avec npm
npm install ./src

# Corriger automatiquement les vulnérabilités de sécurité des dépendances avec npm
npm audit fix --force

# Construire une nouvelle version de l'image Docker (v5) en utilisant Dockerfile04
docker build -t fagnerfgb/chaotique:v5 -f Dockerfile04 ./src

# Taguer la nouvelle version construite comme "latest"
docker tag fagnerfgb/chaotique:v5 fagnerfgb/chaotique:latest

# Pousser les versions v5 et latest vers le Docker Hub
docker push fagnerfgb/chaotique:v5 && docker push fagnerfgb/chaotique:latest

# Analyser la nouvelle image v5 pour détecter les vulnérabilités
trivy image fagnerfgb/chaotique:v5
```

### Inventaire des logiciels installés

```bash
# Analyser l'image fagnerfgb/chaotique:v5 et générer un rapport au format SPDX JSON
trivy image --format spdx-json --output result-spdx.json fagnerfgb/chaotique:v5

# Analyser l'image fagnerfgb/chaotique:v5 et générer un rapport au format CycloneDX JSON
trivy image --format cyclonedx --output result-cyclonedx.json fagnerfgb/chaotique:v5