

from Student import Student



## ONE Student
# s = Student(1,8,4,500,10,"Software")
# print(s)
# s.save_as_csv()

## Create Students
students = Student.create_student(10)
for s in students:
    print(s)
    
Student.save_students_csv(students)
