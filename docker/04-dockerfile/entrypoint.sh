#!/bin/bash

if [ -z $1 ]
then
    echo "Démarrage du conteneur sans paramètre"
else
    echo "Démarrage du conteneur avec le paramètre $1"
fi