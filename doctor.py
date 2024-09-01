from uuid import uuid4

class Doctor:
    def __init__(self,dni, first_name, last_name, specialty):
        self.id = uuid4()
        self.dni = dni
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
    
    def get_doctor_details(self):
        return {
            'dni' : self.dni,
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'self.specialty' : self.specialty
        }
    
    def __str__(self):
        return f"Dr. {self.first_name}{self.last_name} - {self.specialty}"
    