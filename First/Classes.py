class Person: 
    def __init__(self, age, RUT, gender, wigth, higth):
        self.__age = age
        self.__RUT = RUT
        self.__gender = gender
        self.__wigth = wigth
        self.__higth = higth

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
    


class Pacient(Person):
    def __init__(self, age, RUT, gender, wigth, higth, firstConsultationDate, treatingDoctor):
        super().__init__(age, RUT, gender, wigth, higth)
        self.__firstConsultationDate = firstConsultationDate
        self.__treatingDoctor = treatingDoctor

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
        if gender == "M":
            return gender
        else:
            return "H"



class Medic(Person):
    def __init__(self, age, RUT, gender, wigth, higth, priceConsult, especiality):
        super().__init__(age, RUT, gender, wigth, higth)
        self.__priceConsult = priceConsult
        self.__especiality = especiality

    def get_priceConsult(self):
        return self.__priceConsult
    
    def get_especiality(self):
        return self.__especiality
    
