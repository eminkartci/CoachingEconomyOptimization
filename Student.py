

class Student:

    # Constructor
    def __init__(self,ID):
        self.ID = ID

    # toString
    def __str__(self) -> str:
        
        content = f"""
----- Student {self.ID} -----
|
|
"""
        return content