# Projet-Mediatheque

#### Mini projet de fin d'année 2019-2020 de terminal sti2d

## Sujet

Gestion d'une médiathèque.
Utiliser un langage orienté objet (C++, java, python, appInventor, ...) pour réaliser le tri d'un ou plusieurs types d'éléments.

## Instalation

```cmd
git clone https://github.com/jumscrafteur/Projet-Mediatheque.git

pip install -r requirements.txt -t <Current directory>
```

## Aide
###### Egalement disponile via `> main.py --help`
### USAGE

Lancer :

```cmd
main.py <options>
```
| Argument  | Utilité                       | Valeurs                                                                                     | Alisas |
| --------- | ----------------------------- | ------------------------------------------------------------------------------------------- | ------ | 
| --element | selectionner l'element de tri | name - path -creationDate - modificationDate                                                | -e     |
| --sort    | selectionner le type de tri   | croissant - decroissant                                                                     | -s     |
| --create  | creer un objet                | ❌                                                                                          | -c     |
| --remove  | suprimer des objets           | ❌                                                                                          | -r     |
| --modify  | modifier un objet             | ❌                                                                                          | -m     |
| --find    | rechercher des objets         | expression boolean <br/>(variables utilisables:  name  ; type ; creationDate ; modificationDate) | ❌     |

### EXEMPLES

* Afficher tout les elements dans l'ordre alphabetique 
  ```
  main.py -e name -s croissant
  ```
  ![search help](https://i.imgur.com/P3RoVQS.gif)

- Creer un element
  ```
  main.py -c
  ```
  ![create help](https://i.imgur.com/2kLlOgc.gif)

* Supprimer des elements
  ```
  main.py -r
  ```
  ![delete help](https://i.imgur.com/Bdg1W3r.gif)

- Modifier un element
  ```
  main.py -m
  ```
  ![modify help](https://i.imgur.com/IATcFbR.gif)

* Chercher tout les elements dont le nom est 'zoo.txt' et dont le type est 'Livre'
  ```
  main.py --find="name == 'zoo' and type == 'Livre'"
  ```
  ![find help](https://i.imgur.com/5BBfiH3.gif)

## Fonctionnalités 

* [x] créer un élément
* [x] détruire un élément
* [x] déplacer un élément
* [x] trier un élément
* [x] rechercher un élément
* [x] rechercher un groupe d'élément
* [x] afficher un groupe d'élément
* [x] afficher un élément
