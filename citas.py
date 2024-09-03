'''... . Citas
IdCita (identificador único)
IdPaciente (id del paciente asociado)
IdDoctor (id del doctor asociado)
Fecha
Hora
Estado (confirmada, cancelada, etc.) '''
import uuid
class Apt:
    def __init__(self, patient_id, doctor_id, date, status) -> None:
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.it_apt = uuid.uuid4
        self.status = status
        
    def get_patient_id(self):
        return (self.patient_id)
    
    def get_doctor_id(self):
        return (self.doctor_id)