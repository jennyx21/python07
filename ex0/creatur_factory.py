from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def attack(self) -> str:
        pass


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolve(self) -> Creature:
        pass
