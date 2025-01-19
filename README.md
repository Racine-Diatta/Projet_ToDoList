# Description du Projet:

L'objectif de ce projet est de développer une application de gestion des tâches (Todo List) en suivant une architecture en couches.

- L'interface graphique est réalisée en PyQt6.
- MySQL est a base de données relationnelle utilisée.

L'application contient les fonctionnalités suivantes (cf. la maquette de l'application) :

- Ajout de tâches
- Affichage des tâches dans une liste avec un checkboxpour marquer les tâches "faites ou non faites" et un bouton pour "supprimer" pour une tâche.
- Persistance des données : toutes les tâches seront stockées dans une base de données MySQL.
- Mis en place d'un systeme pour sécuriser l'application via un validateur anti-injection SQL au niveau de la couche métier (BLL)

Un certains nombre de série de tests unitaires sur les anti-injection SQL pour vérifier le bon fonctionnement des validateurs

# Comment faire marcher ce projet :

Rmq : Pour des mesures de sécurité, les remarques suivantes peuvent être prises en compte:

1. le nom de la base de données peut porter un autre nom que "todolist".
2. D'autres valeurs que "myuser", "localhost" et "mypassword" de l'utilisateur peuvent être choisi.

## Créer la base de données "todolist" et sa table "task" dans une base de données mySql:

```SQL
SET default_storage_engine = InnoDB;
CREATE DATABASE IF NOT EXISTS todolist
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE todolist;

CREATE TABLE task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    is_done BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDAT CURRENT_TIMESTAMP
);
```

## Créer un utilisateur myuser avec le mot de passe mypassword:

```SQL
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
```

## Octroyer les droits à notre utilisateur sur todolist:

```SQL
GRANT SELECT, INSERT, UPDATE, DELETE ON todolist.* TO 'myuser'@'localhost';
```

## Installer les dépendances suivantes sur le projet:

    pip install PyQt6
    pip install mysql-connector-python
    pip install python-dotenv

## Définir les variables d'environnement:

- Adapter les variables d'environnement dans ".env" à la configuration de votre base de données.

## Installer PlantUML sur vscode

Deux options pour voir le diagramme de classe :

- Option 1: aller sur classDiag.wsd et faire Alt + D
- Option 2: aller sur classDiag.wsd et faire "click droit" => "Preview Current Diagram"

## Lancer le projet

    python main.py
