# You will create a superclass and three subclasses. The Shape superclass will have generic
# properties. These will ultimately hold the areas and boundary lengths of your shapes. The
# superclass will also count how many Shapes have created.
import math


# Shape superclass
class Shape:
    # initialize count - private
    __count = 0

    def __init__(self):
        self.area = None
        self.boundary = None
        Shape.__count += 1

    def getArea(self, length):
        return 0

    def getBoundary(self, length):
        return 0

    @classmethod
    def getCount(cls):
        return Shape.__count

    def printDetails(self):
        print("Area:", self.area)
        print("Boundary", self.boundary)


# Create subclass called square
# Determine the appropriate access modifier for this property
# Access modifiers : public, _protected, __private
class Square(Shape):
    # Need to initialize count class property for each subclass
    __count = 0

    def __init__(self):
        super().__init__()
        # increment when instance of square created
        Square.__count += 1

    # Override two instance methods from superclass?
    def getArea(self, length):
        self.area = length * length
        return self.area

    # same as perimeter
    def getBoundary(self, length):
        self.boundary = length * 4  # same as all lengths added.
        return self.boundary

    @classmethod
    def getCount(cls):
        return Square.__count


# Create Triangle subclass
class Triangle(Shape):
    __count = 0

    def __init__(self):
        super().__init__()

        # increment when instance created
        Triangle.__count += 1

    # Override two instance methods from superclass?
    def getArea(self, length):
        # opposite and adjacent are same length
        self.area = (length * length) / 2
        return self.area

    def getBoundary(self, length):
        self.boundary = (2 * length) + (length ** 2 + length ** 2) ** 0.5  # a+b+ square root of a sqrd + b sqrd
        return self.boundary

    @classmethod
    def getCount(cls):
        return Triangle.__count


# Create Triangle subclass
class Circle(Shape):
    __count = 0

    def __init__(self):
        super().__init__()
        # increment when instance created
        Circle.__count += 1

    # Override two instance methods from superclass?
    def getArea(self, radius):
        self.area = math.pi * radius ** 2
        return self.area

    def getBoundary(self, radius):
        self.boundary = 2 * math.pi * radius  # circumference
        return self.boundary

    @classmethod
    def getCount(cls):
        return Circle.__count
