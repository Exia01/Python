class Vehicle:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = None

    def addtax(self):
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        return self

    def displayInfo(self):
        print("Price: " + str(self.price) + "$")
        print("Speed: " + str(self.speed) + "mph")
        print("Fuel: " + str(self.speed))
        print("Mileage: " + str(self.speed) + "mph")
        print("Tax: " + str(self.tax) + "%")


tesla_model_s = Vehicle(200000, 250, "Electric", 400)
tesla_model_s.addtax()
tesla_model_s.displayInfo()

print(" ")

tesla_model_x = Vehicle(200000, 180, "Electric", 450)
tesla_model_x.addtax()
tesla_model_x.displayInfo()

print(" ")

tesla_model_3 = Vehicle(35000, 150, "Electric", 450)
tesla_model_3.addtax()
tesla_model_3.displayInfo()

print("")

BMWi3 = Vehicle(45000, 180, "Gas", 400)
BMWi3.addtax()
BMWi3.displayInfo()
