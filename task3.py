# Zadanie: System tworzenia pojazdów za pomocą fabryki abstrakcyjnej

# --- Opis zadania ---
# Twoim zadaniem jest zaimplementowanie fabryki abstrakcyjnej dla pojazdów oraz klasy,
# na podstawie której będą budowane pojazdy. Każdy pojazd powinien zawierać informacje o:
# - marce,
# - modelu,
# - kolorze,
# - liczbie drzwi.
# Dodatkowo drzwi mają informację o tym, czy są zablokowane, czy nie. Klasa centralnego zamka przesyła
# sygnał blokowania i odblokowania do wszystkich drzwi jednocześnie, korzystając ze wzorca dependency injection.
#
# Pamiętaj!!!
# Fabryka powinna dostać listę pozycji drzwi i wyprodukować dokładnie takie, jakie są na liście,
# bo fabryka drzwi nie może decydować


from abc import ABC, abstractmethod


class Door:
    def __init__(self, position: str):
        self.position = position
        self.locked = False

    def __str__(self):
        state = "locked" if self.locked else "unlocked"
        return f"{self.position} door ({state})"

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False


class CentralLockingSystem:

    def __init__(self, doors: list[Door]):
        self.doors = doors

    def lock_all(self):
        for door in self.doors:
            door.lock()

    def unlock_all(self):
        for door in self.doors:
            door.unlock()


class Vehicle(ABC):

    def __init__(self, brand: str, model: str, color: str, doors: list[Door],
                 central_locking_system: CentralLockingSystem):
        self.brand = brand
        self.model = model
        self.color = color
        self.doors = doors
        self.central_locking_system = central_locking_system

    @abstractmethod
    def car_details(self) -> str:
        pass


class Car(Vehicle):

    def lock_all_doors(self):
        self.central_locking_system.lock_all()

    def unlock_all_doors(self):
        self.central_locking_system.unlock_all()

    def car_details(self):
        return f"Car details: {self.color} {self.brand} {self.model} with doors: {[str(door) for door in self.doors]}"


class Factory(ABC):

    @abstractmethod
    def create_vehicle(self, brand, model, color, doors) -> Vehicle:
        pass


class CarFactory(Factory):

    def create_vehicle(self, brand, model, colour, door_count):
        doors = CarFactory.create_doors(door_count)
        central_locking_system = CentralLockingSystem(doors)
        return Car(brand, model, colour, doors, central_locking_system)

    @staticmethod
    def create_doors(door_count):
        positions = ("Front Left", "Front Right", "Back Left", "Back Right", "Boot")

        if door_count % 2 == 0:
            return [Door(position) for position in positions[:door_count]]

        return [Door(position) for position in positions[:door_count - 1]] + [Door(positions[-1])]


if __name__ == '__main__':
    factory = CarFactory()

    car1 = factory.create_vehicle('Volkswagen', 'Golf', 'Blue', 5)
    car2 = factory.create_vehicle('Ford', 'Mustang', 'Black', 3)
    car3 = factory.create_vehicle('Chevrolet', 'Camaro', 'White', 2)

    print(car1.car_details())
    print(car2.car_details())
    print(car3.car_details())
