﻿try:
    from datetime import datetime
    import os
    import sys
    import cutie
    import re
    pass
except:
    print("[!] Il semble qu'un des modules ne soit pas disponible")
    print("    Essayez cette commande afin de les installer :")
    print("    > pip install -r requirements.txt -t <Current directory>")
    sys.exit(2)
    pass


class MEDIA:
    def __init__(self):
        self.items = []
        self.maxNameLen = 11
        self.maxTypeLen = 6
        self.maxCDLen = 10
        self.maxMDLen = 14
        self.idCount = 0

    def addItem(self, item):
        item.id = self.idCount
        self.items.append(item)
        if self.maxNameLen < len(item.name):
            self.maxNameLen = len(item.name)
            pass
        if self.maxTypeLen < len(str(item.type)):
            self.maxTypeLen = len(str(item.type))
            pass
        if self.maxCDLen < len(datetime.fromtimestamp(item.creationDate).strftime("%d/%m/%Y à %H:%M:%S")):
            self.maxCDLen = len(datetime.fromtimestamp(
                item.creationDate).strftime("%d/%m/%Y à %H:%M:%S"))
            pass
        if self.maxMDLen < len(datetime.fromtimestamp(item.modificationDate).strftime("%d/%m/%Y à %H:%M:%S")):
            self.maxMDLen = len(datetime.fromtimestamp(
                item.modificationDate).strftime("%d/%m/%Y à %H:%M:%S"))
            pass
        self.idCount = self.idCount + 1

    def createItem(self):
        name = input("Nom : ")

        path = input("Chemin : ")
        type = input("type : ")

        now = datetime.now()
        timestamp = int(datetime.timestamp(now))

        fileName = name.replace(" ", "_")
        fileName = re.sub(r"<|>|:|\"|/|\\|\||\?|\*", "", fileName)
        fileName = f'{fileName}__{timestamp}.txt'

        f = open(os.path.join(os.path.abspath('./fichiers'), fileName), "w+")
        f.write(f'"name": "{name}"\n"path": "{path}"\n"type": "{type}"')
        f.close()

    def modifyItem(self):
        choiceList = []
        itemList = []
        for item in self.items:
            choiceList.append(item.name)
            itemList.append(item)
        itemIndex = cutie.select(choiceList)
        item = itemList[itemIndex]

        print(f"\n# Element choisis {item.name}\n")

        f = open(item.idPath, "w")

        newName = input(
            f"Nouveau nom pour l'element [{item.name}] : ") or item.name
        newPath = input(
            f"Nouveau chemin pour l'element [{item.path}] : ") or item.path
        newType = input(
            f"Nouveau type pour l'element [{item.type}] : ") or item.type
        f.write(
            f'"name": "{newName}"\n"path": "{newPath}"\n"type": "{newType}"')
        f.close()

    def sort(self, element, sortType):
        lenght = len(self.items)
        for i in range(lenght-1):
            for j in range(0, lenght-i-1):
                if sortType == "croissant":
                    if self.items[j][element] > self.items[j+1][element]:
                        self.items[j], self.items[j +
                                                  1] = self.items[j+1], self.items[j]
                    pass
                elif sortType == "decroissant":
                    if self.items[j][element] < self.items[j+1][element]:
                        self.items[j], self.items[j +
                                                  1] = self.items[j+1], self.items[j]
                    pass
                else:
                    print(
                        f"'{sortType}' is invalid please use main.py -h for help")
                    sys.exit(2)
                    pass

    def delete(self):
        choiceList = []
        idPathList = []
        for item in self.items:
            choiceList.append(item.name)
            idPathList.append(item.idPath)
        selected = cutie.select_multiple(
            choiceList,
            deselected_unticked_prefix="[ ] ",
            selected_unticked_prefix='[\033[32;1m‣\033[0m] ',
            selected_ticked_prefix='\033[32;1m[‣]\033[0m ',
            deselected_ticked_prefix='\033[32;1m[\033[0m‣\033[32;1m]\033[0m ')

        for i in range(len(selected)):
            print("removed : ", choiceList[selected[i]])
            os.remove(os.path.join(os. path.abspath(
                './fichiers'), idPathList[selected[i]]))
            pass

    def search(self, arg):
        print("| {0:^{lengthN}} | {1:^{lengthT}} | {2:^{lengthC}} | {3:^{lengthM}} |".format(
            "File Name", "Type", "Creation", "Modification", lengthN=self.maxNameLen, lengthT=self.maxTypeLen, lengthC=self.maxCDLen, lengthM=self.maxMDLen))

        print("|={0:=^{lengthN}}=|={0:=^{lengthT}}=|={0:=^{lengthC}}=|={0:=^{lengthM}}=|".format(
            "", lengthN=self.maxNameLen, lengthT=self.maxTypeLen, lengthC=self.maxCDLen, lengthM=self.maxMDLen))
        for item in self.items:
            name = item.name
            type = item.type
            creationDate = item.creationDate
            modificationDate = item.modificationDate
            if eval(arg):
                print("| {0:<{lengthN}} | {1:<{lengthT}} | {2:<{lengthC}} | {3:<{lengthM}} |".format(
                    item.name, item.type, datetime.fromtimestamp(
                        item.creationDate).strftime("%d/%m/%Y a %H:%M:%S"), datetime.fromtimestamp(
                        item.modificationDate).strftime("%d/%m/%Y a %H:%M:%S"), lengthN=self.maxNameLen, lengthT=self.maxTypeLen, lengthC=self.maxCDLen, lengthM=self.maxMDLen))
                pass
            pass
        pass

    def render(self):
        print("| {0:^{lengthN}} | {1:^{lengthT}} | {2:^{lengthC}} | {3:^{lengthM}} |".format(
            "File Name", "Type", "Creation", "Modification", lengthN=self.maxNameLen, lengthT=self.maxTypeLen, lengthC=self.maxCDLen, lengthM=self.maxMDLen))

        print("|={0:=^{lengthN}}=|={0:=^{lengthT}}=|={0:=^{lengthC}}=|={0:=^{lengthM}}=|".format(
            "", lengthN=self.maxNameLen, lengthT=self.maxTypeLen, lengthC=self.maxCDLen, lengthM=self.maxMDLen))

        for item in self.items:
            print("| {0:<{lengthN}} | {1:<{lengthT}} | {2:<{lengthC}} | {3:<{lengthM}} |".format(
                item.name, item.type, datetime.fromtimestamp(
                    item.creationDate).strftime("%d/%m/%Y a %H:%M:%S"), datetime.fromtimestamp(
                        item.modificationDate).strftime("%d/%m/%Y a %H:%M:%S"), lengthN=self.maxNameLen, lengthT=self.maxTypeLen, lengthC=self.maxCDLen, lengthM=self.maxMDLen))
            pass
        pass

    def helpCmd(self):
        try:
            helpFile = open(os.path.join(os.path.abspath('./'),
                                         "help_.txt"), "r", encoding="utf-8")
            pass
        except:
            print("Il semble que le fichier help_.txt n'existe pas 🤔")
            sys.exit(2)
            pass
        helpTxt = helpFile.read()
        print(helpTxt)
        helpFile.close()
        sys.exit()
        pass
