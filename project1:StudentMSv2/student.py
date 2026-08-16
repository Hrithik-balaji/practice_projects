class Student:
    
    def __init__(self,name,student_id,cgpa,branch):
        self.name=name
        self.student_id=student_id
        self.cgpa=cgpa
        self.branch=branch
    
    def display(self):
        print(
            f"Name:{self.name}\n"
            f"Student ID:{self.student_id}\n"
            f"CGPA:{self.cgpa}\n"
            f"Branch:{self.branch}\n"
        )