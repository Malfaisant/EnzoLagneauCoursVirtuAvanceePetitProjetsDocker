# Projet Docker : Communication entre deux applications Flask

Ce projet démontre la communication entre deux applications web basées sur Flask, chacune exécutée dans un conteneur Docker distinct. L'application `app1` envoie des requêtes HTTP à l'application `app2` et affiche les réponses.

## Structure du Projet

- `app1`: Application Flask qui présente un formulaire web pour collecter un nom et fait des requêtes HTTP POST vers `app2`.
- `app2`: Application Flask qui reçoit les requêtes HTTP POST de `app1`, traite les données reçues et renvoie une réponse JSON.

### Arborescence du Projet

my_docker_project/
├── app1/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
├── app2/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
└── docker-compose.yml


## Description des Fichiers

### app1

- `app1/app.py`: Contient le code Flask pour l'application `app1`. Cette application affiche un formulaire web, envoie le nom saisi à `app2` et affiche la réponse.
- `app1/requirements.txt`: Spécifie les dépendances Python pour `app1`.
- `app1/Dockerfile`: Définit l'image Docker pour `app1`.

### app2

- `app2/app.py`: Contient le code Flask pour l'application `app2`. Cette application reçoit les données de `app1`, traite le nom et renvoie une réponse JSON.
- `app2/requirements.txt`: Spécifie les dépendances Python pour `app2`.
- `app2/Dockerfile`: Définit l'image Docker pour `app2`.

### docker-compose.yml

Définit les services Docker pour `app1` et `app2`, leurs images, les ports exposés et les dépendances.

## Instructions de Lancement

Pour lancer les applications, suivez ces étapes :

1. Construire et démarrer les conteneurs :
Utilisez Docker Compose pour construire les images et démarrer les conteneurs :

	sudo docker-compose up --build

2. Accéder aux applications :
- App1 : Ouvrez votre navigateur et accédez à http://localhost:5000. Vous verrez un formulaire où vous pouvez entrer un nom.
- App2 : Ouvrez votre navigateur et accédez à http://localhost:5001. Vous verrez un message de bienvenue de app2.

# Comment Tester l'Échange entre les Applications

1. Ouvrir App1 :

Dans votre navigateur, allez à http://localhost:5000.

2. Soumettre un Nom :
- Entrez un nom dans le formulaire et cliquez sur "Submit".
- app1 enverra une requête HTTP POST à app2 contenant le nom.

3. Vérifier la Réponse :
- app2 reçoit la requête, traite le nom, et renvoie une réponse JSON contenant un message de salutation.
- app1 affiche la réponse de app2 sur la même page.

