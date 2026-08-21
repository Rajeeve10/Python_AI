class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Attribute for the vehicle make
        self.model = model    # Attribute for the vehicle model

    def Description(self):
        return f"{self.make,self.model}"  # Method to return a description of the vehicle



veh1 = Vehicle("Audi", "A4")
veh2 = Vehicle("Toyota", "Yaris")
	
print(veh1.Description())
print(veh2.Description())