import json
import os
import random
import string

ID_Length = 16


class HallBotDB(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.ID = str(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=ID_Length)))  # https://www.javatpoint.com/python-program-to-generate-a-random-string
        self.database = []

    def create_table(self, name):
        self.database.append(Table(name))

    def delete_table(self, ID):
        for each in self.database:
            if each.ID == ID:
                self.database.remove(each)
                
    def get_table(self, ID):
        for each in self.database:
            if each.ID == ID:
                return each
        return False

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dumpdb(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False


class Table(object):
    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.ID = str(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=ID_Length)))


class Attribute(object):
    def __init__(self, value):
        self.value = value
        self.ID = str(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=ID_Length)))


print(str(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=ID_Length))))
