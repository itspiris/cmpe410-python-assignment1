import student_class
import functions

s1 = student_class.Student("piris","the assistant",20,"male","computer engineer")
functions.students.append(s1)
print()

def options():
    print("Enter the integer corresponding to what you need: ")
    print("\t1 : Add a student\n\t2 : Find a specific student\n\t3 : Display all students stored")
    print("\t4 : Display students in certain age range\n\t5 : Modify an attribute of a specific student")
    print("\t6 : Delete a student with a specific first name-last name\n\t7 : exit")
options()
choice = int(input("\nAction: "))
print()
while choice != 7:
    if choice == 1:
        fname = input("Enter first name of student: ")
        lname = input("Enter last name of student: ")
        age = int(input("Enter age of student: "))
        sex = input("Enter gender of student: ")
        major = input("Enter the major of the student: ")
        functions.ToDo(choice,fname,lname,age,sex,major)
    elif choice == 2:
        fname = input("Name: ")
        lname = input("Surname: ")
        functions.ToDo(choice,fname,lname)
    elif choice == 3:
        functions.ToDo(choice)
    elif choice == 4:
        min_age = int(input("Minimum age: "))
        max_age = int(input("Maximum age: "))
        functions.ToDo(choice,min_age,max_age)
    elif choice == 5:
        name = input("Name: ")
        surname = input("Surname: ")
        functions.ToDo(choice,name,surname)
    elif choice == 6:
        name = input("Name of student to be deleted: ")
        surname = input("Surname of student to be deleted: ")
        functions.ToDo(choice,name,surname)
    
    print()
    options()
    choice = int(input("\nAction : "))
    print()

print()
