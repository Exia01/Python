class Product:
    def __init__(self, ItemName, price, status, brand, weight, retur_r):
        self.ItemName = ItemName
        self.price = price
        self.status = status
        self.brand = brand
        self.weight = weight
        self.tax = None
        self.retur_r = 'Like new'

    def addtax(self):
        self.tax = self.price * .025
        return self

    def typestat(self):
        self.status = "Sold"
        return self

    def reason(self):
        if self.retur_r == 'Defective':
            self.price = 0
        elif self.retur_r == 'Like New':
            self.status = 'For sale'
        elif self.retur_r == 'Used':
            self.price = self.price - self.price * .20
        else:
            self.retur_r == 'New'
            self.price == self.price
        return self

    def displayInfo(self):
        print(self.ItemName)
        print(self.status)
        print(self.brand)
        print(self.weight)
        print("Tax: .025%: " + str(self.tax) + " Taxation is theft")
        print(self.reason)


Purse = Product("Allguchi-purse", 4000, "Sold!", "Wakaflocka", "--", 'Defective')
Purse.addtax()
Purse.typestat()
Purse.displayInfo()
