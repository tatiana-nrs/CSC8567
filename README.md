# CSC 8567 - Architectures distribuées et applications web

## Auteurs : Timothée Mathubert, Gatien Roujanski, Arthur Jovart

## Emails

timothee.mathubert@telecom-sudparis.eu
gatien.roujanski@telecom-sudparis.eu
arthur.jovart@telecom-sudparis.eu

## Installation

**Il est recommandé d'utiliser un système d'exploitation type Linux.**

1. Créer un environnement virtuel Python avec conda
```
sudo apt install conda
sudo apt install python
sudo apt install pip
conda init
conda create -n CSC8567
conda activate CSC8567
```
2. Installer les dépendances utiles
```
pip install django
```
3. Créer le projet Django & vérifier qu'il tourne correctement
```
cd django-site
django-admin startproject django-site
python manage.py runserver
```
Allez sur 127.0.0.1:8000 sur un navigateur. Si une page "Congratulations!" s'affiche, c'est que tout fonctionne bien !

4. Créez les applications utiles
```
python manage.py startapp public
python manage.py startapp api
```