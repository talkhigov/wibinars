class Cell:
    def __init__(self, cell, cellule):
        self.cell = cell
        self.cellule = cellule

    def __add__(self, other):
        return self.cell + other.cell, self.cellule + other.cellule
    
    def __sub__(self, other):
        if self.cellule - other.cellule > 0:
            return self.cell - other.cell, self.cellule - other.cellule
        else:
            return 'Разность количества ячеек двух клеток должно быть больше 0'

    def __mul__(self, other):
        return self.cell * other.cell, self.cellule * other.cellule
    
    def __truediv__(self, other):
        return self.cell // other.cell, self.cellule // other.cellule

    def make_order(self, quantity):
        if self.cellule % quantity == 0:
            colvo = self.cellule // quantity
            result = ("*" * quantity + '\\n') * colvo
            print(result[:-2])
        else:
            remainder = self.cellule % quantity
            colvo = self.cellule // quantity
            result = ("*" * quantity + '\\n') * colvo
            print(result + '*' * remainder)

cell = Cell(10, 2)
cell2 = Cell(15, 3)
print(cell + cell2)
cell3 = cell2 - cell
print(cell3)
print(cell - cell2)
cell5 = Cell(6, 2)
cell6 = Cell(3, 1)
cell4 = cell5 * cell6
print(cell4)
cell7 = cell5 / cell6
print(cell7)
cell8 = Cell(30, 15)
cell8.make_order(6)