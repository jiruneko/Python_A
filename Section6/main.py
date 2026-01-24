class Person():
    def say_hello(self):
        return 'hello'

person = Person()
print(person.say_hello())

class Person():
    def __init__(self):
        print('first')

Person()
