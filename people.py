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
        description = self.name + ", ему " + str(self.age) + "лет, а его рост " + str(
            self.height) + " и его вес " + str(self.weight)
        print(description)

    def get_weight(self):
        """get weight of person"""
        print(f"Вес нужного человека {self.name} -  {self.weight}")

    def update_weight(self, kg):
        """update weigth person"""
        self.weight = kg



man = Person("Vasya", 30, 180)
man.description_person()
man.get_weight()
man.weight = 222
man.get_weight()
man.update_weight(12)
man.get_weight()
