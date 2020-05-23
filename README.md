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
| Argument  | Utilité                       | Valeurs                                      | Alisas |
| --------- | ----------------------------- | -------------------------------------------- | ------ | 
| --element | selectionner l'element de tri | name - path -creationDate - modificationDate | -e     |
| --sort    | selectionner le type de tri   | croissant - decroissant                      | -s     |
| --remove  | suprimer des objets           | ❌                                           | -r     |
| --find    | rechercher des objets         | expression boolean                           | ❌     |

### EXEMPLES

* Afficher tout les elements dans l'ordre alphabetique 
  ```
  main.py -e name -s croissant
  ```

- Supprimer des elements
  ```
  main.py -r
  ```


* Chercher tout les elements dont le nom est 'zoo.txt' et dont le type est 'Livre'
  ```
  main.py --find="name == 'zoo' and type == 'Livre'"
  ```

## Fonctionnalités 

* [x] créer un élément
* [x] détruire un élément
* [ ] déplacer un élément
* [x] trier un élément
* [x] rechercher un élément
* [x] rechercher un groupe d'élément
* [x] afficher un groupe d'élément
* [x] afficher un élément
