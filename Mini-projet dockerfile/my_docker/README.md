# Projet simple avec un Dockerfile

Attention de bien effectuer les commandes dans le fichier app/

## Structure du Projet

- `app`: Application Flask qui présente une page web statique basique.

### Arborescence du Projet

my_docker_project/
├── app/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
└── 

### app

- `app/app.py`: Contient le code Flask pour l'application `app`. Cette application affiche une page web statique.
- `app1/requirements.txt`: Spécifie les dépendances Python pour `app`.
- `app/Dockerfile`: Définit l'image Docker pour `app`.


## Instructions de Lancement

Pour lancer les applications, suivez ces étapes :

1. Construire et démarrer le conteneur :
 - docker build -t app .
 - docker run app

2. Accéder à l'application :
- App : Ouvrez votre navigateur et accédez à http://127.0.0.1:5000.
