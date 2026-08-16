from student import Student

database={}

def add_students(s):
    rollNumber=s.student_id
    database[rollNumber]=s

def findById(id):
    return database.get(id)