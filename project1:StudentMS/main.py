import json
database=[]
MAXCGPA=10
MINCGPA=0
#convert to json
def save_database():
    with open("student.json",'w') as file:
        json.dump(database,file,indent=3)

#load database
def load_database():
    global database
    try:
        with open("student.json","r") as file:
            database=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        database=[]
        return

#add student function
def add_Student():
    #validation for name
    name=input("Enter student name:")
    if(name.strip()==""):
        print("Empty field!!Enter a valid one,,,,")
        return
    #validation for id
    try:
        student_id=int(input("Enter student_id:"))
        if student_id<1:
            print("Invalid id,Enter a valid one,,,,,")
            return
        if find_student(student_id):
            print("Student with this student_ID already exists. Please use a unique student_ID.")
            return
    except ValueError:
         print("Invalstudent_id input. Please enter a valstudent_id integer for the student_ID.")
         return
    #validation for branch
    branch=input("Enter branch:")
    if(branch.strip()==""):
        print("Empty field,Enter a valid one,,,,")
        return
    #validation for CGPA
    try:
        cgpa=float(input("Enter cgpa:"))
        if not(MINCGPA<=cgpa<=MAXCGPA):
            print("Invalid CGPA,Enter a valid one,,,,")
            return
    except ValueError:
        print("Invalid CGPA input. Please enter a valid float for the CGPA.")
        return

    ls=dict()
    ls['name']=name
    ls['student_id']=student_id
    ls['branch']=branch
    ls["cgpa"]=cgpa
    database.append(ls)
    save_database()
    print("Successfully added !!!!!!!!!!!!!")


#student find function
def find_student(student_student_id):
    for student in database:
        if student['student_id'] == student_student_id:
            return student
    return None

#total students function
def  total_students():
    print("Total number of students:",len(database))

#view student function
def view_Students():
    if len(database)==0:
        print("No student available !! Empty database")
        return
    print("-"*60)
    print(f"|{'Name':^25}|{'Student ID':^10}|{'Branch':^10}|{'CGPA':^10}|")
    print("-"*60)
    for student in database:
        print(f"|{student['name']:^24}|{student['student_id']:^10}|{student['branch']:^10}|{student['cgpa']:^5}|")
    print("-" * 60)
#update student function
def update_Student():
    try:
        student_id=int(input("Enter student_id:"))
    except ValueError:
         print("Invalid student_id input. Please enter a valid student_id.")
         return
    student = find_student(student_id)
    if student:
        required=(input("Enter the field needed to be updated:")).lower()
        if required=="name":
            name=input("Enter the new name:")
            student['name'] = name
            print("Successfully updated")
            save_database()
            return
        elif required=="branch":
            branch=input("Enter the new branch:")
            student['branch'] = branch
            print("Successfully updated")
            save_database()
            return
        elif required=="cgpa":
            try:
                cgpa=float(input("Enter the new cgpa:"))
                if not(MINCGPA<=cgpa<=MAXCGPA):
                    print("Invalid CGPA,Enter a valid one,,,,")
                    return
                student['cgpa'] = cgpa
                save_database()
                print("Successfully updated")
                return
            except ValueError:
                print("Invalid CGPA input. Please enter a valid float for the CGPA.")
                return
        else:
            print("Invalid field!!")
            return
    print("Student not found")
    return

#search student function
def search_student():
    try:
        student_id=int(input("Enter student_id:"))
    except ValueError:
         print("Invalid student_id input. Please enter a valid student_id.")
         return
    student = find_student(student_id)
    if student: 
        print("Student found")
        print("name:",student['name'],"\n"+"student_ID:",student['student_id'],"\n","Branch:",student['branch'],"\n"+"CGPA:",student['cgpa'],"\n")
        return
    print("Student not found")
    return
#average of students
def Average_students():
    required_branch=input("Enter the branch of students:").strip().upper()
    number_of_students=sum(1 for student in database if student['branch'].upper()==required_branch)
    if number_of_students == 0:
        print("No students found in this branch.")
        return
    total=sum(student['cgpa'] for student in database if student['branch'].upper()==required_branch)    
    avg=total/number_of_students
    print("Average of the students :",round(avg,2))
    return
#pause function
def pause():
    input("\nPress Enter to continue...")

#delete student function
def delete_Student():
    try:
        student_id=int(input("Enter student_id:"))
    except ValueError:
         print("Invalid student_id input. Please enter a valid student_id.")
         return
    student = find_student(student_id)
    if student:
        database.pop(database.index(student))
        save_database()
        print("Successfully deleted")
    else:
        print("Student not found")
    return

#main function
load_database()
start=input("Start the system:")
while start=="yes" or start=="YES" or start=="start":
    print("""
        #######################################################
                    Student Management System
        #######################################################
        1.add Students
        2.view Students
        3.Search Students
        4.Update Students
        5.Delete student
        6.Total number of students
        7.Average of students
        8.exit
    """)
    try:
        ops=int(input("Enter the operation:"))
    except ValueError:
        print("Invalid operation!! please enter a valid one........")
        pause()
        continue
    if ops==1:
            add_Student()
            pause()
    elif ops==2:
            view_Students()
            pause()
    elif ops==3:
            search_student()
            pause()
    elif ops==4:
            update_Student()
            pause()
    elif ops==5:
            delete_Student()
            pause()
    elif ops==6:
            total_students()
            pause()
    elif ops==7:
            Average_students()
            pause()
    elif ops==8:
        break
    elif ops>8 or ops<1:
        print("Invalid option!! Enter a valid one......")
        pause()
