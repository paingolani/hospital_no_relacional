import patient
import doctor
from patient import Patient

def main():
    paciente = Patient("34.567.890", "Juan", "Pérez", "1990-02-12", "Masculino", "Calle 123, Buenos Aires", "011-1234-5678", "juanperez@example.com")
    print(paciente.__dict__)

if __name__ == "__main__":
    main()