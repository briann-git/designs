from typing import Protocol

        
class Observer(Protocol):
    def update():
        ...
        
class Observable(Protocol):
    def registerObserver(o: Observer):
        ...
        
    def deregisterObserver(o: Observer):
        ...
        
    def notify():
        ...
        
        
class BroadcastNumber(Observable):
    def __init__(self) -> None:
        self.observers:list = [Observer]
        self.number = None
        
    def registerObserver(self, o: Observer):
        self.observers.append(o)
        
    def deregisterObserver(self, o: Observer):
        try:
            self.observers.remove(o)
        except ValueError:
            pass
        
    def notify(self):
        for o in self.observers:
            o.update()
            
    def set_number(self, v:int):
        if not isinstance(v, int):
            return
        self.number = v
        self.notify()
    

def calculate_power(v, f):
    return pow(v, f)
    
        
class Squares(Observer):
    def __init__(self, subject:Observable) -> None:
        self.subject = subject
        subject.registerObserver(self)
        self.factor = 2
        
    def calculate(self, v:int):
        if not isinstance(v, int):
            return
        print(calculate_power(v, self.factor))
        
    def update(self):
        v = self.subject.number
        f"{v} squared is {self.calculate(v)}"
        
        
class Cubes(Observer):
    def __init__(self, subject:Observable) -> None:
        self.subject = subject
        subject.registerObserver(self)
        self.factor = 3
        
    def calculate(self, v:int):
        if not isinstance(v, int):
            return
        print(calculate_power(v, self.factor))
        
    def update(self):
        v = self.subject.number
        f"{v} cubed is {self.calculate(v)}"
        
class SquareRoots(Observer):
    def __init__(self, subject:Observable) -> None:
        self.subject = subject
        subject.registerObserver(self)
        self.factor = .5
        
    def calculate(self, v:int):
        if not isinstance(v, int):
            return
        print(calculate_power(v, self.factor))
        
    def update(self):
        v = self.subject.number
        f"The Squareroot of {v} is {self.calculate(v)}"
    
    

broadcast = BroadcastNumber()
sq = Squares(broadcast)
cb = Cubes(broadcast)
sqrts = SquareRoots(broadcast)

for i in range(1,6):
    broadcast.set_number(i)
    print()