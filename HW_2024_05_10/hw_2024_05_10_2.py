class Dinosaur(ABC):
    def __init__(self, breed, personal_name, height, weight):
        self.breed = breed
        self.personal_name = personal_name
        self.height = height
        self.weight = weight

    @abstractmethod
    def get_personal_name(self):
        pass

    @abstractmethod
    def get_breed(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_diet(self):
        pass

class Carnivore(Dinosaur):
    def get_personal_name(self):
        return self.personal_name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return f"{self.height} см"

    def get_weight(self):
        return f"{self.weight} кг"

    def get_diet(self):
        return "Плотоядный"

class Herbivore(Dinosaur):
    def get_personal_name(self):
        return self.personal_name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return f"{self.height} см"

    def get_weight(self):
        return f"{self.weight} кг"

    def get_diet(self):
        return "Травоядный"

class DinosaurPark:
    def __init__(self):
        self.dinosaurs = []

    def add_dinosaur(self, dinosaur):
        self.dinosaurs.append(dinosaur)

    def list_dinosaurs(self):
        return [(dino.get_personal_name(), dino.get_breed(), dino.get_weight(), dino.get_height(), dino.get_diet()) for dino in self.dinosaurs]

    def list_carnivores(self):
        return [(dino.get_personal_name(), dino.get_breed(), dino.get_weight(), dino.get_height(), dino.get_diet()) for dino in self.dinosaurs if isinstance(dino, Carnivore)]

    def list_herbivores(self):
        return [(dino.get_personal_name(), dino.get_breed(), dino.get_weight(), dino.get_height(), dino.get_diet()) for dino in self.dinosaurs if isinstance(dino, Herbivore)]

# Пример использования
t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)
park = DinosaurPark()
park.add_dinosaur(t_rex)
park.add_dinosaur(velociraptor)
park.add_dinosaur(stegosaurus)
park.add_dinosaur(triceratops)

for dinosaur in park.list_dinosaurs():
    print(f'Имя: {dinosaur[0]}\nВид: {dinosaur[1]}\nВес: {dinosaur[2]} кг\nРост: {dinosaur[3]} см\nРацион: {dinosaur[4]}\n')
