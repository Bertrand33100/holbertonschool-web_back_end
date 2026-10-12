# Python - Async

## Description

Ce projet a pour objectif de découvrir la programmation asynchrone en Python à l'aide du module `asyncio`. Il permet de comprendre comment exécuter des coroutines, gérer des tâches asynchrones et effectuer plusieurs opérations concurrentes sans bloquer inutilement l'exécution du programme.

Le projet utilise également le module `random` pour générer des délais aléatoires.

## Objectifs d'apprentissage

À la fin de ce projet, je dois être capable de :

- Comprendre la syntaxe `async` et `await`.
- Créer et exécuter des coroutines asynchrones.
- Utiliser le module `asyncio` pour exécuter un programme asynchrone.
- Exécuter plusieurs coroutines de manière concurrente.
- Créer et gérer des tâches avec `asyncio.Task`.
- Utiliser le module `random`, notamment `random.uniform()`.
- Ajouter des annotations de types aux fonctions et aux coroutines.
- Documenter correctement les modules et les fonctions en Python.

## Concepts étudiés

### 1. La programmation asynchrone

La programmation asynchrone permet de suspendre temporairement une opération en attente, par exemple une temporisation ou une réponse réseau, afin de laisser d'autres tâches avancer.

### 2. `async` et `await`

- `async` permet de déclarer une fonction asynchrone, appelée coroutine.
- `await` permet de suspendre l'exécution d'une coroutine jusqu'à ce que l'opération attendue fournisse son résultat.

### 3. Le module `asyncio`

Le module `asyncio` fournit les outils nécessaires pour exécuter des coroutines et organiser des opérations asynchrones.

### 4. Le module `random`

La fonction `random.uniform(a, b)` génère un nombre flottant aléatoire entre deux bornes.

Dans ce projet, elle permet de choisir un délai aléatoire compris entre `0` et `max_delay`.

## Tâches du projet

### 0. The basics of async

**Fichier :** `0-basic_async_syntax.py`

Créer une coroutine appelée `wait_random` qui :

- Accepte un paramètre entier `max_delay`, avec une valeur par défaut de `10`.
- Génère un délai aléatoire compris entre `0` et `max_delay`.
- Attend ce délai de manière asynchrone.
- Retourne le délai utilisé sous forme de nombre flottant.

Cette première tâche permet de comprendre le fonctionnement d'une coroutine et l'utilisation de `asyncio.sleep()`.

## Structure du projet

```text
python_async_function/
└── 0-basic_async_syntax.py
```

## Environnement technique

- **Langage :** Python 3
- **Version :** Python 3.8
- **Système :** Ubuntu 20.04 LTS
- **Module asynchrone :** `asyncio`
- **Module aléatoire :** `random`
- **Style de code :** PEP 8 avec `pycodestyle` 2.5.x

## Exigences

- Chaque fichier Python doit commencer par `#!/usr/bin/env python3`.
- Les fichiers doivent se terminer par une nouvelle ligne.
- Les fichiers doivent être exécutables.
- Les fonctions et les coroutines doivent posséder des annotations de types.
- Les modules et les fonctions doivent comporter une documentation explicite.
- Le code doit respecter les règles de style imposées par le projet.

## Ressources

- [Python - Asynchronous execution](https://intranet.hbtn.io/concepts/1173)
- [Python - Asynchronous Programming](https://intranet.hbtn.io/concepts/1174)
- [Async IO in Python: A Complete Walkthrough](https://intranet.hbtn.io/rltoken/IDv2YZ5p7QHF5SxYZBMGdQ)
- [Documentation officielle de asyncio](https://docs.python.org/3.8/library/asyncio.html)
- [Documentation officielle de random.uniform()](https://docs.python.org/3.8/library/random.html#random.uniform)

## Compétences développées

Ce projet contribue au développement de compétences en programmation asynchrone, gestion des coroutines, annotations de types et structuration de code Python.

Ces notions sont utiles pour développer des applications capables de gérer efficacement des opérations d'attente, des appels réseau et plusieurs tâches concurrentes.
