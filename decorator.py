""" The Decorator Pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

----->Designing a hotel ordering system (add quanitity, extra cheese etc , eg zomato food ordering system)
----->Designing a Shopping cart ( With each user as Base decorator and items as extra)

"""

from abc import abstractclassmethod

#abstract beverage class
class BeverageAbstract:
    @abstractclassmethod
    def __init__(self):
        self.description="Unknown Beverage"
    

    @abstractclassmethod
    def getDescription(self):
        return self.description
    
    @abstractclassmethod
    def getCost(self):
        pass

#abstact Decorator the main decorator
class mainDecorator(BeverageAbstract):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def getDescription(self):
        pass

    @abstractclassmethod
    def getCost(self):
        pass


class Espresso(BeverageAbstract):

    @classmethod
    def __init__(self):
        self.description="Espresso"

    @classmethod
    def getCost(self):
        return 0.20

class HouseBlend(BeverageAbstract):

    @classmethod
    def __init__(self):
        self.description="House Blend"

    @classmethod
    def getCost(self):
        return 1.20

class Mocha(mainDecorator):

    @classmethod
    def __init__(self,beverage):
        self.beverage=beverage

    @classmethod
    def getDescription(self):
        return self.beverage.getDescription()+" mocha"
    
    @classmethod
    def getCost(self):
        return self.beverage.getCost()+0.20

class Whip(mainDecorator):

    @classmethod
    def __init__(self,beverage):
        self.beverage=beverage

    @classmethod
    def getDescription(self):
        return self.beverage.getDescription()+" whip"
    
    @classmethod
    def getCost(self):
        return self.beverage.getCost()+1.10

def  DecoratorTest():
    beverage=Espresso()
    print(beverage.getDescription(),beverage.getCost())
    beverage=Mocha(beverage)
    print(beverage.getDescription(),beverage.getCost())
    beverage=Whip(beverage)
    print(beverage.getDescription(),beverage.getCost())



DecoratorTest()
