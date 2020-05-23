import os
import stat
import sys
import getopt
from packages import cutie
import re
from datetime import datetime


class FILE:
    def __init__(self, fContent, fileName):
        searchObj = re.search(r'\"name\": \"(.+)\"$', fContent, re.M | re.I)
        self.name = searchObj.group(1)
        # self.extension = os.path.splitext(name)[1]
        searchObj = re.search(r'\"path\": \"(.+)\"$', fContent, re.M | re.I)
        self.path = searchObj.group(1)
        self.idPath = os.path.join(os.path.abspath('./fichiers'), fileName)
        st = os.stat(self.idPath)
        searchObj = re.search(r'\"type\": \"(.+)\"$', fContent, re.M | re.I)
        self.type = searchObj.group(1)
        self.creationDate = st[stat.ST_CTIME]
        self.modificationDate = st[stat.ST_MTIME]
        self.id = 0

    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "path":
            return self.path
        if key == "size":
            return self.size
        if key == "type":
            return self.type
        if key == "creationDate":
            return self.creationDate
        if key == "modificationDate":
            return self.modificationDate
        if key == "id":
            return self.id


class MEDIA:
    def __init__(self):
        self.items = []
        self.maxNameLen = 9
        self.maxTypeLen = 0
        self.maxCDLen = 0
        self.maxMDLen = 0
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
        print("| {0:^{lengthN}} | {1:^{lengthS}} | {2:^{lengthC}} | {3:^{lengthM}} |".format(
            "File Name", "Size", "Creation", "Modification", lengthN=mediatheque.maxNameLen, lengthS=mediatheque.maxSizeLen, lengthC=mediatheque.maxCDLen, lengthM=mediatheque.maxMDLen))

        print("|={0:=^{lengthN}}=|={0:=^{lengthS}}=|={0:=^{lengthC}}=|={0:=^{lengthM}}=|".format(
            "", lengthN=mediatheque.maxNameLen, lengthS=mediatheque.maxSizeLen, lengthC=mediatheque.maxCDLen, lengthM=mediatheque.maxMDLen))
        for item in mediatheque.items:
            name = item.name
            extension = item.extension
            type = item.type
            size = item.size
            creationDate = item.creationDate
            modificationDate = item.modificationDate
            if eval(arg):
                print("| {0:<{lengthN}} | {1:<{lengthS}} | {2:<{lengthC}} | {3:<{lengthM}} |".format(
                    item.name, item.size, datetime.fromtimestamp(
                        item.creationDate).strftime("%d/%m/%Y a %H:%M:%S"), datetime.fromtimestamp(
                        item.modificationDate).strftime("%d/%m/%Y a %H:%M:%S"), lengthN=mediatheque.maxNameLen, lengthS=mediatheque.maxSizeLen, lengthC=mediatheque.maxCDLen, lengthM=mediatheque.maxMDLen))
                pass
            pass
        pass

    def render(self):
        print("| {0:^{lengthN}} | {1:^{lengthT}} | {2:^{lengthC}} | {3:^{lengthM}} |".format(
            "File Name", "Type", "Creation", "Modification", lengthN=mediatheque.maxNameLen, lengthT=mediatheque.maxTypeLen, lengthC=mediatheque.maxCDLen, lengthM=mediatheque.maxMDLen))

        print("|={0:=^{lengthN}}=|={0:=^{lengthT}}=|={0:=^{lengthC}}=|={0:=^{lengthM}}=|".format(
            "", lengthN=mediatheque.maxNameLen, lengthT=mediatheque.maxTypeLen, lengthC=mediatheque.maxCDLen, lengthM=mediatheque.maxMDLen))

        for item in mediatheque.items:
            print("| {0:<{lengthN}} | {1:<{lengthT}} | {2:<{lengthC}} | {3:<{lengthM}} |".format(
                item.name, item.type, datetime.fromtimestamp(
                    item.creationDate).strftime("%d/%m/%Y a %H:%M:%S"), datetime.fromtimestamp(
                        item.modificationDate).strftime("%d/%m/%Y a %H:%M:%S"), lengthN=mediatheque.maxNameLen, lengthT=mediatheque.maxTypeLen, lengthC=mediatheque.maxCDLen, lengthM=mediatheque.maxMDLen))
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
        helpTxt = helpFile.read
        print(helpTxt)
        helpTxt.close()
        sys.exit()
        pass


def main(argv):

    element = None
    sortType = None
    try:
        opts, args = getopt.getopt(
            argv, "he:s:rfc", ["help", "element=", "sortType=", "remove", "find=", "create"])
        args = args
    except getopt.GetoptError:
        print('Invalid arguments please use main.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            mediatheque.helpCmd()
        elif opt in ("-e", "--element"):
            element = arg
        elif opt in ("-s", "--sType"):
            sortType = arg
        elif opt in ("-r", "--remove"):
            mediatheque.delete()
        elif opt in ("-f", "--find"):
            mediatheque.search(arg)
        elif opt in ("-c", "--create"):
            mediatheque.createItem()

    if element != None and sortType != None:
        mediatheque.sort(element, sortType)
        mediatheque.render()
        pass


listFileName = os.listdir(os.path.abspath('./fichiers'))
mediatheque = MEDIA()

for fileName in listFileName:
    f = open(os.path.join(os.path.abspath('./fichiers'), fileName), 'r')
    # print(f.read())
    item = FILE(f.read(), fileName)
    mediatheque.addItem(item)
    f.close()
    # print(item.name)
    pass


if __name__ == "__main__":
    main(sys.argv[1:])
