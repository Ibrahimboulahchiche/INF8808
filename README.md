# README — TP1 et TP2
## INF8808 — Visualisation de données

Ce dépôt regroupe deux travaux pratiques du cours **INF8808 – Visualisation de données** réalisés en **Python** avec **Dash**, **Plotly** et **Pandas**.

Les deux projets reposent sur la création de visualisations interactives, le prétraitement de données et l’utilisation d’un thème graphique personnalisé.

## Contenu du dépôt
- **TP2** : visualisation du nombre de lignes prononcées par les personnages de *Roméo et Juliette*
- **TP3** : visualisation des plantations d’arbres à Montréal entre **2010 et 2020**

## Technologies utilisées
- Python
- Dash
- Plotly
- Pandas

## Installation
Créer un environnement virtuel puis installer les dépendances nécessaires.

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
pip install dash plotly pandas
```

## Lancement des projets
Selon l’organisation de vos dossiers, exécuter le fichier `server.py` du TP correspondant.

```bash
python server.py
```

Ensuite, ouvrir l’adresse locale indiquée dans le terminal, généralement :

```text
http://127.0.0.1:8050/
```

---

# TP1 — Diagramme à bandes empilées interactif

## Description
Le **TP1** consiste à développer une **visualisation interactive** permettant d’explorer le nombre de lignes prononcées par les personnages de *Roméo et Juliette*.

L’application affiche un **diagramme à bandes empilées** par acte et permet de basculer entre deux modes d’affichage :
- **Count** : nombre brut de lignes prononcées
- **Percent** : proportion de lignes prononcées dans chaque acte

## Objectifs
- Prétraiter un fichier CSV contenant les répliques de *Roméo et Juliette*
- Résumer les lignes prononcées par personnage et par acte
- Regrouper les personnages secondaires dans une catégorie **Other**
- Générer un diagramme à bandes empilées interactif avec Plotly
- Créer un thème visuel personnalisé
- Définir une info-bulle cohérente selon le mode d’affichage
- Mettre à jour le graphique dynamiquement via un bouton radio

## Fonctionnalités
- Affichage des données par **acte**
- Affichage des **5 personnages principaux** et de la catégorie **Other**
- Changement dynamique entre les modes **Count** et **Percent**
- Mise à jour automatique :
  - des valeurs affichées
  - de l’axe des y
  - de l’info-bulle
  - du texte descriptif

## Rôle des fichiers
- `app.py` : construit l’interface Dash et gère les interactions
- `bar_chart.py` : initialise et dessine le diagramme à bandes empilées
- `hover_template.py` : définit le contenu de l’info-bulle
- `modes.py` : contient les constantes liées aux modes d’affichage
- `preprocess.py` : effectue le nettoyage et la transformation des données
- `server.py` : lance l’application
- `template.py` : crée le thème Plotly personnalisé

## Prétraitement des données
Le prétraitement comprend principalement :
1. le résumé des lignes par acte et par personnage
2. le calcul du pourcentage représenté dans chaque acte
3. le regroupement des personnages secondaires dans la catégorie `Other`
4. le nettoyage des noms pour obtenir un format uniforme

## Utilisation
1. Lancer l’application
2. Observer le diagramme à bandes empilées
3. Utiliser le bouton radio pour passer de **Count** à **Percent**
4. Survoler les barres pour afficher les détails dans l’info-bulle

---

# TP2 — Carte de chaleur et graphique linéaire

## Description
Le **TP2** consiste à développer une **application interactive** permettant d’explorer les **plantations d’arbres à Montréal** entre **2010 et 2020**.

L’application combine deux visualisations :
- une **carte de chaleur** montrant le nombre d’arbres plantés par **quartier** et par **année**
- un **graphique linéaire** qui s’adapte à la cellule sélectionnée dans la carte de chaleur pour afficher l’évolution quotidienne des plantations pour le quartier et l’année choisis

## Objectifs
- Prétraiter des données ouvertes sur les plantations d’arbres à Montréal
- Convertir les dates dans un format exploitable
- Filtrer les données entre **2010 et 2020**
- Résumer les plantations par **année** et par **quartier**
- Restructurer les données pour une carte de chaleur Plotly
- Générer un graphique linéaire lié à la sélection de la carte
- Afficher une figure vide informative lorsqu’aucune donnée n’est disponible
- Personnaliser l’apparence avec un thème Plotly
- Définir une info-bulle adaptée à chaque type de graphique

## Fonctionnalités
- Carte de chaleur des plantations par quartier et par année
- Sélection interactive d’une cellule de la heatmap
- Affichage d’un graphique linéaire quotidien selon la sélection
- Affichage d’un message lorsqu’aucune cellule n’est sélectionnée
- Affichage d’un message lorsqu’aucune donnée n’est disponible
- Gestion du cas où une seule date est disponible dans le graphique linéaire

## Rôle des fichiers
- `app.py` : construit la page et coordonne les composants interactifs
- `heatmap.py` : génère la carte de chaleur principale
- `hover_template.py` : définit les info-bulles
- `line_chart.py` : construit la figure vide et le graphique linéaire détaillé
- `preprocess.py` : convertit, filtre, résume et restructure les données
- `server.py` : lance l’application
- `template.py` : crée et applique le thème par défaut

## Données utilisées
Le jeu de données contient notamment les colonnes suivantes :
- `Arrond`
- `Arrond_Nom`
- `Date_Plantation`
- `Longitude`
- `Latitude`

## Prétraitement des données
Le prétraitement comprend notamment :
1. la conversion des dates
2. le filtrage de la période 2010–2020
3. le résumé annuel du nombre d’arbres plantés par quartier
4. la restructuration des données pour la heatmap
5. l’extraction des données quotidiennes pour le graphique linéaire

## Utilisation
1. Lancer l’application
2. Observer la carte de chaleur
3. Cliquer sur une cellule correspondant à un quartier et une année
4. Consulter le graphique linéaire mis à jour automatiquement
5. Survoler les éléments pour afficher les détails via l’info-bulle

---

## Résumé
Ces deux travaux pratiques mettent en œuvre des techniques de **prétraitement**, de **visualisation interactive** et de **mise à jour dynamique** avec Dash et Plotly.  
Le **TP1** met l’accent sur la comparaison par catégories avec un diagramme à bandes empilées, tandis que le **TP2** met l’accent sur l’exploration spatio-temporelle à l’aide d’une heatmap couplée à un graphique linéaire.


