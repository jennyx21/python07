from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability

class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature) -> None:
        pass 

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature):
        print(f"{creature.attack()}")
    
    def is_valid(self, creature):
        return True


class AgressivStrategy(BattleStrategy):

    def act(self, creature):
        print(f"{creature.attack()}")
        if hasattr(creature, "transform"):
            print(f"{creature.transform()}")
        if hasattr(creature, "revert"):
            print(f"{creature.revert()}")

    def is_valid(self, creature) -> bool:
        if hasattr(creature, "transform"):
            return True
        else:
            raise Exception(f"Invalid Creature '{creature.__class__.__name__}' "
                            f"for this agressiv Strategy")


class DefensivStrategy(BattleStrategy):

    def act(self, creature):
        print(f"{creature.attack()}")
        if hasattr(creature, "heal"):
            print(f"{creature.heal('itself')}")

    def is_valid(self, creature) -> bool:
        if hasattr(creature, "heal"):
            return True
        else:
            raise Exception(f"Invalid Creature '{creature.__class__.__name__}' "
                            f"for this defensiv Strategy")