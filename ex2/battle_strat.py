from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature: Any) -> None:
        print(f"{creature.attack()}")

    def is_valid(self, creature: Any) -> bool:
        return True


class AgressivStrategy(BattleStrategy):

    def act(self, creature: Any) -> None:
        if hasattr(creature, "transform"):
            print(f"{creature.transform()}")
            print(f"{creature.attack()}")
        if hasattr(creature, "revert"):
            print(f"{creature.revert()}")

    def is_valid(self, creature: Any) -> bool:
        if hasattr(creature, "transform"):
            return True
        else:
            raise Exception(f"Invalid Creature"
                            f"'{creature.__class__.__name__}'"
                            f" for this agressiv Strategy")


class DefensivStrategy(BattleStrategy):

    def act(self, creature: Any) -> None:
        print(f"{creature.attack()}")
        if hasattr(creature, "heal"):
            print(f"{creature.heal('itself')}")

    def is_valid(self, creature: Any) -> bool:
        if hasattr(creature, "heal"):
            return True
        else:
            raise Exception(f"Invalid Creature"
                            f" '{creature.__class__.__name__}' "
                            f"for this defensiv Strategy")
