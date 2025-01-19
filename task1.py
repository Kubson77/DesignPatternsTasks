# Zadanie: System tworzenia pojazdów za pomocą fabryki abstrakcyjnej

# --- Opis zadania ---
# Twoim zadaniem jest zaimplementowanie fabryki abstrakcyjnej dla pojazdów oraz klasy,
# na podstawie której będą budowane pojazdy. Każdy pojazd powinien zawierać informacje o:
# - marce,
# - modelu,
# - kolorze,
# - liczbie drzwi.
# Następnie należy stworzyć 3 obiekty samochodów o różnych właściwościach.


from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, brand: str, model: str, color: str, doors: int):
        self.brand = brand
        self.model = model
        self.color = color
        self.doors = doors

    @abstractmethod
    def car_details(self):
        pass


class Car(Vehicle):

    def car_details(self):
        return f"Car details: {self.color} {self.brand} {self.model} {self.doors}"


class Factory(ABC):

    @abstractmethod
    def create_vehicle(self, brand, model, color, doors) -> Vehicle:
        pass


class CarFactory(Factory):

    def create_vehicle(self, brand, model, color, doors):
        return Car(brand, model, color, doors)


if __name__ == '__main__':
    factory = CarFactory()

    car1 = factory.create_vehicle('Volkswagen', 'Golf', 'Blue', 4)
    car2 = factory.create_vehicle('Ford', 'Mustang', 'Black', 2)
    car3 = factory.create_vehicle('Chevrolet', 'Camaro', 'White', 2)

    print(car1.car_details())
    print(car2.car_details())
    print(car3.car_details())
