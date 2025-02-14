# Calculatrice Indice Masse Corporelle - IMC

### Projet de développement de site web en HTML5 + CSS3 + Bootstrap + Docker

### Des technologies utilisées

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)

### Création d’image Docker 

[Dockerfile](/docker/projets/imc/Dockerfile)

```bash
# Accède au répertoire du projet IMC
cd docker/projets/imc

# Construit l'image Docker avec le tag v1 en utilisant le Dockerfile du répertoire actuel
docker build -t fagnerfgb/imc:v1 -f Dockerfile .

# Crée un tag "latest" pour l'image nouvellement construite
docker tag fagnerfgb/imc:v1 fagnerfgb/imc:latest
```

### Envoyer l’image à DockerHub
```bash
# Se connecte à Docker Hub
docker login

# Pousse l'image avec le tag v1 vers le registre Docker Hub
docker push fagnerfgb/imc:v1

# Pousse l'image avec le tag latest vers le registre Docker Hub
docker push fagnerfgb/imc:latest
```

### Exécuter le conteneur, tester, supprimer le conteneur et supprimer l’image
```bash
# Lance un conteneur en arrière-plan avec le nom 'srv-imc', mappant le port 8080 de l'hôte au port 80 du conteneur
docker container run --name srv-imc -d -p 8080:80 fagnerfgb/imc:v1

# Ouvrir le navigateur et entrer l'URL : http://localhost:8080

# Supprime de force le conteneur 'srv-imc'
docker container rm -f srv-imc
```

### Exécuter et fermer le conteneur à l’aide de Docker Compose

[compose](/docker/projets/imc/compose.yaml)

```bash
docker compose -f compose.yaml up -d

docker compose -f compose.yaml down
```

