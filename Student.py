

class Student:

    # Constructor
    def __init__(self,ID,eager,credible,payment,time,category):
        self.ID = ID
        self.eager = eager
        self.credible = credible
        self.payment = payment
        self.time = time
        self.category = category

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