class Pet:
    allowed = ["cat", "dog", "parrot", "fish", "rat"]
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You cannot have a {species} pet!")
        self.name = name
        self.species = species

cat = Pet("Fluffy", "cat")
dog = Pet("Felix", "dog")
tiger = Pet("Joe", "tiger")
