"""  Observer pattern """
from abc import abstractclassmethod

from jinja2 import TemplateError


class Subject:
    
    @abstractclassmethod
    def registerObserver(self,o):
          pass

    
    @abstractclassmethod
    def removeObserver(self,o):
        pass

    @abstractclassmethod
    def notifyObserver(self):
        pass

class Observer:
    @abstractclassmethod
    def update(self,temp,humidity,pressure):
        pass

class DsiplayElement:

    @abstractclassmethod
    def display():
        pass


class WeatherData(Subject):
    
    
    @classmethod
    def __init__(self) -> None:
        self.observers=[]
        self.temperature=0
        self.humidity=0
        self.pressure=0
    
        
    @classmethod
    def registerObserver(self,o):
        self.observers.append(o)
 

    @classmethod
    def removeObserver(self, o):
        self.observers.remove(o)


    @classmethod
    def notifyObserver(self):
        for o in self.observers:
            o.update(self.temperature,self.humidity,self.pressure)
            print(self.observers)

    
    @classmethod
    def measurementChanges(self):
        self.notifyObserver()


    @classmethod
    def setMeasurements(self,temperature,humidity,pressure):
        self.temperature=temperature
        self.pressure=pressure
        self.humidity=humidity

        self.measurementChanges()

class CurrentConditions(Observer,DsiplayElement):

    @classmethod
    def __init__(self,weatherData):
        self.weatherData=weatherData
        weatherData.registerObserver(self)


    @classmethod
    def update(self,temp,humidity,pressure):
        self.temperature=temp
        self.humidity=humidity
        self.pressure=pressure
        self.display()

    @classmethod
    def display(self):
        print(self.temperature,self.humidity)

class MeanCurrentCOnditions(Observer,DsiplayElement):
    @classmethod
    def __init__(self,weatherData):
        self.weatherData=weatherData
        weatherData.registerObserver(self)

    @classmethod
    def update(self,temp,hum,pres):
        self.temperature=temp
        self.humdity=hum
        self.pressure=pres
        self.display()

    @classmethod
    def display(self):
        print(self.temperature+self.humdity)


def main1():
    weatherdata=WeatherData()
    currentcinditions=CurrentConditions(weatherdata)     #add observer
    meanconditions=MeanCurrentCOnditions(weatherdata)    #add observer
    weatherdata.setMeasurements(80,65,30)
    weatherdata.setMeasurements(70,80,20)
    weatherdata.removeObserver(meanconditions)
    weatherdata.setMeasurements(90,60,25)
main1()

