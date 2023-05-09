
class Brawler:
     def __init__(self,speed,strength,name):
          self.speed =  speed
          self.strength = strength
          self.name = name
          self.power = speed + strength


def fight(op1,op2):
     if op1.power > op2.power:
          print(f"Opponent 1 power({op1.power}) is greater than opponent 2 power({op2.power})")
     elif op1.power < op2.power:
          print(f"Opponent 1 power({op1.power}) is less than opponent 2 power({op2.power})")
     else:
          print(f"Opponent 1 power({op1.power}) is equal to opponent 2 power({op2.power})") 


     
def main():
     gimli  = Brawler(2, 7, 'Gimli')
     legolas = Brawler(7, 7, 'Legolas')
     frodo = Brawler(3, 2, 'Frodo')
     aragorn = Brawler(4, 4, 'Aragorn')

     fight(aragorn,gimli)
     fight(legolas,frodo)

main()