# Zadanie: Zmień klasę z zadania poprzedniego tak, aby obiekt
# pojazdu wymagał obiektu drzwi, na podstawie
# którego utworzysz w pojeździe tyle drzwi, ile zostało
# podane w konstruktorze


from abc import ABC, abstractmethod


class Door:
    def __init__(self, position: str):
        self.position = position

    def __str__(self):
        return f"{self.position} door"


class Vehicle(ABC):

    def __init__(self, brand: str, model: str, color: str, door_count: int):
        self.brand = brand
        self.model = model
        self.color = color
        self.doors: list[Door] = self.create_doors(door_count)

    @abstractmethod
    def car_details(self) -> str:
        pass

    @abstractmethod
    def create_doors(self, door_count) -> list[Door]:
        pass


class Car(Vehicle):

    def car_details(self):
        return f"Car details: {self.color} {self.brand} {self.model} with doors: {[str(door) for door in self.doors]}"

    def create_doors(self, door_count):
        positions = ("Front Left", "Front Right", "Back Left", "Back Right", "Boot")

        if door_count % 2 == 0:
            return [Door(position) for position in positions[:door_count]]
        else:
            return [Door(position) for position in positions[:door_count - 1]] + [Door(positions[-1])]


class Factory(ABC):

    @abstractmethod
    def create_vehicle(self, brand, model, color, doors) -> Vehicle:
        pass


class CarFactory(Factory):

    def create_vehicle(self, brand, model, color, doors):
        return Car(brand, model, color, doors)


if __name__ == '__main__':
    factory = CarFactory()

    car1 = factory.create_vehicle('Volkswagen', 'Golf', 'Blue', 5)
    car2 = factory.create_vehicle('Ford', 'Mustang', 'Black', 3)
    car3 = factory.create_vehicle('Chevrolet', 'Camaro', 'White', 2)

    print(car1.car_details())
    print(car2.car_details())
    print(car3.car_details())
