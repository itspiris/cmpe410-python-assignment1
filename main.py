import student_class
import functions

s1 = student_class.Student("piris","the assistant",20,"male","computer engineer")
functions.students.append(s1)
print()
print("I am the student council, " + s1.getAttb("first name"))
print(functions.students)

choice = int(input("Enter the integer corresponding to what you need: "))
print()
while choice != 7:
    if choice == 1:
        fname = input("Enter first name of student: ")
        lname = input("Enter last name of student: ")
        age = input("Enter age of student: ")
        sex = input("Enter gender of student: ")
        major = input("Enter the major of the student: ")
        functions.ToDo(choice,fname,lname,age,sex,major)
    elif choice == 2:
        fname = input("Name: ")
        lname = input("Surname: ")
        functions.ToDo(choice,fname,lname)
    elif choice == 3:
        functions.ToDo(choice)
    
    print()
    choice = int(input("Enter the integer corresponding to what you need: "))

print()
