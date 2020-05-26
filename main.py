try:
    import os
    import sys
    import getopt
    from FILE import FILE
    from MEDIA import MEDIA
    pass
except:
    print("[!] Il semble qu'un des modules ne soit pas disponible")
    print("    Essayez cette commande afin de les installer :")
    print("    > pip install -r requirements.txt -t <Current directory>")
    sys.exit(2)
    pass


# Fonction main
def main(argv):
    element = None
    sortType = None
    # On essaye :
    try:
        # Recuperer les arguments et options
        opts, args = getopt.getopt(
            argv, "he:s:rfcm", ["help", "element=", "sortType=", "remove", "find=", "create", "modify"])
    # Si il y a une erreur :
    except getopt.GetoptError:
        print('Invalid arguments please use main.py -h for help')
        # Arreter le programme
        sys.exit(2)
    # Pour chaque options :
    for opt, arg in opts:
        # Si l'option est -h ou --help
        if opt == '-h' or opt == '--help':
            # Afficher l'aide
            mediatheque.helpCmd()
        # Sinon si l'option est -e ou --element
        elif opt in ("-e", "--element"):
            element = arg
        # Sinon si l'option est -s ou --sType
        elif opt in ("-s", "--sType"):
            sortType = arg
        # Sinon si l'option est -r ou --remove
        elif opt in ("-r", "--remove"):
            # Lancer la fonction de supression
            mediatheque.delete()
        # Sinon si l'option est -f ou --find
        elif opt in ("-f", "--find"):
            # Lancer la fonction de recherche
            mediatheque.search(arg)
        # Sinon si l'option est -c ou --create
        elif opt in ("-c", "--create"):
            # Lancer la fonction de creation d'un element
            mediatheque.createItem()
        # Sinon si l'option est -m ou --modify
        elif opt in ("-m", "--modify"):
            # Lancer la fonction de creation d'un element
            mediatheque.modifyItem()

    # Si il y a un element et un type de tri
    if element != None and sortType != None:
        # Lancer la fonction de tri des elements
        mediatheque.sort(element, sortType)
        # Lancer la fonction de rendu des elements
        mediatheque.render()
        pass


# Chercher le nom de tout les fichiers dans le dossier 'fichiers'
listFileName = os.listdir(os.path.abspath('./fichiers'))
# Creer une nouvelle instance de la class 'MEDIA'
mediatheque = MEDIA()

# Pour chaque nom de fichier dans la liste :
for fileName in listFileName:
    # Ouvrir le fichier
    f = open(os.path.join(os.path.abspath('./fichiers'), fileName), 'r')
    # Creer une nouvelle instace de la class 'FILE' (cf : XXX)
    item = FILE(f.read(), fileName)
    # On ajoute cette instance à la mediatheque (cf : XXX)
    mediatheque.addItem(item)
    # On ferme le fichier
    f.close()
    pass

# Si on lance directement main.py et qu'il y a des arguments :
if __name__ == "__main__" and len(sys.argv[1:]) != 0:
    # On lance la fonction main
    main(sys.argv[1:])
# Sinon :
else:
    # On affiche l'aide
    mediatheque.helpCmd()
    pass
