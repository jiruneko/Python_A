class Person():
    def __init__(self, name):
        self.name = name
    
    def say_something(self):
        print('I am {}, hello'.format(self.name))

person = Person('Kenichi')
person.say_something()

class Person():
    def __init__(self, name):
        self.name = name
    
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)
    
    def run(self, num):
        print('run' * 10)

person = Person('Kenji')
person.say_something()