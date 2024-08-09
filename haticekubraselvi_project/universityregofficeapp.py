#ALL COURSES
def courses(x):
    fc = open(x, "r")
    course = fc.readline()
    for course in fc:
        values = course.split(";")
        print(values[0] + ";" + values[1] + ";" + values[2] + ";" + values[3])

    fc.close()
#courses("course.txt")


#REGISTERED COURSES
print("Question 2")
def courses1(x):
    fc = open(x, "r")
    course = fc.readline()
    for course in fc:
        values = course.split(";")
        if int(values[3]) > 0:
            print(values[0] + ";" + values[1] + ";" + values[2] + ";" + values[3])
    fc.close()
#courses1("course.txt")


#ADDING NEW COURSE
print("adding a new course..")
def courses2(filename, code, cname, cinstructor, cregistered):
    fc = open(filename, "a")
    new_course = "{};{};{};{}\n".format(code,  cname, cinstructor, cregistered)
    fc.write(new_course)
    fc.close()
    courses(filename)
#courses2("course.txt","CENG1009", "Pragramming", "Baris Suzek", 5)



#FINDING A COURSE BY ITS CODE
def courses3(code):
    fc = open("course.txt", "r")
    course = fc.readline()
    for course in fc:
        values = course.split(";")
        if values[0] == code:
            print(values[0] + ";" + values[1] + ";" + values[2] + ";" + values[3])
    fc.close()
#courses3("CENG6789")



#FINDING A COURSE BY ITS NAME
def courses4(name):
    fc = open("course.txt", "r")
    for aline in fc.readline():
        course = aline.split(";")
        for name in course[1]:
            print(course[0] + ";" + course[1] + ";" + course[2] + ";" + course[3])
    fc.close()
courses4("Programminglanguages")






