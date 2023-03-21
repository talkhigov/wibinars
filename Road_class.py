class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def formula(self):
        print(self._length * self._width * 25 * 1,'кг')

shali_baumana = Road(5, 200)
shali_baumana.formula()