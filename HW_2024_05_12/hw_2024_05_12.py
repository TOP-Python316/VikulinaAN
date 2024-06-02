
from abc import ABC, abstractmethod

class Unit(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class Infantry(Unit):
    def move(self):
        print("Пехота передвигается в пешем порядке")

    def attack(self):
        print("Пехота участвует в ближнем бою")

    def defend(self):
        print("Пехота держит строй")

class Cavalry(Unit):
    def move(self):
        print("Кавалерия передвигается верхом")

    def attack(self):
        print("Кавалерия переходит в атаку")

    def defend(self):
        print("Кавалерия защищает фланги")

class Squad:
    def __init__(self):
        self.army = []

    def add_unit(self, unit):
        if isinstance(unit, Unit):
            self.army.append(unit)
        else:
            raise TypeError("Only instances of Unit class can be added to the squad.")

    def attack(self):
        for unit in self.army:
            unit.move()
            unit.attack()

    def defend(self):
        for unit in self.army:
            unit.move()
            unit.defend()

def validate_unit(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, Unit):
                raise TypeError("Invalid unit type.")
        return func(*args, **kwargs)
    return wrapper

# Пример работы
Squad = Squad()
Squad.add_unit(Infantry())
Squad.add_unit(Cavalry())
Squad.add_unit(Infantry())
Squad.add_unit(Cavalry())
Squad.attack()
Squad.defend()
