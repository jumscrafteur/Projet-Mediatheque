try:
    import re
    import os
    import stat
    pass
except:
    print("[!] Il semble qu'un des modules ne soit pas disponible")
    print("    Essayez cette commande afin de les installer :")
    print("    > pip install -r requirements.txt -t <Current directory>")
    sys.exit(2)
    pass


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
