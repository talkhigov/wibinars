def type_logger(func):
    def some(*x):
        for i in x:
            print(f'calc_cube({i}: {type(i)})')
    return some


@type_logger
def calc_cube(*x):
    print(x ** 3)


calc_cube(5)