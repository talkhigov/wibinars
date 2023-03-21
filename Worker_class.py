class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income['wage'] + _income['bonus']

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        print(f'Полное Имя: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учётом премии: {self._income}')

person = Position('Isa', 'Bazaev', 'devoloper python', {'wage': 100_000, 'bonus': 25000})
person.get_full_name()
person.get_total_income()
print(person.position)
Musa = Position('Musa', 'Turaev', 'devoloper Python Midle', {'wage': 150_000, 'bonus': 10_000})
Musa.get_total_income()