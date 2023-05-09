class Wall:
     # armor = 10
     # height = 5
     # __init__ constructor method. called when object init
     def __init__(self,depth,height,width):
          self.armor = 10
          self.depth = depth
          self.height = height
          self.width = width

     def fortify(self):   # As you can see, methods are nested within the class declaration. Methods always take a special parameter as their first argument called self.The self variable is a reference to the object itself, so by using it you can read and update the properties of the object.
          self.armor *= 2

     def get_cost(self):
          return self.armor * self.height

def main():
     wall = Wall(2,3,4)
     print(wall.armor)
     print(wall.height)
     print('Fortifying wall....')
     wall.fortify()
     print(wall.armor)
     print(wall.height)
     print(f"Cost of wall {wall.get_cost()}")
main()