from Pizza import Pizza
class SpecialtyPizza(Pizza):

    def __init__(self,size,name):
        super().__init__(size)
        self.name = name
        if self.size == "S":
            super().setPrice(12.00)
        if self.size == "M":
            super().setPrice(14.00)
        if self.size == "L":
            super().setPrice(16.00)

    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def getPizzaDetails(self):
        return f"SPECIALTY PIZZA\n\
Size: {super().getSize()}\n\
Name: {self.name}\n\
Price: ${super().getPrice():.2f}\n"
        
