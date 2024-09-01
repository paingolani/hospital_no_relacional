from uuid import uuid4

class Patient(self,dni,first_name, last_name, date_of_birth, address, phone_number, email):
    def __init__(self, dni, first_name, last_name, date_of_birth, sex, address, phone_number, email):
            self.dni = dni
            self.id_number = uuid.uuid4()
            self.first_name = first_name
            self.last_name = last_name
            self.date_of_birth = date_of_birth
            self.sex = sex
            self.address = address
            self.phone_number = phone_number
            self.email = email
            self.medical_history = []
            
    def get_patient_details(self):
        return {
            'dni' : self.dni,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'id_number': self.id_number,
            'date_of_birth' : self.date_of_birth,
            'address' : self.address,
            'phone_number' : self.phone_number,
            'email' : self.email
        }
    def update_patient_address(self, new_address):
        self.address = new_address

    def update_patient_phone(self, new_phone_number):
        self.phone_number = new_phone_number

    def get_patient_medical_history(self):
        return self.medical_history

    def add_patient_medical_record(self, new_record):
        self.medical_history.append(new_record)