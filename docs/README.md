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
cd {repertoire}

# install des lib du requirements
pip install -r requirements.txt