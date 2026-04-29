from .capability import TransformCapability
from ex0 import Creature, CreatureFactory


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Shiftling"
        self.type = "Normal"
        self.transformed = False

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        if not self.transformed:
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} performs a boosted strike!")

    def transform(self) -> str:
        self.transformed = True
        return (f"{self.name} shifts into a shaper form!")

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return (f"{self.name} returns to normal.")
        else:
            return (f"Nothing happens {self.name} never was transformed")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Morphagon"
        self.type = "Normal/Dragon"
        self.transformed = False

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    def attack(self) -> str:
        if not self.transformed:
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} unleashes a devastating morph strike!")

    def transform(self) -> str:
        self.transformed = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return (f"{self.name} stabilizes its form.")
        else:
            return (f"Nothing happens {self.name} never was transformed")


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolve(self) -> Creature:
        return Morphagon()
