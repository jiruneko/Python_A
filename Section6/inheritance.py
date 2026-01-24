class Car():
    def run(self):
        print('run')

class MyCar(Car):
    def run(self):
        print('fast')

class Advanced(Car):
    def run(self):
        print('super fast')

car = Car()