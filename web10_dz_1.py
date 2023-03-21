class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return f'|{self.lst[7][0]} {self.lst[8][0]}|\n|{self.lst[0][0]} {self.lst[1][0]} {self.lst[2][0]}|\n|{self.lst[3][0]} {self.lst[4][0]} {self.lst[5][0]} {self.lst[6][0]}|'

    def __add__(self, other):
        return f'|{self.lst[0][0]} {other.lst[0][0]}|\n|{self.lst[1][0]} {other.lst[1][0]}|'

lsts = Matrix([[1], [2], [3], [11], [12], [13], [14], [5], [7]])
lst = Matrix([[11], [9]])
lst_2 = Matrix([[3], [1]])
print(lsts)
print()
print(lst + lst_2)