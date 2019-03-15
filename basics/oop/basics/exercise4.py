class Chicken:
    total_eggs = 0
    def __init__(self, name, species, eggs=0):
        self.name = name
        self.species = species
        self.eggs = eggs
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1


c1 = Chicken("Amelia", "Speckled Sussex")
c2 = Chicken("Alice", "Speckled Sussex")
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
c2.lay_egg()
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
print(c1.eggs)
print(c2.eggs)
