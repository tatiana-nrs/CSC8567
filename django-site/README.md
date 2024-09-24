LISTE DES CHEMINS URL DU SITE: 

Pour l'application api: 

URL de base: /api/ 

Liste des chemins: 
/api/garages/ : Vue pour la liste des garages (GarageList).
/api/voitures/ : Vue pour la liste des voitures (VoitureList).
/api/cles/ : Vue pour la liste des clés (CleList).


Pour l'application public:

URL de base: /public/

Liste des chemins :
/public/ : Page d'accueil.
/public/voitures/ : Vue pour la liste des voitures (list_cars).
/public/voitures/<int:voiture_id>/ : Vue pour le détail d'une voiture spécifique (detail_cars).
/public/cles/ : Vue pour la liste des clés (list_keys)

Enfin au niveau du projet:

Liste des chemins :

/admin/ : Interface d'administration de Django.
/api/ : Inclut les URL de l'application api.
/public/ : Inclut les URL de l'application public.



QUESTIONS:

Fonctionnement de Django:

Questions 1: Vous disposez d'un projet Django dans lequel une application public a été créée. Décrivez la suite de requêtes et d'exécutions permettant l'affichage d'une page HTML index.html à l'URL global / via une application public, ne nécessitant pas de contexte de données. Vous décrirez la position exacte dans l'arborescence des répertoires des différents fichiers utiles à cette exécution.

Afin d'afficher une page HTML index.html à l'URL global / via une application public, il existe plusieurs étapes:

Premièrement, l'arborescence des répertoires des différents fichiers utiles à cette éxécution est la suivante: 

projet/
│
├── manage.py
├── projet/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── public/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── index.html

Ainsi les fichiers qui nous intéressent pour cette étape sont les fichiers projet/public/views.py, projet/public/templates/index.html ainsi que les deux fichiers projet/public/urls.py et projet/projet/urls.py.

Tout d'abord, il faut créer la fonction qui va renvoyer la page index.html lorsque l'on accède à l'URL / dans projet/public/views.py. Ce fichier utilise la fonction render() pour afficher le template projet/public/templates/index.html. Il est de la forme suivante:

from django.shortcuts import render

def index(request):
    return render(request, 'public/index.html')


Ensuite, il faut il faut rajouter l'URL de la vue dans projet/public/views.py puis inclure cette URL dans les URLs principales du projet:

projet/public/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL / redirige vers la vue index
]


projet/projet/urls/py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('public.urls')),
]

Puis, il faut créer le template html projet/public/templates/index.html avec le contenu que l'on souhaite afficher.

Enfin il faut s'assurer que le paramètres APP_DIRS soit à true dans les settings pour permettre la recherche des fichiers dans les templates.

On peut lancer le serveur Django avec la commande python manage.py runserver 




Question 2: Dans quelle(s) section(s) de quel(s) fichier(s) peut-on configurer la base de données que l'on souhaite utiliser pour un projet Django ?

Généralement, la configuration de la base de données que l'on souhaite utiliser dans un projet Django se fait dans le fichier projet/projet/settings.py. Ce fichier contient une section DATABASES qui définit la base de données que le projet Django utilise. 

Par défaut, cette section configure une base de données SQLite :

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

Cette base de données est généralement utilisée pour le développement. 

Cependant, avec Django, on peut séparer facilement les réglages de production des réglages de developpemnt ou test en faisant des fichiers de settings différents. Pour la production, il est mieux d'utiliser une base de données PostgreSQL ou MySQL. 

Ainsi, il est possible de créer des fichiers de configuration spécifiques à la production par exemple et de créer un fichier prod_settings.py qui surchargerait la section DATABASES du fichier settings.py ou encore un fichier de settings par application d'un même projet Django. 



Question 3: Dans quel(s) fichier(s) peut-on configurer le fichier de paramètres que l'on souhaite faire utiliser par le projet Django ? Si plusieurs fichers sont à mentionner, expliquez le rôle de chaque fichier.

Le fichier de paramètres que l'on souhaite utiliser pour le projet Django peut être configuré dans plusieurs fichiers. En effet, lorsque l'on lance une application Django, la valeur d'une variable d'environnement DJANGO_SETTINGS_MODULE est récupérée et cette dernière peut pointer vers un fichier de settings particulier. Par défaut, si cette variable est absente, c'est le fichier settings.py qui est utilisé. 

Il est possible de préciser cette valeur dans le fichier manage.py. Ce fichier est crée automatiquement dans chaque projet Django et permet d'éxécuter les commande Django (démarrer le serveur, effectuer les migrations). La variable DJANGO_SETTINGS_MODULE peut être définie de la sorte:

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.public_settings') #pour l'application public par exemple

De manière similaire, il est possible de spécifier cette valeur dans le fichier wsgi.py qui est un point d’entrée pour les serveurs Web compatibles WSGI (comme Apache) ou encore dans le fichier asgi.py qui est un point d’entrée pour les serveurs Web compatibles ASGI (Asynchronous Server Gateway Interface). 

De plus, si l'on souhaite placer les applications dans des conteneurs, il est également possible de définir cette varibale dans le Dockerfile de chaque application avec:

