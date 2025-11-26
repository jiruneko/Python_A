def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')

print(r)


# デコレーター
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(20, 30)
print(r)


# @print_info
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(40, 55)
print(r)