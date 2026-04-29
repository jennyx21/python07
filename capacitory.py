from ex1 import TransformCreatureFactory, HealingCreatureFactory


def Transformer(factory: TransformCreatureFactory) -> None:
    creature = factory.create_base()
    evolv = factory.create_evolve()
    print("base:")
    print(f"{creature.describe()}")
    print(f"{creature.attack()}")
    print(f"{creature.transform()}")
    print(f"{creature.attack()}")
    print(f"{creature.revert()}")
    print("evolved:")
    print(f"{evolv.describe()}")
    print(f"{evolv.attack()}")
    print(f"{evolv.transform()}")
    print(f"{evolv.attack()}")
    print(f"{evolv.revert()}")


def healer(factory: HealingCreatureFactory) -> None:
    creature = factory.create_base()
    evolv = factory.create_evolve()
    print("base:")
    print(f"{creature.describe()}")
    print(f"{creature.attack()}")
    print(f"{creature.heal('itself')}")
    print("evolved:")
    print(f"{evolv.describe()}")
    print(f"{evolv.attack()}")
    print(f"{evolv.heal('itself and others')}")


def main() -> None:
    print("Testing Creature with healing capability")
    healer(HealingCreatureFactory())
    print("\nTesting Creature with transform capability")
    Transformer(TransformCreatureFactory())


if __name__ == "__main__":
    main()