ENV DJANGO_SETTINGS_MODULE=projet.public_settings

Le Dockerfile permet de créer une image Docker contenant tout ce dont a besoin l'application pour fonctionner à savoir le code source, les bibliothèques, les dépendances...

Enfin, on peut également définir cette variable dans le docker-compose.yaml avec: 

    environment:
      - DJANGO_SETTINGS_MODULE=projet.public_settings

Ce fichier permet de gérer et de coordonner plusieurs conteneurs Docker formant un ensemble d'applications interconnectées en définissant la manière dont plusieurs services (ici base de données, nginx, api et public) intéragissent entre eux.


Question 4: Nous nous plaçons à la racine de votre projet Django. Quel effet a l'exécution python manage.py makemigrations ? Et l'exécution python manage.py migrate ? Quel(s) fichier(s) sont mis en oeuvre pendant ces exécutions ?

Premièrement, ces deux commandes jouent un rôle dans la gestion de la base de données et des modèles. En effet, elles permettent de transformer les modèles Python en tables SQL dans la base de données. 

La commande python manage.py makemigrations ne modifie pas la base de données mais génère des fichiers de migrations qui traduisent les modifications apportées aux modèles Django en opérations (création de table, suppression, modification...) pour la base de données.

La commande python manage.py migrate elle, lit les fichiers de migrations et applique les migrations générées par la commande précédente à la base de données en appliquant les opérations.

Pendant ces éxécutions, les fichiers mis en oeuvre sont:

Le fichier models.py qui contient la définissions des modèles de l'application qui sont des classes Python définissant la structure de la base de données (tables, champs... )

les fichiers dans migrations/. Ce répertoire est crée automatiquement dans le répertoire des applications. En effet, à l'éxécution de la première commande, Django crée un fichier de migration dans ce répertoire avec un nom qui commence par un numéro (0001_initial.py). Ces fichiers contiennent les instructions pour Django sur les modifications apportées aux modèles et donc à la base de données. Ces modifications sont apportées à la base de données du fichiers de settings choisi. 




Fonctionnement de Docker

Question 1: Expliquez l'effet et la syntaxe de ces commandes, communément vues dans des fichiers Dockerfile : FROM, RUN, WORKDIR, EXPOSE, CMD.

La commande FROM permet de spécifier l'image de base à partir de laquelle l'image Docker sera construite (distribution linux, environnement de langage spécifique...).

La commande RUN crée des couches dans l'image et exécute des instructions (commandes shell) à l'intérieur du conteneur pendant la création de l'image et est utilisée pour installée des dépendances ou configurer l'environnement d'exécution.

La commande WORKDIR définit (le crée s'il n'existe pas) le répertoire de travail pour les instructions suivantes.

La commande EXPOSE indique les ports sur lesquels une application dans le conteneur écoute les connexions réseau. Cette commande sert plus d'instruction à titre informatif. 

Enfin, la commande CMD définit la commande par défaut à exécuter une fois que le conteneur est démarré. Une seule commande CMD est permise par Dockerfile. 


Question 2: Dans la définition d'un service dans le fichier docker-compose.yml, expliquez l'effet des mentions :

ports:
    - "80:80"

build: 
    context: .
    dockerfile: Dockerfile.api

depends_on:
    - web
    - api

environment:
    POSTGRES_DB: ${POSTGRES_DB}
    POSTGRES_USER: ${POSTGRES_USER}
    POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}


Premièrement, ces mentions configurent différents aspects d'un service donné. 

La première ports permet de publier des ports internes du conteneur Docker vers l'hôte éxecutant Docker. Dans l'exemple donné, le port 80 du conteneur est mappé au port 80 de l'hôte. Ici,  dans "80:80" le premier 80 correspond au port de l'hôte. 

build: 
    context: .
    dockerfile: Dockerfile.api

Cette section permet de définir le contexte de construction de l'image, ici le répertoire courant . et indique à Docker le Dockerfile à utiliser pour construire l'image. 


depends_on:
    - web
    - api

Cette section gère l'ordre de démarrage des services et indique que le service dépend d'autres services ici web et api et Docker démarrera donc ces services avant de démarrer le service en cours sans garantir pour autant que les services listés sont totalement prêts. 


Enfin, la section environnement permet de définir des variables d'environnement pour le service donné (ici celles de configuration de la base de données). 


Question 3: Citez une méthode pour définir des variables d'environnement dans un conteneur.

Il est possible de définir des variables d'environnement dans le Dockerfile à l'aide de la commande ENV.


Question 4: Dans un même réseau Docker, nous disposons d'un conteneur nginx (utilisant l'image nginx:latest) et d'un conteneur web (utilisant une image contenant un projet web Django, ayant la commande python manage.py runserver 0.0.0.0:8000 de lancée au démarrage du conteneur). Comment adresser le serveur web tournant dans le conteneur web depuis le conteneur nginx, sans utiliser les adresses IP des conteneurs ?

Pour adresser le serveur web tournant dans le conteneur web depuis le conteneur nginx, sans utiliser les adresses IP des conteneurs, il faut savoir que dans Docke, les conteneurs connectés au même réseau peuvent se communiquer par leurs noms de service, grâce au DNS interne de Docker.


































