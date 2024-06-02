from abc import ABC, abstractmethod

class Ingredient(ABC):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

class Vegetable(Ingredient):
    def get_name(self):
        return self.name

    def get_quantity(self):
        return f"{self.quantity} ��"

class Fruit(Ingredient):
    def get_name(self):
        return self.name

    def get_quantity(self):
        return f"{self.quantity} ��"

# ������ �������������
carrot = Vegetable("�������", 5)
apple = Fruit("������", 10)
print(carrot.get_name())
print(carrot.get_quantity())
print(apple.get_name())
print(apple.get_quantity())
