#Auteur : Fagner Geraldes Braga  
#Date de création : 21/01/2025  
#Date de mise à jour : 21/01/2025  
#Version : 0.01  

### Installer Docker Engine sur Ubuntu

```bash
# Mettre en place des Dockers apt archivage.
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```bash
# Pour installer la dernière version, exécutez:
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```bash
# Créer le docker groupe
sudo groupadd docker
```

```bash
# Ajoutez votre utilisateur au docker groupe.
sudo usermod -aG docker $USER
```

```bash
# Connectez-vous et reconnectez-vous afin que votre appartenance à un groupe soit réévaluée.
exit

# Vérifier que l'installation est réussie en exécutant le hello-world image
docker run hello-world
```