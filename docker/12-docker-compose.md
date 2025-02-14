#Auteur : Fagner Geraldes Braga  
#Date de création : 06/02/2025  
#Date de mise à jour : 13/02/2025  
#Version : 0.03  

## Docker Compose

### Nginx basique
### Compose01.yaml
[compose01](12-compose/compose01.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les services définis dans 'compose01.yaml' en mode détaché
docker compose -f compose01.yaml up -d

# Lister les conteneurs en cours d'exécution
docker container ls

# Arrêter les services définis dans 'compose01.yaml'
docker compose -f compose01.yaml stop

# Redémarrer les services définis dans 'compose01.yaml'
docker compose -f compose01.yaml start

# Supprimer les services et les réseaux associés définis dans 'compose01.yaml'
docker compose -f compose01.yaml down
```
### CMD
### Compose02.yaml
[compose02](12-compose/compose02.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les services définis dans 'compose02.yaml' en mode détaché
docker compose -f compose02.yaml up -d

# Lister tous les conteneurs, y compris ceux qui sont arrêtés
docker container ls -a

# Supprimer les services et les réseaux associés définis dans 'compose02.yaml'
docker compose -f compose02.yaml down
```

### 2 conteneurs Nginx
### Compose03.yaml
[compose03](12-compose/compose03.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les services définis dans 'compose03.yaml' en arrière-plan
docker compose -f compose03.yaml up -d

# Lister les conteneurs en cours d'exécution
docker container ls

# Arrêter et supprimer les services et réseaux définis dans 'compose03.yaml'
docker compose -f compose03.yaml down
```

### Variables d'environnement
### Compose04.yaml
[compose04](12-compose/compose04.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les services définis dans 'compose04.yaml' en arrière-plan
docker compose -f compose04.yaml up -d

# Lister les conteneurs en cours d'exécution
docker container ls

# Arrêter et supprimer les services et réseaux définis dans 'compose04.yaml'
docker compose -f compose04.yaml down
```
### Bind Mount
### Compose05.yaml
[compose05](12-compose/compose05.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les services définis dans 'compose05.yaml' en arrière-plan
docker compose -f compose05.yaml up -d

# Lister les conteneurs en cours d'exécution
docker container ls

# Arrêter et supprimer les services et réseaux définis dans 'compose05.yaml'
docker compose -f compose05.yaml down
```

### Volume
### Compose06.yaml
[compose06](12-compose/compose06.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les services définis dans 'compose06.yaml' en arrière-plan
docker compose -f compose06.yaml up -d

# Lister les conteneurs en cours d'exécution
docker container ls

# Lister les volumes Docker existants
docker volume ls

# Inspecter les détails du conteneur nommé 'fgb-postgre'
docker container inspect fgb-postgre

# Inspecter les détails du volume nommé 'my_postgre_vol'
docker volume inspect my_postgre_vol

# Arrêter et supprimer les services, réseaux et volumes définis dans 'compose06.yaml'
docker compose -f compose06.yaml down
```

### Volume externe
### Compose07.yaml
[compose07](12-compose/compose07.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Créer un volume Docker nommé "my_external_volume"
docker volume create my_external_volume

# Démarrer les conteneurs définis dans le fichier compose07.yaml en mode détaché
docker compose -f compose07.yaml up -d

# Lister tous les volumes Docker existants
docker volume ls

# Inspecter le conteneur "fgb-postgre" et rechercher l'utilisation du volume "my_external_volume"
docker container inspect fgb-postgre | grep '"Name": "my_external_volume"' -A 4

# Afficher les détails du volume "my_external_volume"
docker volume inspect my_external_volume

# Arrêter et supprimer les conteneurs définis dans le fichier compose07.yaml
docker compose -f compose07.yaml down
```

### Réseau Bridge
### Compose08.yaml
[compose08](12-compose/compose08.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les conteneurs définis dans le fichier compose08.yaml en mode détaché
docker compose -f compose08.yaml up -d

# Lister tous les réseaux Docker existants
docker network ls

# Inspecter le réseau Docker nommé "knews_network"
docker network inspect knews_network

# Arrêter et supprimer les conteneurs définis dans le fichier compose08.yaml
docker compose -f compose08.yaml down
```

### Exécution des conteneurs postgre et de l’application sur le même réseau bridge
### Compose09.yaml
[compose09](12-compose/compose09.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les conteneurs définis dans le fichier compose09.yaml en mode détaché
docker compose -f compose09.yaml up -d

# Arrêter et supprimer les conteneurs définis dans le fichier compose09.yaml
docker compose -f compose09.yaml down
```

### Host driver et Add host
### Compose10.yaml
[compose10](12-compose/compose10.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les conteneurs définis dans le fichier compose10.yaml en mode détaché
docker compose -f compose10.yaml up -d

# Lister les conteneurs en cours d'exécution
docker container ls

# Inspecter le conteneur fgb-nginx pour afficher ses détails
docker container inspect fgb-nginx

# Inspecter le conteneur fgb-curl pour afficher ses détails
docker container inspect fgb-curl

# Accéder à un shell interactif dans le conteneur fgb-curl
docker container exec -it fgb-curl /bin/bash
```

```bash
# Envoyer une requête HTTP à fagner.com.br
curl fagner.com.br

# Quitter le conteneur
exit
```

```bash
# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans compose10.yaml
docker compose -f compose10.yaml down

```

### Ordonner l’exécution des conteneurs
### Compose11.yaml
[compose11](12-compose/compose11.yaml)
```bash
# Se déplacer vers le répertoire contenant le fichier compose
cd docker/12-compose/

# Démarrer les conteneurs en arrière-plan en utilisant le fichier compose11.yaml
docker compose -f compose11.yaml up -d

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans compose11.yaml
docker compose -f compose11.yaml down
```

### Réalisation de la construction de l’image avec docker compose
### Compose12.yaml
[compose12](projets/kube-news/compose12.yaml)
```bash
# Se déplacer vers le répertoire du projet kube-news
cd docker/projets/kube-news/

# Démarrer les conteneurs en arrière-plan avec le fichier compose12.yaml
docker compose -f compose12.yaml up -d

# Reconstruire les images et redémarrer les conteneurs en arrière-plan
docker compose -f compose12.yaml up -d --build

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans compose12.yaml
docker compose -f compose12.yaml down
```

### Fichier .env
### Compose13.yaml
[compose13](projets/kube-news/compose13.yaml)
```bash
# Se déplacer vers le répertoire du projet kube-news
cd docker/projets/kube-news/

# Générer la configuration Docker Compose avec les variables d'environnement définies directement dans la commande
KUBE_NEWS_TAG=v1 POSTGRES_TAG=12.17 POSTGRES_PASSWORD=pwdkubenews POSTGRES_USER=kubenews POSTGRES_DB=kubenews docker compose -f compose13.yaml config

# Générer la configuration Docker Compose en utilisant un fichier d'environnement
docker compose --env-file dev.env -f compose13.yaml config

# Démarrer les conteneurs en arrière-plan en utilisant un fichier d'environnement
docker compose --env-file dev.env -f compose13.yaml up -d

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans compose13.yaml
docker compose --env-file dev.env -f compose13.yaml down
```

### Extends
### kube-news-compose.yaml e Compose14.yaml 
[kube-news-compose](projets/kube-news/kube-news-compose.yaml)
[compose14](projets/kube-news/compose14.yaml)
```bash
# Se déplacer vers le répertoire du projet kube-news
cd docker/projets/kube-news/

# Générer la configuration Docker Compose en utilisant un fichier d'environnement
docker compose --env-file dev.env -f compose14.yaml config

# Démarrer les conteneurs en arrière-plan en utilisant un fichier d'environnement
docker compose --env-file dev.env -f compose14.yaml up -d

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans compose14.yaml
docker compose --env-file dev.env -f compose14.yaml down
```

### Merge
### Compose15.yaml e Compose16.yaml 
[compose15](projets/kube-news/compose15.yaml)
[compose16](projets/kube-news/compose16.yaml)
```bash
# Se déplacer vers le répertoire du projet kube-news
cd docker/projets/kube-news/

# Générer la configuration Docker Compose en combinant deux fichiers de configuration
docker compose --env-file dev.env -f compose15.yaml -f compose16.yaml config

# Démarrer les conteneurs en arrière-plan en utilisant les deux fichiers de configuration
docker compose --env-file dev.env -f compose15.yaml -f compose16.yaml up -d

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans les fichiers de configuration
docker compose --env-file dev.env -f compose15.yaml -f compose16.yaml down
```

### Include
### kube-news-compose.yaml e Compose17.yaml 
[kube-news-compose](projets/kube-news/kube-news-compose.yaml)
[compose17](projets/kube-news/compose17.yaml)
```bash
# Se déplacer vers le répertoire du projet kube-news
cd docker/projets/kube-news/

# Générer la configuration Docker Compose en combinant deux fichiers de configuration
docker compose --env-file dev.env -f compose17.yaml -f kube-news-compose.yaml config

# Démarrer les conteneurs en arrière-plan en utilisant les deux fichiers de configuration
docker compose --env-file dev.env -f compose17.yaml -f kube-news-compose.yaml up -d

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans les fichiers de configuration
docker compose --env-file dev.env -f compose17.yaml -f kube-news-compose.yaml down
```

### Profiles
### Compose18.yaml
[compose18](projets/kube-news/compose18.yaml)
```bash
# Se déplacer vers le répertoire du projet kube-news
cd docker/projets/kube-news/

# Générer la configuration Docker Compose en activant le profil "dev"
docker compose --env-file dev.env -f compose18.yaml --profile dev config

# Démarrer les conteneurs en arrière-plan en activant uniquement le profil "dev"
docker compose --env-file dev.env -f compose18.yaml --profile dev up -d

# Arrêter et supprimer les conteneurs, réseaux et volumes définis dans le profil "dev"
docker compose --env-file dev.env -f compose18.yaml --profile dev down
```
