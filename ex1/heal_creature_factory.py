from .capability import HealCapability
from ex0 import Creature, CreatureFactory


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Sproutling"
        self.type = "Grass"

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self, target: str) -> str:
        return (f"{self.name} heals {target} for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Bloomelle"
        self.type = "Grass"

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self, target: str) -> str:
        return (f"{self.name} heals {target} for a large amount")


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolve(self) -> Creature:
        return Bloomelle()
