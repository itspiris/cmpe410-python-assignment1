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


