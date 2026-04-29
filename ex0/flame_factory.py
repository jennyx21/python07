from .creatur_factory import Creature, CreatureFactory


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire"

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class FlameFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolve(self) -> Creature:
        return Pyrodon()
