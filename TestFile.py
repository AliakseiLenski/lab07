from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_customPizza():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")

    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"

    cp2 = CustomPizza("M")
    cp2.addTopping("pineapple")
    assert cp2.getPizzaDetails() == "CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ pineapple\n\
Price: $10.75\n"

def test_specialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    sp2 = SpecialtyPizza("M", "Chief's favorite")
    assert sp2.getPizzaDetails() == "SPECIALTY PIZZA\n\
Size: M\n\
Name: Chief's favorite\n\
Price: $14.00\n"

def test_pizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"


def test_orderQueue():
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
    assert orderq[0] == order1

    
