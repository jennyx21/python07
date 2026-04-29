from .creatur_factory import Creature, CreatureFactory


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Aquabub"
        self.type = "Water"

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolve(self) -> Creature:
        return Torragon()
