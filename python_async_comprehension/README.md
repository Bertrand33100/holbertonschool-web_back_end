# Python - Async Comprehension

## Description

Ce projet fait partie du cursus **Holberton School – Web Back-End**. Il permet d'approfondir la programmation asynchrone en Python, notamment à travers les générateurs asynchrones, les compréhensions asynchrones et les annotations de types.

L'objectif est d'apprendre à produire des valeurs progressivement sans bloquer l'exécution du programme, tout en utilisant les fonctionnalités introduites dans Python 3.6 et les versions suivantes.

## Objectifs d'apprentissage

À la fin de ce projet, je dois être capable d'expliquer, sans utiliser Google :

- Comment écrire un générateur asynchrone (*asynchronous generator*).
- Comment utiliser les compréhensions asynchrones (*async comprehensions*).
- Comment annoter les types des générateurs.

## Environnement et exigences

- **Langage :** Python 3
- **Version :** Python 3.8
- **Système :** Ubuntu 20.04 LTS
- **Style de code :** pycodestyle 2.5.x
- **Éditeurs autorisés :** `vi`, `vim`, `emacs`

### Règles à respecter

- Tous les fichiers Python doivent commencer par `#!/usr/bin/env python3`.
- Tous les fichiers doivent se terminer par une nouvelle ligne.
- Le fichier `README.md` doit se trouver à la racine du dossier du projet.
- Tous les modules et toutes les fonctions doivent posséder une documentation (*docstring*) rédigée sous forme de phrase complète.
- Toutes les fonctions et coroutines doivent comporter des annotations de types.
- La longueur des fichiers peut être vérifiée avec la commande `wc`.

## Notions essentielles

### 1. Programmation asynchrone

La programmation asynchrone permet de suspendre temporairement une opération en attente, par exemple une temporisation, afin de laisser la boucle d'événements gérer d'autres tâches.

En Python, on utilise notamment :

- `async` : déclare une fonction asynchrone.
- `await` : attend le résultat d'une opération asynchrone.
- `asyncio.sleep()` : suspend une coroutine pendant une durée donnée sans bloquer la boucle d'événements.

### 2. Générateur asynchrone

Un générateur asynchrone produit des valeurs progressivement. Il utilise `yield` pour fournir une valeur et peut suspendre son exécution entre deux valeurs.

Il est notamment parcouru avec `async for`.

### 3. Compréhension asynchrone

Une compréhension asynchrone permet de construire une collection à partir des valeurs produites par un itérable asynchrone, avec une syntaxe concise utilisant `async for`.

### 4. Annotations de types

Les annotations de types indiquent les types attendus ou produits par une fonction. Elles permettent de mieux comprendre le rôle d'une fonction et de documenter son comportement.

Pour les générateurs asynchrones, il faut notamment savoir identifier le type des valeurs produites.

## Tâches du projet

### 0. Async Generator

**Fichier :** `0-async_generator.py`

Créer une coroutine nommée `async_generator` qui ne prend aucun argument.

La fonction doit :

1. Répéter une opération 10 fois.
2. Attendre une seconde de manière asynchrone à chaque itération.
3. Générer un nombre aléatoire compris entre 0 et 10 à l'aide du module `random`.
4. Produire ce nombre avec `yield`.

Le générateur doit pouvoir être parcouru à l'aide de `async for`.

**Résultat attendu :** une liste contenant 10 nombres générés progressivement, avec une attente asynchrone entre chaque valeur.

Les nombres obtenus peuvent être différents à chaque exécution.

## Commandes utiles

Exécuter le programme de test :

```bash
./0-main.py
```

Vérifier le style du code :

```bash
pycodestyle 0-async_generator.py
```

Afficher la documentation du module :

```bash
python3 -c 'print(__import__("0-async_generator").__doc__)'
```

Afficher la documentation de la fonction :

```bash
python3 -c 'print(__import__("0-async_generator").async_generator.__doc__)'
```

Vérifier la longueur du fichier :

```bash
wc -l 0-async_generator.py
```

## Structure du projet

```text
python_async_comprehension/
├── README.md
└── 0-async_generator.py
```

## Conclusion

Ce chapitre permet de comprendre comment produire des données de manière asynchrone, parcourir des générateurs asynchrones et exploiter les compréhensions asynchrones.

Ces compétences sont utiles pour développer des applications capables de gérer efficacement des opérations d'attente, des entrées-sorties et plusieurs tâches asynchrones.
