#command pattern in python

from abc import abstractclassmethod


class Command:    #we have a command interface
    @abstractclassmethod
    def execute(self):
        pass

class Light:      #we have class we need to invoke
    @classmethod
    def on(self):
        print("LIGHT IS ON")

    @classmethod
    def off(self):
        print("LIGHT IS OFF")

class lightCommand(Command):    #lighcommand class that invokes the light class using command
    
    @classmethod
    def __init__(self,light):
        self.light=light

    @classmethod
    def execute(self):
        self.light.on()
     
class simpleRemote:   #objects in which we passs all the commands

    @classmethod
    def setCommand(self,command):
        self.command=command

    @classmethod
    def buttonWasPressed(self):
        self.command.execute()

remote=simpleRemote()
light=Light()
lighton=lightCommand(light)
remote.setCommand(lighton)
remote.buttonWasPressed()
