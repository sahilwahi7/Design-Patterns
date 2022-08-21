""" 
MEMENTO PATTERN
The contents of the memento aren’t accessible to any other object except the one that produced it.

"""
from abc import abstractclassmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

class originator:
    
    @abstractclassmethod
    def __init__(self,state):
        pass
    @abstractclassmethod
    def save(self):
        pass

class ConcreteOriginator(originator):  #originator is creating a new state(Concrete Memento)
    _state=None
    @classmethod
    def __init__(self,state):
        self._state=state
        print(f"My original state is :{self._state}")

    @classmethod
    def doOperation(self):
        print("State is updating by originator")
        self._state=self.generate_random_string(30)
        print(f"Updated state is :{self._state}")

    @classmethod
    def generate_random_string(self,length):
        return "".join(sample(ascii_letters, length))

    @classmethod
    def getState(self):
        return self._state

    @classmethod
    def restore(self,memento):
        self._state=memento.getState()
        print(f"My state has been changed to :{self._state}")

    @classmethod
    def save(self):
        return ConcreteMemento(self._state)

class Memento:
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.
    """

    @abstractclassmethod
    def get_name(self) -> str:
        pass

    @abstractclassmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def getState(self) -> str:
        """
        The Originator uses this method when restoring its state.
        """
        return self._state

    def get_name(self) -> str:
        """
        The rest of the methods are used by the Caretaker to display metadata.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


   


class Caretaker:

    @classmethod
    def __init__(self,originator):
        self._mementos=[]
        self.originator=originator

    @classmethod
    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self.originator.save())

    @classmethod
    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self.originator.restore(memento)
        except Exception:
            self.undo()

    @classmethod
    def show_history(self) -> None:
            print(f"Caretaker: Here's the list of mementos:")
            for memento in self._mementos:
                print(memento.getState())


originator = ConcreteOriginator("Super-duper-super-puper-super.")
caretaker = Caretaker(originator)
caretaker.backup()
originator.doOperation()
caretaker.backup()
originator.doOperation()
print()
caretaker.show_history()
print("\nClient: Now, let's rollback!\n")
caretaker.undo()

print("\nClient: Once more!\n")
caretaker.undo()

