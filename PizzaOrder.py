from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.pizzalist = []
        self.time = time


    def getTime(self):
        return self.time

    def setTime(self,time):
        self.time = time

    def addPizza(self,pizza):
        #adds Pizza object to the end of the list
        self.pizzalist.append(pizza)
        
    def getOrderDescription(self):        
        joining ="\n----\n"
        return f"******\n\
Order Time: {self.getTime()}\n\
{joining.join([pizza.getPizzaDetails() for pizza in self.pizzalist])}\
\n\
----\n\
TOTAL ORDER PRICE: ${sum([(pizza.getPrice()) for pizza in self.pizzalist]):.2f}\n\
******\n"

    def __lt__(self, other):
        if self.time < other.time:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.time > other.time:
            return True
        else:
            return False
        
        
