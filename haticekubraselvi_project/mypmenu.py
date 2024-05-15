def allcourses():
    fc = open(r"C:\Users\Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\course.txt", "r")
    course = fc.readline()
    while course:
        values = course.split(";")
        print(values[0] + ";" + values[1] + ";" + values[2] + ";" + values[3])
        course = fc.readline()
    fc.close()

def registered_courses():
    fc = open(r"C:\Users\Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\course.txt", "r")
    course = fc.readline()
    while course:
        a = course.split(";")
        if int(a[3]) > 0:
            print(a[0] + ";" + a[1] + ";" + a[2] + ";" + a[3])
            course = fc.readline()
        else:
            course = fc.readline()
    fc.close()


def adding_course():
    fc = open(r"C:\Users\Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\course.txt", "a+")
    code = input("Please enter the course code:")
    cname = input("Please enter the name of wanted course:")
    cinstructor = input("Please enter the instructor of wanted course:")
    cregistered = int(input("Please enter the number of students registered for this course:"))
    new_course = "{};{};{};{}\n".format(code,  cname, cinstructor, cregistered)
    fc.write(new_course)
    fc.close()
    print("The operation is done successfully...")
    print("--------LIST OF COURSES--------")
    allcourses()

def find_courseCode():
    fc = open(r"C:\Users\Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\course.txt", "r")
    code = input("Please enter the code of the wanted course:")
    course = fc.readline()
    for i in course:
        values = course.split(";")
        if values[0] == code:
            print(values[0] + ";" + values[1] + ";" + values[2] + ";" + values[3])
            print("The wanted course is here..")
            break
        else:
            course = fc.readline()
    fc.close()

def find_courseName():
    fc = open(r"C:\Users\Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\course.txt", "r")
    name = input("Please enter the name of the course:")
    course = fc.readline()
    while course:
        items = course.split(";")
        if items[1] == name:
            print(items[0] + ";" + items[1] + ";" + items[2] + ";" + items[3])
        course = fc.readline()
    fc.close()



"""
def adding_student():
    fc = open(r"C:Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\course.txt", "a+")
    fs = open(r"C:\Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\student.txt", "a+")
    id = int(input("Please enter the student no:"))
    course_code = input("Please enter the course code you want:")
    course = fc.readline()
    while course:
        a = course.split(";")
        if int(a[3]) > 0:
            print(a[0] + ";" + a[1] + ";" + a[2] + ";" + a[3])
            course = fc.readline()
        else:
            course = fc.readline()

    allcourses()

    for i in range(len(course)):
        items = course.split(";")
        if items[0] == course_code:

   for i in course:
        items = course.split(";")
        if items[0] == course_code:
            
            fc.write(a + 1)
  
    new = "{};{};{}\n".format(id, name_surname, course_code)
    fs.write(new)
    student = fs.readline()
    while student:
        values = student.split(";")
"""
def allstudents():
    fs = open(r"C:\Users\Hksel\PycharmProjects\pythonProject\haticekubraselvi_project\student.txt", "r")
    student = fs.readline()
    while student:
        items = student.split(";")
        if len(items[2]) > 0:
            print("Student:  " + items[0] + ";" + items[1])
            print("")
            print("Taken courses list:   " + items[2])
            print("")
            student = fs.readline()
        else:
            print("Student:  " + items[0] + ";" + items[1])
            print("")
            print("There isn't taken a course:    " + items[2])
            print("")
            student = fs.readline()
    fs.close()

def universityofficeappmenu():

    functionlist = [allcourses, registered_courses, adding_course, find_courseCode, find_courseName, """adding_student""",allstudents]

    while True:
        print("(1)- All the courses:")
        print("(2)- All the courses that have students registered:")
        print("(3)- Adding a new Course:")
        print("(4)- Searching a course by course code:")
        print("(5)- Searching a course by course name:")
        print("(6)- Registering a student to a course:")
        print("(7)- All the students:")
        print("(8)- Top 3 most crowded courses:")
        print("(9)- Top 3 students with the most course registrated:")
        print("(0)- Exit the program..")
        print("\n" * 2)
        yourchoice = int(input("Please choose the option you want(0-9):"))
        print("\n" * 2)

        if yourchoice <= 9 and yourchoice >= 1:
            functionlist[yourchoice - 1]()
            print("\n" * 1)

        elif yourchoice == 0:
            print("Exiting...")
            break
        else:
            print("Please choose an option between 0 and 9!")
            print("\n" * 2)


universityofficeappmenu()


