from typing import Protocol

class QuackSimple():
    def quack():
        print("Quack!!!")
        
class QuackComplex():
    def quack():
        print("Quack Quack Haha!!")
        
        
class FlySimple:
    def fly():
        print('Whoosh!!')
        
class FlySilent:
    def fly():
        print("Whoo")
        
class Fly(Protocol):
    def fly():
        ...
        
class Quack(Protocol):
    def quack():
        ...
        
class Duck:
    def __init__(self, fly:Fly, quack:Quack) -> None:
        self.fly = fly
        self.quack = quack
        
    def performQuack(self):
        self.quack.quack()
        
    def performFly(self):
        self.fly.fly()
        

print("Duck1: flies silent, quacks alot")
duck1 = Duck(fly=FlySilent, quack=QuackComplex)
duck1.performFly(); duck1.performQuack()
print()
        
print("Duck2: flies silent, quacks simple")
duck2 = Duck(fly=FlySilent, quack=QuackSimple)
duck2.performFly(); duck2.performQuack()
print()

print("Duck3: flies simple, quacks alot")
duck3 = Duck(fly=FlySimple, quack=QuackComplex)
duck3.performFly(); duck3.performQuack()
print()

print("Duck4: flies simple, quacks simple")
duck4 = Duck(fly=FlySimple, quack=QuackSimple)
duck4.performFly(); duck4.performQuack()
print()
