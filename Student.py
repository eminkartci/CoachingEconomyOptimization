from array import ArrayType
from os import stat
import random

class Student:

    ## STATIC
    @staticmethod
    def create_student(student_count) -> ArrayType:
        # CONSTANT
        categories = ["Software","Math","Consulting","Music","Sport"]
        students = []
        for i in range(student_count):
            s = Student(i,random.randint(0,11),random.randint(0,11),random.randint(200,700),random.randint(5,15),random.choice(categories))
            students.append(s)

        return students

    # Constructor
    def __init__(self,ID,eager,credible,payment,time,category):
        self.ID = ID
        self.eager = eager
        self.credible = credible
        self.payment = payment
        self.time = time
        self.category = category

    # Save as csv
    def save_as_csv(self):
        with open(f'./Student/{self.ID}.csv', 'w') as f:
            f.write(self.to_string_csv())

    # toStringCSV
    def to_string_csv(self) -> str:
        csv_content = "ID,Eager,Credible,Payment,Time,Category\n"
        csv_content += f"{self.ID},{self.eager},{self.credible},{self.payment},{self.time},{self.category}"

        return csv_content
    # toString
    def __str__(self) -> str:
        
        content = f"""
----- Student {self.ID} -----
|   Eager [1-10]    : {self.eager}
|   Credible [1-10] : {self.credible}
|   Payment [1-10]  : {self.payment}
|   Time [1-10]     : {self.time}
|   Category [1-10] : {self.category}
------------------------------
"""
        return content