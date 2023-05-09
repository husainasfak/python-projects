class Archer:
     def __init__(self,num_arrows,health,name):
          self.num_arrows = num_arrows
          self.health = health
          self.name = name
     
     def get_shot():
          if health > 0:
               health = health - 1
          else: 
               print(f"{name} is dead")
     
     def shoot(archer):
          if archer.num_arrows <= 0:
               raise Exception(f"{archer.name} can't shoot")
          else:
               raise Exception(f"{name} shoots {archer.name}")
               get_shot()


def main():
    bard = Archer(1, 3, "Bard")
    legolas = Archer(1000, 3, "Legolas")

    while bard.health > 0 and legolas.health > 0:
        try:
            print_status(bard)
            print_status(legolas)
            bard.shoot(legolas)
        except Exception as e:
            print(e)

        try:
            print_status(bard)
            print_status(legolas)
            legolas.shoot(bard)
        except Exception as e:
            print(e)


def print_status(archer):
    print(f"{archer.name} has {archer.health} health and {archer.num_arrows} arrows")


main()