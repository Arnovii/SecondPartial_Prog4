import Classes as cls

# Create an instance of the class Medic
print("Enter the information of the medic: \n")
medicName = input("Name: ")
medicAge = int(input("Age (years): "))
medicRUT = input("RUT: ")
medicGender = input("Gender (H or M): ").upper()
medicWigth = float(input("Wigth (kg): "))
medicHigth = float(input("Higth (m): "))
medicPriceConsult = float(input("Price of the consult ($): "))
medicSpecialty = input("Specialty: ")
medic1 = cls.Medic(medicName, medicAge, medicRUT, medicGender, medicWigth, medicHigth, medicPriceConsult, medicSpecialty)

# Create an instance of the class Patient
print(f"\nEnter the information of {medic1.get_name()}'s patient: \n")
patientName = input("Name: ")
patientAge = int(input("Age (years): "))
patientRUT = input("RUT: ")
patientGender = input("Gender (H or M): ").upper()
patientWigth = float(input("Wigth (kg): "))
patientHigth = float(input("Higth (m): "))
patientFirstConsultationDate = input("First consultation date (DD/MM/YYYY): ")

patient1 = cls.Pacient(patientName, patientAge, patientRUT, patientGender, patientWigth, patientHigth, patientFirstConsultationDate, medic1.get_name())

