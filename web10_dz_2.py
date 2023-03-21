class Cloth:
    def __init__(self, name, size_or_height):
        self.name = name
        self.size_or_height = size_or_height

    @property
    def fabric_consumption(self):
        if self.name == 'костюм':
            return 2 * self.size_or_height + 0.3
        else:
            return self.size_or_height / 6.5 + 0.5
        
    def __add__(self, other):
        self.size_or_height = 2 * self.size_or_height + 0.3
        other.size_or_height = other.size_or_height / 6.5 + 0.5
        return self.size_or_height + other.size_or_height

costume = Cloth('костюм', 175)
coat = Cloth('пальто', 54)
print(costume.fabric_consumption)
print(coat.fabric_consumption)
print(costume + coat)