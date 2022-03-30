import functions

class Student:
    def __init__(self,first_name,last_name,age,sex,major):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.sex = sex
        self.major = major
    

    def getAttb(self,attribute):
        options = {"first name" : self.fname,
                   "last name" : self.lname,
                   "age" : self.age,
                   "sex" : self.sex,
                   "major" : self.major,
                   }
        att = options[attribute]
        return att

    def setAttb(self,attribute,value):
        attribute = attribute.lower()
        if attribute == "first name":
            self.fname = value
            return self.fname
        elif attribute == "last name":
            self.lname = value
            return self.lname
        elif attribute == "age":
            self.age = value
            return self.age
        elif attribute == "sex":
            self.sex = value
            return self.sex
        elif attribute == "major":
            self.major = value
            return self.major
        else:
            print("wrong attribute entered")

    def write_data_to_file(self):
        try:
            with open('studentsList.txt', 'w') as f:
                for student in functions.students:
                    f.write("Name: " + student.fname +
                            " Surname: " + student.lname +
                            " Age: {0} ".format(student.age) +
                            " Sex: " + student.sex +
                            " Major: " + student.major +
                            "\n")
            f.close()
        except IOError:
            print("File not found or path is incorrect")

    def read_data_from_a_file(self):
        def string(s):
            return s
        try:
            my_file = open('studentsList.txt', 'r')
            for line in my_file:
                # if major is two words, line.split() will have 2 elements for the major
                # so we check whether that is the case or if the major is only 1 word
                # and accordingly we give enough variables to the map() funcion 
                if len(line.split()) > 10:
                    name, surname, age, sex, major, xtra = map(string, [x for x in line.split() if x.find(':') == -1])
                    functions.students.append(Student(name, surname, age, sex, major+" "+xtra))
                else:
                    name, surname, age, sex, major = map(string, [x for x in line.split() if x.find(':') == -1])
                    functions.students.append(Student(name, surname, age, sex, major))
            
            my_file.close()
            
        except IOError:
            print("File not found or path is incorrect")
