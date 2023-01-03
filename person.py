class Person():
    """Модель человека"""
    def __init__(self, name, age):
        """Инициализация атрибутов """
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поёт")

    def danse(self):
        """Просим человека танцевать"""
        print(self.name + " танцует")


man = Person("Vasya", 32)
woman = Person('Sveta', 99)

man.sing()
man.danse()
woman.danse()
woman.sing()