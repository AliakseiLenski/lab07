# lab07
The seventh lab from the Intermediate Python class
Managing incoming pizza orders using the MinHeap 
Pizza.py - creates the mother class for all pizza classes
CustomPizza.py - Child of Pizza. Inherits all methods from Pizza.py, but also adds toppings
to the customer order
SpecialtyPizza.py - Child of Pizza. Defined by a name and have set price depending on the size
PizzaOrder.py - Represents a collection of various pizza orders. Total price is the sum of all pizzas' prices. Also has an estimated time of pickup of each pizza
OrderQueue.py - Defines a MinHeap to organize and process pizza orders by their estimated time of pickup.
Tested in a tester file
