import student_class
students = []

def ToDo(*args):
    print("args[0]: ",args[0])
    if args[0] == 1:
        AddStd(args[1],args[2],args[3],args[4],args[5])
    elif args[0] == 2:
        FindStd(args[1],args[2])
    elif args[0] == 3:
        DispStd()
    elif args[0] == 4:
        DispFewStd(args[1],args[2])
    elif args[0] == 5:
        ModifyStd(args[1],args[2])
    elif args[0] == 6:
        DelStd(args[1],args[2])
    
    """options = {1 : AddStd(args[1],args[2],args[3],args[4],args[5]),
               2 : FindStd(args[1],args[2]),
               3 : DispStd,
               4 : DispFewStd,
               5 : ModifyStd,
               6 : DelStd,
               7 : exit}
    print(type(options))
    options[args[0]]"""

def AddStd(first_name,last_name,age,sex,major):
    print("\nAddStd function\n")
    students.append(student_class.Student(first_name,last_name,age,sex,major))

def FindStd(name,surname):
    print("\nFindStd function\n")
    for obj in students:
        if obj.fname == name and obj.lname == surname:
            print("Name: "+obj.fname)
            print("Surname: "+obj.lname)
            print("Age: ",obj.age)
            print("Sex: "+obj.sex)
            print("Major: "+obj.major)

def DispStd():
    print("\nDispStd function\n")
    for obj in students:
        print("Name: "+obj.fname)
        print("Surname: "+obj.lname)
        print("Age: ",obj.age)
        print("Sex: "+obj.sex)
        print("Major: "+obj.major)
        print()
    print("-----------------------------------------")

def DispFewStd():
    print("\nDispFewStd function\n")

def ModifyStd():
    print("\nModifyStd function\n")

def DelStd():
    print("\nDelStd function\n")
