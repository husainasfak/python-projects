'''
     DRY -> DONT REPEAT YOURSELF
'''
def get_soldier_dps(soldier):
    dps = soldier['damage'] * soldier['attacks_per_second']
    return dps



def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    print(
        fight_soldiers(
            {"damage": 10, "attacks_per_second": 3},
            {"damage": 20, "attacks_per_second": 1},
        )
    )
    print(
        fight_soldiers(
            {"damage": 50, "attacks_per_second": 1},
            {"damage": 50, "attacks_per_second": 2},
        )
    )
    print(
        fight_soldiers(
            {"damage": 100, "attacks_per_second": 1},
            {"damage": 1, "attacks_per_second": 200},
        )
    )
    print(
        fight_soldiers(
            {"damage": 100, "attacks_per_second": 1},
            {"damage": 50, "attacks_per_second": 2},
        )
    )
    print(get_soldier_dps.__name__)


main()
