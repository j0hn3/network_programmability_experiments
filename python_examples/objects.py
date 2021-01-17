#below is vehicle.py a custom class for a vehicle to create a custom class more speific to our problem
#this is the shell of an object, when an object is crated using the class below it is initialized with all the attributes present
#in addation to attributes this class also contains a custom methiod to print details about the object
class Vehicle:
    """
    Docstring describing the class - This class defines the basic compoents of a vehicle
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")

#this is an example of loading vehicle.py (above) and loading it into the REPEL using -i
#civic a type of vehicle is created using the class, attributes are added and accessed (using name.attribute)
#the custom methiod is also accessed 
'''
[cloud_user@johnwright1c python_objects]$ python -i vehicle.py 
>>> 
>>> 
>>> civic = Vehicle('4-cylinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'])
>>> civic.serialnumber = 1234
>>> print(civic.serialnumber)
1234
>>> print(civic.engine)
4-cylinder
>>> 
>>> civic.description()
A vehicle with an 4-cylinder engine, and ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'] tires
>>> 
'''

+++++

class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """
    default_tire = 'tire'

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    @classmethod
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")

$ python3.7 -i vehicle.py
>>> bike = Vehicle.bicycle()
>>> bike
<__main__.Vehicle object at 0x7f947c0f7750>
>>> bike.description()
A vehicle with an None engine, and ['tire', 'tire'] tires
>>> bike.engine
>>> bike.tires
['tire', 'tire']