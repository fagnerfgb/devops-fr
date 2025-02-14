#Auteur : Fagner Geraldes Braga  
#Date de création : 14/02/2025  
#Date de mise à jour : 14/02/2025  
#Version : 0.01  

## Troubleshooting

### Docker info
```bash
# Exécuter un conteneur de test pour vérifier si Docker fonctionne correctement
docker container run hello-world

# Démarrer un conteneur Nginx en arrière-plan
docker container run -d nginx

# Afficher les informations du serveur Docker, y compris la version et d'autres détails
docker info | grep Server: -A 5
```

### Docker events
```bash
# Afficher en temps réel les événements Docker
docker events

# Afficher les événements Docker des deux dernières heures
docker events --since 2h

# Afficher les événements Docker jusqu'à il y a 10 minutes
docker events --until 10m

# Filtrer uniquement les événements liés à la création de ressources
docker events --filter event=create

# Afficher les événements de création des deux dernières heures
docker events --since 2h --filter event=create

# Afficher uniquement les événements liés aux images Docker des deux dernières heures
docker events --since 2h --filter type=image

# Afficher uniquement les événements liés aux réseaux Docker des deux dernières heures
docker events --since 2h --filter type=network

# Filtrer uniquement les événements de création de réseaux des deux dernières heures
docker events --since 2h --filter type=network --filter event=create
```

### Docker logs
```bash
# Exécuter un conteneur Nginx en arrière-plan et exposer le port 8080
docker container run --name nginx -d -p 8080:80 nginx

# Afficher les journaux du conteneur Nginx
docker logs nginx

# Tester l'accès au serveur Nginx avec curl
curl http://localhost:8080

# Afficher à nouveau les journaux après la requête curl
docker logs nginx

# Suivre les journaux en temps réel du conteneur Nginx
docker container logs nginx --follow

# Tester à nouveau l'accès au serveur Nginx avec curl
curl http://localhost:8080

# Afficher les journaux du conteneur Nginx après la dernière requête
docker logs nginx

# Afficher les journaux des 10 dernières minutes
docker logs nginx --since 10m

# Afficher les journaux jusqu'à il y a 3 minutes
docker logs nginx --until 3m

# Afficher les journaux jusqu'à il y a 1 minute
docker logs nginx --until 1m

# Afficher les journaux depuis une date et heure spécifiques
docker logs nginx --since "2025-01-06T12:14:00Z"

# Afficher uniquement les 3 dernières lignes des journaux
docker logs nginx --tail 3
```
### Docker inspect
```bash
# Inspecter les détails du conteneur Nginx
docker container inspect nginx 

# Inspecter les détails de l'image Nginx
docker image inspect nginx

# Inspecter les détails du réseau bridge par défaut
docker network inspect bridge
```
### Docker Top
```bash
# Afficher les processus en cours d'exécution dans le conteneur Nginx
docker top nginx

# Alternative pour afficher les processus en cours d'exécution dans le conteneur Nginx
docker container top nginx
```

### Docker Stats
```bash
# Afficher les statistiques en temps réel des conteneurs en cours d'exécution
docker stats

# Afficher une seule mise à jour des statistiques des conteneurs en cours d'exécution
docker stats --no-stream

# Afficher les statistiques en temps réel du conteneur Nginx
docker container stats nginx 

# Afficher une seule mise à jour des statistiques du conteneur Nginx
docker container stats --no-stream nginx 

# Afficher les statistiques complètes du conteneur Nginx sans troncature
docker container stats --no-trunc nginx
```

### Docker exec
```bash
# Lister les fichiers et dossiers dans le conteneur Nginx avec des détails sur la taille
docker exec nginx ls -lh

# Afficher le répertoire de travail actuel dans le conteneur Nginx
docker exec nginx pwd

# Ouvrir un terminal interactif Bash dans le conteneur Nginx
docker exec -it nginx /bin/bash

# Ouvrir un terminal interactif SH dans le conteneur Nginx (utile si Bash n'est pas installé)
docker exec -it nginx /bin/sh
```