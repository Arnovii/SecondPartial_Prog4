import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
print(scriptPath)
fileTextName = "Nutrition Clinic.txt"
fileTextPath = os.path.join(scriptPath, fileTextName)
print(fileTextPath)

class Person: 
    def __init__(self, name, age, RUT, gender, wigth, higth):
        self.__name = name
        self.__age = age
        self.__RUT = RUT
        self.__gender = gender
        self.__wigth = wigth
        self.__higth = higth
        self.type = "Person"

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_RUT(self):
        return self.__RUT
    
    def get_gender(self):
        return self.__gender
    
    def get_wigth(self):
        return self.__wigth

    def get_higth(self):
        return self.__higth
    
    def get_type(self):
        return self.type

    def save_info(self):
        with open(fileTextPath,"a") as file:
            file.write("|-------------------------------------------|\n")
            file.write(f"name: {self.get_name()}\n")
            file.write(f"type: {self.get_type()}\n")
            file.write(f"age: {self.get_age()}\n")
            file.write(f"RUT: {self.get_RUT()}\n")
            file.write(f"gender: {self.get_gender()}\n")
            file.write(f"wigth: {self.get_wigth()}\n")
            file.write(f"higth: {self.get_higth()}\n")
        print(f"\nSaved in {fileTextName}\n")

class Pacient(Person):
    def __init__(self, name, age, RUT, gender, wigth, higth, firstConsultationDate, treatingDoctor):
        super().__init__(name, age, RUT, gender, wigth, higth)
        self.__firstConsultationDate = firstConsultationDate
        self.__treatingDoctor = treatingDoctor
        self.type = "Pacient"
    def get_firstConsultationDate(self):
        return self.__firstConsultationDate
    
    def get_treatingDoctor(self):
        return self.__treatingDoctor
    
    def calculate_BMI(self):
        BMI = self.get_wigth() / self.get_higth()**2

        if BMI < 18.5:                      # Underweight
            return -1
        elif BMI >= 18.5 and BMI <= 24.9:   # Normal
            return 0
        else:                               # Overweight
            return 1
    def validateLegalAge(self):
        if self.get_age() >= 18:
            return True
        else:
            return False
        
    def validateGender(self, gender):
        if gender == self.get_gender():
            return True 
        else:
            return False 

    def save_info(self):
        with open(fileTextPath, "a") as file:
            super().save_info()
            file.write(f"firstConsultationDate: {self.get_firstConsultationDate()}\n")
            file.write(f"treatingDoctor: {self.get_treatingDoctor()}\n")
            
class Medic(Person):
    def __init__(self, name, age, RUT, gender, wigth, higth, priceConsult, especiality):
        super().__init__(name, age, RUT, gender, wigth, higth)
        self.__priceConsult = priceConsult
        self.__especiality = especiality
        self.type = "Medic"

    def get_priceConsult(self):
        return self.__priceConsult
    
    def get_especiality(self):
        return self.__especiality
    
    def save_info(self):
        with open(fileTextPath, "a") as file:
            super().save_info()
            file.write(f"priceConsult: {self.get_priceConsult()}\n")
            file.write(f"especiality: {self.get_especiality()}\n")

