import os
import random
import string

ID_Length = 16
parent_path = "C:\\Users\\elizt\\PycharmProjects\\pythondb\\"


class HallBotDB(object):
    def __init__(self, name):
        self.database = []
        self.name = name
        self.path = os.path.join(parent_path, name)
        if os.path.isdir(self.path):
            self.loaddb()
        else:
            os.mkdir(self.path)
            self.ID = str(''.join(random.choices(string.ascii_letters + string.digits, k=ID_Length)))  # https://www.javatpoint.com/python-program-to-generate-a-random-string

    def create_table(self, name, headers):
        self.database.append(Table(name, headers))

    def delete_table(self, name):
        for each in self.database:
            if each.name == name:
                self.database.remove(each)

    def get_table(self, name):
        for each in self.database:
            if each.name == name:
                return each
        return False

    def loaddb(self):
        for file in os.listdir(self.path):
            table_name = file.split(".")[0]
            file_path = os.path.join(self.path, file)
            f = open(file_path, 'r')
            lines = f.readlines()
            self.create_table(table_name, lines.pop(1)[:-1].split(":"))
            self.get_table(table_name).ID = lines.pop(0)[:-1]
            for line in lines:
                print(line[:-1].split(":"))
                self.get_table(table_name).add_attribute(Attribute(line[:-1].split(":"), True))

    def dumpdb(self):
        for table in self.database:
            file_path = os.path.join(self.path, table.name + ".txt")
            output_str = ""
            with open(file_path, 'w') as file:
                output_str += table.ID + "\n"
                for attribute in table.attributes:
                    for value in attribute.values:
                        output_str += str(value) + ":"
                    output_str = output_str[:-1]
                    output_str += "\n"
                file.truncate(0)
                file.write(output_str)
                file.close()


class Table(object):
    def __init__(self, name, headers):
        self.name = name
        self.attributes = []
        header_attribute = Attribute(headers, True)
        self.attributes.append(header_attribute)
        self.ID = str(''.join(random.choices(string.ascii_letters + string.digits, k=ID_Length)))

    def add_attribute(self, attribute):
        if len(self.attributes[0].values) == len(attribute.values):
            self.attributes.append(attribute)
            return True
        else:
            return False

    def remove_attribute(self, ID):
        for each in self.attributes:
            if each.ID == ID:
                self.attributes.remove(each)


class Attribute(object):
    def __init__(self, values, header):
        self.values = values
        self.ID = str(''.join(random.choices(string.ascii_letters + string.digits, k=ID_Length)))
        if not header:
            self.values.insert(0, self.ID)


test_db = HallBotDB("Test")
test_db.create_table("Players", ["ID", "Name", "RPS Score"])
test_db.get_table("Players").add_attribute(Attribute(["test_name1", 2], False))
test_db.get_table("Players").add_attribute(Attribute(["test_name2", 5], False))
for table in test_db.database:
    print(table.name)
    for attribute in table.attributes:
        print(attribute.values)
test_db.dumpdb()
copy_test_db = HallBotDB("Test")
for table in copy_test_db.database:
    print(table.name)
    for attribute in table.attributes:
        print(attribute.values)
copy_test_db.get_table("Players").add_attribute(Attribute(["test_name3", 3], False))
copy_test_db.create_table("Servers", ["ID", "Server"])
copy_test_db.get_table("Servers").add_attribute(Attribute(["server_name"], False))
for table in copy_test_db.database:
    print(table.name)
    for attribute in table.attributes:
        print(attribute.values)
copy_test_db.dumpdb()
