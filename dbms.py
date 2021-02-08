import csv

class DataBaseManager:

    def __init__(self, database='classDB.csv'):
        self.database = database

    def update(self, class_list):
        with open(self.getDataBaseName, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in class_list:
                writer.writerow(line)
        csv_file.close()

    def read(self):
        class_list = []
        try:
            with open(self.getDataBaseName, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                for line in reader:
                    if line:
                        class_list.append(line)
                csv_file.close()
            return class_list
        except FileNotFoundError:
            print('Fail Connection')
            return class_list

    @property
    def getDataBaseName(self):
        return self.database

    def __str__(self):
        return f'filename: {self.getDataBaseName}\nAmount of data: {len(self.read())}'



