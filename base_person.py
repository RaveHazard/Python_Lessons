class Person():
    """Create person"""

    def __init__(self, name, age, height):
        """Init attributes for class Person"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 999

    def description_person(self):
        """Description of person"""
        description = self.name + ", ему " + str(self.age) + " лет, а его рост " + str(
            self.height) + " и его вес " + str(self.weight)
        print(description)

    def get_weight(self):
        """get weight of person"""
        print(f"Вес нужного человека {self.name} -  {self.weight}")

    def update_weight(self, kg):
        """update weigth person"""
        self.weight = kg


class Warrior(Person):
    """create class Warrior"""

    def __init__(self, name, age, height):
        """Init attributes parent class"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Get rage """
        print(f"Ярость {self.name}: {self.rage}")

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + " лет, а его ярость " + str(self.rage)
        # print(description)
        return description


warrior = Warrior('Conan', 77, 200)
warrior.update_weight(120)
warrior.height = 777

# man = Person("Vasya", 30, 180)
# man.description_person()
# man.update_weight(111)
# man.get_weight()
