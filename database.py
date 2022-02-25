import os
import random
import string

ID_Length = 16
parent_path = "C:\\Users\\elizt\\PycharmProjects\\pythondb\\"


# Database Object
# Acts as a folder holding the tables within the database
class HallBotDB(object):
    # Initialize the database with just a name which will be the name of the folder.
    # Creates the list of tables, named database.
    # If the folder already exists it will load the database from memory.
    # @param string name: The name of your database. Acts as the name of the folder.
    def __init__(self, name):
        self.database = []
        self.name = name
        self.path = os.path.join(parent_path, name)
        if os.path.isdir(self.path):
            self.loaddb()
        else:
            os.mkdir(self.path)
            self.ID = str(''.join(random.choices(string.ascii_letters + string.digits, k=ID_Length)))  # https://www.javatpoint.com/python-program-to-generate-a-random-string
    
    # Adds a table to your database.
    # Your table will automatically have "ID" as the first header.
    # @param string name: The name of your table. Will act as the file name for your table.
    # @param list headers: A list of the headers for each column in your table.
    def create_table(self, name, headers):
        self.database.append(Table(name, headers))
    
    # Deletes the named table from your database.
    # @param string name: The name of the table you would like to delete from the database.
    def delete_table(self, name):
        for each in self.database:
            if each.name == name:
                self.database.remove(each)
    
    # Fetches a table object from your database.
    # @param string name: The name of the table you would like to fetch from the database.
    def get_table(self, name):
        for each in self.database:
            if each.name == name:
                return each
        return False
    
    # Loads the database from memory.
    def __loaddb(self):
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
    
    # Saves the database to memory.
    # Will overwrite any files or folders with the same names.
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


# Table Object
# Acts as a .txt file holding rows of attributes
class Table(object):
    # Initializes a table to put in the database.
    # Creates a list of attributes and adds the headers as the first attribute.
    # Your table will automatically have "ID" as the first header.
    # @param string name: The name of the table. Acts as the name of the .txt file when saved to memory.
    # @param list headers: A list of the headers for each column in your table.
    def __init__(self, name, headers):
        self.name = name
        self.attributes = []
        header_attribute = Attribute(headers, True)
        self.attributes.append(header_attribute)
        self.ID = str(''.join(random.choices(string.ascii_letters + string.digits, k=ID_Length)))
    
    # Adds an attribute to the attributes list.
    # Effectively adds a row to your table.
    # Attribute must have same number of values as the header for your table.
    # @param Attribute attribute: The attribute that you are adding to the table.
    def add_attribute(self, attribute):
        if len(self.attributes[0].values) == len(attribute.values):
            self.attributes.append(attribute)
            return True
        else:
            return False
    
    # Removes an attribute from the attributes list.
    # Effectively removes a row from your table.
    # @param string ID: The ID of the attribute you would like to remove.
    def remove_attribute(self, ID):
        for each in self.attributes:
            if each.ID == ID:
                self.attributes.remove(each)

# Attribute Object
# Acts as a row in your table .txt file.
class Attribute(object):
    # Initializes an attribute to put in your table.
    # Copies a list of values and stores that in the attribute.
    # Automatically adds a unique ID as the first value in attribute.
    # If this is the header attribute it will add "ID" as the first value.
    # @param list values: A list of values that is being added to the attribute
    # @param bool header: Tells the program whether it is a header or not.
    def __init__(self, values, header):
        self.values = values
        self.ID = str(''.join(random.choices(string.ascii_letters + string.digits, k=ID_Length)))
        if header:
            self.values.isert(0, "ID")
        else:
            self.values.insert(0, self.ID)
