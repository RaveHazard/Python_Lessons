class Car():
    """create class"""

    def __init__(self, model, building, value_engine, price, mileage):
        """init attributes car"""
        self.model = model
        self.building = building
        self.value_engine = value_engine
        self.price = price
        self.mileage = mileage
        self.weels_value = 2

    def car_info(self):
        """print car info"""
        car_info = f"Название модели: {self.model}, это {self.weels_value}-х колесный монстр\n" \
                   f"Год выпуска - {self.building} с пробегом {self.mileage}km и объемом двигателя {self.value_engine}\n" \
                   f"Цена за данную модель = {self.price}$"
        print(car_info)


class Track(Car):
    """create child class """

    def __init__(self, model, building, value_engine, price, mileage):
        """init attributes car"""
        super().__init__(model, building, value_engine, price, mileage)
        self.weels_value = 8

    def car_info(self):
        """print car info"""
        car_info = f"Название модели: {self.model}, это {self.weels_value}-х колесный монстр\n" \
                   f"Кузов из оцинкованной стали, наличие штыря для прицепа\n" \
                   f"Комфортный сон в дальней дороге обеспечен.\n" \
                   f"Год выпуска - {self.building} с пробегом {self.mileage}km и объемом двигателя {self.value_engine}\n" \
                   f"Цена за данную модель = {self.price}$"
        print(car_info)


subaru = Car("Subaru Legasy", "2004", "2l", 2_000, 130_000)
subaru.car_info()
print("========================================================")
volvo = Track("VOLVO truck", "2002", "8l", 10_000, 333_000)
volvo.car_info()
