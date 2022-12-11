# EPSI B3 ASRBD 2022 - Aline REVERSAT - Simon MARTIN - Antonin NOIRAULT

# Install de virtualenv
py -m pip install virtualenv

# Création du dossier environement
mkdir environementPython && cd environementPython

# Install de l'environement 
py -m venv .env

# Démarrage de l'environnement 
.env\Scripts\activate 

# mise a jour de pip si nécésaire
py -m pip install --upgrade pip

# Retourner au répertoire du projet 
cd {repertoire/pokedexv2}

# install des lib du requirements
pip install -r requirements.txt

# aller dans le repertoire de code 
cd /src

# Exécuter les commandes suivantes:
py manage.py  makemigrations
py manage.py  migrate

# lancer l'application avec 
py manage.py  runserver

# ouvrir la page dans la navigateur 
http://127.0.0.1:8000/pokedex/