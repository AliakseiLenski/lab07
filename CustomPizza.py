from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if self.size == "S":
            super().setPrice(8.00)
        elif self.size == "M":
            super().setPrice(10.00)
        elif self.size == "L":
            super().setPrice(12.00)
            
    def addTopping(self,topping):
        self.toppings.append(topping)
        if self.size == "S":
            super().setPrice(self.getPrice() + 0.5)
        if self.size == "M":
            super().setPrice(self.getPrice() + 0.75)
        if self.size == "L":
            super().setPrice(self.getPrice() + 1.00)

    def getPizzaDetails(self):
        New_Topping = "\n\t+ "
        Tab = '\t+ '
        New_line ='\n'
        return f"CUSTOM PIZZA\n\
Size: {self.getSize()}\n\
Toppings:{New_line + Tab + New_Topping.join(self.toppings)  if len(self.toppings) > 0 else ''}\n\
Price: ${super().getPrice():.2f}\n"

