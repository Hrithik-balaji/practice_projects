from datetime import datetime
import os
import json
database=[]
MAXCGPA=10
MINCGPA=0
#convert to json
def save_database():
    with open("student.json",'w') as file:
        json.dump(database,file,indent=3)

#backup creation
def create_backup():
    with open("student.json",'r') as file:
        data=json.load(file)
    date=str(datetime.now().strftime("%Y-%m-%d"))
    name=date+".json"
    with open(name,'w') as file:
        json.dump(data,file,indent=3)
        print("Backup has been created");

#deleting backup
def delete_backup():
    date=input("Enter the date:")
    name=date+".json"
    os.remove(name)
    print("Backup deleted!!!")

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
def add_student():
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
    branch=input("Enter branch:").strip().upper()
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

    student = {
        "name": name,
        "student_id": student_id,
        "branch": branch,
        "cgpa": cgpa
    }
    database.append(student)
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
    branch=input("Enter the if you want total or branch-wise:").strip().upper()
    if branch=="TOTAL":
        print("Total number of students:",len(database))
        return
    else:
        section=input("Enter the department:").strip().upper()
        count=sum(1 for student in database if student['branch'].upper()==section)
        print("Total number of students in",section,"are: ",count)
        return

#convert to txt file
def convert_file():
    with open("report.txt",'w') as file:
        for student in database:
            file.write(
                f"|{student['name']} | "
                f"|{student['student_id']} | "
                f"|{student['branch']} | "
                f"|{student['cgpa']}|\n"
            )
    print("Report Generated......")

#view student function
def view_students():
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
def update_student():
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
        print("name:",student['name'],"\n","\n","Branch:",student['branch'],"\n"+"CGPA:",student['cgpa'],"\n")
        return
    print("Student not found")
    return
#fliter 
def filter_students():
    options=input("Enter the filter").strip().lower()
    if options=="cgpa":
        cgpa=float(input("Enter the cgpa:"))
        l=[s for s in database if s['cgpa']>=cgpa]
        sorted(l,reverse=True)
        print(f"Name:{l['name']}\tcgpa:{l['cgpa']}")
    

#average of students
def average_students():
    option=input("Enter if total or branch:").strip().upper()
    number_of_students=0
    total=0
    if option=="TOTAL" :
        number_of_students=sum(1 for student in database)
        if number_of_students == 0:
            print("No students found in this branch.")
            return
        total=sum(student['cgpa'] for student in database) 
    elif option=="BRANCH":
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

#sorting students
def sort():
    option=input("How do you want to sort:\n1)by name \n2)by cgpa \nEnter your choice:").strip().upper()
    if option=="NAME":
        database.sort(key=lambda student:student['name'])
        save_database()
        print("Students have been sorted based on name")
    elif option=="CGPA":
        database.sort(key=lambda student:student['cgpa'],reverse=True)
        save_database()
        print("Students have been sorted based on cpga")
        return

#topper seach
def topper():
    option=input("which one do you want ? overall or branch:").strip().upper()
    students = [
    s for s in database
    if s['branch'].upper() == branch.upper()
]
    if option=="OVERALL":
        topper = max(
            students,
            key=lambda s:s['cgpa']
        )
        print("The topper of the colleger:\n")
        print(f"Name:{topper['name']}\nStudent ID:{topper['student_id']}\nBranch:{topper['branch']}\nCGPA:{topper['cgpa']}")
        return
    elif option=="BRANCH":
        branch=input("Enter the branch:")
        mark=max(
            students,
            key=lambda s:s['cgpa'] and s['branch'].upper()==branch
        )
        print("The topper of ",branch," is ")
        print(f"Name:{topper['name']}\nStudent ID:{topper['student_id']}\nBranch:{topper['branch']}\nCGPA:{topper['cgpa']}")
        return
    
#delete student function
def delete_student():
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
def main():
    load_database()
    start=input("Start the system:")
    while start.lower() in ["yes","start"]:
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
            8.sort
            9.find highest scorer
            10.generate report
            11.create backup
            12.delete backup
            13.filter
            14.exit
        """)
        try:
            ops=int(input("Enter the operation:"))
        except ValueError:
            print("Invalid operation!! please enter a valid one........")
            pause()
            continue
        if ops==1:
            add_student()
            pause()
        elif ops==2:
            view_students()
            pause()
        elif ops==3:
            search_student()
            pause()
        elif ops==4:
            update_student()
            pause()
        elif ops==5:
            delete_student()
            pause()
        elif ops==6:
            total_students()
            pause()
        elif ops==7:
           average_students()
           pause()
        elif ops==8:
            sort()
            pause()
        elif ops==9:
            topper()
            pause()
        elif ops==10:
            convert_File()
            pause()
        elif ops==11:
            create_backup()
            pause()
        elif ops==12:
            delete_backup()
            pause()
        elif ops==13:
            filter_students()
            pause()
        elif ops==14:
            break
        elif ops>14 or ops<1:
            print("Invalid option!! Enter a valid one......")
            pause()

if __name__=="__main__":
    main()
