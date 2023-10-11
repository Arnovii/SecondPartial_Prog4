import Classes as cls

# Create an instance of the class Medic
print("\nENTER THE INFORMATION OF THE MEDIC... \n")
medicName = input("Name: ")
medicAge = int(input("Age (years): "))
medicRUT = input("RUT: ")
medicGender = input("Gender (H or M): ").upper()
medicWigth = float(input("Weigth (kg): "))
medicHigth = float(input("Higth (m): "))
medicPriceConsult = float(input("Price of the consult ($): "))
medicSpecialty = input("Specialty: ")
medic1 = cls.Medic(medicName, medicAge, medicRUT, medicGender, medicWigth, medicHigth, medicPriceConsult, medicSpecialty)

# Create an instance of the class Patient
print(f"\nENTER THE INFORMATION OF {medic1.get_name().upper()}'S PATIENT: \n")
patientName = input("Name: ")
patientAge = int(input("Age (years): "))
patientRUT = input("RUT: ")
patientGender = input("Gender (H or M): ").upper()
patientWigth = float(input("Weigth (kg): "))
patientHigth = float(input("Higth (m): "))
patientFirstConsultationDate = input("First consultation date (DD/MM/YYYY): ")
patient1 = cls.Pacient(patientName, patientAge, patientRUT, patientGender, patientWigth, patientHigth, patientFirstConsultationDate, medic1.get_name())

print(f"\nThe medic {medic1.get_name()} has a patient called {patient1.get_name()}\n")

# Calculate the BMI of the patient
BMI = patient1.calculate_BMI()

if BMI == -1:
    print(f"The patient {patient1.get_name()} is underweight")
elif BMI == 0:
    print(f"The patient {patient1.get_name()} has a normal weight")
else:
    print(f"The patient {patient1.get_name()} is overweight")

# Validate if the patient is of legal age
if patient1.validateLegalAge():
    print(f"The patient {patient1.get_name()} is of legal age")
else:
    print(f"The patient {patient1.get_name()} is not of legal age")


# Validate gender of the patient
gender = input("Input the gender of the patient (H or M): ").upper()

if patient1.validateGender(gender):
    print(f"The patient is {gender}...")
else:
    print(f"The patient isn't {gender}...")

# Save the information of the medic and the patient in a text file
medic1.save_info()
patient1.save_info()