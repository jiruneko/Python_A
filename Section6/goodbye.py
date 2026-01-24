class Person():
    def __init__(self, name):
        self.name = name
    
    def __del__(self) -> None:
        print('good bye')

person = Person('Mike')
# print(person())
print('##########')

class Car():
    def run(self):
        print('run')

class MyCar(Car):
    pass

car = Car()
car.run()

mycar = MyCar()
mycar.run()