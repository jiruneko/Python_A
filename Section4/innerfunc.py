def outer(a, b):
    
    def plus(c, d):
        return c + d
    
    r = plus(a, b)
    print(r)
    
outer(1, 5)

def outer2(a, b):
    def inner():
        return a * b
    
    return inner

f = outer2(3, 4)
r = f()
print(r)