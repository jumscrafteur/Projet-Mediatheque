# Mediatheque Project

#### Mini project for the end of the year 2019-2020 of sti2d terminal

## Subject

Management of a media library.
Use an object-oriented language (C++, java, python, appInventor, ...) to sort one or more types of elements.

## Installation

```cmd
git clone https://github.com/jumscrafteur/Projet-Mediatheque.git

pip install -r requirements.txt -t <Current directory>
```

## Help
###### Also available via `> main.py --help`
### USE

Run :

```cmd
main.py <options>
```
| Argument  | Utilité                       | Valeurs                                                                                          | Alisas |
| --------- | ----------------------------- | ------------------------------------------------------------------------------------------------ | ------ | 
| --element | select sorting element        | name - path -creationDate - modificationDate                                                     | -e     |
| --sort    | select the type of sorting    | croissant - decroissant                                                                          | -s     |
| --create  | objectify                     | ❌                                                                                               | -c     |
| --remove  | delete items                  | ❌                                                                                               | -r     |
| --modify  | make a change                 | ❌                                                                                               | -m     |
| --find    | search for objects            | expression boolean <br/>(variables utilisables:  name  ; type ; creationDate ; modificationDate) | ❌     |

### EXEMPLES

* Display all elements in alphabetical order 
  ```
  main.py -e name -s croissant
  ```
  ![search help](https://i.imgur.com/P3RoVQS.gif)

- Create an element
  ```
  main.py -c
  ```
  ![create help](https://i.imgur.com/2kLlOgc.gif)

* Delete items
  ```
  main.py -r
  ```
  ![delete help](https://i.imgur.com/Bdg1W3r.gif)

- Modify an item
  ```
  main.py -m
  ```
  ![modify help](https://i.imgur.com/IATcFbR.gif)

* Search for all elements whose name is 'zoo' and whose type is 'Livre' (Livre = Book).
  ```
  main.py --find="name == 'zoo' and type == 'Livre'"
  ```
  ![find help](https://i.imgur.com/5BBfiH3.gif)

## Fonctionnalités 

* [x] create an item
* [x] destroy an item
* [x] move an item
* [x] sort a item
* [x] item search
* [x] search for a group of items
* [x] display a group of items
* [x] display an item
