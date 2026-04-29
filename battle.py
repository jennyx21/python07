from ex0 import FlameFactory, AquaFactory


def test_flame(factory: FlameFactory) -> None:
    creature1 = factory.create_base()
    creature2 = factory.create_evolve()
    print(f"{creature1.describe()}")
    print(f"{creature1.attack()}")
    print(f"{creature2.describe()}")
    print(f"{creature2.attack()}")


def test_aqua(factory: AquaFactory) -> None:
    creature1 = factory.create_base()
    creature2 = factory.create_evolve()
    print(f"{creature1.describe()}")
    print(f"{creature1.attack()}")
    print(f"{creature2.describe()}")
    print(f"{creature2.attack()}")


def battle(fa1: AquaFactory | FlameFactory, fa2: AquaFactory | FlameFactory):
    creature1 = fa1.create_base()
    creature2 = fa2.create_base()
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(f"{creature1.attack()}")
    print(f"{creature2.attack()}")


def main():
    print("Testing factory")
    test_flame(FlameFactory())
    print("\nTesting factory")
    test_aqua(AquaFactory())
    print("\nTesting Battle")
    battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
