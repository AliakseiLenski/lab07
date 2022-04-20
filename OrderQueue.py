from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
class OrderQueue:
    def __init__(self):
        self.heapList = [PizzaOrder(0)]
        self.currentSize = 0
        
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].getTime() < self.heapList[i // 2].getTime():
                temp = self.heapList[i // 2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2
            
    def addOrder(self, pizzaOrder):
        self.heapList.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        #print(pizzaOrder.getOrderDescription())

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].getTime() > self.heapList[mc].getTime(): 
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i): 
        if (i * 2 + 1) > self.currentSize: 
            return i * 2
        else:
            if self.heapList[i*2].getTime() < self.heapList[i*2+1].getTime():
                return i * 2
            else:
                return i * 2  + 1

    def processNextOrder(self):
        if len(self.heapList) < 2:
            raise QueueEmptyException()

        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval.getOrderDescription()


        
class QueueEmptyException(Exception):
    pass
    

'''
cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order1 = PizzaOrder(123000) #12:30:00PM
order1.addPizza(cp1)
order1.addPizza(sp1)
order2 = PizzaOrder(214500)
order2.addPizza(cp1)
order2.addPizza(sp1)
orderq = OrderQueue()
orderq.addOrder(order1)
orderq.addOrder(order2)
orderq.processNextOrder()
'''
