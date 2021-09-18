

class Student:

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