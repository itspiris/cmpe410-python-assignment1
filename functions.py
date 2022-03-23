import student_class

students = []
def ToDo(*args):
    #print("args[0]: ",args[0])
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
    elif args[0] == 7:
        args[1].write_data_to_file()
    elif args[0] == 8:
        args[1].read_data_from_a_file()
    
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
    #print("\nAddStd function\n")
    students.append(student_class.Student(first_name,last_name,age,sex,major))

def FindStd(name,surname):
    #print("\nFindStd function\n")
    found = False
    for obj in students:
        if obj.fname == name and obj.lname == surname:
            found = True
            print("\n-----------------------------------------\n")
            print("Name: "+obj.fname)
            print("Surname: "+obj.lname)
            print("Age: ",obj.age)
            print("Sex: "+obj.sex)
            print("Major: "+obj.major)
            print("\n-----------------------------------------")
    if not found:
        print("\nNo such student exists on our system")

def DispStd():
    #print("\nDispStd function\n")
    print("\n-----------------------------------------\n")
    for obj in students:
        print("Name: "+obj.fname)
        print("Surname: "+obj.lname)
        print("Age: ",obj.age)
        print("Sex: "+obj.sex)
        print("Major: "+obj.major)
        print()
    print("-----------------------------------------")

def DispFewStd(min_age,max_age):
    #print("\nDispFewStd function\n")
    for obj in students:
        if obj.age >= min_age and obj.age <= max_age:
            print("\n-----------------------------------------\n")
            print("Name: "+obj.fname)
            print("Surname: "+obj.lname)
            print("Age: ",obj.age)
            print("Sex: "+obj.sex)
            print("Major: "+obj.major)
            #print()
    print("\n-----------------------------------------")


def ModifyStd(fname,lname):
    #print("\nModifyStd function\n")
    found = False
    for obj in students:
        if obj.fname == fname and obj.lname == lname:
            attbt = input("Attribute to change: ")
            newvalue = input("New value: ")
            obj.setAttb(attbt,newvalue)
            found = True
    if not found:
        print("\nNo such student exists on our system")

def DelStd(fname,lname):
    #print("\nDelStd function\n")
    found = False
    for obj in students:
        if obj.fname == fname and obj.lname == lname:
            students.remove(obj)
            found = True
    if not found:
        print("\nNo such student exists on our system")
