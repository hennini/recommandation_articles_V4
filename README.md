# Recommandation d'Articles - Azure Function

Cette application déployée sur **Azure Functions** fournit des recommandations d'articles personnalisées pour un utilisateur donné, en fonction d'un modèle pré-entraîné.

---

## Table des matières

1. [Description]
2. [Fonctionnalités]
3. [Technologies Utilisées]
4. [Données Nécessaires]
5. [Prérequis]
6. [Installation et Déploiement]
7. [Contributions]
8. [Licence]

---

## Description

Cette API fournit des recommandations d'articles pour un utilisateur en fonction des catégories préférées du modèle d'utilisateur.  
Le système s'appuie sur :
- Un fichier **pickle** contenant un modèle `KNNWithMeans` de `Surprise` pour estimer les préférences utilisateur.
- Un fichier CSV contenant des métadonnées d'articles.

---

## Fonctionnalités

- Accepter un **ID utilisateur** en tant que paramètre de requête ou dans le corps de la requête.
- Prédire les **catégories préférées** de l'utilisateur à l'aide du modèle pré-entraîné.
- Sélectionner des articles pertinents à partir des catégories identifiées.
- Retourner les résultats sous forme de réponse JSON.

---

## Technologies Utilisées

- **Azure Functions :** Déploiement de l'API sans serveur.
- **Python :** Langage principal utilisé pour l'application.
- **Bibliothèques :**
  - `pandas` pour la manipulation des données.
  - `pickle` pour le chargement du modèle de prédiction.
  - `numpy` pour les calculs numériques.
  - `azure-functions` pour le développement d'une fonction HTTP.
  - `Surprise` pour le modèle de recommandation.

---

## Données Nécessaires

- **Modèle pré-entraîné :** `pickle_surprise_model_KNNWithMeans.pkl`
- **Fichier CSV :** `articles_metadata.csv` contenant :
  - `article_id` : Identifiant unique d'article.
  - `category_id` : Identifiant de la catégorie associée à l'article.

Ces fichiers doivent être placés dans le même répertoire que le code avant exécution.

---

## Prérequis

- **Python 3.9 ou supérieur** installé.
- **Azure Functions Core Tools** pour tester localement.
- Modules Python suivants (installés via `pip`) :
  ```bash
  pip install pandas numpy azure-functions scikit-surprise

## Installation et Déploiement

### Installation locale

1. Clonez le dépôt :
  
  git clone https://github.com/votre-utilisateur/votre-repo.git
  cd votre-repo
  Placez les fichiers nécessaires (pickle_surprise_model_KNNWithMeans.pkl et articles_metadata.csv) dans le répertoire.

2. Installez les dépendances :

  pip install -r requirements.txt
  
3. Testez localement avec Azure Functions Core Tools :

  func start
  
## Structure du Projet
.
├── articles_metadata.csv             # Métadonnées des articles

├── pickle_surprise_model_KNNWithMeans.pkl # Modèle de recommandation pré-entraîné

├── function_app/

│   ├── __init__.py                   # Code principal de l'API Azure

│   ├── function.json                 # Configuration de la fonction Azure

├── requirements.txt                  # Dépendances Python

├── README.md                         # Documentation

## Contributions
Les contributions sont les bienvenues ! 
Pour contribuer :

Forkez le dépôt.
Créez une branche spécifique pour vos modifications :

  git checkout -b feature/ajout-nouvelle-fonctionnalite
  Soumettez une pull request avec une description claire de vos changements.
  
## Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.


Ce fichier `README.md` contient toutes les informations nécessaires pour comprendre, installer, tester et utiliser votre projet.
