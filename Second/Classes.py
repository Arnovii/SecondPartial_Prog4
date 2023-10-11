import os

scriptPath = os.path.dirname(os.path.realpath(__file__))
fileTextVehicles = "Vehicles.txt"
fileTextPath = os.path.join(scriptPath, fileTextVehicles)

fileTextConverter = "Converter.txt"
fileTextConverterPath = os.path.join(scriptPath, fileTextConverter)

class Vehicle:
    def __init__(self, vehicleID, brand, model, year):
        self.__vehicleID = vehicleID
        self.__brand = brand
        self.__model = model
        self.__year = year
    
    def get_vehicleID(self):
        return self.__vehicleID
    
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def __str__(self):
        return f"ID: {self.get_vehicleID()}\nBrand: {self.get_brand()}\nModel: {self.get_model()}\nYear: {self.get_year()}\n"

    def save_info(self):
        with open(fileTextPath, "a") as file:
            file.write("|-------------------------------------------|\n")
            file.write(self.__str__())

class Converter:
    def __init__(self, miles):
        self.__miles = miles
        self.__kilometers = self.__miles * 1.60934

    def get_miles(self):
        return self.__miles
    
    def get_kilometers(self):
        return self.__kilometers
    



