import re
from dbms import DataBaseManager


class Class(DataBaseManager):

    def __init__(self):
        super().__init__()
        self.class_name = None
        self.professor = None
        self.day = None
        self.hour = None
        self.semester_year = None
        self.semester = None
        self.class_line =[]
        self.class_list = []

    def __str__(self):
        return f'{self.getClassName},{self.getProfessor},{self.getDay},{self.getHour},{self.getSemesterYear},{self.getSemester}'

    def showData(self):
        # load data to a list
        self.class_list = self.read()

        # Show Data
        print('')
        for line in self.class_list:
            print(f'{self.class_list.index(line)}. {line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}')

        # clear list
        self.reset()

    def modify(self, column, new_data, data):
        # local variables
        counter = 0
        match_list = []

        self.class_list = self.read()

        # Verify if data exist in the DATABASE show the position in it
        for line in self.class_list:
            if line[column] == data:
                match_list.append(self.class_list.index(line))
                print(f'{self.class_list.index(line)}. {line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}')
                counter = counter + 1

        if counter == 0:
            return 0

        # Select which row you want to modify
        row = input('Choose between the postion: ')

        # Modify specify row, column
        if re.search('[0-9]+', row):
            row = int(row)
            self.class_list[row][column] = new_data

        # load data into database and reset all variables used
        self.reset()

        # return status of operation
        return 1

    def insert(self):
        # load data to a list
        self.class_list = self.read()
        self.to_list()

        # Verifying if data exists in the list
        countEquals: int = 0
        if self.class_list:
            for line in self.class_list:
                copy_line = line.copy()
                copy = self.class_line.copy()
                copy_line = set(copy_line)
                copy = set(copy)
                equal = copy_line.difference(copy)
                if not equal:
                    countEquals = countEquals + 1

            if countEquals >= 1:
                output = 0
            else:
                self.class_line = list(self.class_line)
                self.class_list.append(self.class_line)
                output = 1
        else:
            self.class_list.append(self.class_line)
            output = 1

        # load new process Data to the DATABASE
        self.reset()
        return output

    def delete(self):
        # Load data
        self.class_list = self.read()

        # Process Data check if data exist to delete it
        acum, count, countDelete = 0, 0, 0
        while count != len(self.class_list):
            if acum == 0:
                acum = countDelete

            countDelete, count = 0, 0
            for line in self.class_list:
                if line[0] == self.getClassName:
                    countDelete = countDelete + 1
                    self.class_list.remove(line)
                else:
                    count = count + 1
        # load data to the DATABASE
        self.reset()
        return acum

    def reset(self):
        self.update(self.class_list)
        self.class_list.clear()
        self.class_line.clear()

    def to_list(self):
        self.class_line.append(self.getClassName)
        self.class_line.append(self.getProfessor)
        self.class_line.append(self.getDay)
        self.class_line.append(self.getHour)
        self.class_line.append(self.getSemesterYear)
        self.class_line.append(self.getSemester)

    @property
    def getClassName(self):
        return self.class_name

    @property
    def getProfessor(self):
        return self.professor

    @property
    def getDay(self):
        return self.day

    @property
    def getHour(self):
        return self.hour

    @property
    def getSemesterYear(self):
        return self.semester_year

    @property
    def getSemester(self):
        return self.semester

    def setClassName(self, class_name: str):
        self.class_name = class_name

    def setProfessor(self, professor: str):
        self.professor = professor

    def setDay(self, day: str):
        self.day = day

    def setHour(self, hour: str):
        self.hour = hour

    def setSemesterYear(self, semester_year: str):
        self.semester_year = semester_year

    def setSemester(self, semester: str):
        self.semester = semester

