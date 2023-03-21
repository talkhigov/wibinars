import time

class TrafficLight:
    def __init__(self, __color):
        self.__color = __color

    def running(self):
        print('КРАСНЫЙ')
        time.sleep(7)
        print('ЖЕЛТЫЙ')
        time.sleep(2) 
        print('ЗЕЛЕНЫЙ')
        time.sleep(10)
        print(self.__color)

Traffic_Light = TrafficLight('')
Traffic_Light.running()
