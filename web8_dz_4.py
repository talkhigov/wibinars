def val_cheker(func):
    def some(x):
        if x <= 0:
            print(ValueError)
            print('ошибка значения')
        else:
            func(x)
    return some

@val_cheker
def calc_cube(x):
    print(x ** 3)

calc_cube(-5)