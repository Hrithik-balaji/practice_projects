from student import Student
import StudentRepository

def add_students(self,name,rollNumber,cgpa,branch):
    if not isinstanse(rollNumber,int):
        return "Invalid id"
    if cgpa>10.0 or cgpa<0.0:
        return "Invalid cgpa"
    if branch.lower().trim() not in ['cse','ece','mech','csm']:
        return "Invalid branch"
    if len(name)>32:
        return "lenght exceeded"
    if StudentRepository.findById(id):
        return "Student already exist"
    s1 = new Student(name,rollNumber,cgpa,branch)
