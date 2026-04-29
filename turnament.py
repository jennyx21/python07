from ex2 import NormalStrategy, AgressivStrategy
from ex2 import DefensivStrategy, BattleStrategy
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import AquaFactory, FlameFactory, CreatureFactory


def battle(t: list[tuple[CreatureFactory, BattleStrategy]]):
    opponents = []
    for f, s in t:
        creature = f.create_base()
        if creature.__class__.__name__ == "Aquabub":
            name = creature.__class__.__name__
        elif creature.__class__.__name__ == "Flameling":
            name = creature.__class__.__name__
        elif creature.__class__.__bases__[1].__name__[0] == "H":
            name = "Healing"
        else:
            name = "Transform"
        strat = s.__class__.__name__.replace("Strategy", "")
        opponents.append(f"({name}+{strat})")
    print(f"{'[ ' + ', '.join(opponents) + ' ]'}")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponent involved")
    n = len(t)
    for i in range(n):
        c1 = t[i][0].create_base()
        s1 = t[i][1]
        for j in range(i + 1, n):
            c2 = t[j][0].create_base()
            s2 = t[j][1]
            try:
                print("\n* Battle *")
                print(f"{c1.describe()}")
                print(" vs.")
                print(f"{c2.describe()}")
                print("now fight!")
                s1.is_valid(c1)
                s2.is_valid(c2)
                s1.act(c1)
                s2.act(c2)
            except Exception as e:
                print(f"Battle Error, aborting tournament: {e}")


def main():
    flameling = FlameFactory()
    aquabub = AquaFactory()
    healing = HealingCreatureFactory()
    shiftling = TransformCreatureFactory()

    normal = NormalStrategy()
    agressiv = AgressivStrategy()
    defensiv = DefensivStrategy()

    t1 = [(flameling, normal), (healing, defensiv)]
    t2 = [(flameling, agressiv), (healing, defensiv)]
    t3 = [(aquabub, normal), (healing, defensiv), (shiftling, agressiv)]

    print("Tournament 0 (basic)")
    battle(t1)
    print("\nTournament 1 (error)")
    battle(t2)
    print("\nTournament 2 (multiple)")
    battle(t3)


if __name__ == "__main__":
    main()
